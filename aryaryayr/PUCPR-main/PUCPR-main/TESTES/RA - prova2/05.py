import math

def area_base_circulo(r):
    return math.pi * r ** 2

def comprimento_base_circulo(r):
    return 2 * math.pi * r

def area_cilindro(h, r):
    return 2*area_base_circulo(r) + h*comprimento_base_circulo(r)

h = float(input('Altura do cilindro (cm): '))
r = float(input('Raio da base do cilindro (cm): '))
area = area_cilindro(h, r)

print(f'Area do Cilindro = {area}cm²')