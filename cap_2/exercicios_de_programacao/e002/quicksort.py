from random import randint
import quicksort_recursivo




def partition(input_list: list, start: int, end: int) -> int:
    pivot_element = input_list[end]
    i  = start
    
    for j in range(start, end):
        if input_list[j] <= pivot_element:
            input_list[j], input_list[i] = input_list[i], input_list[j]
            i += 1

    input_list[i], input_list[end] = input_list[end], input_list[i]

    return i

def quicksort(input_list: list, start: int=0, end: int=None):
    test_list = input_list[:]
    if end is None:
        end = len(test_list) - 1

    pivot_left = partition(test_list, start, end)
    pivot_right = partition(test_list, start, end)
    

    while start < pivot_left:
        pivot_left = partition(test_list, start, pivot_left - 1)
         

    while pivot_right < end:
        pivot_right = partition(test_list, pivot_right + 1, end)
        

    return test_list






random_list = [randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100)]

test = random_list[:]

print(f"Lista desordenada -> {random_list}")
print(f"Lista ordenada quicksort NÃO RECURSIVO: {quicksort(random_list)}")
quicksort_recursivo.quicksort(test)
print(f"Lista ordenada quicksort RECURSIVO: {test}")

assert test == quicksort(random_list)
