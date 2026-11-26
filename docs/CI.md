# Continuous Integration

The repository CI workflow runs on pushes to main and pull requests targeting main.

Checks:
1. Compile all modules in locality_kernel.
2. Run the standard-library unittest suite.

A green CI run validates only the checked-in code under the tested Python version. It does not validate Host integration, Agent runtime, permission enforcement, SEED regeneration, or the full One-Person Company product.
