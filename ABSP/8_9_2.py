text = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'
words = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
for word in words:
    if word in text:
        print('Enter an %s:' % word.lower())
        new_word = input()
        text = text.replace(word, new_word)
print(text)
with open('text.txt', 'w') as f:
    f.write(text)
