# File Handling

# 19. Write a program to read a file line by line and print the content.
def read_text_file():
    with open('sample.txt', 'r') as file:
        for line in file:
            print(line.strip())

# 20. Write a program to count the number of words in a file.
def count_word_file():
    with open('sample.txt', 'r') as file:
        content = file.read()
    word_count = len(content.split())
    print(f"Number of words in file: {word_count}")

# 21. Write a program to append text to an existing file.
def append_text_file():
    with open('sample.txt', 'a') as file:
        file.write("\nThis line is appended.")
    print("Text appended successfully.")

