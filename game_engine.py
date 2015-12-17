from dictionaries import splashes
    # Gets the game splashes
from dictionaries import rooms
    # Gets the room dictionaries.
from dictionaries import arsenal
    # Gets the weapon dictionaries.
    
# Sets initial values.

current_room = rooms.room['start']
prev_room = {}
health = 100
playing = True

# To-Do List:
"""
    - Functions
        - Play - Holds main game logic - nothing else. 
        - Health Handler - Returns health, checks against environment/actions.
        - Announcer - Reads greetings/options.
        - Battle Handler - Handles the battle.
        - Weaponry handler - add weapons to arsenal if in room.
        - Death
        - Splashes
    - Output
        - Add descriptions for all rooms.
        - Add ASCII art to intro/exit/start/death/game-over/etc.
    - Rubric & Assignment Considerations
        Entry Event  - https://s3.amazonaws.com/echo_files/20140507/_1399426771_pythonista_entry_event.pdf 
        Project Rubtic - https://s3.amazonaws.com/echo_files/20140514/_1400074736_pythonista_rubric.pdf
        - Get player name and use it somehow.
        - Weapons need to have range? Ask faciliatator for clarity.
        - Hook player w/ intro
    - Storyline Ideas
        - Whole game is in castle.
        - Objective is to escape the castle alive.
        - Dungeon?
    - Engine Logic
    - Repo on GitHub
    - Replace graveyard room with just exiting loop and displaying death message. 
"""

def health_handler(initial, change, kill=False):
    health = initial + change
    health = 100 if health > 100 else health
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
            print(str(id) + ". " + weapons[weapon]['label'] + ", which deals " + str(weapons[weapon]['damage']).lstrip("-") + " damage per hit.")
        
        print()
        print("What do you choose?")
        choice = input("> ")
        if choice.isnumeric() and 0 <=int(choice) <= len(id_key) and id_key[int(choice)-1] in weapons:
            print("You chose the " + id_key[int(choice)-1])
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
    
def battle(battle, weapons):
    
    # should return array of [whether won or not, health left]
    
    battling = True
    usable_weapons = get_usable_weapons(weapons)
    
    print("You must now fight", battle['monster_name'] + ".")
    print(battle['monster_name'] + "'s weapon is the", battle['monster_weapon']['name'] + ".")
    print(battle['monster_weapon']['name'], "deals", str(battle['monster_weapon']['damage']), "damage per hit.")
    while battling and battle['monster_health'] > 0:
        
        weapon = usable_weapons[choose_weapon(usable_weapons, battle['monster_name'])]
        
        battle['monster_health'] += weapon['damage']
        
        print("battling in progress...")
        # health  -= 200
        
        won = True
        battling = False
        
    if won:
        return True

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
    
while playing:
    
    
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
        won = battle(current_room['battle_props'], arsenal.weapon)
        
        if won:
            prev_room = current_room
            current_room = rooms.room[current_room['battle_props']['on_defeat']]
    else:
        prev_room = current_room
        current_room = rooms.room[next_room(current_room['option_text'], current_room['next'])]
        
        