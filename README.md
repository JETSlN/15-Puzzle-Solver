# 15-Puzzle_Solver
Solving 15-piece-puzzle using heuristics

Input and output file formats: Your program will read in the value for W, the initial and goal 
states from a text file that contains 11 lines as shown in Figure 1 below. Line 1 contains the value 
for W. Line 2 is a blank line. Lines 3 to 6 contain the tile pattern for the initial state. Line 7 is a 
blank line. Lines 8 to 11 contain the tile pattern for the goal state. W is a floating point number. n
and m are integers that range from 0 to 15, representing the blank position (0) and the tile numbers
(1-15.)

Your program will produce an output file that contains 15 lines as shown in Figure 2 below. Lines 
1 to 4 contain the tile pattern for the initial state. Line 5 is a blank line. Lines 6 to 9 contain the tile 
pattern for the goal state. You can just copy the initial and goal states from the input file to the 
output file. Line 10 is a blank line. Line 11 is the W value from the input file. Line 12 is the depth 
level d of the shallowest goal node as found by your search algorithm (assume the root node is at 
level 0.) Line 13 is the total number of nodes N generated in your tree (including the root node.) 
Line 14 contains the solution (a sequence of actions from root node to goal node) represented by 
A’s. The A’s are separated by blank spaces. Each A is a character from the set {L, R, U, D}, 
representing the left, right, up and down movements of the blank position. Line 15 contains the f(n) 
values of the nodes along the solution path from the root node to the goal node, separated by blank 
spaces. There should be d number of A values in line 14 and d+1 number of f values in line 15.

W
n n n n 
n n n n
n n n n
n n n n
m m m m
m m m m
m m m m
m m m m
Figure 1. Input file format (11 lines.)
***************************
n n n n 
n n n n
n n n n
n n n n
m m m m
m m m m
m m m m
m m m m
W
d
N
A A A A A A A …………
f f f f f f f f ……………..
Figure 2. Output file format (15 lines.
