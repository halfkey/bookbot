def number_of_words(text):
    return len(text.split())

def count_chars(text):
    char_count = {}
    
    for char in text:
        char = char.lower()
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def chars_dict_to_sorted_list(char_dict):
    chars_list = []
    
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    
    def sort_on(dict):
        return dict["count"] 
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list