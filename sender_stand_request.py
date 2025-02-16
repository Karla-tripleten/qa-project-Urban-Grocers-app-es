import configuration
import requests
import data

def post_new_user(body): # Función para crear un nuevo usuario
    user_creation_response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers) # inserta los encabezados
    return user_creation_response.json()

#Función para obtener el token del usuario creado
def get_new_user_token():
    new_user = post_new_user(data.user_body) #Crear un nuevo usuario
    return new_user ["authToken"]  # Extraer token

#Función para crear un nuevo kit de usuario
def post_new_client_kit(kit_body, auth_token):
    new_kit = requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,  # URL para crear el kit
        json=kit_body.copy(),  # Copiar el cuerpo del kit para no modificar el original
        headers={
            "Authorization": f"Bearer {auth_token}",  # Usar el token de autenticación
            "Content-Type": "application/json"  # Establecer el tipo de contenido a JSON
        }
    ) # Realizar la solicitud POST y devolver la respuesta
    return new_kit

response = post_new_user(data.user_body) #El nuevo usuario generado se guarda en esta variable
user_token = get_new_user_token() #Se obtiene el token de ese usuario
kit_response = post_new_client_kit(data.kit_body, user_token) #Respuesta a la creación del kit
print (data.user_body) #Imprimir los datos enviados

response_raw = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=data.user_body.copy(),
                             headers=data.headers)#Imprimir la respuesta en formato JSON
print (response_raw.status_code) #Imprimir la respuesta
print (response) #Imprimir la respuesta completa
print (response.get("authToken")) #Imprimir token y nombre de usuario
print (kit_response)
print (kit_response.json().get("name"))







