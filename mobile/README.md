# App móvil – Flutter

Responsable: Carlos Hernández. Patrón MVC.

| Carpeta | Parte | Responsabilidad |
|---|---|---|
| `lib/models/` | Modelo | Clases de datos: usuario, categoría, movimiento, presupuesto |
| `lib/views/` | Vista | Pantallas y widgets; no contienen lógica de negocio |
| `lib/controllers/` | Controlador | Reciben las acciones del usuario, llaman a los servicios y actualizan la vista |
| `lib/services/` | Apoyo | Cliente de la API y reconocimiento de voz del sistema operativo |
| `assets/` | — | Imágenes, íconos y fuentes |
| `test/` | — | Pruebas de widgets y controladores |

El proyecto Flutter (`pubspec.yaml`, `android/`, `ios/`) se genera dentro de esta carpeta con `flutter create` cuando empiece el desarrollo.
