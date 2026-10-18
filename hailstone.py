"""
File: hailstone.py
Name:
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    n = int(input('n: '))
    counter = 0
    while n!=1:
        if n % 2 == 1:
            n=3*n+1
            print(str((n-1)//3) + ' is odd, so I make 3n+1: ' + str(n))
        else:
            n=n//2
            print(str(n*2) + ' is even, so I take half: ' + str(n))
        counter += 1
    print('It took '+str(counter)+' steps to reach 1')

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
