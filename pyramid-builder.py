



def e_pyramid(height):
    for i in range(1, height + 1):
        # Calculate the number of "E" characters to print with spaces between them
        num_es = 4 * i
        # Calculate the number of leading spaces for centering
        leading_spaces = (4 * height - num_es) // 2
        # Print the pyramid row with centered "E"s
        print(' ' * leading_spaces + 'E' * num_es)

print("Welcome to Pyramid Builder!")
x = int(input("Enter the height of the pyramid: "))
e_pyramid(x)