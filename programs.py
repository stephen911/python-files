from itertools import combinations
import itertools

text = "university of cape coast"
lst = text.split()
list_of_words = []


def forming_words():
    count = 0
    for i in text:
        print(i)
        list_of_words.append(i)

    for start, end in combinations(range(len(list_of_words)), 2):
        print(list_of_words[start:end+1])
        count += 1
    print(count)


def even_sqrt():
    for i in range(1, 50):
        if i % 2 == 0:
            print(i, i**0.5)


def even_numbers():
    for i in range(20, 100):
        if i % 2 == 0:
            print(i)


# if __name__ == "__main__":
#     forming_words()
#     even_sqrt()
#     even_numbers()


name_of_institution = 'university of cape coast'
words = name_of_institution.split()
print(name_of_institution)
print(words[:2])
print(words[:3])
print(words[1:])
print(words[2:])
print(words[1:3])
for i in range(4):
    print(words[i])


count1 = 0

for i in range(len(words)+1):
    for combination in itertools.combinations(words, i):
        print(combination)
        count1 += 1
print(count1)