# Data Assimilation

Data assimilation is a mathematical discipline that seeks to optimally combine theory (usually in the form of a numerical model) with observations. There may be a number of different goals sought, for example—to determine the optimal state estimate of a system, to determine initial conditions for a numerical forecast model, to interpolate sparse observation data using (e.g. physical) knowledge of the system being observed, to train numerical model parameters based on observed data. Depending on the goal, different solution methods may be used. **Data assimilation is distinguished from other forms of machine learning, image analysis, and statistical methods** in that it utilizes a **dynamical model** of the system being analyzed.

# Data Assimilation methods
## **Variational** methods
- **3D-VAR**: best state estimator at a given time 
- **4D-VAR**: best state estimation all over the assimilation period(optimal control theory- minimization of a cost function)

## **Sequential** methods
- **Optimal interpolation**: very easy implementation but physically incoherent 
- **Nudging**: suboptimal Kalman filter, feedback to the observations 
- **Kalman filter**: theory of optimal statistical estimation 
- **SEEK filter**: Singular Evolutive Extended Kalman filter(reduced-order scheme for nonlinear models)

# Source
Data assimilation, Didier AUROUX, Jacques BLUM, Universit ́e de Nice Sophia Antipolis \
Wikipedia Data Assimilation: https://en.wikipedia.org/wiki/Data_assimilation \
A Novel Neural Network Training Framework with Data Assimilation: https://arxiv.org/abs/2010.02626 \
JulianMack's amazing github: https://github.com/julianmack/Data_Assimilation \
Attention-based Convolutional Autoencoders for 3D-Variational Data Assimilation, Julian Mack, Rossella Arcucci, Miguel Molina-Solana, Yi-Ke Guo https://arxiv.org/abs/2101.02121
