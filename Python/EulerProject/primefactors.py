#What is the largest prime factor of the number 600851475143 ?
number = 50
l_prime = 3

#Function to determine if the number passed to it is a prime prime
def is_prime(x):
    for num in range(3, x):
        if x % num == 0:
            return False
            break
    return True

for x in range(l_prime, number+1):
    if is_prime(x) and l_prime < x:
        print (l_prime)
        l_prime = x



#print (is_prime(int(input("Enter a num: "))))
print (is_prime(number), l_prime)
