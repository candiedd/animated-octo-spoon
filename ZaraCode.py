import random
Username=input("What is your name? ")
print("Classes: Warrior, Mage")
Class=input("Class: ")
if Class=='Warrior':
    attack=8
if Class=='Mage':
    attack=2
    magic=5
if Class=='Mage':
    print("A rat comes before you. What do you do? Attack, use magic, or block")
    rathealth=6
    action=input('Action: ')
    if action=='Attack':
        print('This is underdeveloped. I need to finish this. Read the comment for why') # I need to work on the magic system
if Class=='Warrior':
    print('A rat comes before you. What do you do? Attack or block')
    rathealth=6
    action=input('Action: ')
    if action=='Block':
        print('The rat attacks for 4 health, but you block the attack.')
        action=input('Action: ')
    if action=='Attack':
        Damage=random.randint(4,6)
        print('You stab the rat with your sword, dealing '+str(Damage)+' damage')
        if Damage>=rathealth:
            print('The rat is dead! Good job')
        else:
            print('The rat is not killed yet.')
            action=input('Action: ')