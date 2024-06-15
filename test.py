def rewrite_file(file_path, new_content):
    with open(file_path, 'w') as file:
        file.write(new_content)
    print(f"File {file_path} has been rewritten with the new content.")

file_path = 'example.txt'
new_content = "Это новый контет файла."
rewrite_file(file_path, new_content)

#2дз 
def count_words_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
    print(f"The file {file_path} contains {word_count} words.")
    return word_count

file_path = 'example.txt'
count_words_in_file(file_path)


#3дз 
def write_user_input_to_file(file_path):
    user_input = input("Enter the text you want to save to the file: ")
    with open(file_path, 'w') as file:
        file.write(user_input)
    print(f"Your input has been saved to {file_path}.")

file_path = 'user_input.txt'
write_user_input_to_file(file_path)

    
