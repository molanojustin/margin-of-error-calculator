import pandas as pd

# Create an empty DataFrame
df = pd.DataFrame()

# Define the sample sizes
sample_sizes = list(range(50, 2050, 50))

# Define the prevalence of condition values
prevalence_values = [0.1, 0.2, 0.3, 0.4, 0.5]

# Iterate over the sample sizes
for sample_size in sample_sizes:
    # Create a dictionary to store the margin of errors for each prevalence value
    margin_of_errors = {}
    
    # Iterate over the prevalence values
    for prevalence_value in prevalence_values:
        # Calculate the margin of error
        margin_of_error = 1.96 * ((prevalence_value * (1 - prevalence_value)) / sample_size) ** 0.5
        
        # Multiply the margin of error by 100 and round to 1 decimal place
        margin_of_error = round(margin_of_error * 100, 1)
        
        # Add the margin of error to the dictionary
        margin_of_errors[prevalence_value] = margin_of_error
    
    # Convert the dictionary to a DataFrame
    margin_of_errors_df = pd.DataFrame(margin_of_errors, index=[sample_size])
    
    # Concatenate the DataFrame to the main DataFrame
    df = pd.concat([df, margin_of_errors_df])

# Set the sample sizes as the index of the DataFrame
df.index = sample_sizes

# Export the DataFrame as a CSV file in the current directory with the same filename
df.to_csv('moeWithPrevelance.csv')