"""Step 1 checks. Run with: uv run pytest

Qiskit is the reference: if your answer disagrees with it, dig in.
"""

import numpy as np
import pytest
from qiskit.circuit.library import HGate, XGate, ZGate
from qiskit.quantum_info import Operator

from qsim import gates
from qsim.state import apply, ket0, ket1


@pytest.mark.parametrize(
    ("name", "reference"),
    [("X", XGate()), ("Z", ZGate()), ("H", HGate())],
)
def test_gate_matches_qiskit(name, reference):
    ours = getattr(gates, name)
    assert ours is not None, f"gates.{name} is still a TODO"
    np.testing.assert_allclose(ours, Operator(reference).data, atol=1e-12)


@pytest.mark.parametrize("name", ["I", "X", "Z", "H"])
def test_gates_are_unitary(name):
    assert gates.is_unitary(getattr(gates, name))


def test_is_unitary_rejects_non_unitary():
    assert not gates.is_unitary(np.array([[1, 1], [0, 1]], dtype=complex))


def test_x_flips_bits():
    np.testing.assert_allclose(apply(gates.X, ket0()), ket1())
    np.testing.assert_allclose(apply(gates.X, ket1()), ket0())


def test_hadamard_twice_is_identity():
    np.testing.assert_allclose(apply(gates.H, apply(gates.H, ket0())), ket0(), atol=1e-12)
