""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values) """
""" for i in values:
    print(i) """

""" print(values[0])
print(values[6]) """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z)
 """

""" sentence = input("Write_a_sentence: ") 
print(len(sentence.split())) """

""" noun = input("noun: ")
number = input("number: ")
verb = input("verb: ")
celebrity = input("celebrity: ")
adjective = input("adjective: ")
adjective2 = input("adjective2: ")
number2 = input("one_digit_number: ")
result = input("winner_or_loser: ")
verb2 = input("verb: ")
emotion = input("emotion: ")

print(f"Today was the {noun} competition and there were {number} other contestants. However, you were late to the competition so you decided to {verb} there. When you got there you were confronted by {celebrity} who turns out to be the judge! It was time to present your {noun}. My {noun} is very {adjective} and {adjective2}, you said. At the end of the competition you were announced as the #{number2} {result}. As a result, you decided to {verb2} {celebrity}. At the end of the day, you were {emotion}.") """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else: 
    print("incorrect") """ 

""" x = "test"
print(f"hello {x}") """

""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" number = int(input("number: "))
if (int(number % 2 )) == 0:
    print('even')
else:
    print('odd') """

""" 
bill = int(input("Bill: "))
service = input("Service: ")
if service == ("bad"):
    print('0% tip')
elif service == ("okay"):
    print('15% tip')
elif service == ("good"):
    print('20% tip')
elif service == ("great"):
    print('25% tip')
else:
    print('error') """

""" def print_factors(x):
    print("The factors of",x,"are: ")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

num=int(input("Number: "))
print_factors(num) """

""" num1 = int(input("First Number: "))
x = num1
num2 = int(input("Second Number: "))
y = num2

def gcf(x,y):
    if x > y:
        smaller = y
    
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            gcf = i
    return gcf
 
print("The greatest common factor of",x," and ",y,"is: ")
print(gcf(x,y))
 """



    








