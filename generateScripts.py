##
# Script for generate all combinations of paremetrs for test
# @autor Lukas Plevac

from os import listdir
from os.path import isfile, join
import numpy as np

lbacks = np.linspace(0,20,2)
gsizes = np.linspace(3,500,3)
crosses = [1,2]
max_one_errors = np.linspace(0,2,2)
max_abs_errors = np.linspace(0,20,2)
mutations_counts = np.linspace(1,10,2)
mutations_sigmas = np.linspace(1,5,2)
selections = np.linspace(1,50,4)
power_accuracy_ratios = np.linspace(0.25,0.75,3)
representations = ["mig", "aig", "gates"]

verilogfiles = [f for f in listdir("verilogs") if isfile(join("verilogs", f))]

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
											if cross == 2:
												f = open("scripts/test_{}_{}_{}_{}_{}_{}_{}_{}_{}_{}_{}_{}".format(vfile, representation, power_accuracy_ratio, mutations_sigma, mutations_count, max_abs_error,  max_one_error, cross, gsize, lback, 2, selection), "a")
												f.write("read_verilog verilogs/{}\n".format(vfile))
												f.write("techmap\n")
												f.write("cgploss -generations=10000 -representation={} -max_abs_error={} -max_one_error={} -generation_size={} -mutations_count={} -mutations_count_sigma={} -parents={} -power_accuracy_ratio={} -cross_parts=2 -l-back={} -profile -selection_size={}".format(
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
											else:
												f = open("scripts/test_{}_{}_{}_{}_{}_{}_{}_{}_{}_{}_{}_{}".format(vfile, representation, power_accuracy_ratio, mutations_sigma, mutations_count, max_abs_error,  max_one_error, cross, gsize, lback, "none", selection), "a")
												f.write("read_verilog verilogs/{}\n".format(vfile))
												f.write("techmap\n")
												f.write("cgploss -generations=10000 -representation={} -max_abs_error={} -max_one_error={} -generation_size={} -mutations_count={} -mutations_count_sigma={} -parents={} -power_accuracy_ratio={} -l-back={} -profile -selection_size={}".format(
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