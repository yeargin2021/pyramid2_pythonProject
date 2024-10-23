def pyramid(height):
    """
    Function to build a pyramid with specified height
    """
    for i in range(1, height + 1):
        print(('E' * (4 * i)).center(4 * height))


print("Welcome to Pyramid Builder!")
x = int(input("Enter the height of the pyramid: "))
pyramid(x)