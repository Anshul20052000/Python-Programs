largest = None
smallest = None
while True:
    num1 = input("Enter a number: ")
    num = float(num1)
    if num == "done" : 
        break
    try :
        if smallest is none :
            smallest=num
        elif num<smallest:
                smallest=value
        if largest is none :
            largest= num
        elif num>largest:
                largest=num
    except: 
        print("Ivalid input")
        continue
print("Maximum is", largest)
print("Minimum is",smallest)
