# Deniz Erisgen ©

from my_utils import make_list_from_file


def get_words_from_file(filename: str):
    words = make_list_from_file(filename)
    print(words)


def process_words(line: str) -> tuple:
    pass
    # tokenize and clean words


def check_spelling(words: tuple) -> tuple:
    pass


def read_text_file(input_filename: str):
    misspelled_words = []
    with open(input_filename, "r") as fin:
        line = fin.readline()
        while line:
            words = process_words(line)
            misspelled_words.extend(words)
            line = fin.readline()

    print(f"There are {(len(misspelled_words))}misspelled words :\n"
          f"{misspelled_words}")


if __name__ == '__main__':
    get_words_from_file("words")
    read_text_file("ihaveadream.txt")
    # print report
