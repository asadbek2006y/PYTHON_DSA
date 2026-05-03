num = 17 
is_prime = True
i  = 2 

if num <= 1: 
    is_prime = False
else: 
    while i < num: 
        if num % i == 0: 
            is_prime = False
            break
        i += 1

print(f"{num} is {'a prime' if is_prime else 'not a prime'} number.")