def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        c = i - 1
        print(list)
        while c >= 0 and key < list[c]:
            list[c+1] = list[c]
            c -= 1
        list[c+1] = key
        
a = [5,4,3,2,1,23,4,22,3,22]
insertion_sort(a)
print(a)

def sort_colors(list):
    list_order = ["Gold","Silver","Bronze","Yellow","Grey","Brown"]
    for i in range(1, len(list)):
        key = list[i]
        c = i - 1
        while c >= 0 and list_order.index(key) < list_order.index(list[c]):
            list[c+1] = list[c]
            c -= 1
        list[c+1] = key
    return list
colorlist = ["Silver","Gold","Yellow"]
print(sort_colors(colorlist ))