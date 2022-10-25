def upper_lower_count(string):
    count_1 = 0
    count_2 = 0
    for i in string:
       if i.isupper(): #function to find upper case
           count_1 += 1
       elif i.islower(): #counts the lower case
           count_2 += 1
    return count_1
    return count_2

count_1 = upper_lower_count(input("Enter a sample text: "))
print("This is the number of upper case letters:",count_1)

count_2 = upper_lower_count(input("Enter a sample text: "))
print("This is the number of lower case letters:",count_2)
