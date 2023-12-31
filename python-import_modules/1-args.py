# import sys

# def print_arguments():
#     # Get the number of arguments
#     num_arguments = len(sys.argv) - 1

#     # Print the number of arguments
#     # print(num_arguments, "argument:")

#     if num_arguments == 0:
#         # If no arguments were passed, print a period and a new line
#         print("0 arguments.")
        
#     elif num_arguments == 1:
#             # If no arguments were passed, print a period and a new line
#         print("1 argument:")
        
#     else:
#         print(num_arguments,"arguments:")
#         # If at least two arguments were passed, print each argument and its position
        
#         for i in range(num_arguments):
#             print("{}: {}".format(i + 1, sys.argv[i + 1]))


# if __name__ == "__main__":
#     print_arguments()


#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
