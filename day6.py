numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(numbers)
print(numbers[0])
print(numbers[2])

for n in numbers:
    if n % 3 == 0:
        print(n)

result = sum(numbers)
print(result)