# def e_pyramid(height):
#     for i in range(1, height + 1):
#         # Calculate the number of "E" characters to print
#         num_es = 4 * i
#         # Print the pyramid row with appropriate leading spaces
#         print(' ' * (height - i) + 'E' * num_es)
#
# # Example: Construct a pyramid of height 3
# e_pyramid(3)

# def e_pyramid(height):
#     for i in range(1, height + 1):
#         # Calculate the number of "E" characters to print
#         num_es = 4 * i
#         # Print the pyramid row with additional leading space
#         print(' ' * (height - i + 1) + 'E' * num_es)
#
# # Example: Construct a pyramid of height 3
# e_pyramid(3)

def e_pyramid(height):
    for i in range(1, height + 1):
        # Calculate the number of "E" characters to print with spaces between them
        num_es = 4 * i
        # Calculate the number of leading spaces for centering
        leading_spaces = (4 * height - num_es) // 2
        # Print the pyramid row with centered "E"s
        print(' ' * leading_spaces + 'E' * num_es)

# Example: Construct a pyramid of height 3
e_pyramid(22)