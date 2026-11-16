# Voz Gasto

Aplicación móvil para registrar ingresos y gastos por voz, clasificarlos por categoría y controlarlos frente a un presupuesto mensual.

- **Materia:** Construcción y Evolución de Software, ESPE
- **Docente:** Ing. Nancy Betancourt
- **NRC:** 36848, Grupo N.º 4

## Integrantes

| Integrante | Área técnica | Rol en el sprint 1 | Rol en el sprint 2 |
|---|---|---|---|
| Antonio Revilla | Backend | Líder | Calidad y DevOps |
| Carlos Granda | Voz, PLN y pruebas | Analista | Líder |
| Carlos Hernández | App móvil en Flutter | Calidad y DevOps | Analista |

Las áreas técnicas son fijas. Los roles del proceso rotan cada sprint según el [plan de rotación](docs/proceso/PROCESO.md#b3-plan-de-rotación).

## Arquitectura

| Nivel | Arquitectura | Tecnología | Carpeta |
|---|---|---|---|
| General | Cliente-servidor de tres niveles | — | — |
| Frontend | MVC | Flutter (Android e iOS) | [mobile/](mobile/) |
| Backend | Capas | FastAPI + PostgreSQL | [backend/](backend/) |

El detalle está en [docs/05-arquitectura/](docs/05-arquitectura/).

## Estructura del repositorio

```
docs/      Documentación del proyecto (definición, requisitos, UML, arquitectura, pruebas, proceso)
backend/   Servidor FastAPI organizado en capas
mobile/    App Flutter organizada con MVC
infra/     Docker y despliegue
.github/   Plantillas de PR e issues, script de configuración y flujos de CI
```

## Documentación

| Carpeta | Contenido |
|---|---|
| [01-definicion](docs/01-definicion/) | Acta de constitución, matriz de decisión y registro de riesgos |
| [02-requerimientos](docs/02-requerimientos/) | Requisitos, historias de usuario, backlog y plan de sprints |
| [03-documentacion](docs/03-documentacion/) | Documento de la necesidad (protocolo) |
| [04-uml](docs/04-uml/) | Diagramas de casos de uso (nivel 1 y 2) |
| [05-arquitectura](docs/05-arquitectura/) | Arquitectura de la aplicación (Taller 1) |
| [06-pruebas](docs/06-pruebas/) | Estrategia de pruebas y banco de frases |
| [proceso](docs/proceso/) | Proceso del equipo y actas de retrospectiva |

## Cómo trabajar

Usamos GitHub Flow con una rama por issue: `main` está protegida y todo entra por un pull request revisado.

1. Tomar un issue del tablero y crear la rama `tipo/N-descripcion` desde `main`.
2. Hacer commits `tipo: descripción (#N)`.
3. Abrir un PR hacia `main` con `Closes #N`. Otro integrante lo revisa y lo aprueba.
4. Fusionar con **Squash and merge**.

Las reglas y la definición de terminado están en [CONTRIBUTING.md](CONTRIBUTING.md). Los roles, los eventos y los artefactos están en [docs/proceso/PROCESO.md](docs/proceso/PROCESO.md).
