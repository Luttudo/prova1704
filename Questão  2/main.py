import pytest

# Enunciado

# Você foi designado(a) para realizar testes unitários em Python utilizando Pytest em métodos de string de uma aplicação do cenário a seguir: Link

from testar import (inverter_string, contar_vogais, contar_palavras, eh_palindromo, 
                    maiusculas, minusculas, contar_caracter, concatenar_strings, 
                    substituir_caracter, inverter_palavras)

def test_inverter_string():
    assert inverter_string("abc") == "cba"
    assert inverter_string("123") == "321"

def test_contar_vogais():
    assert contar_vogais("aeiou") == 5
    assert contar_vogais("AEIOU") == 5
    assert contar_vogais("bcdfg") == 0

def test_contar_palavras():
    assert contar_palavras("uma duas três") == 3
    assert contar_palavras("") == 0

def test_eh_palindromo():
    assert eh_palindromo("arara") == True
    assert eh_palindromo("python") == False

def test_maiusculas():
    assert maiusculas("abc") == "ABC"
    assert maiusculas("123") == "123"

def test_minusculas():
    assert minusculas("ABC") == "abc"
    assert minusculas("123") == "123"

def test_contar_caracter():
    assert contar_caracter("banana", "a") == 3
    assert contar_caracter("123123", "2") == 2

def test_concatenar_strings():
    assert concatenar_strings("abc", "def") == "abcdef"
    assert concatenar_strings("123", "456") == "123456"

def test_substituir_caracter():
    assert substituir_caracter("banana", "a", "o") == "bonono"
    assert substituir_caracter("123123", "2", "4") == "143143"

def test_inverter_palavras():
    assert inverter_palavras("abc def") == "cba fed"
    assert inverter_palavras("123 456") == "321 654"
