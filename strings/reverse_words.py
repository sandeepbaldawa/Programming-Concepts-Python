def reverse(input):
    return (" ").join([each[::-1] for each in input.split()])

print reverse("Mary had a little lamb")
