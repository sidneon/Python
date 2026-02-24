import numpy as np

#Q1. create a 4x4 matirx and calculate the sum of its rows and coloum

matrix = np.array([[1, 2, 3, 7], [4, 5, 6, 7], [7, 8, 9, 5], [9, 4, 6, 7]])

rows_sum = np.sum(matrix, axis=1)
coloum_sum = np.sum(matrix, axis=0)

print("Original_Matrix:\n",matrix)
print("Sum of Rows:\n", rows_sum)
print("Sum of Coloums:\n", coloum_sum)

#Q2. Write a program to normalize an arrray (scale values between 0 and 1)

def normalize_arrary(arr):

    #to find min and max value in array
    min_value = np.min(arr)
    max_value = np.max(arr)

    #normalize array using formula
    normalize_arr = (arr - min_value)/ (max_value - min_value)

    return normalize_arr

if __name__ == "__main__":
    arr = np.array([1, 4, 5, 7, 8, 11])
    normalize_arr = normalize_arrary(arr)

    print("Original array: ", arr)
    print("Normalize array: ", normalize_arr)


#Q3. Generate a random array and find the minimum and max values

def random_array_for_max_and_min_value(low_bound, high_bound, size):
   
    #generate random array
    random_array = np.random.randint(low_bound, high_bound, size=size)

    #to find min and max falue
    min_value = np.min(random_array)
    max_value = np.max(random_array)

    return random_array, min_value, max_value

if __name__ == "__main__":
    array, min_value, max_value = random_array_for_max_and_min_value(6, 29, 23)

    print("Generated Array: ", array)
    print("Minimum Value: ", min_value)
    print("Maximum value: ", max_value)

