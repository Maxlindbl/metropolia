def value(numbers):
    output = []
    for num in numbers:
        if num % 2 == 0:
            output.append(num)
    return output

numbers = [1,5,9,2,4,13,4,8,16,21]
print(value(numbers))
print(numbers)
