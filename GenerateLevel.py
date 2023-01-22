import random
def GenerateLevel(n):
    letters='fjghdksla;\'tyrueiwoqp[]vnbcmx,z./'
    use_letters_len=0
    if (n==15):
        use_letters_len=n*2+3
    elif (n>=12):
        use_letters_len=n*2+2
    elif(n>=5):
        use_letters_len=n*2+1
    else:
        use_letters_len=n*2
    use_letters=letters[0:use_letters_len]
    result =[]
    for i in range(20):
        len_word=random.randint(1,6)
        word=''
        for j in range(len_word):
            word+=random.choice(use_letters)
        result.append(word)
    return ' '.join(result)

print(GenerateLevel(1))
print(GenerateLevel(2))
print(GenerateLevel(5))
print(GenerateLevel(15))


