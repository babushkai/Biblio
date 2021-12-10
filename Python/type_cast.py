from fastnumbers import fast_real

def type_check(string):
    if isinstance(string, str):
        fast_real(string)
    else:
        TypeError