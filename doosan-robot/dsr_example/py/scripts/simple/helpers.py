
# def log_custom(function_name,message):
#     return print("function_name: %s" % function_name,"message: %s" % message)
import math

list1 = []



while True:
    try:
        x = int(input("Enter a numeric value"))
    except ValueError:
        print('please enter a number')
        x = int()
        
    else:
        if x>1000:
             print('please enter less than thousand')

    if x > 0 and x< 500 :
        num = x
        num_string = str(num)
        size = len(num_string)
        reversed_num = num_string[size::-1]
        print("Reversed Number is: " + reversed_num)
        num1 = reversed_num
        list1.append(num1)
        print(list1)

    elif x > 500 and x <1000:
        num = int (x/2)
        num_string = str(num)
        size = len(num_string)
        reversed_num = num_string[size::-1]
        print("Reversed Number is: " + reversed_num)
        num1 = reversed_num
        list1.append(num1)
        print(list1)
