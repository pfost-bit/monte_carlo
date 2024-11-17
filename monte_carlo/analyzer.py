import numpy as np
import pandas as pd

from .game import Game
class Analyzer():
    """
    An Analyzer object takes the results of a single game and computes various descriptive statistical properties about it.

    Methods:
        JackPot(): A method to determine the numnber of "jackpots" rolled in a game.
        FaceCounts(): A method to return a datframe with the total number of facecounts for each die.
        ComboCounts(): A method to count the counts of each combination of faces rolled.
        PermCounts(): A method to count the counts of each permuatation of the face rolled.

    Attributes:
        game: The game object to analyze, must be a game object
    
    """

    def __init__(self, game):
        if isinstance(game, Game): #check to see if game is a game object
            self.game = game
        else:
            raise ValueError("The input should be a Game object")
            
    def JackPot(self):
        """
        A method to determine how many jackpots were rolled in the game, i.e. all of the faces are the same for the die. All heads on a coin for example.

        returns:
            int for the number of times all the outcomes were the same.
        """

        results = self.game.show_results().copy() #get results
        jackpots = results.apply(lambda die_rolls: len(set(die_rolls)) == 1, axis=1).sum()# for a row wise function we can use .apply, lamba function checks the set of the row and sees if it has one value. 
        
        return jackpots

    def FaceCounts(self):
        """
        A method to count the total number of each face.

        returns:
            face_counts: pd.DataFrame of the results. A wide dataframe that shows how many times each face was rolled per dice.
        """

        results0 = self.game.show_results("narrow").copy() #get results in the narrow format
        face_counts = results0.groupby(["Die", "Outcome"]).value_counts() #use groupby to get the value of each outcome, for each die
        face_counts = face_counts.unstack() #convert to wide
        face_counts.index.name = "Die"
        
        return face_counts

    def ComboCounts(self):
        """
        A method to count the counts of each combination of faces rolled.

        returns:
            combo_counts: pd.DataFrame of the results. A datframe with the the Combinations and their counts 
        """
        results1 = self.game.show_results().copy() # get the wide format
        combo_counts = results1.apply(lambda die_rolls: tuple(sorted(die_rolls)), axis=1).value_counts().reset_index() #since the order does not matter in a combination we sort the tuples so that for example (1,2) = (2,1)
        combo_counts.columns = ["Combination", "Count"] #give new column names
        combo_counts = combo_counts.set_index("Combination").sort_index(axis=0) #create MultIndex

        return combo_counts

    def PermCounts(self):
        """
        A method to count the counts of each permuatation of the face rolled.

        returns:
            perm_counts: pd.DataFrame of the results.
        """

        results = self.game.show_results().copy() #get the wide
        perm_counts = results.apply(lambda die_rolls: tuple(die_rolls), axis=1).value_counts().reset_index() #like above, however it treats each tuple as distinct. (1,2) neq (2,1)
        perm_counts.columns = ["Permutation", "Count"] #give new column names
        perm_counts = perm_counts.set_index("Permutation").sort_index(axis=0) #createMultIndex

        return perm_counts