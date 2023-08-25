The program implements the basic functionality for Connect 4 game. It can be run from the terminal
by typing python ./counter.py 

The 4 basic requirements were: 
1. user input: This must be the player 1 as the other player is computer who's turns are random.
2. Checking the validity of user input: If the user input is out of column range. here it is (0, 6) which means there are 7 column spaces for input. 
3. Display the grid: there is a grid displayed after every player turn and the computer turn. Computer turns are typed as 2 and player turns are typed as 1. Design could be better.
4. Check stalemate: Stalemate is when the grid has no space left for any input. 

Functions:
1. Create_board function creates the board with zeros. (design could have been better, due to time limitation, I could not do it).
2. print_board function prints the grids in a board like form on terminal.
3. is_valid_move check returns the board after the turns are placed. 
4. is_stalemate checks if there are no columns left to place any more counters.

Challenges: 
1. Better design could be implemented (we could use pygame)
2. proper testing is needed (pytest)
3. proper documentation is missing. (docstrings could be used)

These challenges could be overcome with time.