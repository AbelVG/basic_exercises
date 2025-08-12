#This script should take a string of only parenthesis 
# and return True if they're balanced or false if they aren't.

parenthesisString = input("Enter a parenthesis string: ")
leftParenthesis = []
rightParenthesis = []
def parenthesisEvaluation(parenthesisString):
    for i in parenthesisString:
        if i == '(':
            leftParenthesis.append(i)
        elif i == ')':
            rightParenthesis.append(i)
    
    if len(leftParenthesis) == len(rightParenthesis):
        return True
    else:
        return False

print("Is your provided parenthesis string balanced?...: " + str(parenthesisEvaluation(parenthesisString)))