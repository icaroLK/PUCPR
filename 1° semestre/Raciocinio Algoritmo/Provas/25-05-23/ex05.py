import math

def area_base_circulo(raio):
    AB = math.pi * (raio**2)
    return AB

def comprimento_base_circulo(raio):
    CB = 2 * math.pi * raio
    return CB

def area_cilindro(alt, raio):
    A = 2 * area_base_circulo(raio) + alt * comprimento_base_circulo(raio)
    return A

altura = float(input('Altura: '))
raio = float(input('Raio da base: '))
print('O cilindro tem uma área igual a {}'.format(area_cilindro(altura, raio)))

