from stats import get_num_words
from stats import get_num_chars

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents

def main():
    file_path = "./books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    num_words = get_num_words(file_contents)
    num_chars = get_num_chars(file_contents)
    print(f"'{num_words} words found in the document'")
    print(num_chars)

main()