def insert_spaces(string):
    result = []
    current_word = []

    for char in string:
        if char.isupper():
            if current_word:
                result.append(''.join(current_word))
                current_word = [char]
            else:
                current_word.append(char)
        else:
            current_word.append(char)

    if current_word:
        result.append(''.join(current_word))

    return ' '.join(result)

input_string = input("Enter a string: ")

result_string = insert_spaces(input_string)

print("String with spaces between words starting with capital letters:", result_string)
