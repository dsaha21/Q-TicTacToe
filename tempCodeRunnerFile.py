import qiskit
from qiskit import QuantumCircuit,Aer

def superposition():
    ckt=QuantumCircuit(1,1)
    ckt.h(0) #HedaMart gate
    ckt.measure(0,0)
    
    sim=Aer.get_backend('aer_simulator') # A simulator
    result=sim.run(ckt).result().get_counts()
    return result

#res=superposition()
print(superposition())    