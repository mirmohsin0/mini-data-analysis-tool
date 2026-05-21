import numpy as np


# function to load data.
def load_data():

    try:
        data = np.genfromtxt(
            "data.csv",
            delimiter=",",
            skip_header=1
        )

        return data

    except Exception as e:
        print("Error loading file:", e)
        return None


# function to show basic statistics
def show_statistics(sales):

    print("\n----- SALES STATISTICS -----")

    print(f"Total Sales: {np.sum(sales)}")

    print(f"Average Sales: {np.mean(sales):.2f}")

    print(f"Highest Sales: {np.max(sales)}")

    print(f"Lowest Sales: {np.min(sales)}")


# function to analyze sales trend
def analyze_trend(sales):

    print("\n----- SALES TREND -----")

    changes = np.diff(sales)

    for i, change in enumerate(changes):

        if change > 0:
            print(f"Day {i+1} to Day {i+2}: Increased by {change}")

        elif change < 0:
            print(f"Day {i+1} to Day {i+2}: Decreased by {abs(change)}")

        else:
            print(f"Day {i+1} to Day {i+2}: No Change")


# function to filter high sales
def filter_high_sales(days, sales):

    print("\n----- SALES GREATER THAN 500 -----")

    high_sales = sales[sales > 500]

    high_days = days[sales > 500]

    if len(high_sales) == 0:
        print("No sales above 500")

    else:
        for i in range(len(high_sales)):
            print(f"Day {int(high_days[i])}: {high_sales[i]}")


# main function
def main():

    data = load_data()

    if data is None:
        return

    # separate columns
    days = data[:, 0]
    sales = data[:, 1]

    print("Dataset Loaded Successfully!")

    print("\nSales Data:")
    print(sales)

    show_statistics(sales)

    analyze_trend(sales)

    filter_high_sales(days, sales)

    # highest sales day
    highest_day = days[np.argmax(sales)]

    print(f"\nHighest sales happened on Day {int(highest_day)}")



main()

