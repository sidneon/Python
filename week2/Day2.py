import numpy as np

#Q1. Create 3D random array and compute statistics along specific axis.

array_3d = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [5, 6, 4, 3]],
                    [[5, 3, 5, 6], [5, 7, 5, 8], [3, 6, 9, 0]],
                    [[9, 5, 6, 3], [9, 4, 3, 2], [9, 2, 3, 4]]])

total_sum = np.sum(array_3d)
print("Sum: ", total_sum)

Mean = np.mean(array_3d)
print("Mean: ", Mean)

Median = np.median(array_3d)
print("Median: ", Median)

Min = np.min(array_3d)
print("Min: ", Min)

Max = np.max(array_3d)
print("Max: ", Max)


#Q2. Write a program to generate a dataset of random floats and normalize the values between 0 and 1

def generate_and_normalize_dataset(min_value, max_value, size):
    #Generate random datasets of floats
    dataset = np.random.uniform(min_value, max_value, size)

    #Normalize Dataset between 0 and 1
    normalize_dataset = (dataset - np.min(dataset)) / (np.max(dataset) -np.min(dataset))

    return dataset, normalize_dataset

min_value = 1
max_value = 50
size = 45

orginal_data, normalize_data = generate_and_normalize_dataset(min_value, max_value, size)
print("Original Dataset: ", orginal_data)
print("Normalize Dataset: ",normalize_data)

#Q3. Implement conditional replacement to create a binary mask for values above the threshold.

data = np.array([1, 4, 5, 6, 7, 3, 7, 5, 6])

threshold = 5

binary_mask = (data > threshold).astype(int)

print(data)
print(binary_mask)
