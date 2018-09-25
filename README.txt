README file for Lexical Analysis
Kevin Lane

	I wrote this program in python using a Wing IDE.  This program needs the user to specify which 
file they want to analyze.  In the case of the example that I have created, that file will be 'input.c'.

After reading in each line, this program calls an auxillary function to split the line into lexemes 
and remove the whitespace in the line.  Those lexemes are put into a list.  That list is then analyzed 
by a separate function.  There, each lexeme is compared to a dictionary of where lexemes are keys and
tokens are values.  If the lexeme is in that dictionary, then it is printed out along with its token.
Otherwise, it is compared to intLiteral, floatLiteral, charLiteral, and id by using regex's .match 
function.  Then the process repeats for the next lexeme.  If at any point the current lexeme is a "//",
indicating a comment, then the loop breaks, and the rest of the lexemes in that line are ignored.