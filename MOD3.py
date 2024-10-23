HowManyLayers = 10

LongestLength = (3 * (HowManyLayers + 1))
CapStone = (LongestLength // 2)  # Use integer division to get an integer value

# Print the top capstone centered
print(" " * (CapStone - 1) + "EE")  # Center the "EE"

# Print each layer
for EachLayer in range(HowManyLayers):
    # Calculate the number of 'E's for the current layer
    num_Es = (EachLayer + 2) * 3
    # Center each layer
    print(" " * (CapStone - (num_Es // 2)) + "E" * num_Es)

print(CapStone, LongestLength)
