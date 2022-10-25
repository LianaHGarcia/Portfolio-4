def removeChar():
    string = input("Please enter a text: ")
    if string <= "1":
        print(string)
    else:
        text = string.rstrip(string[-1]) #remove last character
        print(text)
removeChar()