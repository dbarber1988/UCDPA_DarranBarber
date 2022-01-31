# Define a custom function to create reusable code.
def sum_the_numbers (num1 = 0, num2 = 0):
  total = num1 + num2
  return total

summation = sum_the_numbers(10, 20)
print(summation)

# Show Numpy - create 2 Numpy arrays from lists and convert height in inches to height in centimetres enabling the appending of 1 Numpy array to another.
gym_class_height_cm = [180.50, 210.60, 200.40, 215.50, 185.30, 195.70, 190.50, 225.50, 205.40]
import numpy as np
gym_class_height_np = np.array(gym_class_height_cm)
print(type(gym_class_height_np))

additional_members_height_in = [60.50, 70.50, 65.40, 80.20, 55.70, 75.60, 85.90]
additional_members_height_in_np = np.array(additional_members_height_in)
additional_members_height_cm_np = additional_members_height_in_np * 2.54
additional_members_height_cm_np2 = np.around(additional_members_height_cm_np, decimals=2)
print(additional_members_height_cm_np2)

total_gym_class_height_np = np.append(additional_members_height_cm_np2, gym_class_height_np)
print(total_gym_class_height_np)


