#!/usr/bin/env python3
"""
Mission 05: Number Converter
Converts a positive decimal integer into binary and hexadecimal notations.
"""

def convert_number():
    try:
        raw_input = input("Enter a positive decimal number: ").strip()
        if not raw_input:
            print("Error: Input cannot be empty.")
            return

        decimal_value = int(raw_input)
        if decimal_value < 0:
            print("Error: Please enter a positive integer.")
            return

        binary_str = bin(decimal_value)[2:]
        hex_str = hex(decimal_value)[2:].upper()

        print(f"Binary: {binary_str}")
        print(f"Hexadecimal: {hex_str}")

    except ValueError:
        print("Error: Invalid integer input.")

if __name__ == "__main__":
    convert_number()
