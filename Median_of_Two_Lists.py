
list1=[1,2,6,8,9,10]
list2=[2,3,4,5,6,7,8,9]

def find_median_sorted_arrays(list1, list2):
    list1.extend(list2)
    list1.sort()
    n = len(list1)
    if n % 2 == 0:
        median = (list1[n//2] + list1[n//2 - 1]) / 2
    else:
        median = list1[n//2]
    return median

print(find_median_sorted_arrays(list1, list2))