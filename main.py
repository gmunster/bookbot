def character_count(book):
    chars_in_book = {}
    for char in book:
        if char in chars_in_book:
            chars_in_book[char] += 1 
        else:
            chars_in_book[char] = 1   
    return chars_in_book

def list_chars(list_in):
    list_out = ""
    for key, value in list_in.items():
            letter = "The '" + str(key) + "' character was found " + str(value) + " times\n"
            list_out += letter  
    return list_out    

def sort_by_value_desc_order(sorted_chars):
    sorted_items = sorted(sorted_chars.items(), key=lambda item: item[1], reverse=True)
    sorted_dictionary = dict(sorted_items) 
    return sorted_dictionary


def main():
    path_to_file = "books/frankenstein.txt"
    only_alpha_char = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    word_count = len(file_contents.split())
    for char in file_contents.lower():
        if char.isalpha():
            only_alpha_char += char 

    print(f"--- Begin report of", path_to_file, "---")
    print(word_count, "words found in the document\n")
    character_counted = character_count(only_alpha_char)
    sorted_character_counted = sort_by_value_desc_order(character_counted)
    print(list_chars(sorted_character_counted))


main()
