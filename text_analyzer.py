'''
author = Micha Suchorova
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

credentials = {'bob': '123',
               'ann': 'pass123',
               'mike': 'password123',
               'liz': 'pass123'}

line = '-' * 60

print(line)
print('Hello there! Welcome to Text Analyzer! Please log in:')
username = input('Username: ')
password = input('Password: ')

if username not in credentials or credentials[username] != password:
    print('Username or password are incorrect! Access denied.')
    quit()
else:
    print('Logged successfully!')

print(line)

print('There are 3 texts which can be analyzed!')
select_text = int(input('Enter umber of text to be analyzed (1 - 3): '))
print(line)

text = TEXTS[select_text - 1]

words_draft = text.split()
words = []

while words_draft:
    word = words_draft.pop()
    word = word.strip('.,:')
    words.append(word)

titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
dict_count = {}
num_sum = 0

index = 0

while index < len(words):
    if words[index].istitle():
        titlecase = titlecase + 1
    elif words[index].isupper():
        uppercase = uppercase + 1
    elif words[index].islower():
        lowercase = lowercase + 1
    elif words[index].isnumeric():
        numeric = numeric + 1
        num_sum = num_sum + float(words[index])

    length = len(words[index])
    dict_count[length] = dict_count.get(length,0) + 1

    index = index + 1

print('There are ', len(words), ' words in the selected text.')
print('There are ', titlecase, ' titlecase words.')
print('There are ', uppercase, ' uppercase words.')
print('There are ', lowercase, ' lowercase words.')
print('There are ', numeric, ' numeric string.')
print(line)


graph = sorted(dict_count)

index = 0

while index < len(graph):
    len_graph = graph[index]
    frequency = dict_count[len_graph]

    if len(str(len_graph)) == 1:
        str_len = ' ' + str(len_graph)
    else:
        str_len = len_graph

    print(str_len, '*' * frequency, frequency)

    index = index + 1

print(line)
print('If we summed all the numbers in this text we would get: ', num_sum)
print(line)

