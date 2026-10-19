"""Single-qubit state vectors."""

import numpy as np


def ket0() -> np.ndarray:
    """The |0> state."""
    return np.array([1, 0], dtype=complex)


def ket1() -> np.ndarray:
    """The |1> state."""
    # TODO(step 1)
    raise NotImplementedError


def apply(gate: np.ndarray, state: np.ndarray) -> np.ndarray:
    """Apply a gate to a state and return the new state."""
    # TODO(step 1)
    raise NotImplementedError


def probabilities(state: np.ndarray) -> np.ndarray:
    """Probability of measuring each basis state (the Born rule)."""
    # TODO(step 2)
    raise NotImplementedError
