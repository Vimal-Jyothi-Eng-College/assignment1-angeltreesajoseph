arr = list(map(int, input("Enter array elements: ").split()))

for num in arr:
    if num % 2 != 0:
        print(num, end=" ")