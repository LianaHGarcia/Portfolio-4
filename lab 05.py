def celsius_to_faren():
    temp_celsius = input("what is the temperature in Celsius?")
    temp_farenheit = (float(temp_celsius) * float(1.8)) + 32
    print("This is the temperature in Farenheit:", temp_farenheit)
celsius_to_faren()

def faren_to_celsius():
    temp_faren = input("what is the temperature in Farenheit?")
    temp_cel = ((float(temp_faren) - 32)  * float(1.8))
    print("This is the temperature in Celcius:", temp_cel)
faren_to_celsius()
