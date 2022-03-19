from random import randint

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
    if end is None:
        end = len(input_list) - 1
    if start < end:
        pivot = partition(input_list, start, end)

        quicksort(input_list, start, pivot - 1)
        quicksort(input_list, pivot + 1, end)


#random_list = [randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100)]
#
#print(random_list)
#quicksort(random_list)
#print(random_list)
