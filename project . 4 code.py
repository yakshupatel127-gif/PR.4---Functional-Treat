data = []
summary = {}

def input_data():
    """Takes 1D or 2D data from user"""
    global data
    choice = int(input("Enter 1 for 1D list or 2 for 2D list: "))
    if choice == 1:
        data = list(map(int, input("Enter numbers separated by space: ").split()))
    elif  choice == 2:
        rows = int(input("Enter number of rows: "))
        data = []
        for i in range(rows):
            row = list(map(int, input(f"Enter row {i+1}: ").split()))
            data.append(row)
        print("Data stored successfully!")
    else:
        print("invaild choice")


def show_summary():
    """Displays built-in function results"""
    global summary
    if type(data[0]) == list:
        flat = [item for sub in data for item in sub]
    else:
        flat = data

    summary = {
        "Total Elements": len(flat),
        "Minimum": min(flat),
        "Maximum": max(flat),
        "Sum": sum(flat),
        "Average": sum(flat) / len(flat)
    }

    for k, v in summary.items():
        print(k, ":", v)


def factorial(n):
    """Recursive factorial function"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def filter_data():
    """Filter data using lambda"""
    t = int(input("Enter threshold: "))
    if type(data[0]) == list:
        flat = [item for sub in data for item in sub]
    else:
        flat = data
    result = list(filter(lambda x: x >= t, flat))
    print("Filtered Data:", result)


def sort_data():
    """Sort data using sort and sorted"""
    if type(data[0]) == list:
        sorted_data = sorted(data)
        print("Sorted 2D Data:")
        for s in sorted_data:
            print(s)
    else:
        data.sort()
        print("Sorted 1D Data:", data)


def multiple_return():
    """Returns min, max and avg"""
    if type(data[0]) == list:
        flat = [item for sub in data for item in sub]
    else:
        flat = data
    return min(flat), max(flat), sum(flat) / len(flat)


def args_func(*args):
    """Displays values using *args"""
    print("Values:", args)


def kwargs_func(**kwargs):
    """Displays dataset info using **kwargs"""
    for k, v in kwargs.items():
        print(k, ":", v)
 
while True:
    print("\n----- Data Analyzer Menu -----")
    print("1. Input Data")
    print("2. Display Summary")
    print("3. Factorial")
    print("4. Filter Data")
    print("5. Sort Data")
    print("6. Return Multiple Values")
    print("7. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        input_data()
    elif ch == 2:
        show_summary()
        kwargs_func(**summary)
    elif ch == 3:
        n = int(input("Enter number: "))
        print("Factorial:", factorial(n))
    elif ch == 4:
        filter_data()
    elif ch == 5:
        sort_data()
    elif ch == 6:
        a, b, c = multiple_return()
        print("Min:", a)
        print("Max:", b)
        print("Average:", c)
    elif ch == 7:
        print("Thank you! Program ended. have a good day.")
        break
    else:
        print("Invalid choice,plzz try one more time.")