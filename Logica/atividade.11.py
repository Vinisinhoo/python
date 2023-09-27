valor= float(input("digite o valor"))
formadepagamento=input("digite a forma de pagamento")
if formadepagamento=='à vista em dinheiro ou cheque':
    print(valor*10/100)
if formadepagamento=='à vista no cartão':
    print(valor*15/100)
if formadepagamento=='à vista no cartão em duas vezes sem juro':
    print(valor)
if formadepagamento=='à vista no cartão em duas vezes com juros':
    print(valor+10/100*valor)
