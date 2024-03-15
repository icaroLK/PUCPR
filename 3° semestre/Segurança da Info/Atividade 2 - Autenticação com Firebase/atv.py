import pyrebase  
  
import getpass     

firebaseConfig = {
    "apiKey": "AIzaSyA9FcJ7YoqE_nDR6sltauKpJxRf6BQwZ-8",
    "authDomain": "atividadade-firebase.firebaseapp.com",
    "projectId": "atividadade-firebase",
    "databaseURL": "https://" + "atividadade-firebase" + ".firebaseio.com",
    "storageBucket": "atividadade-firebase.appspot.com",
    "messagingSenderId": "141714896125",
    "appId": "1:141714896125:web:71c4c26f62dca089827a94",
    "measurementId": "G-JNZNCX7VY9"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

user = input("Digite seu e-mail: ")
password = getpass.getpass("Digite sua senha, com pelo menos 6 caracteres: ")

status = auth.create_user_with_email_and_password(user,password)
idToken = status["idToken"]



print("Resultado: ", status)
print("Token: ", idToken)

info = auth.get_account_info(idToken)
print("Info: ", info)


