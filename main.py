from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted_list

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents

def main():
    file_path = "./books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    num_words = get_num_words(file_contents)
    num_chars = get_num_chars(file_contents)
    sorted_list = get_sorted_list(num_chars)

    #Print Formatting
    print("♢♢♢♢♢ BOOKBOT ♢♢♢♢♢")
    print(f"Analyzing book found at {file_path}...")
    print("⋄⋄⋄⋄⋄ Word Count ⋄⋄⋄⋄⋄")
    print(f"Found {num_words} total words")
    print("⋄⋄⋄⋄⋄ Character Count ⋄⋄⋄⋄⋄")
    for i in range(0, len(sorted_list)):
        print(f"{sorted_list[i]["char"]}: {sorted_list[i]["num"]}")
    print("⋄⋄⋄⋄⋄ END ⋄⋄⋄⋄⋄")

main()