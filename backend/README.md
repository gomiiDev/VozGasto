# Backend – FastAPI

Responsable: Antonio Revilla. Arquitectura en capas.

| Carpeta | Capa | Responsabilidad |
|---|---|---|
| `app/api/` | Presentación | Endpoints: reciben la petición, validan el token y responden |
| `app/schemas/` | Presentación | Datos de entrada y salida de la API |
| `app/services/` | Negocio | Reglas del presupuesto, saldo, alertas (RN1–RN6) |
| `app/nlp/` | Negocio | Extractor de tipo, monto, categoría y fecha de una frase (responsable: Carlos Granda) |
| `app/repositories/` | Datos | Consultas y escritura en PostgreSQL |
| `app/models/` | Datos | Entidades: usuario, categoría, movimiento, presupuesto |
| `app/core/` | Transversal | Configuración y seguridad (JWT, bcrypt) |
| `tests/` | — | Pruebas unitarias y de integración (responsable: Carlos Granda) |

Regla: cada capa solo llama a la capa de abajo (`api` → `services` → `repositories`).
