def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    nums_of_chars = get_nums_of_chars(text)
    print_char_report(book_path, num_words, nums_of_chars)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_nums_of_chars(text):
    lower_case = text.lower()
    char_dict = {}
    for char in lower_case:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_char_report(path, num_words, char_dict):
    char_list = []
    for char in char_dict:
        if char.isalpha():
            char_list.append(f"The '{char}' character was found {char_dict[char]} times")
    char_list.sort()
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document\n")
    for item in char_list:
        print(item)
    print("--- End report ---")

main()