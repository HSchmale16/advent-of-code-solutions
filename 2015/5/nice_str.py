from sys import stdin

def count_vowels(mystr):
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = 0
    for v in vowels:
        s += mystr.count(v)
    return s

def check_dup_letter(word):
    last = word[0]
    for l in word[1:]:
        if l == last:
            return True
        last = l
    return False

def check_word(word):
    bad_str = ['ab', 'cd', 'pq', 'xy']
    for bad in bad_str:
        if bad in word:
            return False
    if count_vowels(word) < 3:
        return False
    return check_dup_letter(word)

for word in stdin.readlines():
    print(check_word(word))
