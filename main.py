def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_dict = count_chars(text)
    char_sorted_list = dict_to_sorted_list(char_dict)
    print_report(book_path, word_count, char_sorted_list)


def dict_to_sorted_list(char_dict):
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char" : ch, "num" : char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def count_chars(text):
    lower_text = text.lower()
    char_map = {}
    for char in lower_text:
        if not char in char_map:
            char_map[char] = 0
        char_map[char] += 1

    return char_map


def print_report(book_name, word_count, char_list):
    print(f"--- Begin report of {book_name} ---")
    print(f"{word_count} words found in the document")
    print()
    for item in char_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")


main()
