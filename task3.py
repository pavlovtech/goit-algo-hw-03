import re

def normalize_phone(phone_number):
    # Remove all characters except digits and '+'
    clean_number = re.sub(r'[^\d+]', '', phone_number.strip())
    
    # Check if the number includes an international prefix
    if clean_number.startswith('+'):
        # Remove redundant plus signs if more than one
        clean_number = '+' + clean_number.lstrip('+')
    elif clean_number.startswith('380'):
        # Add '+' if the number starts with the country code but lacks '+'
        clean_number = '+' + clean_number
    else:
        # Assume the number is a local Ukrainian number and prepend '+38'
        clean_number = '+38' + clean_number

    return clean_number

# Test
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
