import random
from qiskit import QuantumCircuit
from qiskit_aer.primitives import SamplerV2
from bb84 import BB84_simulation

bb84 = BB84_simulation(lenght=10)
alice_random_bits = bb84.generate_random_bits(bb84.lenght)
alice_random_bases = bb84.generate_random_base(bb84.lenght)
bob_random_bases = bb84.generate_random_base(bb84.lenght)

simulation_circuit = QuantumCircuit(bb84.lenght, bb84.lenght)


for i in range(bb84.lenght):
    if alice_random_bits[i] == 1:  simulation_circuit.x(i)
    if alice_random_bases[i] == "x":  simulation_circuit.h(i)
for i in range(bb84.lenght):
    if bob_random_bases[i] == "x":  simulation_circuit.h(i)

simulation_circuit.measure_all()
print(simulation_circuit)

sampler = SamplerV2()
job = sampler.run([simulation_circuit], shots=1)
result_ideal = job.result()
counts_ideal = result_ideal[0].data.meas.get_counts()
print(counts_ideal)
key = list(counts_ideal.keys())[0][::-1]  

print("Bob receives: ", key)
print(str(alice_random_bits))
print(alice_random_bases)
no_match = [i for i in range(len(alice_random_bases)) if alice_random_bases[i] != bob_random_bases[i]]
print(no_match)
sifted_key = [key[i] for i in range(len(key)) if i not in no_match]
print(sifted_key)
        
'''
circuit = QuantumCircuit(1, 1)

bit = random.choice([0, 1])  
alice_basis = random.choice(['+', 'x'])  
test_chance = 128
print("Alice generates: ",bit)
print("Alice generates base: ",alice_basis)
if bit == 1:
    circuit.x(0)  
if alice_basis == 'x':    
    circuit.h(0)
bob_basis = random.choice(['+', 'x']) 
print("Bob generates base: ",bob_basis)

print(circuit)
if bob_basis == 'x':    
    circuit.h(0)
circuit.measure_all()
sampler = SamplerV2()
job = sampler.run([circuit], shots=test_chance)
result = job.result()
counts = result[0].data.meas.get_counts()
if counts[str(bit)] == test_chance:
    print("Bob used right base and recieved the right bit")
else:
    print("Bob used wrong base and recieved a random bit")
print(circuit)
'''