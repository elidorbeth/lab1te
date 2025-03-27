import math
import matplotlib.pyplot as plt
import numpy as np

def count_ordered_sequences(n, base=10):
    # Кількість не спадних (через комбінації з повтореннями)
    non_decreasing = math.comb(base + n - 1, n)
    # Кількість не зростних
    non_increasing = math.comb(base + n - 1, n)
    # Послідовності з усіма однаковими елементами
    all_equal = base
    # Впорядковані
    ordered = non_decreasing + non_increasing - all_equal
    # Загальна кількість
    total = base ** n
    return ordered, total

def probability_ordered(n, base=10):
    ordered, total = count_ordered_sequences(n, base)
    return ordered / total

def plot_probabilities(max_n=15, base=10):
    ns = np.arange(1, max_n + 1)
    probs = [probability_ordered(n, base) for n in ns]

    plt.figure(figsize=(8, 6))
    plt.plot(ns, probs, marker='o')
    plt.title(f"Ймовірність впорядкованої послідовності для різних довжин (base = {base})")
    plt.xlabel("Довжина послідовності")
    plt.ylabel("Ймовірність")
    plt.grid(True)
    plt.show()

# Приклад виклику:
if __name__ == "__main__":
    plot_probabilities(15, 10)
    #hbfchebrfchberhf