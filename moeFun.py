import math
import csv

def calculateMOE(n, z=1.96, p=0.5):
    moe = z * math.sqrt((p*(1-p)))/math.sqrt(n)
    return moe

sampleSizeList = list(range(38, 2001))
sampleSizeList = [x for x in sampleSizeList if (x < 400 and x % 5 == 0) or (x >= 400 and x % 10 == 0)]

moeDict = {}
for sampleSize in sampleSizeList:
    result = calculateMOE(sampleSize)
    moeDict[sampleSize] = result

def export_dict_to_csv(data, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Sample Size', 'Margin of Error'])  # Write header
        for key, value in data.items():
            writer.writerow([key, value])

# Example usage:
if __name__ == '__main__':
    csv_filename = 'marginOfError.csv'
    export_dict_to_csv(moeDict, csv_filename)
    print(f"Dictionary exported to '{csv_filename}' successfully.")

