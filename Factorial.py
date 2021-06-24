def Factorial(number):

    if number==0 or number==1:
        return 1
    else:
        return number*Factorial(number-1)

def TrailingZeros(number):
    count = 0
    i=5
    while(number//i !=0):
        count += int(number/i)
        i=i*5
        return count

if __name__ == '__main__':
    number = int(input("enter a number:\n"))
    fac = Factorial(number)
    print(f"your factorial is: {fac}")
    zero = TrailingZeros(number)
    print(f"no of zeros in this factorial are:{zero}")