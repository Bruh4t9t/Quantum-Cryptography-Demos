import random

def generate_random_bits(length):#Generates random bits
    random_bit = [random.randint(0,1) for i in range(length)]
    return random_bit

def generate_random_base(length):#Generates random base
    randombase = []
    for i in range(length):
        if random.randint(0,1) == 0: randombase.append("+")
        else: randombase.append("x")
    return randombase

def mappingfuntion(bitBase):
    if bitBase[0] == "+":
        if bitBase[1] == "1": return "|1>"
        else: return "|0>"
    else:
        if bitBase[1] == "1": return "|->"
        else: return "|+>"

def encode_qubits(randombit,randombase):
    tempdict = list(zip(randombase,randombit))
    qubitsList = [mappingfuntion(i) for i in tempdict]
    return list(qubitsList)

print(encode_qubits(generate_random_bits(16),generate_random_base(16)))
