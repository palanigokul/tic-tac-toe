from copy import deepcopy
class tic():
    let=[[' ', ' ', ' '], 
         [' ', ' ', ' '], 
         [' ', ' ', ' ']]
    const=[[' ', ' ', ' '], 
         [' ', ' ', ' '], 
         [' ', ' ', ' ']]

    # ins is used display model board
    def ins(self):
        print(f"\n MODEL MAP \n")
        print(f' 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 \n\n')
        print(f'PLAYING MAP')

    # BOARD is used to show each move of player and computer
    def board(self): 
        print(f' {self.let[0][0]} | {self.let[0][1]} | {self.let[0][2]} \n---|---|---\n {self.let[1][0]} | {self.let[1][1]} | {self.let[1][2]} \n---|---|---\n {self.let[2][0]} | {self.let[2][1]} | {self.let[2][2]} \n')

    # 'win' check that if any one has win the match
    def win(self):
        # re=tuple(self.let[0]+self.let[1]+self.let[2],)
        for i in range(3):
            if self.let[i]==["X","X","X"]:
                return 1
            elif self.let[0][i]=='X' and self.let[1][i]=='X' and self.let[2][i]=='X':
                return 1
            elif self.let[0][0]=='X' and self.let[1][1]=='X' and self.let[2][2]=='X':
                return 1
            elif self.let[0][2]=='X' and self.let[1][1]=='X' and self.let[2][0]=='X':
                return 1
            elif self.let[i]==["O","O","O"]:
                return 0
            elif self.let[0][i]=='O' and self.let[1][i]=='O' and self.let[2][i]=='O':
                return 0
            elif self.let[0][0]=='O' and self.let[1][1]=='O' and self.let[2][2]=='O':
                return 0
            elif self.let[0][2]=='O' and self.let[1][1]=='O' and self.let[2][0]=='O':
                return 0 
                       
    # main function is used to call all the functions
    def main(self):
        self.playwith = input(f'Please select the mode :\n\n 1. Two Player \n\n 2. Play with Computer \n\n Enter the number to  select the mode (1 or 2) : ')
        if self.playwith == '1' :
            self.Player1=input('\nEnter First Player Name : ')
            self.Player2=input("\nEnter Second player Name : ")
            if self.Player1==self.Player2:
                print("please check the Name. both name's are same")
                self.Player2=input("Enter Second player Name : ") 
                if self.Player1==self.Player2:
                    se=input("Are you Sure (y/n):").lower()
                    if se!="y":
                        self.Player2=input("Enter Second player Name : ")
            self.ins()
            self.move()
        elif self.playwith == '2':
            self.Player1=input('Enter Player Name : ')
            self.typ=input(f'1 - EASY\n2 - MEDIUM\n3 - HARD\n\nEnter level you want to play:')
            if self.typ in ['1','2','3']:
                self.ins()
            self.comp()
        else:
            print('Please enter the valid number....')
            self.main()
  

    # MOVE is used for 2 player game to make moves
    count=0
    def move(self):
        
        self.board()
        print(self.Player1)
        self.player_1()
        if self.win()==1:
            self.board()
            print(f"{self.Player1} is win the match")
            self.resume()
        self.count += 1
        self.board() 
        if self.count == 9:
            print("Game is TIE")
            self.resume()       
        print(self.Player2)
        self.player_2()
        if self.win()==0:
            self.board()
            print(f"{self.Player2} is win the match")
            self.resume()
        self.count += 1
        self.move()


        
    
    # player_1 - it will get input form player1 and it will change the number into "X"
    def player_1(self):
        num=input('Enter the number :')
        if not num.isdigit():
            re=input('If you want to quit the game "y" else continue the game with enter: ').lower() 
            if re=="y":
                quit()
            else:
                self.player_1()

        elif int(num) in range(1,10):
            if int(num) in range(1,4) and self.let[0][int(num)-1]==' ':
                self.let[0][int(num)-1]="X"
            elif int(num) in range(4,7) and self.let[1][int(num)-4]==' ':
                self.let[1][int(num)-4]="X"
            elif int(num) in range(7,10) and self.let[2][int(num)-7]==' ':
                self.let[2][int(num)-7]="X"
            else:
                print('INVALID Number')
                self.player_1()
        
        else:
            print('INVALID Number')
            self.player_1()

    # player_2 - it will get input form player2 and it will change the number into "O"
    def player_2(self):
        num=input('Enter the number :')
        if int(num) in range(1,10):
            if int(num) in range(1,4) and self.let[0][int(num)-1]==' ':
                self.let[0][int(num)-1]="O"
            elif int(num) in range(4,7) and self.let[1][int(num)-4]==' ':
                self.let[1][int(num)-4]="O"
            elif int(num) in range(7,10) and self.let[2][int(num)-7]==' ':
                self.let[2][int(num)-7]="O"
            else:
                print('INVALID Number')
                self.player_2()
        elif num.isalpha():
            re=input('If you want to quit the game "y" else continue the game with enter: ').lower() 
            if re=="y":
                quit()
            else:
                self.player_2()
        else:
            print('INVALID Number')
            self.player_2()

    # CMMOVE is used to make first move of computer
    def cmmove(self):
        if self.let[0][0]==' ' and self.let[2][2]=='X':
            self.let[0][0]="O"
            return 1
        elif self.let[0][2]==' ' and self.let[2][0]=='X':
            self.let[0][2]="O"
            return 1
        elif self.let[2][0]==' ' and self.let[0][2]=='X':
            self.let[2][0]="O"
            return 1
        elif self.let[2][2]==' ' and self.let[0][0]=='X':
            self.let[2][2]="O"
            return 1
        else:
            if self.let[0][0]==' ' :
                self.let[0][0]="O"
                return 1
            elif self.let[0][2]==' ':
                self.let[0][2]="O"  
                return 1
            elif self.let[2][0]==' ':
                self.let[2][0]="O"
                return 1
            elif self.let[2][2]==' ':
                self.let[2][2]="O"
                return 1
            else:
                return 0




    # TRICKMOVE it is used to make second move when player didn't having any win possiblity
    def trickmove(self):
    
        if self.let[0][1]==' 'and self.let[0][2]==" " and self.let[0][0]=='O':
            self.let[0][1]="O"
            
        elif self.let[1][0]==' 'and self.let[2][0]==" " and self.let[0][0]=='O':
            self.let[1][0]="O"
        
        elif self.let[0][1]==' 'and self.let[0][0]==" " and self.let[0][2]=='O':
            self.let[0][1]="O"
        
        elif self.let[1][2]==' 'and self.let[2][2]==" " and self.let[0][2]=='O':
            self.let[1][2]="O"

        elif self.let[2][1]==' ' and self.let[2][2]==" " and self.let[2][0]=='O':
            self.let[2][1]="O"
        
        elif self.let[1][0]==' 'and self.let[0][0]==" " and self.let[2][0]=='O':
            self.let[1][0]="O"
    
        elif self.let[2][1]==' 'and self.let[2][0]==" " and self.let[2][2]=='O':
            self.let[2][1]="O"
        
        elif self.let[1][2]==' 'and self.let[0][2]==" " and self.let[2][2]=='O':
            self.let[1][2]="O" 

        elif self.let[1][1]==' 'and self.let[0][1]!=' ' and self.let[1][0]!=' ' and self.let[1][2]!=' ' and self.let[2][1]!=' ':
            self.let[1][1]='O'
        
        elif self.let[0][0]==' ':
            self.let[0][0]='O'

        elif self.let[0][1]==' ':
            self.let[0][1]='O'

        elif self.let[0][2]==' ':
            self.let[0][2]='O'

        elif self.let[1][0]==' ':
            self.let[1][0]='O'

        elif self.let[1][1]==' ':
            self.let[1][1]='O'

        elif self.let[1][2]==' ':
            self.let[1][2]='O'

        elif self.let[2][1]==' ':
            self.let[2][1]='O'

        elif self.let[2][0]==' ':
            self.let[2][0]='O'

        elif self.let[2][2]==' ':
            self.let[2][2]='O'

        else:
            print(f"No more move to win \n GAME is TIE")
            self.resume()

    # LENMOVE is used to hard level game it has trick  
    def lenmove(self):

        if self.let[0][0]=='O' and self.let[2][2]==' ' and self.let[1][0]=='X'and  self.let[0][1]=='X' and (self.let[0][2]=='O'or self.let[2][0]=='O'):
            self.let[2][2]='O'
            return 1
        elif self.let[0][0]=='O' and self.let[2][0]==' ' and self.let[0][1]=='X'  :
            self.let[2][0]='O'
            return 1
        elif self.let[0][0]=='O' and self.let[0][2]==' ' and  (self.let[1][0]=='X' or self.let[1][1]=='X' or self.let[1][2]=='X' or self.let[2][1]=='X' or self.let[2][0]=='X' or self.let[2][2]=='X' ):
            self.let[0][2]='O'
            return 1
           
        elif self.let[0][0]=='O' and self.let[0][2]=='O'and self.let[2][0]==' ' and self.let[1][1]=='X' and self.let[1][0]==' ' and self.let[0][1]==' ':
            self.let[2][0]='O'
            return 1
        elif self.let[0][0]=='O' and self.let[0][2]=='O'and self.let[2][0]==' ' and self.let[1][1]==' ' and self.let[1][0]=='X' and self.let[0][1]==' ':
            self.let[2][0]='O'
            return 1
        elif self.let[0][0]=='O' and self.let[0][2]=='O'and self.let[2][0]==' ' and self.let[1][1]==' ' and self.let[1][0]==' ' and self.let[0][1]=='X':
            self.let[2][0]='O'
            return 1
        
        elif self.let[0][0]=='O' and self.let[2][0]=='O'and self.let[2][2]==' ' and self.let[1][1]==' ' and self.let[1][0]==' ' and self.let[2][1]=='X':  
            self.let[2][2]='O'          
            return 1
        elif self.let[0][0]=='O' and self.let[2][0]=='O'and self.let[2][2]==' ' and self.let[1][1]==' ' and self.let[1][0]=='X' and self.let[2][1]==' ':  
            self.let[2][2]='O'
            return 1
        elif self.let[0][0]=='O' and self.let[2][0]=='O'and self.let[2][2]==' ' and self.let[1][1]=='X' and self.let[1][0]==' ' and self.let[2][1]==' ':  
            self.let[2][2]='O'
            return 1
        elif self.let[0][0]=='O' and self.let[2][0]=='O'and self.let[2][2]==' ' and self.let[1][1]==' ' and self.let[1][0]=='X' and self.let[2][1]=='X':  
            self.let[2][2]='O'
            return 1
        
        elif self.let[0][0]=='O' and self.let[0][2]=='O'and self.let[2][2]==' ' and self.let[1][1]=='X' and self.let[1][2]==' ' and self.let[0][1]==' ':  
            self.let[2][2]='O'
            return 1
        elif self.let[0][0]=='O' and self.let[0][2]=='O'and self.let[2][2]==' ' and self.let[1][1]==' ' and self.let[1][2]=='X' and self.let[0][1]==' ':  
            self.let[2][2]='O'
            return 1
        elif self.let[0][0]=='O' and self.let[0][2]=='O'and self.let[2][2]==' ' and self.let[1][1]==' ' and self.let[1][2]==' ' and self.let[0][1]=='X':  
            self.let[2][2]='O'
            return 1
        
        # elif self.let[0][0]=='O' and self.let[2][0]=='O'and self.let[0][2]==' ' and self.let[1][1]==' ' and self.let[1][2]==' ' and self.let[0][1]=='X':  
        #     self.let[0][2]='O'
        #     return 1
        elif self.let[0][0]=='O' and self.let[2][0]=='O'and self.let[0][2]==' ' and self.let[1][1]==' ' and self.let[1][2]=='X' and self.let[0][1]==' ':  
            self.let[0][2]='O'
            return 1
        elif self.let[0][0]=='O' and self.let[2][0]=='O'and self.let[0][2]==' ' and self.let[1][1]=='X' and self.let[1][2]==' ' and self.let[0][1]==' ':  
            self.let[0][2]='O'
            return 1
        
        else :
            return 0
        
#  MEDLEVEL is used to medium level game of computer
    def medlevel(self):
        
        if self.let[1][1]==" " and (self.let[0][0]=='X' or self.let[0][1]=='X' or self.let[0][2]=='X' or self.let[1][0]=='X' or self.let[1][2]=='X' or self.let[2][1]=='X'or self.let[2][0]=='X' or self.let[2][2]=='X'):
            self.let[1][1]='O'
            return 1
        elif self.let[0][0]==' ' and (self.let[1][1]=='X' or self.let[0][1]=='X' or self.let[0][2]=='X' or self.let[1][0]=='X' or self.let[1][2]=='X' or self.let[2][1]=='X' or self.let[2][0]=='X'or self.let[2][2]=='X'):
            self.let[0][0]='O'
            return 1
        #------------------------------------------->
        elif self.let[0][0]=="O" and self.let[1][1]==" " and self.let[2][0]=="O" and ((self.let[0][2]==" " and self.let[2][2]==" ")or(self.let[0][2]==" " and self.let[1][0]==" ")or(self.let[1][0]==" " and self.let[2][2]==" ")):
            self.let[1][1]="O"
            return 1
        elif self.let[0][0]==" " and self.let[1][1]=="O" and self.let[2][0]=="O" and ((self.let[0][2]==" " and self.let[2][2]==" ")or(self.let[0][2]==" " and self.let[1][0]==" ")or(self.let[1][0]==" " and self.let[2][2]==" ")):
            self.let[0][0]="O"
            return 1
        elif self.let[0][0]=="O" and self.let[1][1]=="O" and self.let[2][0]==" " and ((self.let[0][2]==" " and self.let[2][2]==" ")or(self.let[0][2]==" " and self.let[1][0]==" ")or(self.let[1][0]==" " and self.let[2][2]==" ")):
            self.let[2][0]="O"
            return 1
        # ----------------------------------------------<
        elif self.let[0][2]=="O" and self.let[1][1]==" " and self.let[2][2]=="O" and ((self.let[0][0]==" " and self.let[2][0]==" ")or(self.let[0][0]==" " and self.let[1][2]==" ")or(self.let[1][2]==" " and self.let[2][0]==" ")):
            self.let[1][1]="O"
            return 1
        elif self.let[0][2]==" " and self.let[1][1]=="O" and self.let[2][2]=="O" and ((self.let[0][0]==" " and self.let[2][0]==" ")or(self.let[0][0]==" " and self.let[1][2]==" ")or(self.let[1][2]==" " and self.let[2][0]==" ")):
            self.let[0][2]="O"
            return 1
        elif self.let[0][2]=="O" and self.let[1][1]=="O" and self.let[2][2]==" " and ((self.let[0][0]==" " and self.let[2][0]==" ")or(self.let[0][0]==" " and self.let[1][2]==" ")or(self.let[1][2]==" " and self.let[2][0]==" ")):
            self.let[2][2]="O"
            return 1
        # --------------------------------------------v
        elif self.let[0][0]=="O" and self.let[1][1]==" " and self.let[0][2]=="O" and ((self.let[0][2]==" " and self.let[2][2]==" ")or(self.let[0][2]==" " and self.let[0][1]==" ")or(self.let[2][2]==" " and self.let[0][1]==" ")):
            self.let[1][1]="O"
            return 1
        elif self.let[0][0]==" " and self.let[1][1]=="O" and self.let[0][2]=="O" and ((self.let[0][2]==" " and self.let[2][2]==" ")or(self.let[0][2]==" " and self.let[0][1]==" ")or(self.let[2][2]==" " and self.let[0][1]==" ")):
            self.let[0][0]="O"
            return 1
        elif self.let[0][0]=="O" and self.let[1][1]=="O" and self.let[0][2]==" " and ((self.let[0][2]==" " and self.let[2][2]==" ")or(self.let[0][2]==" " and self.let[0][1]==" ")or(self.let[2][2]==" " and self.let[0][1]==" ")):
            self.let[0][2]="O"
            return 1
        # ----------------------------------------^
        elif self.let[2][0]=="O" and self.let[1][1]==" " and self.let[2][2]=="O" and ((self.let[0][0]==" " and self.let[0][2]==" ")or(self.let[0][2]==" " and self.let[2][1]==" ")or(self.let[2][1]==" " and self.let[0][0]==" ")):
            self.let[1][1]="O"
            return 1
        elif self.let[2][0]==" " and self.let[1][1]=="O" and self.let[2][2]=="O" and ((self.let[0][0]==" " and self.let[0][2]==" ")or(self.let[0][2]==" " and self.let[2][1]==" ")or(self.let[2][1]==" " and self.let[0][0]==" ")):
            self.let[2][0]="O"
            return 1
        elif self.let[2][0]=="O" and self.let[1][1]=="O" and self.let[2][2]==" " and ((self.let[0][0]==" " and self.let[0][2]==" ")or(self.let[0][2]==" " and self.let[2][1]==" ")or(self.let[2][1]==" " and self.let[0][0]==" ")):
            self.let[2][2]="O"
            return 1
        # ----------------------_|
        elif self.let[1][0]=="O" and self.let[1][1]==" " and self.let[0][1]=="O" and self.let[2][1]==" " and self.let[1][2]==" ":
            self.let[1][1]="O"
            return 1
        elif self.let[1][0]==" " and self.let[1][1]=="O" and self.let[0][1]=="O" and self.let[2][1]==" " and self.let[1][2]==" ":
            self.let[1][0]="O"
            return 1
        elif self.let[1][0]=="O" and self.let[1][1]=="O" and self.let[0][1]==" " and self.let[2][1]==" " and self.let[1][2]==" ":
            self.let[0][1]="O"
            return 1
        # -------------------------------|_
        elif self.let[1][2]=="O" and self.let[1][1]==" " and self.let[0][1]=="O" and self.let[2][1]==" " and self.let[1][0]==" ":
            self.let[1][1]="O"
            return 1
        elif self.let[1][2]==" " and self.let[1][1]=="O" and self.let[0][1]=="O" and self.let[2][1]==" " and self.let[1][0]==" ":
            self.let[1][2]="O"
            return 1
        elif self.let[1][2]=="O" and self.let[1][1]=="O" and self.let[0][1]==" " and self.let[2][1]==" " and self.let[1][0]==" ":
            self.let[0][1]="O"
            return 1
        # ---------------------------------|``
        elif self.let[1][2]=="O" and self.let[1][1]==" " and self.let[2][1]=="O" and self.let[0][1]==" " and self.let[1][0]==" ":
            self.let[1][1]="O"
            return 1
        elif self.let[1][2]==" " and self.let[1][1]=="O" and self.let[2][1]=="O" and self.let[0][1]==" " and self.let[1][0]==" ":
            self.let[1][2]="O"
            return 1
        elif self.let[1][2]=="O" and self.let[1][1]=="O" and self.let[2][1]==" " and self.let[0][1]==" " and self.let[1][0]==" ":
            self.let[0][1]="O"
            return 1
        # ----------------------------------``|
        elif self.let[1][0]=="O" and self.let[1][1]==" " and self.let[2][1]=="O" and self.let[0][1]==" " and self.let[1][2]==" ":
            self.let[1][1]="O"
            return 1
        elif self.let[1][0]==" " and self.let[1][1]=="O" and self.let[2][1]=="O" and self.let[0][1]==" " and self.let[1][2]==" ":
            self.let[1][0]="O"
            return 1
        elif self.let[1][0]=="O" and self.let[1][1]=="O" and self.let[2][1]==" " and self.let[0][1]==" " and self.let[1][2]==" ":
            self.let[2][1]="O"
            return 1
            

        else :
            return 0

        

    # WINNINGMOVE is computer move it alaways check winning possibilities
    def winningmove(self):
        
        # ------------------1
        if self.let[0][1]=='O' and self.let[0][0]==' ' and self.let[0][2]=='O':
            self.let[0][0]='O'
            return 1
        elif self.let[1][0]=='O' and self.let[0][0]==' 'and self.let[2][0]=='O':
            self.let[0][0]='O'
            return 1
        elif self.let[1][1]=='O' and self.let[0][0]==' 'and self.let[2][2]=='O':
            self.let[0][0]='O'
            return 1
        
        # ------------------2
        elif self.let[0][1]==' ' and self.let[0][0]=='O'and self.let[0][2]=='O':
            self.let[0][1]='O'
            return 1
        elif self.let[2][1]=='O' and self.let[0][1]==' ' and self.let[1][1]=='O':
            self.let[0][1]='O'
            return 1
        
        # ------------------3
        elif self.let[0][1]=='O' and self.let[0][2]==' ' and self.let[0][0]=='O':
            self.let[0][2]='O'
            return 1
        elif self.let[1][2]=='O' and self.let[0][2]==' 'and self.let[2][2]=='O':
            self.let[0][2]='O'
            return 1
        elif self.let[1][1]=='O' and self.let[0][2]==' 'and self.let[2][0]=='O':
            self.let[0][2]='O'
            return 1
        
        # ------------------4
        elif self.let[1][0]==' ' and self.let[2][0]=='O'and self.let[0][0]=='O':
            self.let[1][0]='O'
            return 1
        elif self.let[1][2]=='O' and self.let[1][0]==' ' and self.let[1][1]=='O':
            self.let[1][0]='O'
            return 1
        
        # ------------------5
        elif self.let[0][2]=='O'and self.let[1][1]==' ' and self.let[2][0]=='O': #/
            self.let[1][1]='O'
            return 1
        elif self.let[0][1]=="O" and self.let[2][1]=="O" and self.let[1][1]==' ': #|
            self.let[1][1]="O"
            return 1
        elif self.let[1][0]=='O' and self.let[1][2]=="O" and self.let[1][1]==' ': #-
            self.let[1][1]="O"
            return 1
        elif self.let[0][0]=='O' and self.let[1][1]==' 'and self.let[2][2]=='O': #\
            self.let[1][1]='O'
            return 1
        
        # ------------------6
        elif self.let[1][2]==' ' and self.let[2][2]=='O'and self.let[0][2]=='O':
            self.let[1][2]='O'
            return 1
        elif self.let[1][0]=='O' and self.let[1][2]==' ' and self.let[1][1]=='O':
            self.let[1][2]='O'
            return 1
        
        # ------------------7
        elif self.let[1][0]=='O' and self.let[2][0]==' 'and self.let[0][0]=='O':
            self.let[2][0]='O'
            return 1
        elif self.let[1][1]=='O' and self.let[2][0]==' 'and self.let[0][2]=='O':
            self.let[2][0]='O'
            return 1
        elif self.let[2][1]=='O' and self.let[2][0]==' ' and self.let[2][2]=='O':
            self.let[2][0]='O'
            return 1
        
        # ------------------8
        elif self.let[2][0]=='O' and self.let[2][1]==' 'and self.let[2][2]=='O':
            self.let[2][1]='O'
            return 1
        elif self.let[0][1]=='O' and self.let[2][1]==' ' and self.let[1][1]=='O':
            self.let[2][1]='O'
            return 1
        
        # ------------------9
        elif self.let[1][1]=='O' and self.let[2][2]==' 'and self.let[0][0]=='O':
            self.let[2][2]='O'
            return 1
        elif self.let[1][2]=='O' and self.let[2][2]==' 'and self.let[0][2]=='O':
            self.let[2][2]='O'
            return 1
        elif self.let[2][1]=='O'and self.let[2][2]==' ' and self.let[2][0]=='O':
            self.let[2][2]='O'
            return 1
  
        else:
            return 0

    #BLOCKMOVE is computer move but it alaways check with the player move to reduce the possibility of player 
    def blockmove(self):
    
    # ----------------------1
        if self.let[2][2]=='X' and self.let[1][1]=='X' and self.let[0][0]==' ':
            self.let[0][0]='O'
            return 1
        elif self.let[2][0]=='X' and self.let[1][0]=='X' and self.let[0][0]==' ':
            self.let[0][0]='O'
            return 1
        elif self.let[0][2]=='X' and self.let[0][1]=='X' and self.let[0][0]==' ':
            self.let[0][0]='O'
            return 1
        
        # ------------------2
        elif self.let[0][0]=='X' and self.let[0][1]==' 'and self.let[0][2]=='X':
            self.let[0][1]='O'
            return 1
        elif self.let[2][1]=='X' and self.let[0][1]==' ' and self.let[1][1]=='X':
            self.let[0][1]='O' 
            return 1
        
        # ------------------3
        elif self.let[0][1]=='X' and self.let[0][2]==' ' and self.let[0][0]=='X':
            self.let[0][2]='O'
            return 1
        elif self.let[2][2]=='X' and self.let[1][2]=='X'and self.let[0][2]==' ':
            self.let[0][2]='O'
            return 1
        elif self.let[2][0]=='X' and self.let[1][1]=='X' and self.let[0][2]==' ':
            self.let[0][2]='O'
            return 1
        
        # ------------------4
        elif self.let[2][0]=="X" and self.let[1][0]==' ' and self.let[0][0]=="X":       
            self.let[1][0]='O'
            return 1
        elif self.let[1][2]=='X' and self.let[1][0]==' ' and self.let[1][1]=='X':
            self.let[1][0]='O'
            return 1
        
        # ------------------5
        elif self.let[2][2]=="X" and self.let[1][1]==' ' and self.let[0][0]=="X":  #\
            self.let[1][1]='O'
            return 1
        elif self.let[1][2]=='X' and self.let[1][0]=='X' and self.let[1][1]==' ': #-
            self.let[1][1]='O'
            return 1
        elif self.let[0][1]=='X' and self.let[2][1]=='X' and self.let[1][1]==' ': #|
            self.let[1][1]='O'
            return 1
        elif self.let[2][0]=='X' and self.let[1][1]==' 'and self.let[0][2]=='X':  #/
            self.let[1][1]='O'
            return 1
        
        # ------------------6
        elif self.let[2][2]=='X' and self.let[1][2]==' 'and self.let[0][2]=='X':
            self.let[1][2]='O'
            return 1
        elif self.let[1][0]=='X' and self.let[1][2]==' ' and self.let[1][1]=='X':
            self.let[1][2]='O'
            return 1
        
        # ------------------7
        elif self.let[1][0]=='X' and self.let[2][0]==' 'and self.let[0][0]=='X':
            self.let[2][0]='O'
            return 1    
        elif self.let[1][1]=='X' and self.let[2][0]==' 'and self.let[0][2]=='X':
            self.let[2][0]='O'
            return 1
        elif self.let[2][1]=='X' and self.let[2][0]==' ' and self.let[2][2]=='X':
            self.let[2][0]='O'
            return 1
        
        # ------------------8
        elif self.let[2][2]=='X' and self.let[2][1]==' ' and self.let[2][0]=='X':
            self.let[2][1]='O'
            return 1
        elif self.let[0][1]=='X' and self.let[2][1]==' ' and self.let[1][1]=='X':
            self.let[2][1]='O'
            return 1
        
        # ------------------9
        elif self.let[2][0]=='X' and self.let[2][1]=='X' and self.let[2][2]==' ':
            self.let[2][2]='O'
            return 1
        elif self.let[0][2]=='X' and self.let[1][2]=='X' and self.let[2][2]==' ':
            self.let[2][2]='O'
            return 1
        elif self.let[1][1]=='X' and self.let[2][2]==' 'and self.let[0][0]=='X':
            self.let[2][2]='O'
            return 1
    
        else:
            return 0

    
    def easy(self):    
        self.board()
        print(self.Player1)
        self.player_1()
        if self.win()==1:
            self.board()
            print(f"{self.Player1} is win the match")
            self.resume()
        self.count += 1
        self.board() 
        if self.count == 9:
            print("Game is TIE")
            self.resume()       
        print("computer move")
        self.makemove()
        if self.win()==0:
            self.board()
            print("computer win the match")
            self.resume()
        self.count+=1
        self.easy()


    def medium(self):
        self.board()
        print('Player1')
        self.player_1()
        self.count+=1
        if self.win()==1:
            self.board()
            print("player win the match")
            self.resume()
        self.board()
        if self.count == 9:
            print("Game is TIE")
            self.resume()
        print('Computer move')  
        if self.count==0:
            self.cmmove() 
        if self.count>=1:    
            if self.winningmove()==0:
                if self.blockmove()==0: 
                    if self.lenmove()==0:   
                        if self.medlevel()==0:
                            self.trickmove()    
        self.count += 1
        if self.win()==0:
            self.board()
            print("computer win the match")
            self.resume()
        self.medium()

        
    def hard(self):
        self.board()
        print('Computer move')  
        if self.count==0:
            self.cmmove() 
        if self.count>=1:    
            if self.winningmove()==0:
                if self.blockmove()==0:    
                    if self.lenmove()==0:
                        self.trickmove()    
        self.count += 1
        if self.win()==0:
            self.board()
            print("computer win the match")
            self.resume()
        self.board()
        if self.count == 9:
            print("Game is TIE")
            self.resume()
        print('Player1')
        self.player_1()
        self.count+=1
        if self.win()==1:
            self.board()
            print("player win the match")
            self.resume()
        self.hard()

            
    # COMP is function created to play with computer   in this it will get input from user/player that computer will make move
    def comp(self):
        if self.typ=='1':
            self.easy()
        elif self.typ=="2":
            self.medium()
        elif self.typ=="3":
            self.hard()
        else:
            # self.playwith='2'
            self.typ=input('your are enter invalid level please Re-enter the correct level to play(1,2,3) :')
            if self.typ in ('1','2','3'):
                self.ins()
            self.comp()

   
    #MAKEMOVE is used system move/computer move 
    def makemove(self):
    
        if self.count==1:
            self.cmmove()
        elif self.count>1:
            if not self.winningmove():
                if not self.blockmove():
                    self.trickmove()
            

        
        #  if game is over it will ask from user your want play again or you want quit
    def resume(self):
        self.tac=input('you want to restart the game enter(y/Y) else just enter to exit : ').upper()
        if self.tac=="Y":
            self.let =deepcopy(self.const)
            self.count = 0
            self.main()
        
        else:
            print('Thanks for playing')
            quit()


a=tic()
a.main()
