def max_and_min_number_in_list( list ): #a normal function definition
    max = list[ 0 ]
    min = list[ 0 ] #create a new variable called max
    for a in list:   #create a new variable called a
        if a > max:
            max = a
    for b in list:
        if b < min:
            min = b
    return max, min

print(max_and_min_number_in_list([1,2,3,4,5]))
print(max_and_min_number_in_list([-1,-4,-5,-7]))

def average_list(list):
    total = 0
    average = 0
    for a in list:
        total += a
    average = total/len(list)
    return average
print(average_list([1,2,3,4,5,6,7,10.2]))

def triangle_stars(int):
    for i in range(1,int,+1): 
        for j in range(i):
            print ("* ", end="") 
        print(i)
    for i in range(int,0,-1): 
        for j in range(i):
            print ("* ", end="") 
        print(i)
triangle_stars(8)

def compare(a,b):
    if a > b:
        return a
    if a < b:
        return b
    else:
        return "these values are equal"
    
def bool_test(test):
    if test == None or test == 0 or not test:
        return False
    else:
        return True
    
def type_check(data_type):
    if type(data_type) == str:
        data_type = "String"
    if type(data_type) == int:
        data_type = "Integer"
    if type(data_type) == float:
        data_type = "Float"
    if type(data_type) == list:
        data_type = "List"
    return f"this variable type is: {data_type}"

def foo_looper(n):
    while n <= 10:
        if n == 1:
            print(str(n)+"st loop")
        if n == 2:
            print(str(n)+"nd loop")
        if n == 3:
            print(str(n)+"rd loop")
        if n > 3:
            print(str(n)+"th loop")
        if n == 9:
            print("second to last loop")
        if n == 10:
            break
        n+= 1

def loop_printer(n):
    if int(n) > 0:
        while n > 0:
            print(n)
            n -= 1
    else:
        print("please entre a positive integer")
loop_printer(10)