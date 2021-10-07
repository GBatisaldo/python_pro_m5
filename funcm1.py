
def mult(numero):

    if (numero % 5 == 0) and (numero % 7 ==0):
        print("fizzbuzz")
        return "fizzbuzz"
    
    elif numero % 5 == 0:
        print("fizz")
        return "fizz"
    
    elif numero % 7 == 0:
        print("buzz")
        return "buzz"

    else: 
        print("miss")
        return "miss"