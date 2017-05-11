player = raw_input('Please enter your player name: ')
inventory = []

pulls_chain = ''
gets_knife = ''
attacks_with_knife = ''
answers_phone = ''


def get_inventory():
    if len(inventory) == 0:
        print 'You have nothing in your inventory.'
    else:
        for item in inventory:
            print item, ', '


def convert_input(input):
    return input.lower()


def incorrect_input(func):
    print 'Please enter a correct input.'
    func()


def pickup_item(item):
    if len(inventory) < 4:
        inventory.append(item)
        print 'You have', (4 - len(inventory)), 'spaces left in your inventory.'
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
        pickup_item('Knife')
    elif convert_input(gets_knife) == 'n' or convert_input(gets_knife) == 'no':
        print 'You do not pick up the knife'
    else:
        incorrect_input(interact_knife)


def use_knife_on_figure():
    global attacks_with_knife
    attacks_with_knife = raw_input('Do you attack him with the knife? (Y/N)')
    if convert_input(attacks_with_knife) == 'y' or convert_input(attacks_with_knife) == 'yes':
        print 'You jab the knife towards the figure but he knocks it out of your hands.'
        inventory.remove('Knife')
    elif convert_input(attacks_with_knife) == 'n' or convert_input(attacks_with_knife) == 'no':
        return
    else:
        incorrect_input(use_knife_on_figure)


def uses_phone():
    global answers_phone
    answers_phone = raw_input('Will you answer the phone? (Y/N)')
    if convert_input(answers_phone) == 'y' or convert_input(answers_phone) == 'yes':
        print 'Fearfully you pick up the phone. For a moment there was only static. Faintly you hear a voice in the ' \
              'background \'1 ____ 4 ____ 6 ____ 3.\'. Finally the phone goes dead.'
    elif convert_input(answers_phone) == 'n' or convert_input(answers_phone) == 'no':
        print 'With every ring your heartbeat rises and then the phone goes dead.'
    else:
        incorrect_input(uses_phone)


def start_game():
    global pulls_chain
    global gets_knife
    print 'Your eyes slowly open as you are overwhelmed with the smell of ammonia. ' \
          'Your nostrils burn as the fumes slowly enter and exit your lungs. ' \
          'Stumbling to your feet you see a small glisten in the corner.'
    interact_chain()
    if convert_input(pulls_chain) == 'y' or convert_input(pulls_chain) == 'yes':
        interact_knife()
    print 'You slowly fumble your way to the door. As you feel the cold handle in your fingers you slowly being to ' \
          'turn. Suddenly a figure jumps out from around the corner. The figure screams \'Leaving so soon?!\''
    if convert_input(gets_knife) == 'y' or convert_input(gets_knife) == 'yes':
        use_knife_on_figure()
    print 'The figure grabs you throwing you both to the ground. ' \
          'A distant voice screams an inaudible sentence and the figure recoils as if in pain. ' \
          'Wailing the figure slowly crawls away as you cautiously you look around and see numbered rooms. \n\n' \
          'Standing up you see a light on down the hall. Walking towards the glow of the light the screaming of the ' \
          'inaudible voice grows louder and louder. You can hear more and more people screaming louder and louder. ' \
          'Upon reaching the light you slowly lean your head in and see a phone in the corner. \n\nCarefully you ' \
          'approach the phone. In an instant the screaming that encircled you ends. For a moment there is a peaceful ' \
          'silence. Suddenly your moment of peace is ended as the phone springs to life.'
    uses_phone()
    print 'You step backwards, your eyes never leaving the phone, wondering if this was all a dream or some twisted ' \
          'nightmare. \n\n In the distance you hear footsteps ominously growing closer and closer. You rapidly ' \
          'hunt for a place to hide. You see a locker in the corner and sprint towards it. \n\n Right as you grab ' \
          'the handle you feel a cold big hand firmly grab your shoulder. Horrified you turn around and see that it ' \
          'is the same figure from before. The figure has a ghastly smile across his scarred face, ' \
          '\'There you are!\'. Fear overwhelms you as the hairs on your back stand high like soldiers standing ' \
          'in formation. The figure raises his hand and slams it across your face. In a flash everything goes back. ' \
          '\n\n '


start_game()
