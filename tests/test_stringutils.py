import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from stringutils import is_palindrome


def test_palindrome_simples():
    assert is_palindrome("arara") is True


def test_palindrome_com_espaco_e_maiuscula():
    assert is_palindrome("A base do teto desaba") is True


def test_nao_palindrome():
    assert is_palindrome("python") is False


def test_string_vazia():
    assert is_palindrome("") is True