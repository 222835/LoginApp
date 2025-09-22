# LoginApp
Aplicación web simple en **Python (Flask)** utilizando **MariaDB** para el manejo de base de datos. La aplicación demuestra buenas prácticas básicas de seguridad para el manejo de contraseñas utilizando hashing.

## Características
- Registro de usuarios con validaciones:
  - El nombre de usuario solo puede contener letras y números (5–20 caracteres).
  - La contraseña debe tener al menos 6 caracteres, y utilizar mínimo 1 número, 1 letra y 1 símbolo.
- **Hashing seguro de contraseñas** con `werkzeug.security` (PBKDF2).
- Inicio y cierre de sesión mediante **sesiones seguras** en Flask.
