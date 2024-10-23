# HowManyLayers = 7
HowManyLayers = 10

# LongestLength = (3 * (HowManyLayers + 1))
# for EachLayer in range(HowManyLayers):
#     print((" " * (LongestLength - 3 * (EachLayer + 2)) + ("E" * ((EachLayer + 2) * 3)) + "E" * ((EachLayer + 2) * 3)))

LongestLength = (3 * (HowManyLayers + 1))
CapStone = ((LongestLength / 2) + 14)
print((int(CapStone) * " ") + ("E" * 2))
for EachLayer in range(HowManyLayers):
    print((" " * (LongestLength - 3 * (EachLayer)) + ("E" * ((EachLayer + 2) * 3)) + "E" * ((EachLayer) * 3)))

print(CapStone, LongestLength)