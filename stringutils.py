def is_palindrome(text: str) -> bool:
    """
    Verifica se o texto é um palíndromo, ignorando espaços e
    diferenças entre maiúsculas e minúsculas.
    """
    normalized = "".join(char.lower() for char in text if char != " ")
    return normalized == normalized[::-1]