import random

def get_numbers_ticket(min, max, quantity):
    # Check if the input parameters are valid
    if min < 1 or max > 1000 or quantity < 1 or min > max or (max - min + 1) < quantity:
        return []
    
    # Generate the specified quantity of unique random numbers within the range
    random_numbers = random.sample(range(min, max + 1), quantity)
    
    # Return the sorted list of these numbers
    return sorted(random_numbers)

# Test
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
