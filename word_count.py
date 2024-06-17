import re
import sys
import os


def is_string_contain_only_english_letters(string):
    regular_expression = '^[A-Za-z]+$'

    if re.match(regular_expression, string) is None:
        return False

    return True


def is_string_contain_english_letter(string):
    regular_expression = '[A-Za-z]'

    if re.search(regular_expression, string) is None:
        return False

    return True


def get_fixed_word(word_to_clean):
    new_fixed_clean = ''

    for letter in word_to_clean:
        if is_string_contain_only_english_letters(letter):
            new_fixed_clean += letter

    return new_fixed_clean


def add_word_to_words_dict(word, words_dict):
    if is_string_contain_only_english_letters(word) is True:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    elif is_string_contain_english_letter(word) is True:
        word = get_fixed_word(word)
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1


def get_words_dict(user_file):
    words_dict = {}
    try:
        with open(user_file, 'r', encoding='utf-8') as file:

            for line in file.readlines():
                striped_line = line.strip()

                for word in striped_line.split():
                    add_word_to_words_dict(word, words_dict)

    except FileNotFoundError:
        print('Pay attention!!!,you tried open a file that does not exist.')

    except Exception as error:
        print(f'Pay attention!!!, {error} occurred')

    return words_dict


def print_n_words_with_most_appearances(n, words_dict):
    sorted_words_list_according_to_appearances = sorted(words_dict.items(), key=lambda key_value: key_value[1],
                                                        reverse=True)

    list_of_n_words_with_most_appearances = sorted_words_list_according_to_appearances[0:n]

    for place, key_and_value_tuple in enumerate(list_of_n_words_with_most_appearances, start=1):
        print(f'{place}. [{key_and_value_tuple[0]}] with {key_and_value_tuple[1]} appearances.')


def get_parameters():
    is_length_ok = True
    filename = None
    n = None

    if len(sys.argv) != 3:
        is_length_ok = False

    else:
        filename = sys.argv[1]
        n = sys.argv[2]

    return is_length_ok, filename, n


def are_parameters_valid(filename, n):
    try:
        int(n)

    except ValueError:
        return False

    except TypeError:
        return False

    try:
        if not os.path.isfile(filename):
            return False

    except TypeError:
        return False

    return True


def main():
    is_length_ok, filename, n = get_parameters()
    parameters_valid = are_parameters_valid(filename, n)
    if not is_length_ok or not parameters_valid:
        print('Insert parameters like this : file name  N(number).')
        print('Pay attention that the file exist, and N is number.')
        print('Try again.')

    else:
        words_dict = get_words_dict(filename)
        print_n_words_with_most_appearances(int(n), words_dict)


if __name__ == '__main__':
    main()
