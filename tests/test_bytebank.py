import pytest
from pytest import mark
from bytebank import Funcionario


class TestClass:

    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000'  # Given-Contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()  # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_apenas_Carvalho(self):
        entrada = ' Lucas Carvalho '  # Given-contexto
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '13/03/2000', 1111)
        resultado = lucas.sobrenome()  # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_decrecimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000  # Given-contexto
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        paulo = Funcionario(entrada_nome, '13/03/2000', entrada_salario)
        resultado = paulo.decrecimo_salario()  # When-ação

        assert resultado == esperado  # Then-desfecho

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  # Given-contexto
        esperado = 100

        funcionario_test = Funcionario('Teste', '13/03/2000', entrada)
        resultado = funcionario_test.calcular_bonus()  # When-ação

        assert resultado == esperado  # Then-desfecho

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000000  # Given-contexto

            funcionario_teste = Funcionario('Teste', '13/03/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()  # When-ação

            assert resultado  # Then-desfecho

