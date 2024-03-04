import pyrebase     #importar o pyrebase4 no pip
import getpass      #leitura da senha sem eco

firebaseConfig = {
    "apiKey": "",
    "authDomain": "",
    "projectId": "",
    "databaseURL": "https://" + "<ID_APP>" + ".firebaseio.com",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
user = input("Digite seu e-mail: ")
password = getpass.getpass("Digite sua senha, com pelo menos 6 caracteres: ")
status = auth.create_user_with_email_and_password(user,password)
print("Resultado: ", status)
pausa = input('Pressione ENTER para finalizar...')

# Baseado em código de https://aicodeconvert.com/



