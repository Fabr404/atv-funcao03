
def calcular_area_base(r):
    area = 3.14*r**2
    return area

raio=float(input("digite o valor do raio: "))
resultado = calcular_area_base(raio)
print(f"a area do circulo é {resultado}")

def calcular_volume_cilindro(r, h):
    volume= (3.14*r**2)* h
    return volume

altura = float(input("digite o valor da altura: "))
raio = float(input("digite o raio do cilindro: "))
resultado = calcular_volume_cilindro(raio, altura)
print(f"o volume do cilindro é de : {resultado}")