temp = []
while len(temp) != 6:
    request = temp.append(int(input("Please enter a temperature: ")))

print("The maximum temperature is: ", max(temp))
print("The minimum temperature is: ", min(temp))

mean = sum(temp)/len(temp)
print("The average temperature is:", mean)
