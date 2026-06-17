"""
A function which validates PIC (Finnish Personal Identity)
"""

from datetime import date

def is_it_valid(pic: str) -> bool:
    if len(pic) != 11:
        return False

    CONTROL_CHARS = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    CENTURY_MARKERS = {"+": 1800, "-": 1900, "A": 2000}

    day   = int(pic[0:2])
    month = int(pic[2:4])
    year  = int(pic[4:6])
    century_marker = pic[6]
    personal_id = pic[7:10]
    control_char = pic[10]

    # Valida marcador de século
    if century_marker not in CENTURY_MARKERS:
        return False

    # Monta o ano completo
    full_year = CENTURY_MARKERS[century_marker] + year

    # Valida a data
    try:
        date(full_year, month, day)
    except ValueError:
        return False

    # Valida o caractere de controle
    nine_digits = int(pic[0:6] + personal_id)
    remainder = nine_digits % 31
    if CONTROL_CHARS[remainder] != control_char:
        return False

    return True


if __name__ == "__main__":
    print(is_it_valid("230827-906F"))  # True
    print(is_it_valid("120488+246L"))  # True
    print(is_it_valid("310823A9877"))  # True
    print(is_it_valid("131052-308T"))  # False - data inválida
    print(is_it_valid("130252-308T"))  # False - data inválida
