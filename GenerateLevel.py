import random
def GenerateLevel(n):
    letters='fjghdksla;tyrueiwoqp'
    use_letters=letters[0:n*2]
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
print(GenerateLevel(3))


