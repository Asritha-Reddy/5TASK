str = input("Enter a string: ")

def Dictionary(i):
    dictionary = {}
    for letter in i:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary


def most_frequent(str):
    alphabets = [letter.lower() for letter in str if letter.isalpha()]
    dictionary = Dictionary(alphabets)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for frequency, letter in result:
        print (letter, frequency)

most_frequent(str)

