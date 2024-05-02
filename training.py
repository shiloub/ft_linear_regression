from load_csv import load
from loading import ft_tqdm
from utils import normalize, rescale_thetas, get_rmse, save_thetas, plot_datas

def estimatePrice(milleage, theta0, theta1):
    return theta0 + (milleage * theta1)


def get_ab_math(datas) -> tuple:
    x_bar = datas["km"].mean()
    y_bar = datas["price"].mean()
    m = len(datas)
    cov_ab = sum(((datas["km"][i] - x_bar) * (datas["price"][i] - y_bar)) for i in range(m)) / m
    a = cov_ab / datas["km"].var()
    b = y_bar - (a * x_bar)
    return(a, b)


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


def main():
    cars = load("datas/data.csv")
    if cars is None:
        exit(1)
    normalized_cars = normalize(cars)
    # theta1, theta0 = get_ab_math(cars)
    theta0, theta1 = gradient_descent(normalized_cars, 0, 0, 0.01)
    theta0, theta1 = rescale_thetas(theta0, theta1, cars)
    rmse = get_rmse(cars, theta0, theta1)
    print(f"Mean error of our model: +/- {int(rmse) + 1}$")
    save_thetas(theta0, theta1)
    # plot_datas(cars, theta0, theta1, "Calculated linear regression")
    plot_datas(cars, theta0, theta1, "Gradient descended linear regression")


if __name__ == "__main__":
    main()