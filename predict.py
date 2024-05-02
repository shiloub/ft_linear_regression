import sys


def get_mileage() -> int:
    try:
        mileage = int(input("Mileage :"))
        assert mileage >= 0, "Mileage must be a positive value"
        return (mileage)
    except (AssertionError, ValueError) as err:
        print("Error: ", err)
        return (None)
    
def get_thetas():
    try:
        file = open("thetas.txt", "r")
        thetas = file.read()
        theta0 = float(thetas.split("|")[0])
        theta1 = float(thetas.split("|")[1])
    except:
        print("Error loading thetas.txt file")
        exit(0)
    return (theta0, theta1)

    

def main():
    theta0, theta1 = get_thetas()
    mileage = get_mileage()
    print(f"Predicted price : {int(theta0 + (theta1 * mileage))}$")
    return 0

if __name__ == "__main__":
    main()