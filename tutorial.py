# list in python is an array
print("This is list or array\n")
list = ['a','b','c']
list.append('d')
a = list[1:] #ignores the first element in the array
b = list[:2] #returns only the first 2 element
list[0] = 'boy' #overwrite the first index of the array
print(list)
print(a)
print(b)

# nested array
print('This is nested array\n')
arr = [1,2,3,[4,5,[6,7,8],[9]]]
dex = arr[3][3]
print(dex)

#dictionaries
d = {'name':'john','first':'oluwapelumi','work':{'at':'gitech','new':'andela'}}
print(d['work']['at'],d['first'])

# tuples
print('this is tuples')
tup = (1,2,3)
print(tup[0])

# looping
print('Loooping')
x = [1,2,3,4,5]
out = []
for i in x:
    out.append(i**2)
    print(out)

# declaring a function
print('Function')
def first(params):
    print('hello '+params)
first('john')
print('function to find the square root of a number')
def square(x):
    return x**2
out = square(4)
print(out)

print('stripping out a name from set of names')
def getEmail(name):
    name.lower()
    mail = name.split('@')
    return mail[0]
output = getEmail('User@gmail.com')
print(output)

print('# function that returns true if a word is found in sentence')
def findWord(word):
    word = word.lower()
    return 'dog' in word
info = findWord('is there a dog')
print(info)
# using for loop
txt = 'is there a dog'
d='dog'
for i in txt:
    for j in d:
        if i is j:
            print(True)
        break
print('function that counts the number of times a word is repeated in a sentence')
def countWord(sentence):
    sentence = sentence.lower().split()
    count = 0
    for i in sentence:
        if i == 'dog':
            count = count + 1
    return count
outi = countWord('how many times is dog repeated in bull dog')
print(outi)

# ran = range(0,81,2)
# for x in ran:
#     y = str(x)
#     print(y.split())

def pickMid(word):
    word = word.split(" ")
    lens = len(word)
    if lens % 2 != 0:
        ans = round(lens/2 - 0.5)
        print(word[ans])
    else:
        ans = round(lens/2)
        print(word[ans-1] + " or " + word[ans] )
pickMid('hello here am u')

nums = [1,2,3,4,5]
odds = []
evens = []
for x in nums:
    if x % 2 == 1:
        odds.append(x)
        print (odds)
    else:
        evens.append(x)
        print(evens)