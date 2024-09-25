
fahrenheit_to_celsius_factor = 5 / 9
celsius_to_fahrenheit_factor = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * fahrenheit_to_celsius_factor

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * celsius_to_fahrenheit_factor) + 32

def main():
    try:
        temp_input = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temp_input)
            print(f"{temp_input}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temp_input)
            print(f"{temp_input}°F is {converted_temp}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
