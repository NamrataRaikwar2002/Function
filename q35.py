def drink(age):
    if age<=18:
        return "coke"
    elif age<21:
        return "young adults drink"
    elif age>=21:
        return "whisky"
ag=int(input("enter age:"))
print(drink(ag))