nome = "Ana"
idade = 25
altura = 1.65
peso = 60
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Peso:", peso)
imc = peso / (altura ** 2)
print("IMC:", imc)
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade grau 1")
elif imc < 40:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")
print("Fim do programa")