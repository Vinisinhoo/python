peso=float(input("digite seu peso"))
h=float(input("digite sua altura"))
imc=peso / (h*h) 
if imc<18.5:
    print("abaixo do peso")
if 18.5<imc<25:
    print("peso normal")
if 25<imc<30:
    print("acima do peso")
if imc>30:
    print("obeso") 