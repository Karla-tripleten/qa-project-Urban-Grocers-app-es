import data
import sender_stand_request

# Codigo para obtener el nombre del kit creado por el usuario
def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

#Codigo para obtener el token del nuevo usuario generado
def get_new_user_token():
    user_body = data.user_body
    response = sender_stand_request.post_new_user(user_body)
    return response["authToken"]

def positive_assert(kit_body):
    new_kit = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert new_kit.status_code == 201
    new_kit_json = new_kit.json()
    assert new_kit_json["name"] == kit_body["name"]


def negative_assert_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400


def test1_create_kit_1_letter_in_the_name_success_response(): #Función para probar el número mínimo de caracteres (1)
    current_kit_body = get_kit_body(data.test1_kit_name)
    positive_assert(current_kit_body)

def test2_create_kit_511_letter_in_the_name_success_response(): #Función para probar el maximo de caracteres (511)
    current_kit_body = get_kit_body(data.test2_kit_name)
    positive_assert(current_kit_body)

def test3_create_kit_without_name(): #Función para probar el ingreso de un kit, sin colocar el nombre
    current_kit_body = get_kit_body(data.test3_kit_name)
    negative_assert_400(current_kit_body)

def test4_create_kit_512_letter_in_the_name():
    current_kit_body = get_kit_body(data.test4_kit_name)
    negative_assert_400(current_kit_body)

def test5_kit_especial_caracter_in_the_name_success_response():
    current_kit_body = get_kit_body(data.test5_kit_name)
    positive_assert(current_kit_body)

def test6_kit_with_space_caracter_in_the_name_sucess_response():
    current_kit_body = get_kit_body(data.test6_kit_name)
    positive_assert(current_kit_body)

def test7_kit_with_number_caracter_in_the_name_sucess_response():
    current_kit_body = get_kit_body(data.test7_kit_name)
    positive_assert(current_kit_body)

def test8_create_kit_without_name_parameter():
    current_kit_body = data.kit_body.copy()
    current_kit_body.pop("name")
    negative_assert_400(current_kit_body)

def test9_create_kit_with_number_parameter():
    current_kit_body = get_kit_body(data.test9_kit_name)
    negative_assert_400(current_kit_body)
