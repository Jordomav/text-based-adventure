player = raw_input('Please enter your player name: ')
inventory = []

pulls_chain = ''
gets_knife = ''
attacks_with_knife = ''


def get_inventory():
    if len(inventory) == 0:
        print 'You have nothing in your inventory'
    else:
        for item in inventory:
            print item


def convert_input(input):
    return input.lower()


def incorrect_input(func):
    print 'Please enter a correct input.'
    func()


def pickup_item(item):
    if len(inventory) < 4:
        inventory.append(item)
    else:
        print 'You do not have enough room, would you like to drop an item? (Y/N)'


def interact_chain():
    global pulls_chain
    pulls_chain = raw_input('You hit your head on a chain, will you pull it? (Y/N)')
    if convert_input(pulls_chain) == 'y' or convert_input(pulls_chain) == 'yes':
        print 'You pull the chain'
    elif convert_input(pulls_chain) == 'n' or convert_input(pulls_chain) == 'no':
        print 'You do not pull the chain'
    else:
        incorrect_input(interact_chain)


def interact_knife():
    global gets_knife
    gets_knife = raw_input('You see a knife in the corner, will you pick it up? (Y/N)')
    if convert_input(gets_knife) == 'y' or convert_input(gets_knife) == 'yes':
        print 'You pick up the knife'
        pickup_item('knife')
    elif convert_input(gets_knife) == 'n' or convert_input(gets_knife) == 'no':
        print 'You do not pick up the knife'
    else:
        incorrect_input(interact_knife)


def use_knife_on_figure():
    global attacks_with_knife
    attacks_with_knife = raw_input('Do you attack him with the knife? (Y/N)')
    if convert_input(attacks_with_knife) == 'y' or convert_input(attacks_with_knife) == 'yes':
        print 'You jab the knife towards the figure but he knocks it out of your hands.'
    elif convert_input(attacks_with_knife) == 'n' or convert_input(attacks_with_knife) == 'no':
        return
    else:
        incorrect_input(use_knife_on_figure)


def start_game():
    global pulls_chain
    global gets_knife
    print 'Your eyes slowly open as you are overwhelmed with the smell of ammonia.'
    print 'Your nostrils burn as the fumes slowly enter and exit your lungs.'
    print 'Stumbling to your feet you see a small glisten in the corner.'
    interact_chain()
    if convert_input(pulls_chain) == 'y' or convert_input(pulls_chain) == 'yes':
        interact_knife()
    print 'You slowly fumble your way to the door. As you feel the cold handle in your fingers you slowly being to turn'
    print 'Suddenly a figure jumps out from around the corner. The figure screams \'Leaving so soon?!\''
    if convert_input(gets_knife) == 'y' or convert_input(gets_knife) == 'yes':
        use_knife_on_figure()
    print 'The figure grabs you throwing you both to the ground.'


start_game()
