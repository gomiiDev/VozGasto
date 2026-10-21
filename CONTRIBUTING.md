# Cómo trabajamos en Voz Gasto

## Ramas

| Rama | Para qué sirve | Quién hace merge |
|---|---|---|
| `main` | Versiones entregadas. Cada merge lleva un tag (`v0.1.0`, `v1.0`, `v1.1`). | Líder |
| `testing` | Revisión y pruebas de lo que está en `develop` antes de entregarlo. | Responsable de pruebas |
| `develop` | Integración diaria del equipo. | Cualquier integrante, con revisión |

Las ramas de trabajo salen de `develop`:

- `feature/<tema>`: funcionalidad nueva (por ejemplo `feature/hu1-crear-cuenta`)
- `docs/<tema>`: documentación
- `chore/<tema>`: configuración, estructura o herramientas
- `fix/<tema>`: corrección de errores

## Flujo

1. Actualizar `develop` y crear la rama de trabajo.
2. Hacer commits pequeños.
3. Abrir un PR hacia `develop`. Otro integrante lo revisa y lo aprueba.
4. Al cerrar un sprint, abrir un PR `develop` → `testing`.
5. Si las pruebas pasan, abrir un PR `testing` → `main` y crear el tag de la versión.
6. Si se corrige algo en `testing`, llevar esa corrección también a `develop`.

Los merges se hacen sin fast-forward (`--no-ff`) para que quede visible de dónde viene cada cambio.

## Mensajes de commit

Usamos [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/) en español:

```
<tipo>(<alcance opcional>): <descripción en presente>
```

| Tipo | Uso |
|---|---|
| `feat` | Funcionalidad nueva |
| `fix` | Corrección de un error |
| `docs` | Documentación |
| `test` | Pruebas |
| `chore` | Configuración, estructura o dependencias |
| `refactor` | Cambio de código sin cambiar comportamiento |

Ejemplos:

```
feat(backend): agregar endpoint /usuarios para crear cuenta (HU1)
docs(uml): agregar diagrama de casos de uso nivel 2
chore(mobile): crear estructura MVC en lib
```

## Responsables por área

| Área | Responsable |
|---|---|
| `backend/` (salvo `nlp/` y `tests/`) | Antonio Revilla |
| `backend/app/nlp/`, `backend/tests/`, `docs/06-pruebas/` | Carlos Granda |
| `mobile/` | Carlos Hernández |
