number = int(input("введите число в диапозоне от 1 до 100:"))
if number < 1 or number > 100: 
     print("это число не в диапозоне!")
elif number% 3 == 0 and number % 5 == 0:
    print("Buz Fizz")
elif number % 5 == 0:
    print ("Buzz")
elif number % 3 == 0: 
    print("fizz")
else: 
    print(number) 