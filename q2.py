def is_fibonacci(num, fib_set):
  
    return num in fib_set

def generate_fibonacci_up_to(max_num):
   
    fib_set = set()
    a, b = 0, 1
    while a <= max_num:
        fib_set.add(a)
        a, b = b, a + b
    return fib_set

def count_fibonacci_numbers(arr):
    if not arr:
        return 0
    max_number = max(arr)
    fib_set = generate_fibonacci_up_to(max_number)
    
    count = 0

    for num in arr:
        if is_fibonacci(num, fib_set):
            count += 1

    return count


arr = []
for i in range(5):
    n = int(input('enter number'))
    arr.append(n)

   
print('input', arr)
fib_count = count_fibonacci_numbers(arr)
print("output", fib_count)
