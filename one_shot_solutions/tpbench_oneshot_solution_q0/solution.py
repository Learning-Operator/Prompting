# filename: codebase/expectation_value.py
import numpy as np
from scipy.linalg import expm

def expectation_value(A: float, E_a: float, E_b: float, t: float) -> float:
    """
    Calculate the expectation value of the energy for a three-level quantum system at time t.

    Parameters:
    A (float): Coupling constant (real).
    E_a (float): Energy level of state a.
    E_b (float): Energy level of state b.
    t (float): Time at which to calculate the expectation value.

    Returns:
    float: Expectation value of the energy at time t.
    """
    # Define the Hamiltonian matrix
    H = np.array([[E_a, 0, A],
                  [0, E_b, 0],
                  [A, 0, E_a]])
    
    # Initial state vector at t=0
    psi_0 = np.array([1/np.sqrt(2), 1/np.sqrt(2), 0])
    
    # Calculate the time evolution operator
    U = expm(-1j * H * t)
    
    # Evolve the state vector
    psi_t = U @ psi_0
    
    # Calculate the expectation value of the energy
    expectation_value_result = np.conjugate(psi_t) @ H @ psi_t
    
    return np.real(expectation_value_result)
