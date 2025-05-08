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
        
    #print(num_chars['t'])
    #print(num_chars['p'])
    #print(num_chars['c'])

    return num_chars