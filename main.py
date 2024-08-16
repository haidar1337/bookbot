def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    num_words = count_words(book_text)
    num_characters = count_characters(book_text)
    
    list_dictionary = convert_dictionary_to_list(num_characters)
    list_dictionary.sort(key=sort_on, reverse=True)

    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document\n")

    for entry in list_dictionary:
        char = entry["character"]
        count = entry["count"]
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

    print("--- End report ---")



def count_words(text):
    strs = text.split()
    return len(strs)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    dict = {}

    for str in text:
        lower_string =  str.lower()
        if lower_string not in dict:
            dict[lower_string] = 1
            continue
        
        dict[lower_string] += 1

    return dict

def convert_dictionary_to_list(dict):
    list = []

    for k in dict:
        d = {
            "character": k,
            "count": dict[k]
        }
        list.append(d)

    return list

def sort_on(dict):
    return dict["count"]

main()