# Deniz Erisgen ©
from nltk.tokenize import RegexpTokenizer
from my_utils import make_list_from_file


my_dictionary = ()


def get_words_from_file(filename: str):
    global my_dictionary
    my_dictionary = make_list_from_file(filename)


def process_words(line: str) -> tuple:
    global my_dictionary
    tknzr = RegexpTokenizer('\w+')
    tokens = tknzr.tokenize(line)
    not_found = []
    for wrd in tokens:
        if wrd.lower() not in my_dictionary:
            not_found.append(wrd)

    return tuple(not_found)


def read_text_file(input_filename: str):
    misspelled_words = []
    with open(input_filename, "r") as fin:
        line = fin.readline()
        while line:
            words = process_words(line.strip())
            misspelled_words.extend(words)
            line = fin.readline()

    print(f"There are {(len(misspelled_words))} misspelled words :\n"
          f"{misspelled_words}")


if __name__ == '__main__':
    get_words_from_file("words")
    read_text_file("ihaveadream.txt")
    # print report
