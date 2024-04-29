from load_csv import load
from matplotlib import pyplot as plt

def estimatePrice(milleage, theta0, theta1):
    return theta0 + (milleage * theta1)


def get_ab_math(datas) -> tuple:
    x_bar = datas["km"].mean()
    y_bar = datas["price"].mean()
    m = len(datas)
    cov_ab = sum(((datas["km"][i] - x_bar) * (datas["price"][i] - y_bar)) for i in range(m)) / m
    a = cov_ab / datas["km"].var()
    b = y_bar - (a * x_bar)
    print(f"coef directeur calcule: {a}\nordonnee a l'origine calculee: {b}")
    return(a, b)

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
        theta0_temp =  theta0 - learning_rate * (1 / m) * diff_sum1
        theta1_temp =  theta1 - learning_rate * (1 / m) * diff_sum2
        theta0 = theta0_temp
        theta1 = theta1_temp
    return (theta0, theta1)
    # return (theta0, theta1)


def main():
    cars = load("datas/data.csv")
    # cars = cars[:3]
    # print(cars)
    # a, b = gradient_descent(cars, 0, 0, 0.0001)
    a, b = get_ab_math(cars)
    plt.figure(figsize=(8, 6))
    plt.scatter(x=cars["km"],
                y=cars["price"])
    theta0 = b
    theta1 = a
    plt.plot(cars["km"], (cars["km"] * theta1) + theta0, color = "red", label="Regression lineaire calculee")
    plt.scatter(cars["km"].mean(), cars["price"].mean(), color = "red", label="G")
    plt.title("Nuage de points avec courbe de régression linéaire")
    plt.xlabel("Kilométrage")
    plt.ylabel("Prix")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()