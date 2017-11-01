def reverse(input_string):
    if len(input_string) == 0:
        return input_string
    else:
        return reverse(input_string[1:]) + input_string[0]

print ("Please enter the string you want to reverse: ")
initial_input = input()
print(reverse(initial_input))
