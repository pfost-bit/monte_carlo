import numpy as np
import pandas as pd

from .die import Die

class Game():
    """
    A class to take a list of similar die, and play a game.
        A game is to roll the dice, one or more times
        Similar means to have the same number of "faces", they could have different weights, i.e. flip two coins, one fair one that prefers heads etc
        
    Methods:
        play(rolls): A method to play a game (roll the die objects, num_of_rolls times)
        show_results: A method to return the results in a pd.DataFrame. Can be wide or narrow.
        
    Attributes:
        die_list: A list of Die objects.
        results: A pd.DataFrame of Results. The results are the values for the each time the dice was rolled.
    """

    def __init__(self,  die_list):
        
        # list comprehension to check if all members of type "Die"
        if [die for die in die_list if not isinstance(die, Die)]:
            raise ValueError("All elements in die_list shoud be Die objects")
        self.die_list = die_list
        self.results = pd.DataFrame()

    def play(self, num_of_rolls):
        """
        A method to play a game a certain number of times. Stores the result in a pd.DataFrame()
        args: 
            num_rolls: how many times each die is rolled.
        returns:
            self.results: changes the attribute of results
        """
        #result_dict = {}
        #for die_n, die in enumerate(self.die_list): #loop through the list of die objects
        #    result_of_rolls = die.roll_die(num_of_rolls) # roll the die objects (roll_die returns a list of results)
        #    result_dict[die_n] = result_of_rolls  # add to the dictionary of results 

        result_dict = {die_n: die.roll_die(num_of_rolls) for die_n, die in enumerate(self.die_list)} # dictionary comprehension version

        results = pd.DataFrame(result_dict) #create dataframe (wide)
        results.index.name = "Roll" #each index is an individual Roll 

        self.results = results # set the self_results to the new DataFrame
                
        

    def show_results(self, form = "wide"):
        """
        A method to return the results of the results DataFrame. The dataframe is returned as a wide dataframe by default, and a narrow one if wanted.
        args:
            form: "wide" or "narrow" (default of "wide)
        returns: 
            self.results.copy(): A copy of the results table.
        """
        if form == "wide": 
            return self.results.copy() #returns the wide table made from the play method
        elif form == "narrow":
            self.results = self.results.stack().reset_index() #changes from wide to narrow
            self.results.columns = ['Roll', 'Die', 'Outcome'] # gives new column names
            self.results.set_index(['Roll', 'Die'], inplace = True) # gives new indicies as a multindex
            return self.results.copy() #returns narrow
        else:
            raise ValueError("The parameter of form should by 'wide' or 'narrow'") #error if not wide or narrow
        






if __name__ == '__main__':

    f_coin = np.array(["heads", "tails"])
    f_d6 = np.array([1,2,3,4,5,6])

    d1 = Die(f_d6)
    d2 = Die(f_d6)

    c1 = Die(f_coin)
    c2 = Die(f_coin, np.array([1,2]))
    
    game = Game([c1,c2])
    game.play(10)
    print(game.show_results())
    print(game.show_results("narrow"))