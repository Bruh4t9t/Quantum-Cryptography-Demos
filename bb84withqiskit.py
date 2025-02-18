from qiskit import QuantumCircuit
from qiskit_aer.primitives import SamplerV2
import random
from bb84 import BB84_simulation
'''
bb84 = BB84_simulation(lenght=10)
random_bits = bb84.generate_random_bits(bb84.lenght)

random_bases = bb84.generate_random_base(bb84.lenght)

simulation_circuit = QuantumCircuit(bb84.lenght, bb84.lenght)


for i in range(bb84.lenght):
    if random_bases[i] == "+":  simulation_circuit.h(i)
    else:  simulation_circuit.x(i)

simulation_circuit.measure_all()
print(simulation_circuit)
sampler = SamplerV2()


job = sampler.run([simulation_circuit], shots=1)


result_ideal = job.result()
counts_ideal = result_ideal[0].data.meas.get_counts()

print('Counts (ideal):', counts_ideal)
print(random_bits)
print(random_bases)
'''
circuit = QuantumCircuit(1, 1)

bit = random.choice([0, 1])  
basis = random.choice(['+', 'x'])  
print(bit)
print(basis)
if bit == 1:
    circuit.x(0)  
if basis == 'x':    
    circuit.h(0)

circuit.measure_all()
sampler = SamplerV2()
job = sampler.run([circuit], shots=128)

result = job.result()
counts = result[0].data.meas.get_counts()
print(counts)
print(circuit)
