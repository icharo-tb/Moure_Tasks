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
