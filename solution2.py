# Write code for algorithm 2 below

def natural_numbers(x, n):
    if x > n :
        return
    else: 
        print(x)
        natural_numbers(x+1, n)

n=3
natural_numbers(1, n)

