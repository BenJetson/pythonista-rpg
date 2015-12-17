class splashes:
	
	title = """Welcome to Hostage Escape."""
	instructions = """ """ 
	game_start = """ """
	game_over = """ """
	goodbye = """ """

class rooms:
	room = {
    	'start' : {
        	"greeting" : """Welcome to Hostage Escape. You wake up alone in a locked room. You remember were captured by terrorists, and are being held hostage for a reason unknown..""",
        	"option_text" : """Would you like to try to get the ropes off(A) or examine the room(B)?""",
        	"next" : ['A', 'B'],
        	"found_weapons" : None,
        	"health" : 0,
        	"battle" : False,
        	"battle_props" : None
    	},
   	 `
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
        	"greeting" : """While the terrorists hear you struggling, you are tortured and loose 30 HP. They leave and accidently forgot one AK47."""
        	"option_text" : """Proceed to room B by typing B.""",
        	"next" : ['B'],
        	"found_weapons" : ['AK-47'],
        	"health" : -30,
        	"battle" : False,
        	"battle_props" : None
    	},

    	'B' : {
        	"greeting" : """You choose to examine the room and see a knife on the floor by your foot, which you use to cut the rope."""
        	"option_text" : """Search for a supplies(C) or search for an exit(D).""",
        	"next" : ['C', 'D'],
        	"found_weapons" : None
        	"health" : 0,
        	"battle" : False,
        	"battle_props" : None
    	},

    	'C' : {
        	"greeting" : """You are looking for supplies, but take too long and get caught. You have been shot in the back and died."""
        	"option_text" : """ """,
        	"next" : ['D', 'E', 'F'],
        	"found_weapons" : None,
        	"health" : -100,
        	"battle" : False,
        	"battle_props" : None
    	},

    	'D' : {
        	"greeting" : """You have found a way through the air vent. You see a room, should you drop down or not. """
        	"option_text" : """Choose to drop down(E) or Continue Past(F).""",
        	"next" : ['E', 'F'],
        	"found_weapons" : None,
        	"health" : 0,
        	"battle" : False,
        	"battle_props" : None
    	},

    	'E' : {
        	"greeting" : """You drop down into the room and find and M4A4 with ammo in it. Suddenly you hear a noise.""",
        	"option_text" : """Press F to continue...""",
        	"next" : ['F'],
        	"found_weapons" : ['M4A4'],
        	"health" : 0,
        	"battle" : False,
        	"battle_props" : None
    	},

    	'F' : {
        	"greeting" : """A Terrorist enters the room and you have no choice but to fight him.""",
        	"option_text" : """ """,
        	"next" : [],
        	"found_weapons" : None,
        	"health" : 0,
        	"battle" : True,
        	"battle_props" : {
            	"on_defeat" : 'G',
            	"monster_name" : 'A Terrorist',
            	"monster_health" : 200,
            	"monster_weapon" : {
                	"name" : "AK-47",
                	"damage" : -35,
            	}
        	}
    	},
   	 
    	'G' : {
        	"greeting" : """Good job defeating the terrorist, you have found a health pack!... now you can go past him (F) or stay and try to look for other hostages(H).""",
        	"option_text" : """Go past the terrorist(H) or stay and try to look for other hostages(F)?""",
        	"next" : ['H', 'F'],
        	"found_weapons" : None,
        	"health" : +50,
        	"battle" : False,
        	"battle_props" : None
    	},

    	'H' : {
        	"greeting" : """You have """,
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
        	"found" : False
    	},
   	 
    	'stick' : {
        	"label" : "Pointed Stick",
        	"damage" : -5,
        	"ammo" : None,
        	"found" : False
    	},
   	 
    	'bow' : {
        	"label" : "Bow and Arrow",
        	"damage" : -20,
        	"ammo" : 5,
        	"found" : False
    	},
   	 
    	'waraxe' : {
        	"label" : "War Axe",
        	"damage" : -40,
        	"ammo" : None,
        	"found" : False
    	},
   	 
    	'hand' : {
        	"label" : "Punch with fist",
        	"damage" : -15,
        	"ammo" : None,
        	"found" : True
    	}
	}
