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
            letter = "The '" + str(key) + "' character was found " + str(value) + " times " + str(key) + ": " + str(value) + "\n"
            list_out += letter  
    return list_out

def sort_by_value_desc_order(sorted_chars):
    sorted_items = sorted(sorted_chars.items(), key=lambda item: item[1], reverse=True)
    sorted_dictionary = dict(sorted_items) 
    return sorted_dictionary