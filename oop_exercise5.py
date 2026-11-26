#Practice 5: Temperature Converter
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return  ( 9/5 * celsius + 32)
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return  ( 5/9 * (fahrenheit - 32))
    @staticmethod
    def celsius_to_kelvin(celsius):
        return  (celsius + 273.15)
celsius = 25
fahrenheit = Temperature.celsius_to_fahrenheit(celsius)
celsius_again = Temperature.fahrenheit_to_celsius(fahrenheit)
kelvin = Temperature.celsius_to_kelvin(celsius)
print("celsius:", celsius)
print("fahrenheit:", fahrenheit)
print("kelvin:", kelvin)    
    
    
