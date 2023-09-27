n1 = float(input("digite a sua primeira nota"))
n2 = float(input("digite a sua segunda nota"))
n3 = float(input("digite a sua terceira nota"))
n4 = float(input("digite sua quarta nota"))
media = (n1+n2+n3+n4) / 4
if media >=6:
    print("aprovado", media)
else:
    print("reprovado", media)