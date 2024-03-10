def list_reader(list):
    reversed_list = []
    for i in list:
        reversed_list.insert(0, i)
    print(reversed_list)
    sorted_list = sorted(reversed_list)
    print(sorted_list[0])
    for i in sorted_list:
        if i == "":
            sorted_list.remove(i)
    return len(sorted_list)
print(list_reader(["a","Bee","Sea","D",""]))
print(list_reader([1,2,3]))

def tuple_reader(input):
    new_tuple = sorted(input)
    print(tuple(new_tuple))
    input = input + tuple(new_tuple)
    print(input)
    return len(input)
print(tuple_reader((2,3,1)))
print(tuple_reader((1,2,3,4,3,2,1)))
print("Next Question!\n")

def dict_reader(input):
    #print the values of the dict as a list
    values = list(input.values())
    print(values)
    #print the keys of the dict as a tuple
    key_tuple = tuple(input.keys())
    print(key_tuple)
    #find the key value that is the lowest in the dict
    sorted_values = sorted(values)
    for key, vel in input.items():
        if vel == sorted_values[0]:
            print(key)
        if key == "hello":
            input.update({"hello":"world"})
    return input
d = {"key1": 10, "key2": 23, "hello":24}
print(dict_reader(d))