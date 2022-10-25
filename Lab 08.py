temp = []
request = int(input("Please enter a temperature: "))
if request == "":
    print(temp)
else:
    temp.append(int(temp))
    print("The maximum temperature is: ", max(temp))
    print("The minimum temperature is: ", min(temp))
    mean = sum(temp) / len(temp)
    print("The average temperature is:", mean)
