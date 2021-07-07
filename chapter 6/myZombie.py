import zombiedice
import random

class MyZombie:
        def __init__(self, name):
            # All zombies must have a name:
            self.name = name

        def turn(self, gameState):
            # gameState is a dict with info about the current state of the game.
            # You can choose to ignore it in your code

            diceRollResults = zombiedice.roll() #first roll
            # roll() returns a dictionary with keys 'brains', 'shotgun', and 
            # 'footsteps' with how many rolls of each type there were.
            # The 'rolls' key is a list of (color, icon) tuples with the 
            # exact roll result information.
            # Example of a roll() return value:
            # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
            # 'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
            #           ('green', 'shotgun')]}
            
            # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
            shotguns = 0
            brains = 0
            while diceRollResults is not None: 
                shotguns += diceRollResults['shotgun']
                brains += diceRollResults['brains']
                
                if shotguns > brains:
                    diceRollResults = zombiedice.roll()
                else:
                    break


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    MyZombie(name='My Zombie :)')
)

zombiedice.runTournament(zombies=zombies, numGames=1000)