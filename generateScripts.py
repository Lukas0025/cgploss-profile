##
# Script for generate all combinations of paremetrs for test
# @autor Lukas Plevac

from os import listdir
from os.path import isfile, join
import numpy as np

lbacks = [0,10]
gsizes = [3,300]
crosses = [1,2]
max_one_errors = [0,10,100]
max_abs_errors = [0,10,100,1000]
mutations_counts = [10,50]
mutations_sigmas = [5,25]
selections = [1,10]
power_accuracy_ratios = np.linspace(0.25,0.75,2)
representations = ["mig", "aig", "gates"]
times = 3

verilogfiles = [f for f in listdir("verilogs") if isfile(join("verilogs", f))]

for time in range(times):
	for vfile in verilogfiles:
		for representation in representations:
			for power_accuracy_ratio in power_accuracy_ratios:
				for mutations_sigma in mutations_sigmas:
					for mutations_count in mutations_counts:
						for max_abs_error in max_abs_errors:
							for max_one_error in max_one_errors:
								for cross in crosses:
									for gsize in gsizes:
										for lback in lbacks:
											for selection in selections:
												if (gsize > selection) and (gsize > mutations_count + mutations_sigma) and (max_one_error < max_abs_error):
													f = open("scripts/test_{}_{}_{}_{}_{}_{}_{}_{}_{}_{}_{}_{}_{}".format(vfile, representation, power_accuracy_ratio, mutations_sigma, mutations_count, max_abs_error,  max_one_error, cross, gsize, lback, cross, selection, time), "a")
													f.write("read_verilog verilogs/{}\n".format(vfile))
													f.write("techmap\n")
													f.write("cgploss -generations=10000 -max_duration=60 -representation={} -max_abs_error={} -max_one_error={} -generation_size={} -mutations_count={} -mutations_count_sigma={} -parents={} -power_accuracy_ratio={} -cross_parts=2 -l-back={} -profile -selection_size={}".format(
														representation,
														int(max_abs_error),
														int(max_one_error),
														int(gsize),
														int(mutations_count),
														int(mutations_sigma),
														cross,
														power_accuracy_ratio,
														int(lback),
														int(selection)
													))
													f.close()