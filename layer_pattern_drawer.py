HowManyLayers = 7
LongestLength = (3 * (HowManyLayers + 1))
for EachLayer in range(HowManyLayers):
    print(" " * (LongestLength - 3 * (EachLayer + 2)) + "E" * ((EachLayer + 2) * 3))