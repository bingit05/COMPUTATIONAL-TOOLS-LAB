import numpy as np
import math


marks = [78, 85, 92, 67, 88, 73, 95, 81, 76, 89]

temperatures = [28.5, 30.2, 29.8, 31.4, 27.9, 32.1, 30.5]

sales = [12500, 13800, 14200, 11900, 15100, 14750, 16000]




def calculate_without_numpy(data):
    n = len(data)

    
    mean = sum(data) / n

   
    sorted_data = sorted(data)

    if n % 2 == 0:
        median = (
            sorted_data[n // 2 - 1] +
            sorted_data[n // 2]
        ) / 2
    else:
        median = sorted_data[n // 2]

   
    variance = sum((x - mean) ** 2 for x in data) / n
    standard_deviation = math.sqrt(variance)

    
    minimum = min(data)
    maximum = max(data)

    return mean, median, standard_deviation, minimum, maximum




def calculate_with_numpy(data):
    mean = np.mean(data)
    median = np.median(data)
    standard_deviation = np.std(data)
    minimum = np.min(data)
    maximum = np.max(data)

    return mean, median, standard_deviation, minimum, maximum



datasets = {
    "Marks": marks,
    "Temperatures": temperatures,
    "Sales": sales
}

for name, data in datasets.items():

    print("\n" + "=" * 50)
    print(name)
    print("=" * 50)

    numpy_results = calculate_with_numpy(data)

    print("\nUsing NumPy:")
    print(f"Mean               : {numpy_results[0]:.2f}")
    print(f"Median             : {numpy_results[1]:.2f}")
    print(f"Standard Deviation : {numpy_results[2]:.2f}")
    print(f"Minimum            : {numpy_results[3]:.2f}")
    print(f"Maximum            : {numpy_results[4]:.2f}")


    manual_results = calculate_without_numpy(data)

    print("\nWithout NumPy:")
    print(f"Mean               : {manual_results[0]:.2f}")
    print(f"Median             : {manual_results[1]:.2f}")
    print(f"Standard Deviation : {manual_results[2]:.2f}")
    print(f"Minimum            : {manual_results[3]:.2f}")
    print(f"Maximum            : {manual_results[4]:.2f}")