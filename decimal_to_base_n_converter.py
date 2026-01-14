"""
    This program will convert any integer base 10 (decimal) number into any base n number
"""
# Get a number from the user to convert and the base they want it in
number = int(input('Enter a number: ').strip())
base = int(input('What base do you want the number respresented?: ').strip())

# Main function will call decimal_convert function and display converted number
def main():
    z = decimal_convert(number, base)
    print(z)

def decimal_convert(n, b):
    """
        x is set to n (the number the user will input).
        From then it will go through the arithmetic process of converting a base 10 number into another base. 
        This involves a while loop, mod, and div. 
        The function will end once x < 0.
    """
    # Initialize an empty string to store the base n number representation
    converted_num = ''

    # Create a temporary variable to hold the changing value of n
    x = n

    # Create while loop
    while x > 0:
        y = str(x % b)   # Variable to store the converted digits into converted_num (x mod b = remainder)
        converted_num += y
        x = x // b  # x will be updated for next iteration (x div b = quotient)

    # Flip string
    converted_num = converted_num[::-1]

    # Loop to remove leading zeros
    while converted_num[0] == 0:
        converted_num = converted_num[1::]

    return int(converted_num)


if __name__ == '__main__':
    main()