import numpy as np

def random_bits(n, seed=None):
    return np.random.default_rng(seed).integers(0, 2, n)

def map_bits(bits):
    a = bits[0::2]
    b = bits[1::2]
    print("a:", a)
    print("b:", b)

    c = a * -2 + 1
    d = b * -2 + 1
    print("c:", c)
    print("d:", d)

    e = c / np.sqrt(2)
    f = d / np.sqrt(2)
    print("e:", e)
    print("f:", f)

    return e + 1j*f

if __name__ == "__main__":
    print(random_bits(20, seed=1))
    print(random_bits(20, seed=1))
    s = map_bits(np.array([0, 0, 1, 0, 1, 1, 0, 1]))
    print(s)
    print(np.mean(np.abs(s)**2))