import os
import sys
import string
import shutil
import pickle
import logging
from opal.Solvers.nomad import NOMADBlackbox
from opal.core.modelevaluator import ModelEvaluator
worker = ModelEvaluator(name="model evaluator", modelFile="surrogate.dat")
# Create model evaluation environment
env = NOMADBlackbox(name="surrogate", worker=worker, input=sys.argv[1], output=sys.stdout)
# Activate the environment
env.start()# Wait for environement finish his life time
env.join()