nome = input()
salario = float(input())
total_vendas = float(input())
comissao = float(total_vendas) * (15/100)
soma = float(salario + comissao)
print("TOTAL = R$ {:.2f}".format(soma))