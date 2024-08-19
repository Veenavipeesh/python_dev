
num = int(input("Enter any number to check prime: "))
count = 1
prime_check = True
if(num > 0):
    if(num == 2 or num == 3):
        print("Number is prime")
    else:
        while( count <= num/2 ):
            count += 1
            if (num % count == 0):
                prime_check = False
                break
        if(prime_check):
            print("Number is prime")
        else:
            print("Number is not prime")
else:
    print("Enter a positive number")