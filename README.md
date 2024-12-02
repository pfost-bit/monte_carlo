---
title: monte_carlo
name: By Patrick Foster
---
A repository to create and test a sample Monte-Carlo simulator for DS5100. The project was to create a simple Monte-Carlo simulator. This project entailed two parts.

1. To create a Python project that has three classes.
     * Die: A class to create Die objects
     * Game: A class to create Game objects
     * Analyzer: A class to create Analyzer objects
2. To publish these classes as a downloadable package.

## Getting Started

These instructions will get a copy of the project up and running on your local machine. 

### Installing

The project is a downloadable package that can be accessed here in this file structure.

1. Create a local copy of this Python package by cloning it into the repository using the bash command:
   
   ```bash
   git clone git@github.com:pfost-bit/monte_carlo.git
   ```
2. After you have a cloned repository on your local machine and have navigated to it, you can download the package using the bash command
   
   ```bash
   pip install .
   ```
3. After running the above command, there should be a completion message that looks something like:

   ```raw
   PS Z:\Semester1\Programing for DS\FinalProject\monte_carlo> pip install .
    Processing z:\semester1\programing for ds\finalproject\monte_carlo
      Preparing metadata (setup.py) ... done
    Requirement already satisfied: numpy in c:\users\pfost\appdata\roaming\jupyterlab-desktop\jlab_server\lib\site-packages (from monte_carlo==0.6) (2.1.0) 
    Requirement already satisfied: pandas in c:\users\pfost\appdata\roaming\jupyterlab-desktop\jlab_server\lib\site-packages (from monte_carlo==0.6) (2.2.2)
    Requirement already satisfied: python-dateutil>=2.8.2 in c:\users\pfost\appdata\roaming\jupyterlab-desktop\jlab_server\lib\site-packages (from pandas->monte_carlo==0.6) (2.9.0)
    Requirement already satisfied: pytz>=2020.1 in c:\users\pfost\appdata\roaming\jupyterlab-desktop\jlab_server\lib\site-packages (from pandas->monte_carlo==0.6) (2024.1)
    Requirement already satisfied: tzdata>=2022.7 in c:\users\pfost\appdata\roaming\jupyterlab-desktop\jlab_server\lib\site-packages (from pandas->monte_carlo==0.6) (2024.1)
    Requirement already satisfied: six>=1.5 in c:\users\pfost\appdata\roaming\jupyterlab-desktop\jlab_server\lib\site-packages (from python-dateutil>=2.8.2->pandas->monte_carlo==0.6) (1.16.0)
    Building wheels for collected packages: monte_carlo
      Building wheel for monte_carlo (setup.py) ... done
      Created wheel for monte_carlo: filename=monte_carlo-0.6-py3-none-any.whl size=6827 sha256=cd3367809052ee68a52b4908032f15ed6feaa0f241c7a5874fce23ee3e84f416
      Stored in directory: C:\Users\pfost\AppData\Local\Temp\pip-ephem-wheel-cache-x4hjxsg1\wheels\4b\2d\1d\3f78df0704c4b395080703406b2311162928ebce41f00611dd  
    Successfully built monte_carlo
    Installing collected packages: monte_carlo
      Attempting uninstall: monte_carlo
        Found existing installation: monte_carlo 0.5
        Uninstalling monte_carlo-0.5:
          Successfully uninstalled monte_carlo-0.5
    Successfully installed monte_carlo-0.6
   ```

The package should now be successfully installed.

### Some Examples  

Now that we have installed the package, we can try to use it to our advantage.

First, we need to make sure to import the Classes correctly; this can be done with the call:

```python
import numpy as np #importing numpy
import pandas as pd #importing pandas
from monte_carlo import Die, Game, Analyzer #importing the classes needed for using the monte_carlo package
```

#### The Die Class:

* Now we will create some Die objects:

   ```python
   die1 = Die(np.array([1,2,3,4,5,6]))#fair
   die2 = Die(np.array([1,2,3,4,5,6]))#fair
   ```
   This creates two identical dice with 6 "faces," each with an equal likelihood of being rolled. The faces are passed as a np.array() of objects; the objects should be a number or a string.
  
* Dice can also be created by passing a separate np.array() of likelihoods:

  ```python
  die3 = Die(np.array([1,2,3,4,5,6]),np.array([5,1,1,1,1,1])) #this makes the value 1, 5 times more likely to occur.
  ```

* The side likelihoods can also be changed using the change_weight() method.

  ```python
  die1.change_weight(1,5) # here the "face" 1 is changed to have a weight of 5
  ```
  So now the two die objects, die1 and die3 are equivalent.

* Finally the die objects can be rolled:

  ```python
  die1.roll_die(10) #rolls the die 10 times
  ```

  ```raw
  [np.int64(4), np.int64(2), np.int64(5), np.int64(3), np.int64(6), np.int64(1), np.int64(1), np.int64(5), np.int64(5), np.int64(2)]
  ```
  This roll method is not too important by itself but is very important in expanding to the Game class.


#### The Game Class:

* Now to create some game objects:

  ```python
  game1 = Game([die2,die2]) #this passes two of the same die objects (fair ones)
  ```

* We can now play a game by rolling the two dies passed to the Game object:

  ```python
  game1.play(10) # this rolls each die 10 times
  ```

* We can see the results of these rolls by using the method show_results:

  ```python
  game1.show_results()
  ```

  ```raw
		0	1
	Roll		
	0	4	5
	1	3	2
	2	1	2
	3	2	4
	4	5	6
	5	1	4
	6	4	5
	7	2	4
	8	1	2
	9	6	1
  ```
    * Can also be called in the narrow format

    ```python
    game1.show_results("narrow")
    ```

    ```raw
			Outcome
	Roll	Die	
	0	0	4
		1	5
	1	0	3
		1	2
	2	0	1
		1	2
	3	0	2
		1	4
	4	0	5
		1	6
	5	0	1
		1	4
	6	0	4
		1	5
	7	0	2
		1	4
	8	0	1
		1	2
	9	0	6
		1	1
    ```

#### The Analyzer Class:  

Here we can see some simple statistics about our game.  

* Lets create an Analyzer() Object:

  ```python
   analyzer1 = Analzyer(game1)
  ```

* We can see how many "JackPots" were rolled, which is how many times all of the outcomes were the same.

  ```python
  analyzer1.JackPot()
  ```

  ```raw
  np.int64(0) #in this case, no outcomes were rolled the same
  ```
* We can also see the number of times each face is rolled.

  ```python
  analyzer1.FaceCounts()
  ```

  ```raw
  Outcome	1	2	3	4	5	6
	Die						
	0	3.0	2.0	1.0	2.0	1.0	1.0
	1	1.0	3.0	NaN	3.0	2.0	1.0
  ```

* We can see the number of Combinations that are rolled; combinations are not unique, (1,2) == (2,1)
 
```python
analyzer1.ComboCounts()
```

```raw
      Count
Combination	
(1, 2)	2
(1, 4)	1
(1, 6)	1
(2, 3)	1
(2, 4)	2
(4, 5)	2
(5, 6)	1
```

* We can finally see the different permutations that are rolled; permutations are unique

```python
analyzer1.PermCounts()
```

```raw
      Count
Permutation	
(1, 2)	2
(1, 4)	1
(2, 4)	2
(3, 2)	1
(4, 5)	2
(5, 6)	1
(6, 1)	1
```

## API and Documentation  

We can see some information about the package by using the help command 

```python
help(monte_carlo)
```

```raw
Help on package monte_carlo:

NAME
    monte_carlo - monte_carlo

DESCRIPTION
    This package provides tools for running Monte Carlo simulations, including components for handling dice, games, and analysis.

    Modules:
        - die: Contains the Die class for simulating dice rolls.
        - game: Contains the Game class for managing dice games.
        - analyzer: Contains the Analyzer class for analyzing game results.

PACKAGE CONTENTS
    analyzer
    die
    game

CLASSES
    builtins.object
        monte_carlo.analyzer.Analyzer
        monte_carlo.die.Die
        monte_carlo.game.Game

    class Analyzer(builtins.object)
     |  Analyzer(game)
     |
     |  An Analyzer object takes the results of a single game and computes various descriptive statistical properties about it.
     |
     |  Methods:
     |      JackPot(): A method to determine the numnber of "jackpots" rolled in a game.
     |      FaceCounts(): A method to return a datframe with the total number of facecounts for each die.
     |      ComboCounts(): A method to count the counts of each combination of faces rolled.
     |      PermCounts(): A method to count the counts of each permuatation of the face rolled.
     |
     |  Attributes:
     |      game: The game object to analyze, must be a game object
     |
     |  Methods defined here:
     |
     |  ComboCounts(self)
     |      A method to count the counts of each combination of faces rolled.
     |
     |      returns:
     |          combo_counts: pd.DataFrame of the results. A datframe with the the Combinations and their counts
     |
     |  FaceCounts(self)
     |      A method to count the total number of each face.
     |
     |      returns:
     |          face_counts: pd.DataFrame of the results. A wide dataframe that shows how many times each face was rolled per dice.
     |
     |  JackPot(self)
     |      A method to determine how many jackpots were rolled in the game, i.e. all of the faces are the same for the die. All heads on a coin for example.
     |
     |      returns:
     |          int for the number of times all the outcomes were the same.
     |
     |  PermCounts(self)
     |      A method to count the counts of each permuatation of the face rolled.
     |
     |      returns:
     |          perm_counts: pd.DataFrame of the results.
     |
     |  __init__(self, game)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class Die(builtins.object)
     |  Die(faces, weight=array(-0.))
     |
     |  A class which initializes a Die object. This object has a number of "faces", and weight "w". The after creation the Die object it can be rolled n number of times.
     |
     |  Methods:
     |      change_weight(weight): Changes the weight of a single face
     |      roll_die(n): rolls the die a set number of times
     |      show_die_state(): Shows the current die state
     |
     |  Attributes:
     |      faces: The number of faces a die object has. The faces argument is a numpy array. The array should be of subtypes: str or numbers.
     |      weight: The weight initializes as a weight of 1, but can be changed as needed. The weights should be passed as a np.array of weights.
     |
     |  Methods defined here:
     |
     |  __init__(self, faces, weight=array(-0.))
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  change_weight(self, face, new_weight)
     |      A method to change the weight of a single face.
     |
     |      args:
     |          face:
     |               The name of the Face whose weight is to be changed (should be in list of faces)
     |          new_weight:
     |               The new weight for the face (should be an number or castable as one) larger = more frequent
     |
     |  roll_die(self, n)
     |      A method to roll the die n times.
     |
     |      args:
     |          n: The number of times to roll the dice, should be an int.
     |      returns:
     |          result: a list of outcomes
     |
     |  show_die_state(self)
     |      A method to return a copy of the private die_tables state
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object

    class Game(builtins.object)
     |  Game(die_list)
     |
     |  A class to take a list of similar die, and play a game.
     |      A game is to roll the dice, one or more times
     |      Similar means to have the same number of "faces", they could have different weights, i.e. flip two coins, one fair one that prefers heads etc
     |
     |  Methods:
     |      play(rolls): A method to play a game (roll the die objects, num_of_rolls times)
     |      show_results: A method to return the results in a pd.DataFrame. Can be wide or narrow.
     |
     |  Attributes:
     |      die_list: A list of Die objects.
     |      results: A pd.DataFrame of Results. The results are the values for the each time the dice was rolled.
     |
     |  Methods defined here:
     |
     |  __init__(self, die_list)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  play(self, num_of_rolls)
     |      A method to play a game a certain number of times. Stores the result in a pd.DataFrame()
     |      args:
     |          num_rolls: how many times each die is rolled.
     |      returns:
     |          self.results: changes the attribute of results
     |
     |  show_results(self, form='wide')
     |      A method to return the results of the results DataFrame. The dataframe is returned as a wide dataframe by default, and a narrow one if wanted.
     |      args:
     |          form: "wide" or "narrow" (default of "wide)
     |      returns:
     |          self.results.copy(): A copy of the results table.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables
     |
     |  __weakref__
     |      list of weak references to the object
```












  
