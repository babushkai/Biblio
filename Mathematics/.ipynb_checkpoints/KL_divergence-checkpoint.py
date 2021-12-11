from typing import List, NamedTuple, Dict, Callable
from pprint import pprint

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style("whitegrid")

import tensorflow_probability as tfp
tfd = tfp.distributions

def shannon_entropy(variable1: List) -> float:
    return np.nansum(variable1 * -np.log(variable1))

def cross_entropy(variable1: np.array, variable2: np.array) -> float:
    return - np.nansum(variable1 * np.log(variable2))

def kl_divergence(shannon_entropy: Callable, cross_entropy: Callable) -> float:
    return -shannon_entropy + cross_entropy

A = tfd.Poisson(2) # lambda = 2
sampleA =  A.sample(1000)
B = tfd.Poisson(5) # lambda = 5
sampleB = B.sample(1000)

pdfA = np.unique(A.prob(sampleA))
pdfB = np.unique(B.prob(sampleB))

# Note: This returns error as pdfA and pdfB has different length 
kl_divergence(shannon_entropy(pdfA), cross_entropy(pdfA, pdfB))


