list = [1,2,3,1,3,2,1,2,5,3,8,4,6,3,2,5,7,8,9,6,]
target = 8

def find_quadruplets(list, target):
    list.sort()
    quadruplets = []
    for i in range(len(list)-3):
        for j in range(i+1, len(list)-2):
            left = j + 1
            right = len(list) - 1
            while left < right:
                current_sum = list[i] + list[j] + list[left] + list[right]
                if current_sum == target:
                    quadruplets.append([list[i], list[j], list[left], list[right]])
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
    quadruplets= set(tuple(quadruplets) for quadruplets in quadruplets)
    return quadruplets

print(find_quadruplets(list, target))
