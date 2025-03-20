from qiskit import QuantumCircuit
from qiskit_aer.primitives import SamplerV2
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'BB84')))
from bb84 import BB84_simulation

length = int(input("Length: "))
E91_simulation = BB84_simulation(lenght=length)
qc  = QuantumCircuit(length,length)

for i in range(0, length, 2):
    qc.h(i)          
    qc.cx(i, i + 1)

Alice_base = E91_simulation.generate_random_base(int(length/2))
bob_base = E91_simulation.generate_random_base(int(length/2))
print(Alice_base) 
print(bob_base)
for i in range(length):
    if i % 2 == 0:
        if Alice_base[int(i//2)] == "x": qc.h(i)
    else:
        if bob_base[int(i//2)] == "x": qc.h(i)

print(qc)
qc.measure_all()
print(qc)

sampler = SamplerV2()
job = sampler.run([qc], shots=1)
result_ideal = job.result()
counts_ideal = result_ideal[0].data.meas.get_counts()

print(counts_ideal)