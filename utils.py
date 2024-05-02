from matplotlib import pyplot as plt

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

def save_thetas(theta0, theta1):
    file = open("thetas.txt", "w")
    file.write(f"{theta0}|{theta1}")
    file.close()

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
