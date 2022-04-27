import subprocess
import matplotlib.pyplot as plt
import numpy as np

def get_file(filename):
	filename = "outputs/scripts/{}".format(filename)
	generations = subprocess.getoutput("tac {} | sed '7q;d'".format(filename)).split(";")

	tranzistors = []
	losses = []
	scores = []
	generations_num = 0

	for generation in generations:
		gdata = generation.split("-")
		
		if (len(gdata) == 3):
			tranzistors.append(float(gdata[0]))
			losses.append(float(gdata[1]))
			scores.append(float(gdata[2]))
			generations_num+=1

	return [np.array(tranzistors), np.array(losses), np.array(scores), np.array(range(generations_num))]
	
gates = get_file("test_1badder.v_aig_0.5_5.0_10.0_2.0_1.0_1_500.0_0.0_none_50.0")
aig   = get_file("test_1badder.v_aig_0.25_5.0_10.0_2.0_1.0_1_500.0_0.0_none_50.0")
mig   = get_file("test_1badder.v_aig_0.75_5.0_10.0_2.0_1.0_1_500.0_0.0_none_50.0")

plt.step(gates[3], gates[2], label = "gates")
plt.plot(gates[3], mig[2], label = "mig")
plt.plot(gates[3], aig[2], label = "aig")
plt.legend()
plt.show()