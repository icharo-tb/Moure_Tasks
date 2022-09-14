def draw_form():
    side_lenght = int(input('Choose lenght: '))
    form = input('Choose square or triangle: ')

    if form == 'triangle':
        for j in range(side_lenght):
            for i in range(j+1):
                print('* ',end='')
            print()
        return f'Your {form} has a side lenght of {side_lenght}'
    elif form == 'square':
        for j in range(side_lenght):
            for i in range(side_lenght):
                print('* ',end='')
            print()
        return f'Your {form} has a side lenght of {side_lenght}'
    else:
        return f'Error: form must be square or triangle'
pass
print(draw_form())