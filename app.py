"""
    0   1   2
 0  |0> |1> |1>
 1
 2

1. virtual environment
2. qiskit install    
"""
 
#from multiprocessing.spawn import import_main_pat
from tkinter import Image
#from tkinter.tix import IMAGE
from PIL import Image 
import numpy as np
import pandas as pd
import streamlit as st
import math

from game import getRandom, validate


def main():
    #to give a menu
    menu= ['PLAY','INSTRUCTIONS','ABOUT']
    option=st.sidebar.selectbox("  MENU",menu) 
    

    #cases
    if option==menu[0]: # Play
        st.write("Welcome to Quantum Tic Tac Toe...Lets start playing. Before starting if you dont know What is a Q-comp..then go to [ Quantum Computer/Computing](https://en.wikipedia.org/wiki/Quantum_computing)")
        st.write("Computer --> |0>")
        st.write("User --> |1>") 
        psi= '|φ>'

        if 'board' not in st.session_state:
            st.session_state.board=np.array([[psi,psi,psi],[psi,psi,psi],[psi,psi,psi]])
            st.session_state.available_moves=[0,1,2,3,4,5,6,7,8,9]
        
        #dropdown 
        moves = st.selectbox("Make a move !", st.session_state.available_moves)

        if moves==1:
            if st.session_state.board[0,0]==psi: #for one time initialization-->1 time selection
                
                st.session_state.board[0,0]=getRandom()
                
                userFlag=validate(st.session_state.board)

                if not userFlag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list() # user won
                
                comp_square=np.random.randint(1,9)
                col = (comp_square-1)%3
                row = math.floor((comp_square-1)/3)
                compVal = getRandom()

                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col]=compVal   # if that board piece is unoccupied, to give the value in it
                
                #============== validation for the comp side ==================
                compFlag=validate(st.session_state.board)
                if not compFlag:
                    return 0

                st.write("Computers move :",comp_square)
                st.write("Comps value :",compVal)
                st.dataframe(st.session_state.board)

            else:
                st.dataframe(st.session_state.board)

        elif moves==2:
            if st.session_state.board[0,1]==psi: #for one time initialization-->1 time selection
                
                st.session_state.board[0,1]=getRandom()
                
                userFlag=validate(st.session_state.board)

                if not userFlag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list() # user won
                
                comp_square=np.random.randint(1,9)
                col = (comp_square-1)%3
                row = math.floor((comp_square-1)/3)
                compVal = getRandom()

                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col]=compVal   # if that board piece is unoccupied, to give the value in it
                
                #============== validation for the comp side ==================
                compFlag=validate(st.session_state.board)
                if not compFlag:
                    return 0

                st.write("Computers move :",comp_square)
                st.write("Comps value :",compVal)
                st.dataframe(st.session_state.board)

            else:
                st.dataframe(st.session_state.board)

        elif moves==3:
            if st.session_state.board[0,2]==psi: #for one time initialization-->1 time selection
                
                st.session_state.board[0,2]=getRandom()
                
                userFlag=validate(st.session_state.board)

                if not userFlag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list() # user won
                
                comp_square=np.random.randint(1,9)
                col = (comp_square-1)%3
                row = math.floor((comp_square-1)/3)
                compVal = getRandom()

                if st.session_state.board[row,col] == psi:
                    st.session_state.board[row,col]=compVal   # if that board piece is unoccupied, to give the value in it
                
                #============== validation for the comp side ==================
                compFlag=validate(st.session_state.board)
                if not compFlag:
                    return 0

                st.write("Computers move :",comp_square)
                st.write("Comps value :",compVal)
                st.dataframe(st.session_state.board)

            else:
                st.dataframe(st.session_state.board)
        #********************************************************
         
        if moves==4:
            if st.session_state.board[1,0]==psi: #for one time initialization-->1 time selection
                
                st.session_state.board[1,0]=getRandom()
                
                userFlag=validate(st.session_state.board)

                if not userFlag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list() # user won
                
                comp_square=np.random.randint(1,9)
                col = (comp_square-1)%3
                row = math.floor((comp_square-1)/3)
                compVal = getRandom()

                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col]=compVal   # if that board piece is unoccupied, to give the value in it
                
                #============== validation for the comp side ==================
                compFlag=validate(st.session_state.board)
                if not compFlag:
                    return 0

                st.write("Computers move :",comp_square)
                st.write("Comps value :",compVal)
                st.dataframe(st.session_state.board)

            else:
                st.dataframe(st.session_state.board)

        elif moves==5:
            if st.session_state.board[1,1]==psi: #for one time initialization-->1 time selection
                
                st.session_state.board[1,1]=getRandom()
                
                userFlag=validate(st.session_state.board)

                if not userFlag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list() # user won
                
                comp_square=np.random.randint(1,9)
                col = (comp_square-1)%3
                row = math.floor((comp_square-1)/3)
                compVal = getRandom()

                if (st.session_state.board[row,col]==psi):
                    st.session_state.board[row,col]=compVal   # if that board piece is unoccupied, to give the value in it
                
                #============== validation for the comp side ==================
                compFlag=validate(st.session_state.board)
                if not compFlag:
                    return 0

                st.write("Computers move :",comp_square)
                st.write("Comps value :",compVal)
                st.dataframe(st.session_state.board)

            else:
                st.dataframe(st.session_state.board)

        elif moves==6:
            if st.session_state.board[1,2]==psi: #for one time initialization-->1 time selection
                
                st.session_state.board[1,2]=getRandom()
                
                userFlag=validate(st.session_state.board)

                if not userFlag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list() # user won
                
                comp_square=np.random.randint(1,9)
                col = (comp_square-1)%3
                row = math.floor((comp_square-1)/3)
                compVal = getRandom()

                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col]=compVal   # if that board piece is unoccupied, to give the value in it
                
                #============== validation for the comp side ==================
                compFlag=validate(st.session_state.board)
                if not compFlag:
                    return 0

                st.write("Computers move :",comp_square)
                st.write("Comps value :",compVal)
                st.dataframe(st.session_state.board)

            else:
                st.dataframe(st.session_state.board)
        #********************************************************
         
        if moves==7:
            if st.session_state.board[0,2]==psi: #for one time initialization-->1 time selection
                
                st.session_state.board[0,2]=getRandom()
                
                userFlag=validate(st.session_state.board)

                if not userFlag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list() # user won
                
                comp_square=np.random.randint(1,9)
                col = (comp_square-1)%3
                row = math.floor((comp_square-1)/3)
                compVal = getRandom()

                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col]=compVal   # if that board piece is unoccupied, to give the value in it
                
                #============== validation for the comp side ==================
                compFlag=validate(st.session_state.board)
                if not compFlag:
                    return 0

                st.write("Computers move :",comp_square)
                st.write("Comps value :",compVal)
                st.dataframe(st.session_state.board)

            else:
                st.dataframe(st.session_state.board)

        elif moves==8:
            if st.session_state.board[2,1]==psi: #for one time initialization-->1 time selection
                
                st.session_state.board[2,1]=getRandom()
                
                userFlag=validate(st.session_state.board)

                if not userFlag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list() # user won
                
                comp_square=np.random.randint(1,9)
                col = (comp_square-1)%3
                row = math.floor((comp_square-1)/3)
                compVal = getRandom()

                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col]=compVal   # if that board piece is unoccupied, to give the value in it
                
                #============== validation for the comp side ==================
                compFlag=validate(st.session_state.board)
                if not compFlag:
                    return 0

                st.write("Computers move :",comp_square)
                st.write("Comps value :",compVal)
                st.dataframe(st.session_state.board)

            else:
                st.dataframe(st.session_state.board)

        elif moves==9:
            if st.session_state.board[2,2]==psi: #for one time initialization-->1 time selection
                
                st.session_state.board[2,2]=getRandom()
                
                userFlag=validate(st.session_state.board)

                if not userFlag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves=list() # user won
                
                comp_square=np.random.randint(1,9)
                col = (comp_square-1)%3
                row = math.floor((comp_square-1)/3)
                compVal = getRandom()

                if st.session_state.board[row,col]==psi:
                    st.session_state.board[row,col]=compVal   # if that board piece is unoccupied, to give the value in it
                
                #============== validation for the comp side ==================
                compFlag=validate(st.session_state.board)
                
                if not compFlag:
                    return 0

                st.write("Computers move :",comp_square)
                st.write("Comps value :",compVal)
                st.dataframe(st.session_state.board)

            else:
                st.dataframe(st.session_state.board)
        #********************************************************
         



    elif option==menu[1]:
        st.subheader("Instructions")
        #st.write("The Instructions are here :- ")
        psi='|φ>'
        board=np.array([[psi,psi,psi],[psi,psi,psi],[psi,psi,psi]])
        st.dataframe(board)
        
        instruction1="""
        The super position states are the above. The steps to start are as follows:- 
        
        
        1> The User gets to choose first always and between nos -> 1 to 9
        
        2> The Comp then plays its move 
            Note: Comp can change its normal game symbol from |0> --> |1>
            It can also take the user pos and its previous move pos ...If it occurs then then no move is made by comp 
        
        3> Then User again and Like that it will continue  
        
        4> If you Still dont understand how it will be you can play a demo. Refresh the page and continue with the challenge.
            
            
        ALL THE BEST !! """
        st.write(instruction1)

        #for board numbering
        b_num=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
        st.dataframe(b_num)

        instruction2="""
        The above are the positions of the board and the numberings
        
        These are the original board positions which are as follows :-
        
        1 --> [0,0]
        
        2 --> [0,1] and so on ..
        
        """
        st.write(instruction2)


    else:
        pic=Image.open("QTTlogo.jpg")
        st.image(pic,caption="GAME LOGO")
        st.subheader("A quick intro about the game")
        about="""
        Created by Dripto 
        
        Created using Python, Streamlit, Qiskit
        
        We will basically use the [Quantum Superposition](https://en.wikipedia.org/wiki/Quantum_superposition) technique here"""
        st.write(about)

    
if __name__=='__main__':
    c = main()
    if c == 0:
        st.subheader('GAME OVERRR!! Refresh the page to play again :)')
