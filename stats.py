def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)

def get_character_count(file_contents):
    lower_case_counts = list([char.lower() for char in file_contents if char.isalpha() == True ])
    char_set = set(lower_case_counts)
    char_dict = {}
    for char in char_set:
        char_dict[char] = lower_case_counts.count(char)
    return char_dict

def get_sorted_character_count(char_dict):
    return {k: v for k, v in sorted(char_dict.items(), key=lambda item: item[1], reverse=True)}