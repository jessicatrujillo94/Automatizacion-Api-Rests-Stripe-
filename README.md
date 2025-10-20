# Sansisoft

## Descripción de la Aplicación

**ClickUp** es una plataforma de gestión de proyectos y productividad que centraliza en un solo lugar las tareas, documentos, comunicación y seguimiento del trabajo de los equipos. Está diseñada para reemplazar múltiples herramientas (como Trello, Asana, Jira, Slack, Docs, etc.) y facilitar la organización del trabajo diario.

Este repositorio contiene un conjunto de **pruebas automatizadas** para validar el comportamiento de la API de Reddit utilizando Pytest.

---

## Tipos de Pruebas Incluidas

- **Exploratorias**:
  - Colecciones de pruebas disponibles en el archivo `colecciones_postman.json`.
- **Smoke Tests**:
- Comprenden los test cases que prueban el happy path.
- **Pruebas Funcionales**:
  - Verifican que cada funcionalidad de la API cumpla con los requerimientos esperados, basandose en la documentacion.
- **Pruebas de Regresión**:
  - Comprende todas las pruebas realizadas.
 
---

## Funcionalidades probadas (2do Sprint)

### 1. Tareas
Permite a los usuarios autenticados crear, consultar, editar y eliminar tareas dentro de una lista.

**Endpoints probados:**
- Crear tarea → `POST /api/v2/list/{list_id}/task`  
- Ver tarea → `GET /api/v2/task/{task_id}`  
- Editar tarea → `PUT /api/v2/task/{task_id}`  
- Eliminar tarea → `DELETE /api/v2/task/{task_id}`  

---

### 2. Folders
Gestión de carpetas dentro de un espacio o lista, facilitando la organización de tareas y listas.

**Endpoints probados:**
- Crear folder → `POST /api/v2/folder/{space_id}`  
- Ver folder → `GET /api/v2/folder/{folder_id}`  
- Editar folder → `PUT /api/v2/folder/{folder_id}`  
- Eliminar folder → `DELETE /api/v2/folder/{folder_id}`  

---

### 3. Listas
Permite a los usuarios gestionar listas dentro de un espacio o carpeta.

**Endpoints probados:**
- Crear lista → `POST /api/v2/folder/{folder_id}/list`  
- Ver lista → `GET /api/v2/list/{list_id}`  
- Editar lista → `PUT /api/v2/list/{list_id}`  
- Eliminar lista → `DELETE /api/v2/list/{list_id}`  

---

### 4. Grupos
Gestión de grupos de usuarios dentro de un Workspace, facilitando la asignación de permisos y organización de equipos.

**Endpoints probados:**
- Crear grupo → `POST /api/v2/team/{team_id}/group`  
- Obtener grupo(s) → `GET /api/v2/group?team_id={team_id}&group_ids={group_id}`  
- Editar grupo → `PUT /api/v2/group/{group_id}`  
- Eliminar grupo → `DELETE /api/v2/group/{group_id}` 


---

## Ejecución de Pruebas

### Variables de entorno necesarias

En el archivo del workflow (`.github/workflows/...`) se definen las siguientes variables que deben estar disponibles como **GitHub Secrets**:

- **TOKEN** → Token de autenticación válido  
- **BASE_URL** → URL base de la API de ClickUp  
- **ID_WORKSPACE** → Identificador del Workspace  
- **ID_FOLDER** → Identificador de un Folder  
- **TOKEN_CADUCADO** → Token expirado para pruebas negativas  
- **ID_SPACE** → Identificador de un Space  
- **TOKEN_SIN_PERMISO** → Token sin permisos suficientes

---

### Pasos de ejecución manual (local)

Si deseas correr las pruebas en tu entorno local, sigue los siguientes pasos:

1. Clona el repositorio:
   ```bash
   git clone --branch development https://github.com/LeonelGongora/Sansisoft.git
   ```
   
2. Crear entorno virtual
   ```bash
   python -m venv .venv
   ```

3. Acceder al entorno virtual
   ```bash
   .\.venv\Scripts\Activate.ps1
   ```
   
4. Instalar los modulos requeridos con requirements.txt
   ```bash
   pip install -r requirements.txt
   ```

5. Ejecuta las pruebas de Pytest en la raiz del proyecto :
   ```bash
   pytest
    ```
6. Para generar el reporte de pytest:
   ```bash
   pytest --html=pytest.html
    ```
7. Ejecutar por mark Los marks disponibles son:
- smoke 
- regression 
- functional
 ```bash
pytest -m smoke --html=report.html
```
### Ejecución desde la interfaz de GitHub

El workflow se llama run manual tests y permite la ejecución manual con parámetros:

- marks → introduces el tipo de pruebas a ejecutar (smoke, regression, functional, all)
- suites → introduces la carpeta de pruebas (Groups, Lists, XFolders, Tasks)

### Pasos:

1. Ir a la pestaña Actions del repositorio.
2. Seleccionar el workflow run manual tests.
3. Hacer clic en Run workflow.
4. Ingresar los valores de marks y/o suites.
5. Confirmar la ejecución.

El reporte de resultados quedará disponible en la sección de artefactos del workflow.

---





