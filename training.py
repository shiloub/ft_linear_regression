from load_csv import load
from loading import ft_tqdm
from matplotlib import pyplot as plt

def get_ab_math(datas) -> tuple:
    x_bar = datas["km"].mean()
    y_bar = datas["price"].mean()
    m = len(datas)
    cov_ab = sum(((datas["km"][i] - x_bar) * (datas["price"][i] - y_bar)) for i in range(m)) / m
    a = cov_ab / datas["km"].var()
    b = y_bar - (a * x_bar)
    return(a, b)

def estimatePrice(milleage, theta0, theta1):
    return theta0 + (milleage * theta1)

def normalize(datas):
    normalized = datas.copy()
    normalized["km"] = normalized["km"].apply(lambda x: (x - normalized["km"].min()) / (normalized["km"].max() - normalized["km"].min()))
    normalized["price"] = normalized["price"].apply(lambda x: (x - normalized["price"].min()) / (normalized["price"].max() - normalized["price"].min()))
    return normalized
def get_rmse(datas, theta0, theta1):
    m = len(datas)
    km = datas["km"]
    price = datas["price"]
    rmse = sum(((estimatePrice(km[i], theta0, theta1) - price[i]) ** 2) / m for i in range(m)) ** 0.5
    return rmse

def rescale_thetas(theta0, theta1, datas):
    ymin = datas["price"].min()
    ymax = datas["price"].max()
    xmin = datas["km"].min()
    xmax = datas["km"].max()
    coef = (ymax - ymin) / (xmax - xmin)
    scaled_theta1 = theta1 * coef
    scaled_theta0 = -scaled_theta1 * datas["km"].min() + theta0 * (ymax - ymin) + ymin
    return (scaled_theta0, scaled_theta1)


def gradient_descent(datas, theta0, theta1, learning_rate) -> tuple:
    m = len(datas)
    theta0_temp = theta0
    theta1_temp = theta1
    for i in ft_tqdm(range(10000)):
        diff_sum1 = sum(estimatePrice(datas["km"][x], theta0, theta1) - datas["price"][x] for x in range(m))
        diff_sum2 = sum((estimatePrice(datas["km"][x], theta0, theta1) - datas["price"][x]) * datas["km"][x] for x in range(m))
        theta0_temp =  theta0 - learning_rate * (1 / m) * diff_sum1
        theta1_temp =  theta1 - learning_rate * (1 / m) * diff_sum2
        theta0 = theta0_temp
        theta1 = theta1_temp
    return (theta0, theta1)

def plot_datas(datas, theta0, theta1, name = "Regression lineaire"):
    """Print the data"""
    plt.figure(figsize=(8, 6))
    plt.scatter(x=datas["km"],
                y=datas["price"])
    plt.plot(datas["km"], (datas["km"] * theta1) + theta0, color = "red", label=name)
    plt.scatter(datas["km"].mean(), datas["price"].mean(), color = "red", label="G")
    plt.title("Scatter plot with linear regression curve")
    plt.xlabel("Kilométrage")
    plt.ylabel("Prix")
    plt.legend()
    plt.show()

def save_thetas(theta0, theta1):
    file = open("thetas.txt", "w")
    file.write(f"{theta0}|{theta1}")
    file.close()

def main():
    cars = load("datas/data.csv")
    normalized_cars = normalize(cars)
    # theta1, theta0 = get_ab_math(cars)
    theta0, theta1 = gradient_descent(normalized_cars, 0, 0, 0.01)
    theta0, theta1 = rescale_thetas(theta0, theta1, cars)
    rmse = get_rmse(cars, theta0, theta1)
    print(f"Mean error of our model: +/- {int(rmse) + 1}$")
    save_thetas(theta0, theta1)
    # plot_datas(normalized_cars, theta0, theta1, "Calculated linear regression")
    plot_datas(cars, theta0, theta1, "Gradient descended linear regression")


if __name__ == "__main__":
    main()