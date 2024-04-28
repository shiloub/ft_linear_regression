from load_csv import load
from matplotlib import pyplot as plt
import time

def estimatePrice(milleage, theta0, theta1):
    return theta0 + (milleage * theta1)

def gradient_descent(datas, theta0, theta1, learning_rate) -> tuple:
    m = len(datas)
    print(m)
    theta0_temp = theta0
    theta1_temp = theta1
    for i in range(1000):
        print(f"theta0 = {theta0}, theta1 = {theta1}")
        diff_sum1 = sum(estimatePrice(datas["km"][x], theta0, theta1) - datas["price"][x] for x in range(m))
        diff_sum2 = sum((estimatePrice(datas["km"][x], theta0, theta1) - datas["price"][x]) * datas["km"][x] for x in range(m))
        print(f"diff_sum = {diff_sum2}")
        test = 0
        # for x in range(m):
        #     # print(f"x = {x}")
        #     temp = test + estimatePrice(datas["km"][x], theta0, theta1) - datas["price"][x]
        #     # print(f"{test} + {estimatePrice(datas['km'][x], theta0, theta1)} - {datas['price'][x]} = {temp}")
        #     test = temp
        theta0_temp =  theta0 - learning_rate * (1 / m) * diff_sum1
        theta1_temp =  theta1 - learning_rate * (1 / m) * diff_sum2
        theta0 = theta0_temp
        theta1 = theta1_temp
    return (theta0, theta1)
    # return (theta0, theta1)


def main():
    cars = load("datas/data.csv")
    # cars = cars[:3]
    print(cars)
    a, b = gradient_descent(cars, 0, 0, 0.0001)
    plt.figure(figsize=(8, 6))
    plt.scatter(x=cars["km"],
                y=cars["price"])
    theta0 = a
    theta1 = b
    plt.plot(cars["km"], (cars["km"] * theta1) + theta0, color = "red", label="Regression lineaire")
    plt.title("Nuage de points avec courbe de régression linéaire")
    plt.xlabel("Kilométrage")
    plt.ylabel("Prix")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()