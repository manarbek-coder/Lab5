def camel_to_snake(camel_case):
    snake_case = ''
    for char in camel_case:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    return snake_case.lstrip('_')

camel_case_string = input("Enter a camel case string: ")

snake_case_string = camel_to_snake(camel_case_string)

print("Snake case:", snake_case_string)
