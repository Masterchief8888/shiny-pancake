# The Minion Game in Python - Hacker Rank Solution
def  the minion_game(string):
    # your code goes here
    # The Minion Game in Python - Hacker Rank Solution START
    player1 = 0;  //just the initializing part
    player2 = 0;
    str_len = len(string)       //strlen- The strlen() function calculates the length of a given string.
    for i in range(str_len):    //looping in python using #range
        if s[i] in "AEIOU":
            player1 += (str_len)-i      //can be done as:   player1 = player+ (str_len)-i 
        else :
            player2 += (str_len)-i
    
    if player1 > player2:              //comparison
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart",player2)
    elif player1 == player2:
        print("tie")
    else :
        print("tie")
    # The Minion Game in Python - Hacker Rank Solution END

