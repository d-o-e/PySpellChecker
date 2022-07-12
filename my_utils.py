# Deniz Erisgen ©

def make_list_from_file(filename: str) -> ():
    """
reads words from files with a word per line
    :param filename: filename string from working dir
    :return: words in a dict
    """
    read_list = []
    with open(filename) as fin:
        line = fin.readline()
        while line:
            cleaner = str(line.rsplit()[0])
            read_list.append(cleaner)
            line = fin.readline()
    return tuple(read_list)


def make_list_from_file_for_db(filename: str) -> tuple:
    """
reads words from files with a word per line
    :param filename: filename string from working dir
    :return: words in a tuple of dict with _id and word keys
    """
    read_list = []
    with open(filename) as fin:
        line = fin.readline()
        id = 0
        while line:
            cleaner = str(line.rsplit()[0])
            read_list.append({"_id": id, "word": cleaner})
            id += 1
            line = fin.readline()
    return tuple(read_list)
