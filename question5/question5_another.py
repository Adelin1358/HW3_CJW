def reverse_words(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    s1 = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
    s2 = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"
    result1 = reverse_words(s1)
    result2 = reverse_words(s2)
    print(result1)
    print(result2)
