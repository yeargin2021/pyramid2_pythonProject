
# Pyramid Builder
# pyramid_builder.py
This Python script consists of a function named 'pyramid', and when executed, this script prints a pyramid shape to the console output.
## Function
```pyramid(height: int) -> None```

This function accepts an integer as an argument which represents the height of the pyramid. The function then prints the pyramid to the console. It does not return any value. Because the pyramid is composed of 'E' letter, all the lines of the pyramid except the first one start and end with 'E'.

The height parameter denotes the number of rows in the pyramid. Consider height to be n, the ith row will then contain 4*i 'E's. Each row is also centered to 4 * height, to ensure the pyramid maintains its shape.
## Execution
When the script is run, it prompts the user to input an integer which signifies the height of the pyramid to be built. The pyramid function is then called with this user-provided input.

Here is a Python code block representing the pyramid function:

```
def pyramid(height):
    """
    Function to build a pyramid with specified height
    """
    for i in range(1, height + 1):
        print(('E' * (4 * i)).center(4 * height))

And here is the execution part:

print("Welcome to Pyramid Builder!")
x = int(input("Enter the height of the pyramid: "))
pyramid(x)
```

Example:
If user inputs 3, the output will be:

```
    EEEE    
  EEEEEEEE  
EEEEEEEEEEEE
```