# Voz Gasto

Aplicación móvil para registrar ingresos y gastos por voz, clasificarlos por categoría y controlarlos frente a un presupuesto mensual.

- **Materia:** Construcción y Evolución de Software, ESPE
- **Docente:** Ing. Nancy Betancourt
- **NRC:** 36848, Grupo N.º 4

## Integrantes

| Integrante | Rol |
|---|---|
| Antonio Revilla | Líder del proyecto y backend |
| Carlos Granda | Módulo de voz, PLN y pruebas |
| Carlos Hernández | App móvil en Flutter |

## Arquitectura

| Nivel | Arquitectura | Tecnología | Carpeta |
|---|---|---|---|
| General | Cliente-servidor de tres niveles | — | — |
| Frontend | MVC | Flutter (Android e iOS) | [mobile/](mobile/) |
| Backend | Capas | FastAPI + PostgreSQL | [backend/](backend/) |

El detalle está en [docs/05-arquitectura/](docs/05-arquitectura/).

## Estructura del repositorio

```
docs/      Documentación del proyecto (definición, requisitos, UML, arquitectura, pruebas)
backend/   Servidor FastAPI organizado en capas
mobile/    App Flutter organizada con MVC
infra/     Docker y despliegue
.github/   Plantillas de PR e issues, y flujos de CI
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

## Ramas

| Rama | Uso |
|---|---|
| `main` | Versiones entregadas, cada una con su tag |
| `testing` | Revisión y pruebas antes de pasar a `main` |
| `develop` | Integración del trabajo del equipo |

El flujo de trabajo está en [CONTRIBUTING.md](CONTRIBUTING.md).
