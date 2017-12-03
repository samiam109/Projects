#calculates the sum of even numers in the fibonacci sequence, below 4,000,000
even_nums = []
seq_num = int(input("Please enter a number: "))

#Function to add an even number to the collection of even results from fib
def isEven(num):
    if num % 2 == 0 and num not in even_nums and num < 4000000:
        even_nums.append(num)
    return

def fib(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
#run fib for x number of values
for x in range(seq_num):
    isEven(fib(x))

#print (fib(int(input("Enter a number:    "))))
print (sum(even_nums), even_nums)
