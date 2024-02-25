def snake_to_camel(snake_case):
    words = snake_case.split('_')

    camel_case_words = [words[0]] + [word.capitalize() for word in words[1:]]

    camel_case = ''.join(camel_case_words)

    return camel_case


snake_case_string = input("Enter a snake case string: ")

camel_case_string = snake_to_camel(snake_case_string)

print("Snake case:", snake_case_string)
print("Camel case:", camel_case_string)
