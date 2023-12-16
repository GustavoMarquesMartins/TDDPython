from bytebank import Funcionario

funcionario = Funcionario("Paulo Bragança", "11/12/2000", 100000)

resultado = funcionario.__str__()
print(resultado)

resultado2 = str(funcionario)
print(resultado2)
