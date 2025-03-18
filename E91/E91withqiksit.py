from qiskit import QuantumCircuit
from qiskit_aer.primitives import SamplerV2

length = int(input("Length: "))
qc  = QuantumCircuit(length,length)
qc.h(0)

for i in range(1,length):
    qc.cx(0,i)
print(qc)
qc.measure_all()

print(qc)

sampler = SamplerV2()
job = sampler.run([qc], shots=128)
result_ideal = job.result()
counts_ideal = result_ideal[0].data.meas.get_counts()

print(counts_ideal)