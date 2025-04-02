## Description

This project is the second project in Week 0. The program uses adversarial Search, and in particular, the Minimax algorithm.

## How It Works

1.	The tictactoe.py file is in charge of the backend, while the runner.py file is in charge of the front end.
2.	In the back side, several functions are defined, to find the available actions, to find the winners or for the AI to take the next optimal move, etc. The most important function is the Minimax function, where it calculates the score of resulting board if a certain move is taken by recursively simulate all the possible move by the opponent. A comparison is done following the calucalation and the optimal move is returned.
3.	Theorectically, the result of a tictactoe game in an optimal state is a draw for both of the players.

## Running the Program

1.	Clone the repository:
```bash
git clone https://github.com/blackhole-hope123/CS50-projects.git
cd path/CS50-projects/tictactoe
```

2.	Run the program:

```
python runner.py
```

3.	Choose to go first or second and play with AI!

An example video:



## File Structure

-	tictactoe.py: The back end program that help computer to make decision.
-	runner.py: The front end program that maintain the game interface.
-	requirements.txt : Required python packages to run the codes.
-	OpenSans-Regular.ttf : Ensuring consistent and high-quality text display. .
-	README.md: Project documentation.

## Concepts Used 
-	Minimax algorithm (adversarial search): For the computer to make the optimal 
-	Data Structures: Sets, lists, dictionaries, and trees (implicitly).

## Acknowledgement 
This project is part of CS50’s AI Course by Harvard University.
