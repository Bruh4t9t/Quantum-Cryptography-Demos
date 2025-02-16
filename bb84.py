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

def measure_qubits(qubits,bases):
    postionlist = []
    bitlist = []
    #measure_list = list(zip(qubits,bases))
    for i in range(len(qubits)):
        if qubits[i] == "|1>" and bases[i] == "+": postionlist.append(i);bitlist.append("1")
        elif qubits[i] == "|0>" and bases[i] == "+": postionlist.append(i);bitlist.append("0")
        elif qubits[i] == "|+>" and bases[i] == "x": postionlist.append(i);bitlist.append("0")
        elif qubits[i] == "|->" and bases[i] == "x": postionlist.append(i);bitlist.append("1")
        else: bitlist.append(str(random.randint(0,1)))
    return postionlist,bitlist



def simulate():
    lenght = 32
    Alice_bits = generate_random_bits(lenght)
    alice_base = generate_random_base(lenght)
    qubit_list = encode_qubits(Alice_bits,alice_base)
    bob_base = generate_random_base(lenght)
    measured,finalbits = measure_qubits(qubit_list,bob_base)
    print(measured)
    print(finalbits)

simulate()