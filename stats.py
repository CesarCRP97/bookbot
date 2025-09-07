def num_words_text(text):
    words = text.split()
    return len(words)


def num_chars_in_text(text):
    char_dictionary = {}
    lowered_text = text.lower()
    for c in lowered_text:
        if c in char_dictionary:
            char_dictionary[c] += 1
        else:
            char_dictionary[c] = 1
    return char_dictionary

def sort_on(items):
    return items["char"]
        
def sorted_dict_chars(unsorted_char_dict):
    to_sort = []
    for c in unsorted_char_dict:
        elem = {"char": c, "num": unsorted_char_dict[c]}
        to_sort.append(elem)

    to_sort.sort(reverse=False, key=sort_on)
    return to_sort