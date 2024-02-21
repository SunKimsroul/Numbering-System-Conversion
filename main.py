#####Converts a hexadecimal string to its decimal
def hexToDecimal(hexString):
    """
    Converts a hexadecimal string to its decimal equivalent.
    :param hexString: str, hexadecimal string
    :return: int, decimal equivalent
    """
    return int(hexString, 16)

def main():
    # Receive an input from the user
    hexString = input("Please enter a hexadecimal string: ")

    # Convert the hexadecimal string to its decimal equivalent
    decimal = hexToDecimal(hexString)

    # Print the output
    print(f"The decimal equivalent of hexadecimal {hexString} is {decimal}.")

# Call the main function
if __name__ == "__main__":
    main()



#####Converts a decimal number to its binary
def decimalToBinary(decimalValue):
    """
    Converts a decimal number to its binary string representation.
    :param decimalValue: int, decimal number
    :return: str, binary string representation
    """
    return bin(decimalValue)[2:]  # bin() returns binary string prefixed with '0b', so slice it off.

def main():
    # Receive an input from the user
    decimalValue = int(input("Please enter a decimal number: "))

    # Convert the decimal number to its binary string representation
    binaryString = decimalToBinary(decimalValue)

    # Print the output
    print(f"The binary string representation of decimal {decimalValue} is {binaryString}.")

# Call the main function
if __name__ == "__main__":
    main()