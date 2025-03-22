from qiskit import QuantumCircuit
from qiskit_aer.primitives import SamplerV2
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'BB84')))
from bb84 import BB84_simulation

length = int(input("Length: "))
length = length * 2
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



key = list(counts_ideal.keys())[0][::-1]

Alice_key = [key[i] for i in range(len(key)) if i % 2 == 0]
Bob_key = [key[i] for i in range(len(key)) if i % 2 != 0]

Alice_sifted_key = [Alice_key[i] for i in range(len(Alice_key)) if Alice_base[i] == bob_base[i]]
Bob_sifted_key = [Bob_key[i] for i in range(len(Bob_key)) if Alice_base[i] == bob_base[i]]

print(Alice_sifted_key)
print(Bob_sifted_key)

sifted_key = "".join(Bob_sifted_key)
print(sifted_key)

