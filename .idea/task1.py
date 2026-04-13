numbers = [10, 5, 8, 20, 15, 20, 3]
max_num = max(numbers)
second_max = None
for num in numbers:
    if num < max_num:
        if second_max is None or num > second_max:
            second_max = num
print(f"Task 1: {second_max}")