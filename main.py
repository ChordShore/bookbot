def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents

def main():
    file_path = "./books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    num_words = len(file_contents.split())
    print(f"'{num_words} words found in the document'")

main()