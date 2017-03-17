print('Hello Anaconda!')

a = [1, 2, 'sajad']
print(a)
a.remove(a[2])
print(a)

b = []
for i in range(10):
    b.append(i)

print(b[-len(b)])
b[2:3] = [1, 1, 1]
print(b)

countries = {'United States': 'Washington, DC'}
print(countries)
print(countries.values())
print('Washington, DC' in countries)
countries.update({'Italy': 'Rome'})
print(countries)
for keys, values in countries.items():
    print(keys, " -> ", values)

squares = [i ** 2 for i in range(5) if i**2 >= 5]
print(squares)

file_object = open('words', 'r')
word_list = file_object.readlines()
print(len(word_list))
cleaned_word_list = [item.strip().lower() for item in word_list]
print(cleaned_word_list[0:10])
# Create a set to make everything unique, the cast to list, then sort
word_unique = sorted(list(set(cleaned_word_list)))
print(word_unique[0:10])


# Challenge : Find anagrams
def signature(word):
    return ''.join(sorted(word))


def is_anagram(my_word):
    return [word for word in word_unique if signature(my_word) == signature(word)]


import collections

words_bysig = collections.defaultdict(list)
for word in word_unique:
    words_bysig[signature(word)].append(word)


def anagram_fast(my_word):
    return words_bysig[signature(my_word)]


words_with_lens = {}
for word in word_unique:
    if len(word) in words_with_lens.keys():
        words_with_lens[len(word)].append(word)
    else:
        words_with_lens[len(word)] = [word]

anagrams_bylenght = {}
for lenght, words in words_with_lens.items():
    anagrams_bylenght[lenght] = {word: anagram_fast(word) for word in words if len(anagram_fast(word)) > 1}
print(anagrams_bylenght[22])
