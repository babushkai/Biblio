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

# 1. Get samples 
A = tfd.Poisson(2) # lambda = 2
sampleA =  A.sample(1000)
B = tfd.Poisson(5) # lambda = 5
sampleB = B.sample(1000)
C = tfd.Poisson(10)# lambda = 10
sampleC = C.sample(1000)

# 2. Find lambda: Maximum Likelihood Estimation
lambdaA = sampleA.numpy().sum()/len(sampleA)
lambdaB = sampleB.numpy().sum()/len(sampleB)
lambdaC = sampleC.numpy().sum()/len(sampleC)

# 3. Assume the original distribution and get probabilities for same length
pdfA = []
for k in range(30):
    probability = lambdaA**k*np.e**(-lambdaA)/np.math.factorial(k)
    pdfA.append(probability)
    
pdfB = []
for k in range(30):
    probability = lambdaB**k*np.e**(-lambdaB)/np.math.factorial(k)
    pdfB.append(probability)

pdfC = []
for k in range(30):
    probability = lambdaC**k*np.e**(-lambdaC)/np.math.factorial(k)
    pdfC.append(probability)

# 4. Measure KL Divergence
divergence_AA = kl_divergence(shannon_entropy(pdfA), cross_entropy(pdfA, pdfA))
divergence_AB = kl_divergence(shannon_entropy(pdfA), cross_entropy(pdfA, pdfB))
divergence_BA = kl_divergence(shannon_entropy(pdfB), cross_entropy(pdfB, pdfA))
divergence_AC = kl_divergence(shannon_entropy(pdfA), cross_entropy(pdfA, pdfC))

# Verify the behavior
assert divergence_AA == 0; print("Identical distributions")
assert divergence_AB != divergence_BA; print("KL Divergencve is assymetric")
assert divergence_AB < divergence_AC; print("D_KL(Pois(2) || Pois(5)) < D_KL(Pois(2) || Pois(10)) ")