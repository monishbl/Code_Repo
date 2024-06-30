#Pascal triangle
"""
Pascal Triangle is a triangular array of binomial coefficients. It is named after the French mathematician Blaise Pascal.
The triangle is constructed by summing adjacent elements in preceding rows. The first row is 1. The second row is 1 1. To construct the next row, add the two numbers above
to get the numbers in the new row. The first and last numbers in each row are always 1. The triangle is infinite and can be constructed as far as needed.
example:
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
1 5 10 10 5 1
"""
def pascal_triangle(n):
    for i in range(n):
        print(' '*(n-i),end=' ')
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)),end=' ')
        print()

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
n=int(input('Enter the number of rows: '))
pascal_triangle(n)
