"""A program that takes in a Hexadecimal Value and returns the decimal value
Hexadecimal system leverages base 16 using 0-9 and A-F (0-15)
The index of each value is 16 raised to it's index starting the right most 
value with 16^0

"""
def hex_output(hex_value):
    decimal_value = None
    hex_value = reversed(hex_value)
    for power, digit in enumerate(hex_value):
        decimal_value += int(digit, 16) * (16 ** power)

    return decimal_value