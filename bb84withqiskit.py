import random
from qiskit import QuantumCircuit
from qiskit_aer.primitives import SamplerV2
from bb84 import BB84_simulation# Used to generate random bits and basis from the bb84 simulation in the other file
#'''
# Uncomment above line if you want to see how the key distribution works with one qubit and how superpostioning works
expected_key = int(input("Enter key length: "))
bb84 = BB84_simulation(lenght=(expected_key*2+random.randint(1,expected_key/2)))# Ensure that this is greater than 2 times the expected key e.g. if the final key should be 32 bits then put a number > 64
alice_random_bits = bb84.generate_random_bits(bb84.lenght)
alice_random_bases = bb84.generate_random_base(bb84.lenght)
bob_random_bases = bb84.generate_random_base(bb84.lenght)

simulation_circuit = QuantumCircuit(bb84.lenght, bb84.lenght)# Creates a quantum circuit with bb84.length many qubits

print("Alice bits: ",alice_random_bits)
print("Alice bases: ",alice_random_bases)

for i in range(bb84.lenght):
    if alice_random_bits[i] == 1:  simulation_circuit.x(i)# Encodes qubits look at Readme file for more
    if alice_random_bases[i] == "x":  simulation_circuit.h(i)
print("Quantum circuit before Bob has measured")
print()
print(simulation_circuit)# Shows quantum circuit before Bob has measured

for i in range(bb84.lenght):# Loop for Bob to measure qubits
    if bob_random_bases[i] == "x":  simulation_circuit.h(i)

simulation_circuit.measure_all()#Shows state of qubits
print("Quantum circuit after Bob has measured")
print()
print(simulation_circuit)

sampler = SamplerV2()# Simulator to run the quantum key exchange
job = sampler.run([simulation_circuit], shots=1)
result_ideal = job.result()
counts_ideal = result_ideal[0].data.meas.get_counts()#Retrieves measured bits
#print(counts_ideal)

print()
print("Bob bases: ",bob_random_bases)
key = list(counts_ideal.keys())[0][::-1]  # Reverses key length beacuse for some reason the simulator stores key in little-endian format
print("Bob receives: ", key)

no_match = [i for i in range(len(alice_random_bases)) if alice_random_bases[i] != bob_random_bases[i]]# Calculates postions where basis dont match
print("Bases dont match in these postions: ",no_match)

sifted_key = [key[i] for i in range(len(key)) if i not in no_match]# Sifts key to find where basis between Alice and Bob match
print("Sifted key: ","".join(sifted_key),f"({len(sifted_key)} bits)")

if len(sifted_key) < expected_key:
    print("Sorry generated key is less than expected key, please try again")
elif len(sifted_key) >= expected_key:
    sifted_key = sifted_key[:expected_key]
    print("Your final key: ","".join(sifted_key),f"({len(sifted_key)} bits)")
    
    
        
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
print("Circuit before Bob has measured the qubit")
print(circuit)

if bob_basis == 'x':    
    circuit.h(0)
circuit.measure_all()

sampler = SamplerV2()
job = sampler.run([circuit], shots=test_chance)
result = job.result()
counts = result[0].data.meas.get_counts()

print("Circuit after Bob has measured the qubit")
print(circuit)

if counts[str(bit)] == test_chance:
    print("Bob used right base and recieved the right bit")
    print("Shows that qubit was NOT in a superpostion when measured: ",counts)

else:
    print("Bob used wrong base and recieved a random bit")
    print("Shows that qubit was in a superpostion when measured: ",counts)


'''
# Add comment to above line to prevent EOF error if you have uncommented line 5