import sys


def get_mileage() -> int:
    try:
        mileage = int(input("Mileage :"))
        assert mileage >= 0, "Mileage must be a positive value"
        return (mileage)
    except (AssertionError, ValueError) as err:
        print("Error: ", err)
        return (None)

def main():
    if (len(sys.argv) == 3):
        try :
            theta0 = float(sys.argv[1])
            theta1 = float(sys.argv[2])
        except ValueError:
            print("Error: arguments must be two floats: theta1 and theta2")
            return 1
    elif len(sys.argv) == 1:
        theta0 = 0
        theta1 = 0
    else:
        print("Error: Wrong number of argument:\nExpected theta0 and theta1")
        return 1
    mileage = get_mileage()
    print(f"Predicted price : {theta0 + (theta1 * mileage)}$")
    return 0

if __name__ == "__main__":
    main()