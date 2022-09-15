def word_frame(text):

    words = text.split()

    for word in words:
        center_line = '* ' + word + ' *'
        print(f"{'*'*(len(center_line))}")
        print(center_line)
        print(f"{'*'*(len(center_line))}")
    
    return 'Done!'
pass
print(word_frame('Lorem Ipsum is simply dummy text of the printing and typesetting industry.'))

def word_frame(text):
    
    words = text.split()
    maxLenght = 0

    for word in words:
        if len(word) > maxLenght:
            maxLenght = len(word)

    print('*'*(maxLenght+4))

    for word in words:
        space = ' '*(maxLenght-len(word))
        if word:
            print(f"* {word}{space} *")
        
    print('*'*(maxLenght+4))

    return 'Done!'
pass
print(word_frame('Lorem Ipsum is simply dummy text of the printing and typesetting industry.'))