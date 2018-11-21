characters = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'R',
              'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z', 'a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j',
              'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z', '0', '1', '2', '3', '4',
              '5', '6', '7', '8', '9', '.', ',', ';', ':', '!', '?', '\'', '\"', '^', '/', '\\', '*', '&', '%', '-',
              '(', ')', '[', ']', '{', '}', '+', '=', '_', '<', '>', '|', '$', '#']

tags = ['verb', 'noun', 'adj', 'adv', 'pron', 'prep', 'conj']

def wordEncoder(word):
    encoded = [[0] * len(characters) for _ in range(len(word))]
    for i in range(0, len(word)):
        index = characters.index(word[i])
        encoded[i][index] = 1
    return encoded


def targetEncoder(target):
    encoded = [0] * len(tags)
    index = tags.index(target)
    encoded[index] = 1
    return encoded

