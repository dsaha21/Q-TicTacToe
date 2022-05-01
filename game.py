import qiskit
import numpy as np
from qiskit import QuantumCircuit,Aer
import streamlit as st

def superposition():
    ckt=QuantumCircuit(1,1)
    ckt.h(0) #HedaMart gate
    ckt.measure(0,0)
    
    sim=Aer.get_backend('aer_simulator') # A simulator
    result=sim.run(ckt).result().get_counts()
    return result

def getRandom():
    res=superposition()
    #print(res)  

    values=list(res.values())
    keys= list(res.keys())
    #print(values,keys,sep='\n')

    #replace by random vars
    randomVal= '|' + str(keys[np.argmax(values)]) + '>'
    return randomVal

#Tic Tac Toe Logic
def validate(arr):
    """
    To check whether the game is finished or not 
    Winning condition --> 0 
    else return 1  
    """
    flag=True
    zero_ket='|0>'
    one_ket='|1>'

    #diagonals
    if arr[0,0]==one_ket and arr[1,1]==one_ket and arr[2,2]==one_ket:
        st.success('User has won !!')
        flag=False

    elif arr[0,0]==zero_ket and arr[1,1]==zero_ket and arr[2,2]==zero_ket:
        st.success('Computer has won !!')
        flag=False

    #2nd digonals
    if arr[0,2]==one_ket and arr[1,1]==one_ket and arr[2,0]==one_ket:
        st.success('User has won !!')
        flag=False

    elif arr[0,2]==zero_ket and arr[1,1]==zero_ket and arr[2,0]==zero_ket:
        st.success('Computer has won !!')
        flag=False

    if not flag:
        return 0

    if flag:
        #more 5 conditions 
        for index in [0,1,2]:
            if(list(arr[index])==[one_ket,one_ket,one_ket]):
                st.success("User has won !")
                return 0    

        for index in [0,1,2]:
            if(list(arr[index])==[zero_ket,zero_ket,zero_ket]):
                st.success("Computer winss !")
                return 0 

        for index in [0,1,2]:
            if(list(arr[:,index])==[one_ket,one_ket,one_ket]):
                st.success("User has won !")
                return 0   

        for index in [0,1,2]:
            if(list(arr[:,index])==[zero_ket,zero_ket,zero_ket]):
                st.success("Computer winss !")
                return 0 

        #for draw
        if '|φ>' not in arr:
            st.write("Its a DRAW...")
            return 0
    return 1
