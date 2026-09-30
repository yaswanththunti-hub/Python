def count_vowels(s):
    count = 0

    for i in s:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count = count + 1

    return count

print(count_vowels("python programming"))
