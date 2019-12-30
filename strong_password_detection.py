import re

# A strong password has:
# At least 8 characters
# Contains both upper and lowercase letters
# At least one digit
def is_strong_password(password):
    strong_password_regex = re.compile(r'''
    ^                         # Start anchor
    (?=.*[A-Z])               # Ensure string has two uppercase letters.
    (?=.*[0-9])        # Ensure string has two digits.
    (?=.*[a-z]) # Ensure string has three lowercase letters.
    .{8,}                     # Ensure string length is at least 8.
    $                         # End anchor
    ''', re.VERBOSE)
    return strong_password_regex.search(password) != None

# Test password strengths
pass1 = "Abc123"
print(is_strong_password(pass1))
pass2 = "Abc12345"
print(is_strong_password(pass2))
pass3 = "12345Abc"
print(is_strong_password(pass3))
pass4 = "cBAc112cas345"
print(is_strong_password(pass4))
pass5 = "2"
print(is_strong_password(pass5))
pass6 = "c"
print(is_strong_password(pass6))
pass7 = "cccc2222"
print(is_strong_password(pass7))