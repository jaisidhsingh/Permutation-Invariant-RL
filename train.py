import torch
import numpy as np
import torch.nn as nn
import cma
import argparse
import pickle
from solutions import LinearModelSolution, PermutationInvariantSolution


parser = argparse.ArgumentParser("Training the agents on the evolutionary strategy", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

def save_solutions(folder, iteration, solver, solution_instance, solution_type):
	path = folder+"/"+f"{solution_type}{iteration}.pkl"

	with open(path, 'wb') as f:
		model = (solver, solution_instance)
		pickle.dump(model, f)

def get_fitness():
	pass

def train():
	pass