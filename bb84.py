import random
class BB84_simulation():
    def __init__(self,lenght=32):
        self.lenght = lenght
        
    def generate_random_bits(self,length):#Generates random bits
        random_bit = [random.randint(0,1) for _ in range(length)]
        return random_bit

    def generate_random_base(self,length):#Generates random base
        randombase = []
        for _ in range(length):
            if random.randint(0,1) == 0: randombase.append("+")
            else: randombase.append("x")
        return randombase

    def mappingfuntion(self,bitBase): #Mapping functions that takes in a tuple with the bit and the base and encoded it to produce a qubit
        if bitBase[0] == "+":
            if bitBase[1] == "1": return "|1>"
            else: return "|0>"
        else:
            if bitBase[1] == "1": return "|->"
            else: return "|+>"

    def encode_qubits(self,randombit,randombase):#Encodes a list of qubits
        tempdict = list(zip(randombase,randombit))
        qubitsList = [self.mappingfuntion(i) for i in tempdict]
        return list(qubitsList)

    def measure_qubits(self,qubits,bases):# Measures bits based on base given 
        postionlist = []
        bitlist = []
        correct_measurmenrt = {("|1>", "+"): 1,("|0>", "+"): 0,("|+>", "x"): 0,("|->", "x"): 1}
        measure_list = list(zip(qubits,bases))
        bitlist = [correct_measurmenrt[measure_list[i]] if measure_list[i] in correct_measurmenrt else random.randint(0,1) for i in range(len(measure_list))]
        postionlist = [i+1 for i in range(len(measure_list)) if measure_list[i] in correct_measurmenrt]
        return postionlist,bitlist

    def simulate(self):# To simulate key exchange
        Alice_bits = self.generate_random_bits(self.lenght)
        alice_base = self.generate_random_base(self.lenght)
        qubit_list = self.encode_qubits(Alice_bits,alice_base)
        bob_base = self.generate_random_base(self.lenght)
        measured,finalbits = self.measure_qubits(qubit_list,bob_base)
        print(measured)
        print(finalbits)
        
if __name__ == "__main__":
    bb84 = BB84_simulation(lenght=16)
    bb84.simulate()