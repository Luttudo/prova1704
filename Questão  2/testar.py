def inverter_string(string):
    return string[::-1]

def contar_vogais(string):
    vogais = 'aeiouAEIOU'
    return sum(1 for char in string if char in vogais)

def contar_palavras(string):
    return len(string.split())

def eh_palindromo(string):
    string = string.lower()
    return string == string[::-1]

def maiusculas(string):
    return string.upper()

def minusculas(string):
    return string.lower()

def contar_caracter(string, caracter):
    return string.count(caracter)

def concatenar_strings(string1, string2):
    return string1 + string2
  
def substituir_caracter(string, velho, novo):
    return string.replace(velho, novo)

def inverter_palavras(string):
    palavras = string.split()
    palavras_invertidas = [palavra[::-1] for palavra in palavras]
    return ' '.join(palavras_invertidas)