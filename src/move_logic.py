def move_check():
    letter = input('Type press n e s w to move, and press q to quit: ')
    if letter.lower() in ['n', 'e', 's', 'w', 'q']:
        return(letter.lower())
    else:
        print('')
        tryagain = input('Try again: ')
        while tryagain.lower() not in ['n', 'e', 's', 'w', 'q']:
            tryagain = input('Try again: ')
        return(tryagain)
