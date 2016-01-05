from dictionaries import splashes
    # Gets the game splashes
from dictionaries import rooms
    # Gets the room dictionaries.
from dictionaries import arsenal
    # Gets the weapon dictionaries.
import random

    
# Sets initial values.

playing = True

# To-Do List:
"""
    - Functions
        - Play - Holds main game logic - nothing else. 
    - Output
         Add descriptions for all rooms.
        - Add ASCII art to intro/exit/start/death/game-over/etc.
    - Rubric & Assignment Considerations
        Entry Event  - https://s3.amazonaws.com/echo_files/20140507/_1399426771_pythonista_entry_event.pdf 
        Project Rubtic - https://s3.amazonaws.com/echo_files/20140514/_1400074736_pythonista_rubric.pdf
        - Get player name and use it somehow.
        - Weapons need to have range? Ask faciliatator for clarity.
        - Hook player w/ intro
    - Repo on GitHub
"""

def health_handler(initial, change, max=100, kill=False):
    health = initial + change
    health = max if health > max else health
    health = 0 if health < 0 else health
    
    return health
    
def show_health(health):
    print("You have", str(health) + "/100 health remaining.")
    
def room_greeter(current_room, health):
    print(current_room['greeting'])
    show_health(health)
    print(current_room['option_text'])

def choose_weapon(weapons, monster_name):
    
    """
    Prompts the player to choose a weapon
    from a list.
    
    Returns the id of the weapon chosen.
    """
    
    id_key = []
    
    for weapon in weapons:
        id_key.append(weapon)
    
    while True:
        id = 0
        print()
        print("Attack " + monster_name + " with...")
        print()
        
        for weapon in weapons:
            id += 1
            print(str(id) + ". " + weapons[weapon]['label'] + ", which deals " + str(weapons[weapon]['damage']+5).lstrip("-") + " to " + str(weapons[weapon]['damage']-5).lstrip("-") + " damage per hit.")
        
        print()
        print("What do you choose?")
        choice = input("> ")
        if choice.isnumeric() and 0 <=int(choice) <= len(id_key) and id_key[int(choice)-1] in weapons:
            print("You chose the " + weapons[id_key[int(choice)-1]]['label'])
            print()
            return id_key[int(choice)-1]
        else:
            print("Invalid.")

def get_usable_weapons(weapons):
    
    """
    Loops through all weapons in game
    and determines which have been found
    by the player.
    
    Returns a dictionary of just the weapons
    that are usable and their attributes in
    a sub-dictionary.
    """
    
    usable_weapons = {}
    
    for weapon in weapons:
        if weapons[weapon]['found']:
            usable_weapons[weapon] = weapons[weapon]
    
    return usable_weapons
    
def check_battle(player_health, monster_health):
    
    # Returns [still_battling, won]
    
    if player_health <= 0 and monster_health > 0:
        # print(1)
        # still_battling = False
        # won = False
        # break
        return [False, False]
    elif player_health > 0 and monster_health <= 0:
        # print(2)
        # still_battling = False
        # won = True
        # break
        return [False, True]
    elif player_health <= 0 and monster_health <= 0:
        # print(3)
        # still_battling = False
        # won = False
        # break
        return [False, False]
    else:
        # still_battling = True
        # won = None
        return [True, None]
        
    
def battle(battle, weapons, health):
    
    # should return array of [whether won or not, health left] 
    
    battling = True
    usable_weapons = get_usable_weapons(weapons)
    monster_health = battle['monster_max_health']
    
    print("You must now fight", battle['monster_name'] + ".")
    print(battle['monster_name'] + "'s weapon is the", battle['monster_weapon']['name'] + ".")
    print(battle['monster_weapon']['name'], "deals", str(battle['monster_weapon']['damage']), "damage per hit.")
    while battling and monster_health > 0:
        """
        Problem is caused because monster attacks after you do. 
        
        
        """

        # Monster attacks player with weapon
        health = health_handler(health, battle['monster_weapon']['damage'])
        
        print("*" * 60)
        print("* " + (battle['monster_name'] + " attacks you with the " + battle['monster_weapon']['name'] + ".").center(56, " ") + " *")
        print("* " + ("You lose " + str(battle['monster_weapon']['damage'] * -1) + " health.").center(56, " ") + " *")
        print("* " + (str(health) + " health remaining.").center(56, " ") + " *")
        print("*" * 60)
        
        # Checks to see if player still has health to attack.
        checks = check_battle(health, monster_health)
        if not checks[0]:
            battling = checks[0]
            break
        
        # Player chooses weapon.
        weapon = usable_weapons[choose_weapon(usable_weapons, battle['monster_name'])]
        
        # Monster is attacked with weapon
        monster_health = health_handler(monster_health, (abs(random.randint(weapon['damage']-5, weapon['damage']+5)) * -1), battle['monster_max_health'])
        
        # print("battling in progress...", monster_health, health)
        
        
        # if health <= 0 and monster_health > 0:
            # print(1)
            # won = False
            # Battling = False
            # break
        # elif health > 0 and monster_health <= 0:
            # print(2)
            # won = True
            # battling = False
            # break
        # elif health <= 0 and monster_health <= 0:
            # print(3)
            # won = False
            # battling = False
            # break
            
        checks = check_battle(health, monster_health)
        battling = checks[0]
        won = checks[1]
        
        
        
    return [won, health]
def next_room(option_text, options):
    
    while True:
        decision = input("> ").upper()
            
        if decision in options:
            return decision
        else:
            print("Invalid input.")
            print(option_text)

def weapon_handler(found, existing):
    
    # Adds found weapons to the array.
    #   Also removes all weapons if found equals -1.
    #   
    
    if found != -1:
        for item in found:
            if item in existing:
                existing[item]['found'] = True
        return existing
    elif found == -1:
        for item in existing:
            if existing[item]['can_lose']:
                existing[item]['found'] = False;
    else:
        return existing

def splasher(which):
    
    print()
    print(splashes.splash[which])
    print()

def yn_query(query):
    while True:
        print(str(query) + "?")
        answer = input("[y/n] >")
        
        if answer[0].casefold() == 'y'.casefold():
            return True
        elif answer[0].casefold() == 'n'.casefold():
            return False
            
        print("Invalid input.")
    
def instructions():    
    print("--GAME INSTRUCTIONS--")
    print()
    splasher('instructions')
    print()
    print("Press return to continue.")
    input()
    
def game_menu():
    while True:
        print("""
--GAME MENU--
1. Play Now!
2. Show Instructions
3. Quit Game

What would you like to do?""")
        response = input(">")
        
        if response == '1':
            break
        elif response == '2':
            instructions()
        elif response == '3':
            return 'EXIT'
        else:
            print("Invalid input.")

def get_name():
    while True:
        print('Please input your first name.')
        name = input("> ")
        if name.isalpha():
            return str(name)
        
        print("Invalid input. Only letters are allowed in player names.")
            
splasher('title')
player_name = get_name()
print("Welcome to the game, " + player_name + ".")


while playing:
    
    initial_action = game_menu()
    if initial_action == 'EXIT':
        break
    
    splasher ('game_start')
    
    current_room = rooms.room['start']
    prev_room = {}
    health = 100
    dead = False
    
    while not dead:
        
        # Handle health
        health = health_handler(health, current_room['health'])
        current_room = rooms.room['graveyard'] if health <= 0 else current_room # Sends you to graveyard if you're dead.
        
        # Handle adding weapons to arsenal
        if current_room['found_weapons'] != None:
            arsenal.weapon = weapon_handler(current_room['found_weapons'], arsenal.weapon)
        
        # Outputs the greeting for the room and remaining health to the console.
        room_greeter(current_room, health)
        
        # If current room has battle, run battle handler.
        #   Otherwise, ask what room to proceed to.
        if current_room['battle']:
            battle_results = battle(current_room['battle_props'], arsenal.weapon, health)
            
            won = battle_results[0]
            health = battle_results[1]
            health = health_handler(health, 0)
            
            if won:
                prev_room = current_room
                current_room = rooms.room[current_room['battle_props']['on_defeat']]
            else:
                prev_room = current_room
                dead = True
        else:
            prev_room = current_room
            current_room = rooms.room[next_room(current_room['option_text'], current_room['next'])]
            
        
    splasher('game_over')
    print()    

print("Thanks for playing, " + player_name + ".")
splasher('goodbye')