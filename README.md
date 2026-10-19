# quantum-circuit-simulator
A quantum circuit simulator built from scratch with NumPy, for learning the math and physics.

## Setup

```bash
uv sync                  # create .venv and install dependencies
uv run jupyter lab       # open notebooks/
uv run pytest            # check your implementations against Qiskit
```

## Roadmap

1. Single qubit: state vectors, X/Z/H gates, unitarity
2. Measurement and the Born rule
3. Bloch sphere plot
4. Multiple qubits and tensor products
5. CNOT and entanglement (Bell states)
6. Circuit data structure and diagram drawing
7. Algorithms: Deutsch–Jozsa, teleportation, Grover
8. Stretch: density matrices and noise
