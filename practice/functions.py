def function_name(variable_input):
    #This is my first function!

    print("I am running my function!")

    variable_output = variable_input + " Werld!"

    return(variable_output)


printing_var = function_name("Hello")
print(printing_var)

def function_name(variable_input):
    #This is my first function!

#    print("i am running my function!")

    variable_output = variable_input + " world!"

    return variable_output

print(function_name("Hello"))

def double_input(input):
    return input*2
print(double_input("Hello"))
print(double_input(2))
print(double_input([1,2,3]))

def multiple_input(var1,var2):
    print (var2)
    return(var2[var1])
print(multiple_input(0,[1,2,3,4]))

def square_times(var_one,var_two):
    answer = var_one**2 * var_two
    return answer
print(square_times(3,9))

def uniques(list):
    print(list)
    count = 0
    new_list = set()
    new_list.update(list)
    while count < len(list):
        item = list[count]
        count += 1
        if item not in new_list:
            new_list.append(item)
    return new_list
print(uniques([1,2,3]))
print(uniques([1,1,1,3,2,2,3,2,3]))

def accel_finder(mass, force):
    acceleration = force/mass
    return acceleration
print (accel_finder(10,2))

def test_prime(n):
    flag = True
    result = True
    try:
        int(n)
    except ValueError:
        flag = False
    if flag:
        if n == 1:
            result = False
        if n > 1:
            i = 1
            while i <= n:
                if n % i == 0 and i != 1 and i != n:
                    result = False
                    break
                i += 1
    else:
        print("please enter a intger!!!")
    return result
test_prime(123)

def fizzbuzz(n):
    flag = True
    result = 0
    try:
        int(n)
    except ValueError:
        flag = False
    if flag:
        if n % 5 == 0:
            result = "fizz"
        elif n % 7 == 0:
            result = "buzz"
        elif n % 5 == 0 and n % 7 == 0:
            result = "fizzbuzz"
        else:
        #if n % 5 != 0 and n % 7 != 0:
            result = n
    else:
        print("please enter a intger!!!")
    return result
print(fizzbuzz(207))