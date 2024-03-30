#...Tic-Tac-Toe...#
#Credits: Manogya Sharma
#Credits: Ayush Abad

from operator import truediv
import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def display_list(ltd):
    print(ltd)

def display_board():
  print("\n")
  print(board[0] , " | " , board[1] , " | " , board[2] , "      1 | 2 | 3")
  print(board[3] , " | " , board[4] , " | " , board[5] , "  =>  4 | 5 | 6")
  print(board[6] , " | " , board[7] , " | " , board[8] , "      7 | 8 | 9")
  print("\n")

def rules():
    print("This Is Tic-Tac-Toe Adv")
    print("RULES:::")
    print("a < b < c < d < e < f")
    print("A < B < C < D < E < F")
    print("a = A and so on....")
    print("Now How To Play: ")
    print("Choose A Position On The Board ")
    print("Enter Your Trick But Make Sure That You Tricke Must Be Greater Than The Present Trick On Board")
    print("For Example ")
    display_board()
    print("Let's Say At Position 1 There 'a' ")
    print("\n")
    print("a" , " | " , board[1] , " | " , board[2] , "      1 | 2 | 3")
    print(board[3] , " | " , board[4] , " | " , board[5] , "  =>  4 | 5 | 6")
    print(board[6] , " | " , board[7] , " | " , board[8] , "      7 | 8 | 9")
    print("\n")
    print("Now You Can Only Add b To f Or B To F Depend On Players Turn ")

rules()

display_board()

def boardfull(board):
    for i in range(10):
        if board[i] == "-":
            return False
    return True

p1 = input("Enter Name Of First Player: ")
p2 = input("Enter Name Of Second Player: ")

listp1 = ['a','b','c','d','e','f']
listp2 = ['A','B','C','D','E','F']

print("For " + p1 +" the options are as follows:")
display_list(listp1)

print("For "+ p2+ " the options are as follows:")
display_list(listp2)

def check(q,position):
    if board[position] == '-':
        return True
    t = ord(board[position])
    if t >= 97 and t <= 102:
        if ord(q) >= 97 and ord(q) <= 102:
            if t < ord(q):
                return True
            else:
                return False
        elif ord(q) >= 65 and ord(q) <= 70:
            if (t - 97) < ord(q) - 65:
                return True
            else:
                return False
    elif t >= 65 and t <= 70:
        if ord(q) >= 97 and ord(q) <= 102:
            if (t - 65) < (ord(q) - 97):
                return True
            else:
                return False
        elif ord(q) >= 65 and ord(q) <= 70:
            if (t) < ord(q):
                return True
            else:
                return False

c=0
# check if no of '-' less than 3

def result(player,c):
    if c<=5:
        return 0
    if player == 0:
        if checkrow(player) or checkcol(player) or checkdai(player):
            return 1
        else:
            return 0
    if player == 1:
        if checkrow(player) or checkcol(player) or checkdai(player):
            return 1
        else:
            return 0
    
def checkrow(player):
    if player == 0:
        if ord(board[0]) in range(97,103) and ord(board[1]) in range(97,103) and ord(board[2]) in range(97,103):
            return True
        elif ord(board[3]) in range(97,103) and ord(board[4]) in range(97,103) and ord(board[5]) in range(97,103):
            return True
        elif ord(board[6]) in range(97,103) and ord(board[7]) in range(97,103) and ord(board[8]) in range(97,103):
            return True
        else:
            return False

    if player == 1:
        if ord(board[0]) in range(65,71) and ord(board[1]) in range(65,71) and ord(board[2]) in range(65,71):
            return True
        elif ord(board[3]) in range(65,71) and ord(board[4]) in range(65,71) and ord(board[5]) in range(65,71):
            return True
        elif ord(board[6]) in range(65,71) and ord(board[7]) in range(65,71) and ord(board[8]) in range(65,71):
            return True
        else:
            return False

def checkcol(player):
    if player == 0:
        if ord(board[0]) in range(97,103) and ord(board[3]) in range(97,103) and ord(board[6]) in range(97,103):
            return True
        elif ord(board[1]) in range(97,103) and ord(board[4]) in range(97,103) and ord(board[7]) in range(97,103):
            return True
        elif ord(board[2]) in range(97,103) and ord(board[5]) in range(97,103) and ord(board[8]) in range(97,103):
            return True
        else:
            return False

    if player == 1:
        if ord(board[0]) in range(65,71) and ord(board[3]) in range(65,71) and ord(board[6]) in range(65,71):
            return True
        elif ord(board[1]) in range(65,71) and ord(board[4]) in range(65,71) and ord(board[7]) in range(65,71):
            return True
        elif ord(board[2]) in range(65,71) and ord(board[5]) in range(65,71) and ord(board[8]) in range(65,71):
            return True
        else:
            return False

def checkdai(player):
    if player == 0:
        if ord(board[0]) in range(97,103) and ord(board[4]) in range(97,103) and ord(board[8]) in range(97,103):
            return True
        elif ord(board[2]) in range(97,103) and ord(board[4]) in range(97,103) and ord(board[6]) in range(97,103):
            return True
        else:
            return False

    if player == 1:
        if ord(board[0]) in range(65,71) and ord(board[4]) in range(65,71) and ord(board[8]) in range(65,71):
            return True
        elif ord(board[2]) in range(65,71) and ord(board[4]) in range(65,71) and ord(board[6]) in range(65,71):
            return True
        else:
            return False

def checkiftie(player):
    if len(listp1) == 0 and len(listp2) == 0 and result(player,c) == 0:
        return True
    else:
        return False


def userinput(position):
    if board[position] == '-' and position in [0,1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return int(position)
    while position not in [0,1, 2, 3, 4, 5, 6, 7, 8, 9]:
        position = input("Choose a position from 1-9: ")
    if checklist(position, x):
        return int(position)
    else:
        position = userinput(int(input("Enter Position Again: "))-1)
        return int(position)

#97(a) - 105(i) ascii no
#65(A) - 70(F) ascii no

def checklist(position,player):
    if board[position] == '-':
        return True
    elif player == 1:
        t = ord(listp2[-1])
        u = ord(board[position])
        if u in range(97,103):
            if (t - 65) > (u - 97):
                return True
            else:
                return False
        elif u in range(65,71):
            if t > u:
                return True
            else:
                return False
    elif player == 0:
        t = ord(listp1[-1])
        u = ord(board[position])
        if u in range(97,103):
            if (t) > (u):
                return True
            else:
                return False
        elif u in range(65,71):
            if (t - 97)> (u - 65):
                return True
            else:
                return False





x = random.randrange(2)
if x==0:
    print(p1 + " gets to make his first move.")
elif x==1:
    print(p2 + " gets to make his first move.")

while True:
    if x == 0:
        print(p1 + "'s chance")
        display_board()
        p = userinput(int(input("Enter Position: "))-1)
        display_list(listp1)
        q = (input("Enter Your Trick Number: "))
        while q not in listp1 or not check(q,p):
            q = (input("Enter Your Trick Number Again: "))
        board[p] = q
        listp1.remove(q)
        display_board()
        if result(x,c):
            print(p1 + " wins. ")
            break
        if checkiftie(x):
            print("Ther Is A Tie!!")
            break
        if boardfull(board):
            for t in listp1:
                for i in range(10):
                    check(t,i)
            print("Ther Is A Tie!!")
        x = 1
        c = c + 1
    elif x == 1:
        print(p2 + "'s chance")
        display_board()
        p = userinput(int(input("Enter Position: "))-1)
        display_list(listp2)
        q = input("Enter Your Trick Number: ")
        while q not in listp2 or not check(q,p):
            q = input("Enter Your Trick Number Again: ")
        board[p] = q
        listp2.remove(q)
        display_board()
        if result(x,c):
            print(p2 + " wins. ")
            break
        if checkiftie(x):
            print("There Is A Tie!!")
            break
        x = 0
        c = c + 1