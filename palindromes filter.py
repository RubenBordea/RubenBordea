def is_palindrome(word):
    return word == word[::-1]

def sort_words(word_list):
    normal_words = []
    palindromes = []

    for word in word_list:
        if is_palindrome(word):
            palindromes.append(word)
        else:
            normal_words.append(word)

    return normal_words, palindromes

word_list = ['ananas', 'car', 'speaker', 'laptop', 'race', 'deed', 'racecar', 'mom', 'minim', 'peep']
normal_words, palindromes = sort_words(word_list)

print('Normal words:', normal_words)
print('Palindromes:', palindromes)