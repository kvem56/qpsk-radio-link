import numpy as np

def random_bits(n, seed=None):
    return np.random.default_rng(seed).integers(0, 2, n)

if __name__ == "__main__":
    print(random_bits(20, seed=1))
    print(random_bits(20, seed=1))