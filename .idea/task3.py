numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even, odd = [], []
for num in numbers:
    (even if num % 2 == 0 else odd).append(num)
print(f"Task 3: even, odd")