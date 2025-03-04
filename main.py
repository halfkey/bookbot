from stats import number_of_words, count_chars, chars_dict_to_sorted_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file, 'r') as file:
        return file.read()

    
def main():
    if len(sys.argv) > 1:
        path_to_file = sys.argv[1]
        book_text = get_book_text(path_to_file)
        word_count = number_of_words(book_text)
        counted_chars = count_chars(book_text)
        sorted_chars = chars_dict_to_sorted_list(counted_chars)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
    
        for char in sorted_chars:
            if char['char'].isalpha():
             print(f"{char['char']}: {char['count']}")

        print("============= END ===============")

main()

