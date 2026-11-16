# Retrospectiva del sprint 1 (semanas 1 y 2)

- **Facilitó y redactó:** Antonio Revilla (Líder del sprint 1)
- **Participantes:** Antonio Revilla, Carlos Granda y Carlos Hernández
- **Duración:** 30 minutos

## Cómo nos fue

| Medida | Planificado | Logrado |
|---|---|---|
| Historias (HU1, HU2) | 4 puntos | 0 puntos (0 %) |
| Tareas técnicas (T1 a T6) | 6 | 1 parcial: repositorio creado (T1), sin protección ni tablero |
| Documentos | — | Tarea 2, Tarea 3 (diagramas `.puml` nivel 1 y 2), Taller 1 parte 2 (arquitectura) y estrategia de pruebas en `docs/` |
| Estructura del código | — | Carpetas por capas en `backend/` y MVC en `mobile/` |

No llegamos a la meta de cumplimiento del 80 % del Taller 2. La capacidad del sprint se fue en los entregables del curso, que no estaban planificados como trabajo del sprint.

## Qué funcionó

- La documentación quedó ordenada en `docs/`, una carpeta numerada por entrega e índice en el README. Los diagramas de casos de uso están en PlantUML, así que se pueden editar.
- Usamos Conventional Commits y una rama por tema desde el primer commit.
- Acordamos la estructura de `backend/` (capas) y `mobile/` (MVC) antes de escribir código, siguiendo la arquitectura del Taller 1.

## Qué no funcionó

- Todo se integró sin pull requests: las ramas se fusionaban en local con `--no-ff` desde una sola cuenta. No hubo revisión y el historial no muestra el trabajo de cada integrante.
- El backlog solo existía en el PDF de la Tarea 2. Sin issues ni tablero, no teníamos cómo seguir el avance del sprint.
- Las tres ramas largas (`develop`, `testing` y `main`) obligaban a hacer tres fusiones por cambio y no encajan con *squash and merge*.
- No reservamos tiempo para los entregables del curso, y eso desplazó las historias del sprint.

## Acciones de mejora

| N.º | Acción | Responsable | Fecha | Estado |
|---|---|---|---|---|
| 1 | Todo cambio entra por un PR desde una rama `tipo/N-descripcion`, con revisión de otro integrante y `main` protegida | Calidad y DevOps (Antonio Revilla) | Semana 3 | En curso |
| 2 | Cargar el backlog como issues en el Project y actualizar el tablero en cada seguimiento | Líder (Carlos Granda) | Semana 3 | En curso |
| 3 | Registrar cada entregable del curso como un issue `documentación` con talla, para que cuente en la capacidad del sprint | Analista (Carlos Hernández) | Semana 3 | En curso |

## Cambios que llevamos al sprint 2

- HU1 y HU2 (Must) y las tareas T2 a T6 pasan al sprint 2.
- HU7 (Should) pasa al sprint 3 para no superar la capacidad del sprint 2. Queda registrado en un issue con la etiqueta `cambio`.
- Adoptamos GitHub Flow. Las ramas `develop` y `testing` quedan congeladas (ver [PROCESO.md](../PROCESO.md#e2-decisión)).
