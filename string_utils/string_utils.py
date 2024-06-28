def reverse_string(s: str) -> str:
    """Return the reversed string."""
    return s[::-1]

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome."""
    s = s.lower().replace(' ', '')
    return s == s[::-1]
