"""
#Variáveis livres + nonlocal
def fora(x):
    a=x #Var livre
    def dentro():
        #print(locals()) #Var local
        #print(dentro.__code__.co_freevars)
        return a
    return dentro

dentro1 = fora(10)
dentro2 = fora(20)
#print(dentro1())
#print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial
    def interna(valor_a_concatenar):
        nonlocal valor_final
        valor_final+= valor_a_concatenar
        return valor_final
    return interna
c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
print(c('e'))

"""

""""""
# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.


def criar_funcao(func):  #Função decoradora
    def interna(*args, **kwargs):
        print('Oi função dec aqui')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(resultado)
        return resultado
    return interna


@criar_funcao
def inverte_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

invertida = inverte_string('123')
