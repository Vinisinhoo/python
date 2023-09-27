n1=float(input("digite sua primeira nota"))
n2=float(input("digite sua segunda nota"))
n3=float(input("digite sua terceira nota"))
media=float(input("digite sua média"))
ma=(n1+n2*2+n3*3+media)/7
if ma>=90:
    print("A")
elif 75<=ma<=90:
    print("B")
elif 75>ma>=60:
    print("C")
elif 60>ma>=40:
    print("D")
elif ma<40:
    print("E")
if ma=="A,B,C":
    print("aprovado")
else:
    print("reprovado")
