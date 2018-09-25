"""

Author: Kevin Lane
Lexical Analyzer
Last Modified: 9/21/2017

This reads in a file specified by the user and lexically analyzes the file line 
by line.  It prints out the results of the analysis, with the token on the left 
and the lexeme on the right.  Each token and lexeme combination gets its own 
line.

"""

import re

def main():
    # open file
    filename = input("Please type in a filename: ")
    infile = open(filename, "r")
    
    # read file into a list of lines
    lines = infile.readlines()
    
    # establish dictionary of tokens and lexemes that do not need regex to
    # be identified
    mydict = {"main":"main", "bool":"type", "char":"type", "float":"type", 
              "int":"type", "true":"boolLiteral", "false":"boolLiteral", 
              "==":"equOp", "!=":"equOp", "<":"relOp", "<=":"relOp", 
              ">":"relOp", ">=":"relOp", "=":"assignOp", "if":"if", 
              "else":"else", "while":"while", "+":"addOp", "-":"addOp", 
              "*":"multOp", "/":"multOp", ";":";", "(":"(", ")":")", "{":
              "{", "}":"}", "[":"[", "]":"]", "return":"return", 
              "print":"print"}

    # go through each line and perform analysis
    for line in lines:
        analyze(line, mydict)
    
def splitline(line):
    """This splits each line and removes whitespace"""
    
    # split up lines into lexemes
    # split at non-word characters, at operators with multiple characters,
    # at the beginning of comments, at floats, and characters ('c')
    line = re.split("(>=|<=|==|!=|//|\d+\.\d+|\'\S\'|\W)", line)
    
    # remove whitespace from lexemes
    lexemes = [x for x in line if x != '' and x != ' ' and x != "\n"]    

    return lexemes
    

def analyze(line, mydict):
    """This analyzes each lexeme"""

    # split the line into lexemes
    lexemes = splitline(line)
    
    #establish literals and identifiers using regex
    intLiteral = re.compile('\d+')
    charLiteral = re.compile('\'\S|\s\'')
    floatLiteral = re.compile('\d+\.\d')
    identifier = re.compile('[a-zA-z]\w*')
    
    #go through each lexeme
    for index in range(len(lexemes)):
        
        #write out token first
        
        # if the current lexeme begins a comment
        if lexemes[index] == "//":
            print("comment", end = "\t")
            
            # print out whole comment
            for i in range(len(lexemes) - index):
                print(lexemes[i], end = " ")
            # disregard the rest of the line
            print()
            break
        
        #if the current lexeme is in the dictionary
        if (lexemes[index] in mydict):
            # then just print the value of the key
            print(mydict[lexemes[index]], end = "\t")
            
        # otherwise, look to see which literal the lexeme matches
        elif (floatLiteral.match(lexemes[index]) != None):
            print("floatLiteral", end = "\t")        
            
        elif (intLiteral.match(lexemes[index]) != None):
            print("intLiteral", end = "\t")
 
        elif (charLiteral.match(lexemes[index]) != None):
            print("charLiteral", end = "\t")        
        
        # check ids here because /w catches digits, so it would actually
        # recognize floatLiterals and intLiterals as ids
        elif(identifier.match(lexemes[index]) != None):
            print("id", end = "\t")
        
        # print out lexeme
        print(lexemes[index])
        
main()