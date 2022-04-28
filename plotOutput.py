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

	return {
		"tranzistors": tranzistors, 
		"losses":      losses, 
		"scores":      scores,
		"generations": range(generations_num)
	}

def get_plot(plt, filename, times, label):
	tranzistors = []
	losses = []
	scores = []
	generations = []	
	for time in range(times):
		tmp = get_file(filename + "_" + str(time))
		tranzistors.append(tmp["tranzistors"])
		losses.append(tmp["losses"])
		scores.append(tmp["scores"])

	l_min = min([len(i) for i in tranzistors])
	
	generations = np.array(range(l_min))

	for time in range(times):
		tranzistors[time] = tranzistors[time][:l_min]
		losses[time]      = losses[time][:l_min]
		scores[time]      = scores[time][:l_min]

	tranzistors = np.array(tranzistors, dtype=float)
	losses      = np.array(losses,      dtype=float)
	scores      = np.array(scores,      dtype=float)

	#plt.fill_between(generations, np.amin(tranzistors, axis=0), np.amax(tranzistors, axis=0), alpha=.5, linewidth=0)
	#plt.fill_between(generations, np.amin(losses, axis=0), np.amax(losses, axis=0), alpha=.5, linewidth=0)
	#plt.fill_between(generations, np.amin(scores, axis=0), np.amax(scores, axis=0), alpha=.5, linewidth=0)
	plt.plot(generations, np.mean(losses, axis=0), label=label)
	


get_plot(plt, "test_4badder.v_aig_0.25_9_10_10_5_1_300_10_1_1", 5, "aig")
get_plot(plt, "test_4badder.v_aig_0.25_9_10_10_5_1_300_0_1_1", 5, "mig")
get_plot(plt, "test_4badder.v_gates_0.25_9_10_10_5_1_300_10_1_1", 5, "gates")
plt.legend()
#plt.show()
plt.savefig("test.pdf", format="pdf")