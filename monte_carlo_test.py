import unittest
import numpy as np
import pandas as pd
from monte_carlo import Die, Game, Analyzer


class MonteCarloTestSuite(unittest.TestCase):
    
    def test_1_create_die(self): 
        """ 
        Create a Die object and ensure some of the of attributes are correct
        """
        
        with self.assertRaises(TypeError):
            Die([1,2,3,4,5,6])#test to see if it catches the list vs an array
        
        with self.assertRaises(TypeError):
            Die(np.array([True, False]))#test to see if only numbers or str can be passed
        
        with self.assertRaises(ValueError):
            Die(np.array([1,1]))#check to see if unique values only
            
        with self.assertRaises(TypeError):
            Die(np.array([1,2]), [5,1]) #make sure that weights should be an array
        
        with self.assertRaises(ValueError):
            Die(np.array([1,2]), np.array([1,1,1])) #Makes sure that len(weights) == len(faces)
            
        test_die = Die(np.array([1,2,3,4,5,6])) #create a test die
        self.assertIsInstance(test_die,Die) # assert that it is created correctly
    
    def test_2_change_weight(self):
        """
        Create a Die object and change its weight, assert that it is created correctly
        """
        
        test_die = Die(np.array([1,2,3,4,5,6])) #create a test die
        test_die.change_weight(1,5) #change the weight of face 1 to equal 5
        results = test_die.show_die_state()
        self.assertEqual(results.loc[1,"weight"],5) #assert that the weight was changed
        
        with self.assertRaises(TypeError): #asserts that the new weight is a number 
            test_die.change_weight(1,"No")
        
        with self.assertRaises(ValueError): #asserts the face is in the face list
            test_die.change_weight(7,4)
        
    def test_3_roll_die(self):
        """
        Create a die object, roll it, test various things about it 
        """
        test_die = Die(np.array([1,2,3,4,5,6]))#create a die object
        results = test_die.roll_die(10) #roll the die 10 times
        
        self.assertEqual(len(results), 10) #assert that it was rolled 10 times and wrote an output
        
        for result in results:
            self.assertIn(result, test_die.faces) #assert that each face has a result
            
        
    def test_4_show_die_state(self):
        """
        Create a die object, see if the die_state can be seen as a pd.dataframe
        """
        
        test_die = Die(np.array([1,2,3,4,5,6]))#create a die object
        die_state = test_die.show_die_state() #see the die object 
        
        self.assertIsInstance(die_state, pd.DataFrame)#see if it is a dataframe
        self.assertEqual(sum(die_state.index == test_die.faces), len(test_die.faces)) # check to see if all of the faces are in the resulting die state
        self.assertEqual(sum(die_state.weight),len(test_die.weight)) # check to see if all of the weights are one and are added to the dataframe
        
        


        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)