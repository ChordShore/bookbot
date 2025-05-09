def get_num_words(file_contents):
    num_words = len(file_contents.split())
    return num_words

def get_num_chars(file_contents):
    num_chars = {}   
    for char in range(0, len(file_contents)):
        converted_char = file_contents[char].lower()
        if num_chars == {}:
            num_chars[converted_char] = 1
        elif converted_char not in num_chars:
            num_chars[converted_char] = 1
        else:
            num_chars[converted_char] += 1    
    return num_chars

def sort_on(dict):
    return dict["num"]

def get_sorted_list(num_chars):
    sorted_list = []
    for char in num_chars:
        if char.isalpha() == True:
            sorted_list.append({"char": char, "num": num_chars[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
