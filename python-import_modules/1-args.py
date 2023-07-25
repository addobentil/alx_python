import sys

def print_arguments():
    # Get the number of arguments
    num_arguments = len(sys.argv) - 1

    # Print the number of arguments
    print(num_arguments, "argument:")

    if num_arguments == 0:
        # If no arguments were passed, print a period and a new line
        print(num_arguments ,"arguments.", end="\n")
        
    elif num_arguments == 1:
            # If no arguments were passed, print a period and a new line
        print(num_arguments ,"argument:", end="\n")
        
    else:
        print(num_arguments ,"arguments:", end="\n")
        # If at least two arguments were passed, print each argument and its position
        
        for i in range(1, num_arguments + 1):
            print("{}: {}".format(i, sys.argv[i]), end="\n")


if __name__ == "__main__":
    print_arguments()
