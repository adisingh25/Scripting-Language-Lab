
sentences = []
vowels = ['a', 'e', 'i', 'o', 'u']
def vowelCount(sentence):
        return sum(i in vowels for i in sentence.lower())


class rev_sen:

    def __init__(self, s):
        r=s.split()[::-1]
        l = []
        for i in r:
            l.append(i)
        
        reversedString = (" ".join(l))
        sentences.append(reversedString)
        print('The reversed String is : ' ,reversedString)


def printObjects():
   
    list1 = sorted(sentences,key = lambda sentence: vowelCount(sentence),reverse=True)
    print("\n")
    for x in list1:
        print(x," : Vowel Count -> ",vowelCount(x))



for _ in range(0,3):
    entry=input('Enter the string : ')
    s1 = rev_sen(entry)


printObjects()






