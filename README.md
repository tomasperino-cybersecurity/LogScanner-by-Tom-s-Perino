# Simple Python Security Monitor (EN)

A Python script designed to analyze authentication logs for common security threats.

## Features
- **Brute Force Detection**: Identifies IPs with 3 or more failed login attempts.
- **After-Hours Monitoring**: Flags successful logins that occur outside of standard business hours (09:00 - 18:00).
- **IP Tracking**: Monitors repeated access attempts from the same source.

## How it Works
The script parses a list of log entries (simulated or from a file) and uses `datetime` objects to perform temporal analysis and dictionaries for frequency tracking.

## Usage
1. Clone the repository.
2. Run the script: `logscanner.py`

## Analyst Response Workflow (Playbook)

As a Cybersecurity Analyst, when this script triggers an alert, I follow these SOC (Security Operations Center) steps:

### 1. Brute Force Alert (Multiple Failed Logins)
- **Triage**: Verify if the failed attempts are for a single user or multiple accounts.
- **Containment**: If the IP is external and unknown, temporarily block it at the Firewall level.
- **Investigation**: Check if the IP belongs to a known VPN or a legitimate employee who might have forgotten their password.

### 2. After-Hours Access Warning
- **Verification**: Check if there was a scheduled maintenance or an approved change request for that user.
- **Communication**: Contact the user or their manager to confirm the activity was authorized.
- **Escalation**: If the activity is unauthorized, treat it as an **Account Compromise** and force a password reset + session termination.

### 3. Reporting
- Document the source IP, timestamps, and affected accounts in the incident ticketing system.
- Update the **Blocklist** if the IP shows persistent malicious patterns.

### Monitor de Seguridad Simple en Python (ES)
Un script ligero en Python diseñado para analizar logs de autenticación en busca de amenazas de seguridad comunes.

### Características
Detección de Fuerza Bruta: Identifica IPs con 3 o más intentos de inicio de sesión fallidos.

### Monitoreo Fuera de Horario: Marca los inicios de sesión exitosos que ocurren fuera del horario laboral estándar (09:00 - 18:00).

### Rastreo de IPs: Monitorea intentos de acceso repetidos desde la misma fuente.

### Cómo funciona
El script analiza una lista de entradas de log (simuladas o desde un archivo) y utiliza objetos datetime para realizar análisis temporales y diccionarios para el seguimiento de frecuencias.

### Uso
Clona el repositorio.

Ejecuta el script: logscanner.py

### Respuesta del Analista (Playbook)
Como Analista de Ciberseguridad, cuando este script activa una alerta, sigo estos pasos de un SOC (Centro de Operaciones de Seguridad):

1. ### Alerta de Fuerza Bruta (Múltiples inicios de sesión fallidos)
Triage (Clasificación): Verificar si los intentos fallidos son para un solo usuario o para múltiples cuentas.

Contención: Si la IP es externa y desconocida, bloquearla temporalmente a nivel de Firewall.

Investigación: Comprobar si la IP pertenece a una VPN conocida o a un empleado legítimo que podría haber olvidado su contraseña.

2. ### Aviso de Acceso Fuera de Horario
Verificación: Comprobar si hubo un mantenimiento programado o una solicitud de cambio aprobada para ese usuario.

Comunicación: Contactar al usuario o a su responsable para confirmar si la actividad fue autorizada.

Escalada: Si la actividad no está autorizada, tratarla como una Cuenta Comprometida y forzar el restablecimiento de contraseña.

3. ### Reporte
Documentar la IP de origen, las marcas de tiempo y las cuentas afectadas en el sistema de tickets de incidentes.

Actualizar la Lista de Bloqueo (Blocklist) si la IP muestra patrones maliciosos persistentes.
