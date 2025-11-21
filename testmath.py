import math_utils

# Test math functions written in math_utils.py

print(math_utils.factorial(int(input("Enter number: "))))

print(math_utils.gcd(int(input("Enter number: ")), int(input("Enter number: "))))

print("is prime" if math_utils.is_prime(int(input("Enter number: "))) else "not prime")

# assert math_utils.gcd(48, 18) == 6
# assert math_utils.factorial(10) == 3_628_800
# assert math_utils.is_prime(2) == True
# assert math_utils.is_prime(4) == False
# assert math_utils.is_prime(5) == True
# assert math_utils.is_prime(15) == False
