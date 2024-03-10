def words_to_numbers(list):
    new_list = []
    for a in list:
        a = int(a)
        new_list.append(a)
    return new_list
print(words_to_numbers(["3","4","5"]))

def element_counter(list, type):
    count = 0
    for a in list:
        count += 1
        if isinstance(a,type):
            break
    return count
l = [10,20,30,(10,20),40]
t = tuple
print(element_counter(l,t))

def palindrome_test(str):
    if str == str[::-1]:
        return True
    else:
        return False
print(palindrome_test("ABBA"))

def check_sorted(list):
    n = 1
    for a in list:
        if len(list) == 1:
            return True
        elif list[n] < a:
            return False
        else:
            return True
print(check_sorted([1,2,3,4,5]))
print(check_sorted([2,1,4,51,5]))
print(check_sorted([1]))

"""def bubble_sort(list):
    sorted_list = []
    i = 0
    for a in list:
        if i < len(list)-1:
            if a > list[i+1]:
                list[i] = list[i+1]
                list[i+1] = a
                print(list)
                i += 1
            else:
                i += 1
    return list
nlist = [4,3,2,1]
print(bubble_sort(nlist))
nlist = ["A","C","B","a","c","b"]
print(bubble_sort(nlist))"""
def bubble_sort(list):
    i = 0
    n = 0
    while i <= len(list):
        while n < len(list)-1:
            if list[n] > list[n+1]:
               a = list[n]
               list[n] = list[n+1]
               list[n+1] = a
               print(list)
               n += 1
            else:
               n += 1
        n = 0
        i += 1
    return list
nlist = [4,3,2,1]
print(bubble_sort(nlist))
nlist = ["A","C","B","a","c","b"]
print(bubble_sort(nlist))

