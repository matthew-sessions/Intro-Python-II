def move_check():
    letter = input('Type press n e s w to move, and press q to quit: ')
    while letter.lower not in ['n', 'e', 's', 'w', 'q'] or letter.lower().split(' ')[0] not in ['get', 'drop']:
        if letter.lower().split(' ')[0] in ['n', 'e', 's', 'w', 'q']:
            return(letter.lower())
        elif len(letter.lower().split(' ')) > 1 and letter.lower().split(' ')[0] in ['get', 'drop']:
            return(letter.lower())
        else:
            letter = input('Type press n e s w to move, and press q to quit: ')

def proom_items(room):
    if len(room.item) == 0:
        print('This room has no items')
    else:
        print("Room Items:")
        for i in room.item:
            print(f"{i.name} - {i.description}")

def puser_items(room):
    if len(room.item) == 0:
        print('😰 You currently do not have any items 😰')
    else:
        print("Your Items:")

        for i in room.item:
            try:
                print(f"{i.name} - {i.description}")
            except:
                pass


def get_item(player, command):
    initem = command.split(' ')[1]
    items = [i.name for i in player.item]
    index_item = items.index(initem)
    return(player.item[index_item])
