# Casa Villalba Library

Repositorio público de distribución de las ediciones digitales de **Casa Villalba Editorial**.

Este repositorio funciona como biblioteca de archivos para las publicaciones digitales de Casa Villalba. Los libros se distribuyen mediante **GitHub Releases** en formatos como PDF y EPUB.

El código del sitio web de Casa Villalba se mantiene en un repositorio independiente.

## Casa Villalba Editorial

Casa Villalba es un proyecto editorial dedicado a preparar, editar y publicar obras literarias y de pensamiento, con especial atención a textos clásicos y de dominio público.

Las ediciones digitales pueden consultarse y descargarse desde el sitio oficial de Casa Villalba.

**Sitio oficial:**  
https://casavillalba.com

## Organización del repositorio

Este repositorio no contiene una aplicación ni requiere instalación.

No utiliza React, Vite, Node.js ni ningún otro framework.

Su función principal es alojar las publicaciones digitales mediante **GitHub Releases**.

La estructura del repositorio se mantiene deliberadamente mínima:

```text
casavillalba-library/
├── README.md
└── LICENSE
```

Los archivos PDF y EPUB no se almacenan normalmente mediante commits dentro del repositorio.

Se publican como archivos adjuntos de cada Release.

## Publicaciones

Cada libro de Casa Villalba tiene un identificador editorial estable.

Ejemplo:

```text
cv-001
cv-002
cv-003
...
```

Cada publicación digital utiliza ese identificador como nombre de su Release.

Ejemplo:

```text
Release: cv-001
```

Assets:

```text
seleccion-poetica.pdf
seleccion-poetica.epub
```

De esta forma, cada título puede localizarse y mantenerse independientemente.

## Convención de Releases

Los Releases siguen esta convención:

```text
cv-XXX
```

Donde `XXX` corresponde al número editorial del libro.

Ejemplos:

```text
cv-001
cv-002
cv-003
```

Cada Release debe corresponder a un único título del catálogo de Casa Villalba.

### Ejemplo

```text
Release
cv-001

Título
Selección poética

Autor
Sor Juana Inés de la Cruz

Assets
seleccion-poetica.pdf
seleccion-poetica.epub
```

## Convención de nombres de archivos

Los archivos deben utilizar nombres simples, permanentes y compatibles con URLs.

Se recomienda:

- usar minúsculas;
- utilizar guiones `-` entre palabras;
- evitar espacios;
- evitar caracteres especiales;
- evitar números de versión salvo que sean realmente necesarios.

Ejemplo:

```text
seleccion-poetica.pdf
seleccion-poetica.epub
```

Evitar nombres como:

```text
Seleccion Poetica FINAL 2.pdf
libro_nuevo_definitivo_v4.epub
```

## URLs de descarga

Los archivos publicados mediante GitHub Releases pueden enlazarse directamente desde Casa Villalba.

La estructura general es:

```text
https://github.com/despegaa-com/casavillalba-library/releases/download/{release}/{archivo}
```

Ejemplo:

```text
https://github.com/despegaa-com/casavillalba-library/releases/download/cv-001/seleccion-poetica.pdf
```

y:

```text
https://github.com/despegaa-com/casavillalba-library/releases/download/cv-001/seleccion-poetica.epub
```

Estas URLs pueden utilizarse directamente desde el catálogo de Casa Villalba.

Por ejemplo:

```ts
{
  id: 'cv-001-pdf',
  formato: 'pdf',
  estado: 'disponible',
  descargaUrl:
    'https://github.com/despegaa-com/casavillalba-library/releases/download/cv-001/seleccion-poetica.pdf',
}
```

## Actualización de una edición

Cuando se corrige o actualiza un archivo digital, debe evitarse crear nombres arbitrarios como:

```text
final.pdf
final-2.pdf
final-ahora-si.pdf
```

Siempre que sea posible, el archivo debe conservar su nombre estable:

```text
seleccion-poetica.pdf
```

Si una modificación constituye una nueva edición editorial significativa, puede publicarse como un nuevo Release o identificador, según corresponda al catálogo de Casa Villalba.

Las modificaciones menores, como correcciones tipográficas o ajustes técnicos, pueden documentarse en las notas del Release.

## Notas de cada Release

Cada Release debería indicar como mínimo:

- título;
- autor;
- identificador editorial;
- formatos disponibles;
- información relevante sobre la edición;
- fecha de publicación o actualización;
- enlace a la ficha oficial del libro.

Ejemplo:

```markdown
## Selección poética

**Autor:** Sor Juana Inés de la Cruz  
**Edición:** Casa Villalba Editorial  
**Identificador:** cv-001

### Formatos

- PDF
- EPUB

### Más información

https://casavillalba.com/libros/poesia-sor-juana
```

## Estadísticas de descarga

GitHub mantiene un contador de descargas para los archivos publicados como assets de Releases.

Estos datos pueden utilizarse como una referencia básica para conocer el número de descargas de cada formato.

Las estadísticas pertenecen al archivo concreto del Release y no deben considerarse equivalentes a lectores únicos.

## Repositorio del sitio web

Este repositorio contiene únicamente los archivos de distribución editorial.

El sitio web, sus componentes, datos editoriales y lógica de aplicación se mantienen en:

```text
despegaa-com/casavillalba
```

La separación es intencional:

```text
casavillalba
→ sitio web
→ código
→ catálogo
→ metadata editorial

casavillalba-library
→ archivos publicados
→ PDF
→ EPUB
→ GitHub Releases
```

## Contribuciones

Este repositorio no está planteado como un proyecto comunitario de software.

Los Pull Requests externos pueden no ser aceptados.

Para informar de errores relacionados con una publicación, erratas o problemas con un archivo, utilice los canales oficiales de contacto de Casa Villalba.

## Obras y derechos editoriales

Algunas de las obras publicadas por Casa Villalba pueden encontrarse en el dominio público.

Sin embargo, que una obra original se encuentre en el dominio público no implica necesariamente que todos los elementos de una edición de Casa Villalba estén libres de derechos.

Una edición puede contener elementos sujetos a derechos independientes, entre ellos:

- traducciones;
- prólogos;
- introducciones;
- notas;
- selección y organización editorial;
- ilustraciones;
- fotografías;
- diseño;
- portada;
- composición;
- maquetación;
- otros materiales originales.

Las condiciones aplicables a cada publicación deberán indicarse en el propio libro, en sus créditos o en la información asociada a su Release.

Salvo que una publicación indique expresamente lo contrario, no debe asumirse que todos los materiales editoriales de Casa Villalba se encuentran bajo dominio público o bajo una licencia abierta.

## Licencia del repositorio

La existencia pública de este repositorio facilita el acceso y la descarga de las publicaciones, pero no concede por sí misma derechos adicionales sobre las obras o elementos editoriales incluidos en los archivos.

Las condiciones de uso y distribución de cada publicación se determinan individualmente.

Consulte los créditos y avisos legales incluidos en cada edición.

---

**Casa Villalba Editorial**

Leer. Conservar. Volver.
