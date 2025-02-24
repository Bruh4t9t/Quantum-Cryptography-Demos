# BB84-simulation
Simulation of the BB84 Quantum Key Distribution(QKD) protocol

## What is BB84?
BB84 was the first QKD protocol and was introduced by Charles Bennett and Gilles Brassard in 1984 hence the name BB84.
It works using the following steps

1. A user (Alice in this case) will generate a random sequence of raw bits e.g.(10001011...)

2. Alice will then generate a random seqeunce of bases with the samel length as the length of the random bits sequence(e.g. +xx++xx...)

3. The user will the encode the bits using a corresponding base to produce qubits qubits e.g. 1 encode with the + basis is the |1> qubit and 1 encoded with the x basis is the |-> qubit

4. Reciever (Bob) will generate a random seqeunce of bases of the same length as the random sequence of the raw bits and then will measure the qubits(e.g. +xxx+++x...)

5. If bob uses the same base as Alice used in the corresponding qubit then he will recieve the right qubit else he will recieve a random qubit e.g. if the qubit is the |1> qubit(base used to encode was the + basis) and bob uses the x basis to measure the qubit, he will recieve a random bit either 1 or 0

6. Alice and Bob will then compare their basis and discard the bits in the positions where the basis do not match(as neither Alice nor Bob would know whether they recived the same bit due to randomisation in Step 5)
