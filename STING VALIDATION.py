QUESTION:-
Input Format

A single line containing a string S .

Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.











SOLUTION:--------------------



def fun1(s):
    for i in range(len(s)):
        if(s[i].isalnum()):
            return True;
            
    return False;
        
def fun2(s):
    for i in range(len(s)):
        if(s[i].isalpha()):
            return True;
            
    return False;

def fun3(s):
    for i in range(len(s)):
        if(s[i].isdigit()):
            return True;
            
    return False;

def fun4(s):
    for i in range(len(s)):
        if(s[i].islower()):
            return True;
            
    return False; 
     
def fun5(s):
    for i in range(len(s)):
        if(s[i].isupper()):
            return True;
            
    return False;
 
# String Validators in Python - HackerRank Solution END 
    
if __name__ == '__main__':
    s =input()
    
    # String Validators in Python - HackerRank Solution START
    flagalphanum = fun1(s)
    alphabetical = fun2(s)
    digits = fun3(s)
    lowercase = fun4(s)
    uppercase = fun5(s)
    print(flagalphanum)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)
