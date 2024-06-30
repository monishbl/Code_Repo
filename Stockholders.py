# Solution for a question from Hakerrank - Problem Solving
"""
You are given a list of stockholders.
example: ['A', 'B', 'C', 'A', 'B', 'A', 'C', 'A', 'B', 'C', 'A', 'B', 'A', 'C', 'A', 'B', 'A', 'C', 'A', 'B', 'C', 'A', 'B', 'A']
where A, B, and C are the names of the stockholders and can vary.
Write a function that returns a list of stockholders who own more than 5% of the total shares.
The list should be sorted in alphabetical order. 

"""
import random

stockholders = {}
eligible_stockholders = []

def count_stockholders(list):
    global stockholders
    holders = set(list)
    for holder in holders:
        stockholders[holder] = list.count(holder)
    for name, stocks in stockholders.items():
        if (stocks/len(list)) > 0.05:
            eligible_stockholders.append(name)
    eligible_stockholders.sort()
    print('Elgible Stock Holders: ',eligible_stockholders)


list = []
for j in range(1,random.randint(2,15)):
    list.append(random.choice(['A', 'B', 'C']))

count_stockholders(list)