#time complexity using print statement
#Use loop with print statement
#Addition
#Input from user

def time_complexity(n):
    for i in range(0, n + 1):
        print("First Loop")  # O(n)

    j = 1
    while j <= n + 1:
        print("Second Loop", j)  # O(log n)
        j = j * 2

    for i in range(0, 100):
        print("Third Loop")  # O(1)