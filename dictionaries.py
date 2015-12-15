class splashes:
    title = """ """
    instructions = """ """
    game_start = """ """
    game_over = """ """
    goodbye = """ """
  
class rooms:
    room = {
        'start' : {
            "greeting" : """Welcome to the game.""",
            "option_text" : """Would you like to proceed to room A or B?""",
            "next" : ['A', 'B'],
            "found_weapons" : None,
            "health" : 0,
            "battle" : False,
            "battle_props" : None
        },
        
        'graveyard' : {
            "greeting" : """You are now dead. Welcome to the graveyard!""",
            "option_text" : """ """,
            "next" : [], 
            "found_weapons" : None,
            "health" : 0,
            "battle" : False,
            "battle_props" : None
            # Note - usage of graveyard as room is depreceated
            #   and will be removed soon in favor of a function
            #   within the game engine itself. 
        },

        'A' : {
            "greeting" : """Welcome to room A.
You've found a pointed stick! Now you can defend yourself!""",
            "option_text" : """Proceed to rooms B, C, or E?""",
            "next" : ['B', 'C', 'E'], 
            "found_weapons" : ['stick'],
            "health" : 0,
            "battle" : False,
            "battle_props" : None
        },

        'B' : {
            "greeting" : """Welcome to room B.
You've found a sword! Despite the rust, it'll still
make a valuable tool.""",
            "option_text" : """The next room is room C.""",
            "next" : ['C'], 
            "found_weapons" : ['sword'],
            "health" : 0,
            "battle" : False,
            "battle_props" : None
        },

        'C' : {
            "greeting" : """Welcome to room C.
You've found a piece of bread! 20 health gained.""",
            "option_text" : """Proceed to rooms D, E, or F?""",
            "next" : ['D', 'E', 'F'], 
            "found_weapons" : None,
            "health" : 20,
            "battle" : False,
            "battle_props" : None
        },

        'D' : {
            "greeting" : """What is this? It's a dead end! Just a closet full of old mouldy socks?
Yuck! You hear a sound from above you. Wham! A falling anvil hits 
you on the head, and you lose 40 health.""",
            "option_text" : """Return to room C.""",
            "next" : ['C'], 
            "found_weapons" : None,
            "health" : -40,
            "battle" : False,
            "battle_props" : None
        },

        'E' : {
            "greeting" : """Welcome to room E.
You've found a bow and arrow! Never know when that
might be useful.""",
            "option_text" : """Proceed to room C or F?""",
            "next" : ['C', 'F'], 
            "found_weapons" : ['bow'],
            "health" : 0,
            "battle" : False,
            "battle_props" : None
        },

        'F' : {
            "greeting" : """Welcome to room F.""",
            "option_text" : """ """,
            "next" : [], 
            "found_weapons" : None,
            "health" : 0,
            "battle" : True,
            "battle_props" : {
                "on_defeat" : 'G',
                "monster_name" : 'Zack the Barbarian',
                "monster_health" : 200,
                "monster_weapon" : {
                    "name" : "Club",
                    "damage" : -35,
                }
            }
        },
        
        'G' : {
            "greeting" : """Good job defeating the barbarian! You're
halfway there! Ooh! A plate of spaghetti.
Full health has been restored!""",
            "option_text" : """Where to next? Room H or I?""",
            "next" : ['H', 'I'], 
            "found_weapons" : None,
            "health" : 0,
            "battle" : False,
            "battle_props" : None
        },

        'H' : {
            "greeting" : """Oh no! You've fallen through a trap door in the floor!
You get up, and look around, and you realize that all of your
weaponry is gone. Furthermore, you're not even sure
what's coming next.""",
            "option_text" : """ """,
            "next" : ['I', 'J'], 
            "found_weapons" : None,
            "health" : 0,
            "battle" : False,
            "battle_props" : None
        },

        'I' : {
            "greeting" : """Yay! you found a plate of delicious brownies!
**stomach growls** Or maybe, not so delicious.
You then realize that the brownies were stale and moldy.
20 health lost.""",
            "option_text" : """ """,
            "next" : ['H', 'J'], 
            "found_weapons" : -1,
            "health" : -20,
            "battle" : False,
            "battle_props" : None
        },
        
        'J' : {
            "greeting" : """Welcome to room J.""",
            "option_text" : """ """,
            "next" : [], 
            "found_weapons" : None,
            "health" : 0,
            "battle" : True,
            "battle_props" : {
                "on_defeat" : 'graveyard',
                "monster_name" : 'the Snake',
                "monster_health" : 200,
                "monster_weapon" : {
                    "name" : "Snakebite",
                    "damage" : -40,
                }
            }
        }
    }

class arsenal:
    weapon = {
        'sword' : {
            "label" : "Steel Sword",
            "damage" : -20,
            "ammo" : None,
            "found" : False,
            "can_lose" : True
        },
        
        'stick' : {
            "label" : "Pointed Stick",
            "damage" : -5,
            "ammo" : None,
            "found" : False,
            "can_lose" : True
        },
        
        'bow' : {
            "label" : "Bow and Arrow",
            "damage" : -20,
            "ammo" : 5,
            "found" : False,
            "can_lose" : True
        },
        
        'waraxe' : {
            "label" : "War Axe",
            "damage" : -40,
            "ammo" : None,
            "found" : False,
            "can_lose" : True
        },
        
        'hand' : {
            "label" : "Punch with fist",
            "damage" : -15,
            "ammo" : None,
            "found" : True,
            "can_lose" : False
        }
    }