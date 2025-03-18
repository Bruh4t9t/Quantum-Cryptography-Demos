import random

class BB84_simulation():
    def __init__(self,lenght=32,eavesdropper=False):
        self.lenght = lenght
        self.eavesdropper = eavesdropper
        
    def generate_random_bits(self,length):#Generates random bits
        random_bit = [random.randint(0,1) for _ in range(length)]
        return random_bit

    def generate_random_base(self,length):#Generates random base
        randombase = []
        for _ in range(length):
            if random.randint(0,1) == 0: randombase.append("+")
            else: randombase.append("x")
        return randombase

    def __mappingfuntion__(self,bitBase):#Mapping functions that takes in a tuple with the bit and the base and encoded it to produce a qubit, Should only be called inside the file
        if bitBase[0] == "+":
            if bitBase[1] == 1: return "|1>"
            else: return "|0>"
        else:
            if bitBase[1] == 1: return "|->"
            else: return "|+>"

    def encode_qubits(self,randombit,randombase):#Encodes a list of qubits
        tempdict = list(zip(randombase,randombit))
        qubitsList = [self.__mappingfuntion__(i) for i in tempdict]
        return list(qubitsList)

    def measure_qubits(self,qubits,bases,compare_base):# Measures bits based on base given 
        postionlist = []
        bitlist = []
        correct_measurmenrt = {("|1>", "+"): 1,("|0>", "+"): 0,("|+>", "x"): 0,("|->", "x"): 1}
        measure_list = list(zip(qubits,bases))
        bitlist = [correct_measurmenrt[measure_list[i]] if measure_list[i] in correct_measurmenrt else random.randint(0,1) for i in range(len(measure_list))]
        postionlist = [i for i in range(len(measure_list)) if bases[i] == compare_base[i]]
        return postionlist,bitlist

    def simulate(self):# To simulate key exchange
        Alice_bits = self.generate_random_bits(self.lenght)
        print("Alice bits: ",Alice_bits)
        alice_base = self.generate_random_base(self.lenght)
        print("Alices bases: ",alice_base)
        qubit_list = self.encode_qubits(Alice_bits,alice_base)
        print("Qubits: ",qubit_list)
        if self.eavesdropper: 
            eve_bases = self.generate_random_base(self.lenght)
            print("Eve Bases:",eve_bases)
            eve_measurements,eve_bits = self.measure_qubits(qubit_list,eve_bases,alice_base)
            print("Eve bits: ",eve_bits)
            eve_encoded_qubits = self.encode_qubits(eve_bits,eve_bases)
            print("Eve qubits: ",eve_encoded_qubits)
        bob_base = self.generate_random_base(self.lenght)
        print("Bob base: ",bob_base)
        measured,finalbits = self.measure_qubits((eve_encoded_qubits if self.eavesdropper else qubit_list),bob_base,alice_base)
        print("Bases do match in these positions: ",measured)
        print("Key: ",finalbits)
        
if __name__ == "__main__":
    bb84 = BB84_simulation(lenght=16)
    bb84.simulate()