def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    if unit.lower() == 'c':
        celsius = value
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
    elif unit.lower() == 'f':
        fahrenheit = value
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
    elif unit.lower() == 'k':
        kelvin = value
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
    else:
        return "Invalid unit of measurement"

    return celsius, fahrenheit, kelvin

def main():
    value = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit, K for Kelvin): ")

    result = convert_temperature(value, unit)
    if result != "Invalid unit of measurement":
        celsius, fahrenheit, kelvin = result
        print(f"Temperature in Celsius: {celsius:.2f}°C")
        print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")
        print(f"Temperature in Kelvin: {kelvin:.2f}K")
    else:
        print(result)

if __name__ == "__main__":
    main()
