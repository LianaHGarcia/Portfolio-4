def celsius_to_faren():
    temp_celsius = input("what is the temperature in Celsius?")
    print(temp_celsius+"C")
    temp_farenheit = (float(temp_celsius) * float(1.8)) + 32
    print("This is the temperature in Farenheit:", temp_farenheit, "F")
celsius_to_faren()
