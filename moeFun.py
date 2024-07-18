import math
import csv

# Calculates MOE based on a z-score of 1.96 (95% CI) and a proportion of 0.5
def calculateMOE(n, z=1.96, p=0.5):
    moe = z * math.sqrt((p*(1-p)))/math.sqrt(n)
    return moe

# Defines the function to export to excel as a csv
def export_dict_to_csv(data, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Sample Size', 'Margin of Error'])  # Write header
        for key, value in data.items():
            writer.writerow([key, value])

# Calls function
if __name__ == '__main__':
    
    # Creates a list of sample sizes between 38 and 2000
    sampleSizeList = list(range(38, 2001))

    # Filters the list to only include multiples of 5 below 400 and multiples of 10 above 400
    sampleSizeList = [x for x in sampleSizeList if (x < 400 and x % 5 == 0) or (x >= 400 and x % 10 == 0)]

    # Initializes dictionary
    moeDict = {}

    # For each n, a sample size is calculated and the key/value are added to the dictionary
    for sampleSize in sampleSizeList:
        z = 1.96
        p = 0.5
        result = calculateMOE(sampleSize, z, p)
        moeDict[sampleSize] = result
        csv_filename = 'marginOfError.csv'
        export_dict_to_csv(moeDict, csv_filename)
    print(f"Dictionary exported to '{csv_filename}' successfully.")

