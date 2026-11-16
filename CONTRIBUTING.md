# Cómo trabajamos en Voz Gasto

Seguimos **GitHub Flow con una rama por issue**. El proceso completo (roles, eventos y artefactos) está en [docs/proceso/PROCESO.md](docs/proceso/PROCESO.md).

## Reglas básicas

- `main` es la única rama larga y está protegida. Nadie sube cambios directo a `main`.
- Todo trabajo empieza con un issue: historia, tarea, defecto o cambio.
- Todo cambio entra por un pull request aprobado por otro integrante.
- Los documentos de `docs/` también se cambian solo por PR.

## Flujo

1. Tomar un issue en **Por hacer**, asignárselo y moverlo a **En progreso**.
2. Actualizar `main` y crear la rama:

   ```bash
   git switch main && git pull
   git switch -c docs/24-proceso-del-equipo
   ```

3. Hacer commits pequeños con la convención de abajo.
4. Subir la rama y abrir un PR hacia `main` con la plantilla. En el cuerpo poner `Closes #N`. Mover el issue a **En revisión**.
5. El revisor (Calidad y DevOps del sprint, o el Líder si el autor es Calidad) comenta y aprueba, o pide cambios.
6. Si pide cambios, el autor los corrige con un commit nuevo en la misma rama y vuelve a pedir revisión.
7. Con la aprobación y las conversaciones resueltas, el autor fusiona con **Squash and merge**. La rama se borra sola y el issue pasa a **Hecho**.

Si `main` avanzó y hay conflicto, se resuelve en la rama del PR:

```bash
git switch docs/26-retro-sprint-1
git pull origin main          # Git marca los archivos en conflicto
# editar, dejar la versión correcta y quitar las marcas <<<<<<< ======= >>>>>>>
git add README.md
git commit -m "docs: resuelve conflicto con main en README (#26)"
git push
```

Después se deja un comentario en el PR que explique cómo se resolvió.

## Nombres de ramas

`tipo/N-descripcion`: N es el número del issue. Todo en minúsculas, sin tildes, con guiones.

| Tipo | Uso | Ejemplo |
|---|---|---|
| `feature` | Funcionalidad nueva | `feature/1-crear-cuenta` |
| `fix` | Corrección de un defecto | `fix/31-saldo-negativo` |
| `docs` | Documentación | `docs/24-proceso-del-equipo` |
| `chore` | Configuración, estructura o herramientas | `chore/19-ci-github-actions` |
| `test` | Pruebas | `test/23-integracion-hu1-hu2` |

## Mensajes de commit

Usamos [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/) en español, con el verbo en presente y el número del issue:

```
<tipo>(<alcance opcional>): <descripción en presente> (#N)
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
feat(backend): crea el endpoint /usuarios (#1)
docs: documenta el proceso del equipo (#24)
fix(mobile): corrige el saldo negativo tras editar (#31)
```

## Pull requests

- **Título:** igual que el commit principal, sin el número. Ejemplo: `docs: documenta el proceso del equipo`.
- **Cuerpo:** la plantilla completa, con `Closes #N`.
- **Revisión:** al menos un comentario de revisión y una aprobación de otro integrante. Intentamos revisar en menos de 24 horas.
- **Fusión:** solo con **Squash and merge**.

## Definición de terminado

Un issue está terminado cuando cumple las siete condiciones:

1. Cumple todos los criterios de aceptación del issue, incluidos los casos de rechazo (CR).
2. El trabajo está en una rama `tipo/N-descripcion` y entró a `main` por un PR con `Closes #N`.
3. Otro integrante revisó y aprobó el PR, y no quedan conversaciones abiertas.
4. Los commits siguen la convención `tipo: descripción (#N)`.
5. La documentación afectada (README, `docs/`, PROCESO.md) está actualizada.
6. Desde la semana 5, las pruebas automáticas y el linter pasan en la CI.
7. El issue quedó en Hecho en el tablero, con Prioridad, Talla y Sprint completos.

## Etiquetas

| Etiqueta | Uso |
|---|---|
| `historia` | Historia de usuario del backlog |
| `tarea` | Trabajo técnico o de proceso que no es una historia |
| `documentación` | Cambios en `docs/`, README o guías |
| `defecto` | Algo no funciona como dicen los criterios de aceptación |
| `cambio` | Cambio de alcance o de plan; lo aprueba la docente |
| `bloqueado` | El issue no puede avanzar; explicar el motivo en un comentario |
| `riesgo` | Riesgo nuevo o actualizado del registro de riesgos |

## Versiones

Cada hito se marca con una etiqueta anotada en `main`, que crea el rol de Calidad y DevOps:

```bash
git switch main && git pull
git tag -a v0.1.0 -m "Versión 0.1.0: núcleo manual con pruebas"
git push origin v0.1.0
```

| Versión | Semana |
|---|---|
| `v0.1.0` | 6 |
| `v1.0.0` | 11 |
| `v1.1.0` | 16 |

## Responsables por área técnica

Estas áreas no rotan. Los roles del proceso sí rotan cada sprint (ver [PROCESO.md](docs/proceso/PROCESO.md#b3-plan-de-rotación)).

| Área | Responsable |
|---|---|
| `backend/` (salvo `nlp/` y `tests/`) | Antonio Revilla |
| `backend/app/nlp/`, `backend/tests/`, `docs/06-pruebas/` | Carlos Granda |
| `mobile/` | Carlos Hernández |
