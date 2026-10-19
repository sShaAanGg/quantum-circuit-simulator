"""Single-qubit gates as 2x2 complex matrices.

Basis convention: |0> = [1, 0], |1> = [0, 1].
"""

import numpy as np

# TODO(step 1): replace each `None` with the gate's 2x2 matrix (dtype=complex).
I = np.eye(2, dtype=complex)
X = None  # bit flip:   |0> -> |1>, |1> -> |0>
Z = None  # phase flip: |0> -> |0>, |1> -> -|1>
H = None  # Hadamard:   |0> -> (|0> + |1>)/sqrt(2), |1> -> (|0> - |1>)/sqrt(2)


def is_unitary(U: np.ndarray) -> bool:
    """True if U† U = I. Every valid quantum gate must satisfy this."""
    # TODO(step 1)
    raise NotImplementedError
