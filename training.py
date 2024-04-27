from load_csv import load
from matplotlib import pyplot as plt
import time

def predict(x, theta0, theta1):
    return theta0 + x * theta1

def main():
    cars = load("datas/data.csv")
    plt.figure(figsize=(8, 6))
    plt.scatter(x=cars["km"],
                y=cars["price"])
    theta0 = 9000
    theta1 = -0.03
    plt.plot(cars["km"], (cars["km"] * theta1) + theta0, color = "red", label="Regression lineaire")
    plt.title("Nuage de points avec courbe de régression linéaire")
    plt.xlabel("Kilométrage")
    plt.ylabel("Prix")
    plt.legend()
    plt.show()
    plt.pause(2)
    print("banana")
    plt.close()


if __name__ == "__main__":
    main()