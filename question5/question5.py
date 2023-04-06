def reverse_words(sentence):
    words = sentence.split()
    reversed_words = list(reversed(words))
    return " ".join(reversed_words)

if __name__ == "__main__":
    sentence1 = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
    sentence2 = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"
    
    reversed_sentence1 = reverse_words(sentence1)
    reversed_sentence2 = reverse_words(sentence2)
    
    print(reversed_sentence1)
    print(reversed_sentence2)
