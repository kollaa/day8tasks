#nums = int(input("enter any number:"))
def factor(fact):
    factorial =  1
    if fact == 0:
        print('hello')
    else:
        for i in range(1,fact+1):
            factorial = factorial * i
        
    return(factorial)
       
print(factor(3))




