#!/usr/bin/env python3
"""Crea borradores de Releases; nunca publica ni reemplaza archivos."""

import json
import os
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]


def preparar():
    repo = os.environ.get(
        "GITHUB_REPOSITORY", "Casa-Villalba/casavillalba-library"
    )
    target = os.environ.get("GITHUB_SHA") or subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()
    catalogo = json.loads((ROOT / "ediciones/catalogo.json").read_text(encoding="utf-8"))

    # Validar todo antes de crear el primer borrador.
    publicaciones = []
    ids = set()
    for item in catalogo["publicaciones"]:
        tag = item["id"]
        if not re.fullmatch(r"cv-[0-9]{3}", tag) or tag in ids:
            raise ValueError(f"Identificador inválido o duplicado: {tag}")
        ids.add(tag)
        titulo = item["titulo"].strip()
        notas = (ROOT / item["notas"]).resolve()
        if (
            not titulo
            or not notas.is_relative_to(ROOT / "ediciones")
            or not notas.is_file()
            or not notas.read_text(encoding="utf-8").strip()
        ):
            raise ValueError(f"Título o notas inválidos para {tag}")
        publicaciones.append((tag, titulo, notas))

    # Un fallo de autenticación o de red aborta; no se interpreta como Release ausente.
    existentes = set(subprocess.check_output(
        ["gh", "api", "--paginate", f"repos/{repo}/releases", "--jq", ".[].tag_name"],
        text=True,
    ).splitlines())

    for tag, titulo, notas in publicaciones:
        if tag in existentes:
            print(f"{tag}: ya existe; se conservan sus archivos y notas.")
            continue
        subprocess.run(
            [
                "gh", "release", "create", tag,
                "--repo", repo,
                "--target", target,
                "--title", titulo,
                "--notes-file", str(notas),
                "--draft", "--latest=false",
            ],
            check=True,
        )
        print(f"{tag}: borrador creado. Falta adjuntar y revisar los archivos.")


if __name__ == "__main__":
    preparar()
