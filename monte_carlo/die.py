import numpy as np
import pandas as pd

class Die():
    """
    A class which initializes a Die object. This object has a number of "faces", and weight "w". The after creation the Die object it can be rolled n number of times.
    
    Methods: 
        change_weight(weight): Changes the weight of a single face
        roll_die(n): rolls the die a set number of times
        show_die_state(): Shows the current die state
        
    Attributes:
        faces: The number of faces a die object has. The faces argument is a numpy array. The array should be of subtypes: str or numbers.
        weight: The weight initializes as a weight of 1, but can be changed as needed. The weights should be passed as a np.array of weights.
    """

    def __init__(self, faces, weight = np.ndarray([])):

        #creates the self.faces array 
        if type(faces) != np.ndarray: #test to see if faces is correct type
            raise TypeError("The type() of faces should be a ndarray")
        elif (not np.issubdtype(faces.dtype, np.number) and (not np.issubdtype(faces.dtype, np.str_))): #Checks to see if the datatype of the list is number or str (MOORE'S LAW!)
            raise TypeError("The dtype of the faces should be int or str")
        elif len(faces) != len(np.unique(faces)): #Checks for uniquiness
            raise ValueError("The values of faces should be unique") 
        else:
            self.faces = np.array(faces) #finally creates the array of faces

        #creates the self.weights array (defaults to 1)
        if weight.ndim == 0: #check to see if base case (weight = 1)
            self.weight = np.ones(len(self.faces))
        elif type(weight) != np.ndarray: #check to see if weight is correct type
            raise TypeError("The type() of weights should be a ndarray")
        else:    
            self.weight = weight

        #creates a dataframe with faces/weights, the indeces are the faces
        self.__dTable = pd.DataFrame(
            index = self.faces,
            columns = ["weight"],
            data = self.weight
            ) 
        
    def __calc_prob(self):
        """
        A method to add a new column of data to the dataframe, "probabilities", which is the weight/total
        """
        total = self.__dTable["weight"].sum() #calculate total weight
        self.__dTable["probabilites"] = self.__dTable["weight"]/total #calc probabilites by dividing weight by total
        
    def change_weight(self, face, new_weight):
        """
        A method to change the weight of a single face.

        args: 
            face:
                 The name of the Face whose weight is to be changed (should be in list of faces)
            new_weight:
                 The new weight for the face (should be an number or castable as one) larger = more frequent
        """


        if face in self.faces:
            try:
                new_weight = float(new_weight)
                self.__dTable.loc[face].weight = new_weight
            except:    
                raise TypeError("The new_weight should be a number")
        else:
            raise ValueError("face is not in the list of faces")


    def roll_die(self, n):
        """
        A method to roll the die n times.

        args:
            n: The number of times to roll the dice, should be an int.
        returns:
            result: a list of outcomes
        """
        result = []
        self.__calc_prob()
        for i in range(n):
            result.append(np.random.choice(self.faces, p=self.__dTable["probabilites"]))
        return result
        
    def show_die_state(self):
        """
        A method to return a copy of the private die_tables state
        """
        return self.__dTable.copy()

if __name__ == '__main__':

    data1 = [1,2,3,4,5,6]
    six_side = np.array(data1)
    d6 = Die(six_side)
    print(d6.show_die_state())