# Function to compute maximum heart rate
def maxHR(age):
    return 208-0.7*age


# Ask user for age
age=int(input('Enter your age: '))

# Print estimation of maximum heart rate based on age
print(f'Your max heart rate is {maxHR(age)} bpm')
