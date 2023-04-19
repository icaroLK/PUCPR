#  A senha deve ter mínimo 8 e máximo 15 caracteres.
#  A senha deve ter pelo menos uma letra maiúscula.
#  A senha deve ter pelo menos uma letra minúscula.
#  A senha deve ter pelo menos um símbolo. Ex: * ! # $ % & + - / : ; = ? @ \ |
#  A senha deve ter pelo menos um número.
from random import randint, choice

numeros = [0,1,2,3,4,5,6,7,8,9]
alphaP = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphaG = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T', 'U','V','W','X','Y','Z']
especial = ['*', '!', '#', '$', '%', '&', '+', '-', '/', ':', ';', '=', '?', '@','|']
opcoes = [numeros, alphaP, alphaG, especial]
senha = [ ]
qtd = int(input('Quantidade de caracteres [8-15]: '))
