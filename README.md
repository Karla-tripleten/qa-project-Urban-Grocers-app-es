# Proyecto Urban Grocers Karla_Muñoz

### Descripción de las secciones:

# Descripción del proyecto:  
Urban Grocers es un API que sirve para hacer pedidos de comida, el usuario puede crear  
sus propios kits de comida

# Documentación

Para la documentación de la API se utilizó apiDoc.  
Para generar la documentación, se utilizo el siguiente link: 
https://cnt-bd84dfb9-9b09-4029-aa4a-57bc2ceeca12.containerhub.tripleten-services.com/docs/#api-Main.Kits-CreateKit

# Requisitos previos: 
El proyecto utiliza lenguaje Python y los paquetes de python pip y pytest

# Instalación**: 
El repositorio se clona a través de Github, ingresando el comando:  
git clone git@github.com:username/qa-project-Urban-Grocers-app-es.git
**No olvidar de crear primero una clave SSH desde la computadora para agregarla a la cuenta de Github**

# Tecnologías y Técnicas Utilizadas

- Lenguaje: Python 3.11  
- Framework de Pruebas: pytest  
- Documentación: apiDoc  
- Metodología: Se utilizó Test-Driven Development (TDD) para escribir pruebas antes de desarrollar las funcionalidades.  
- Validación: Se realizaron pruebas unitarias y de integración con diferentes entradas para verificar el correcto 
  funcionamiento del sistema.  


# Ejecución de pruebas:
    - El archivo create_kit_name_kit_test.py contiene las funciones declaradas para ejecutar  
     las pruebas automatizadas para el parámetro "name" que se necesita para que el usuario cree
     su propio kit
     

# Archivos importantes: 
- `data.py`: Contiene los datos de prueba: los cuerpos de las solicitudes para los usuarios y kits; así como
los datos usados para hacer pruebas en el parámetro "name" para la creación de un kit hecho por el usuario
- `sender_stand_request.py`: Contiene funciones para interactuar con la API (crear usuarios y kits).
- `create_kit_name_kit_test.py`: Contiene las pruebas de creación de kits para el proyecto en el parámetro "name"






