# Publicar una edición digital

Los archivos terminados se adjuntan a un Release de este repositorio. Los manuscritos de trabajo, las pruebas y los archivos con comentarios permanecen en el flujo editorial privado.

## Primera publicación: cv-001

1. Entra en [Releases](https://github.com/Casa-Villalba/casavillalba-library/releases) con tu cuenta de GitHub.
2. Abre el borrador **Selección poética — Sor Juana Inés de la Cruz** y pulsa **Edit**. Su etiqueta es `cv-001`.
3. Adjunta el EPUB final con el nombre exacto `seleccion-poetica.epub`. Adjunta `seleccion-poetica.pdf` solamente si también tienes el PDF de distribución terminado.
4. Revisa las notas del Release. Deben reflejar los formatos que vas a publicar y los créditos de esa edición.
5. Guarda el borrador y descarga los adjuntos para probarlos: abre el EPUB en una aplicación de lectura y comprueba portada, índice, notas, saltos de sección y créditos. Haz lo mismo con el PDF, si lo incluyes.
6. Cuando los archivos estén revisados, pulsa **Publish release**. Publicar permite que cualquier persona descargue los adjuntos.
7. Comprueba las URLs desde una ventana sin sesión de GitHub antes de activar los botones de descarga en la web.

Puedes publicar el EPUB primero y añadir el PDF más adelante. Cada formato se habilita de forma independiente en el catálogo del sitio web.

## Enlaces de cv-001

| Formato | Nombre del adjunto | URL pública al publicar |
| --- | --- | --- |
| EPUB | `seleccion-poetica.epub` | `https://github.com/Casa-Villalba/casavillalba-library/releases/download/cv-001/seleccion-poetica.epub` |
| PDF | `seleccion-poetica.pdf` | `https://github.com/Casa-Villalba/casavillalba-library/releases/download/cv-001/seleccion-poetica.pdf` |

Estas URLs no funcionan mientras el Release sea un borrador o falte el adjunto correspondiente. No uses `/releases/latest/download/`: cada libro tiene su propia etiqueta.

## Segunda publicación: cv-002 — La metamorfosis

Esta edición se prepara mediante `ediciones/cv-002.md` y su entrada en `ediciones/catalogo.json`. Al fusionar el PR en `main`, la acción **Preparar ediciones** creará un **borrador** del Release `cv-002` si aún no existe. No publica el libro ni adjunta archivos.

1. Revisa en [Releases](https://github.com/Casa-Villalba/casavillalba-library/releases) el borrador **La metamorfosis — Franz Kafka**, con etiqueta `cv-002`. Si la acción aún no lo creó, consulta **Actions → Preparar ediciones**.
2. Renombra el EPUB final a **`la-metamorfosis.epub`**.
3. Abre **Edit** en el borrador y adjunta `la-metamorfosis.epub` en **Attach binaries**. **No lo subas mediante un commit/push a `main` ni a `ediciones/`**: los libros terminados viven como archivos del Release.
4. Comprueba la cubierta, los enlaces del índice y las notas en un lector EPUB. Revisa las notas del Release para que solo anuncien los formatos realmente adjuntos.
5. Pulsa **Publish release** cuando estés conforme y prueba la descarga sin iniciar sesión.
6. Actualiza por separado el catálogo de la web de Casa Villalba para activar el EPUB. El PDF se puede adjuntar y activar después, sin modificar el identificador de la edición.

| Formato | Archivo | URL pública después de publicar y adjuntar el archivo |
| --- | --- | --- |
| EPUB | `la-metamorfosis.epub` | `https://github.com/Casa-Villalba/casavillalba-library/releases/download/cv-002/la-metamorfosis.epub` |
| PDF (cuando exista) | `la-metamorfosis.pdf` | `https://github.com/Casa-Villalba/casavillalba-library/releases/download/cv-002/la-metamorfosis.pdf` |

**Importante:** el catálogo web aún debe configurarse para CV002; registrar esta publicación en la biblioteca no crea automáticamente el botón de descarga en `casavillalba.com`.

## Habilitar la descarga en Casa Villalba

En `despegaa-com/casavillalba`, abre `src/shared/data/book.data.ts`. Para CV001 existen las entradas `cv-001-epub` y `cv-001-pdf`. Para CV002 tendrás que incorporar `cv-002-epub` (y, más adelante, `cv-002-pdf`) con su correspondiente `descargaUrl`.

Después de comprobar la descarga pública de cada formato, configura su `estado` como `disponible` y enlázalo a su adjunto de GitHub. Si la entrada ya existe en la web y está en `en-preparacion`, bastará cambiar ese estado; si todavía no existe (como en CV002), primero habrá que crearla. El cambio debe publicarse en la web para que aparezca el botón.

El estado general del libro y el de cada formato son independientes. Un EPUB publicado no habilita automáticamente el PDF ni anuncia una edición impresa.

## Cómo se crean los borradores

La acción **Preparar ediciones** consulta `ediciones/catalogo.json` cuando se incorporan cambios a `main`. También puede ejecutarse desde **Actions → Preparar ediciones → Run workflow**.

Por cada ficha que todavía no tenga un Release, crea un borrador con las notas indicadas. No publica nada, no sube archivos y no modifica los Releases existentes. Para usar GitHub desde el navegador no necesitas instalar herramientas ni configurar un token personal.

Si el borrador no aparece, consulta el resultado de esa acción. También puedes crearlo manualmente desde **Releases → Draft a new release**, usando la etiqueta, título y notas de la ficha.

## Añadir otro libro

1. Crea sus notas en `ediciones/cv-002.md`, con título, autor, identificador, enlace a su ficha y los datos confirmados de la edición.
2. Añade su entrada a `ediciones/catalogo.json` siguiendo el ejemplo de `cv-001`. Hazlo cuando vayas a preparar esa publicación; no hace falta crear Releases para todo el catálogo futuro.
3. Incorpora el cambio a `main`. La acción creará el borrador pendiente.
4. Adjunta y revisa los archivos finales, publica el Release y activa los formatos correspondientes en la web.

## Corregir un archivo ya publicado

Conserva la etiqueta y el nombre del archivo para mantener estable la URL. Para reemplazar un adjunto es necesario quitar el anterior y subir el archivo corregido con el mismo nombre; durante ese intervalo la descarga no estará disponible.

Antes de quitarlo, conserva una copia del archivo anterior. Documenta la fecha y el motivo de la corrección en las notas. El contador de descargas pertenece a cada adjunto: reemplazarlo crea un contador nuevo.

Una nueva edición editorial significativa se decide por separado. No cambies de identificador por una simple corrección técnica ni reutilices una etiqueta de otro libro.
