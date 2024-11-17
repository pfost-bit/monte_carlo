# monte_carlo

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
  game1 = Game([die1,die1]) #this passes two of the same die objects
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















  
