import numpy

def distance(input_word, dict_word):
    """calculates edit distance between words"""
    input_word = [char for char in input_word]
    dict_word = [char for char in dict_word]
    words = numpy.zeros((len(input_word), len(dict_word)))  # array of size m * n

    """first row and column"""
    words[0] = [n for n in range(len(dict_word))]  # first row
    words[:, 0] = [n for n in range(len(input_word))]  # first column

    """pseudocode implementation"""
    for i in range(1, len(dict_word)):
        for j in range(1, len(input_word)):
            temp = 0
            if dict_word[i] != input_word[j]:
                temp = 1

            words[j, i] = min(
                words[j - 1, i] + 1,
                words[j, i - 1] + 1,
                words[j - 1, i - 1] + temp
                )
    return words[-1, -1]

def main():
    words = {}  # create empty dictionary

    with open("words.txt") as f:
        """opening and reading file"""
        for line in f:
            words[str(line.strip())]=0

    while True:
        input_word = str(input("Enter a word: "))
        recommendation = []  # empty list of recommendations

        if input_word =="":
            break
        if input_word in words:
            print(f"{input_word} is a valid word")
        else:
            print(f"{input_word} is an invalid word!")

            """added the symbol # so that it doesn't affect when initializing the first row and column"""
            input_word = "#" + input_word
            for key in words:
                temp= "#" + key
                total = distance(input_word, temp)
                words[key] = total

            """searching for the words with the minimum distance"""
            for i in range(0, 5):
                min_key = min(words, key=words.get)
                recommendation.append(min_key)  # filling the recommendations
                del words[min_key]  # delete the word from dictionary so that it doesn't repeat itself
            print(f"Did you mean?: {recommendation}")

            """adding the deleted words back for future use"""
            for i in range(len(recommendation)):
                words[recommendation[i]] = 0

if __name__ == "__main__":
    main()
