import argparse

def binarycalculator(num):
    temp = num
    solution = []
    while (2>1):
        solution.append(num%2)
        num = num//2
        if num == 0:
            break
    print("The binary equivalent of {} is: ".format(temp))
    print(solution[::-1])

parser = argparse.ArgumentParser(description='Enter a valid number that you want to convert into binary. Do this after you type out the code name')
parser.add_argument("number", help = 'The number that you would like to convert into it\'s binary equivalent', type = int)
args = parser.parse_args()
binarycalculator(args.number)
