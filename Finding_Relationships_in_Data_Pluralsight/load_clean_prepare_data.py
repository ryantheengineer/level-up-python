# Follow along code from Load Clean and Prepare Data module in Pluralsight
# Course, "Finding Relationships in Data"
import matplotlib
import pandas as pd

import matplotlib.pyplot as plt

crude_oil_data = pd.read_csv('U.S._crude_oil_production.csv')
print(crude_oil_data.head(5))

print(crude_oil_data.shape)

print(crude_oil_data.columns)

# Does any individual state have oil production equal to zero?
print(crude_oil_data.columns[(crude_oil_data.sum(axis=0)) == 0])

# We find that Arizona and Virginia both had zero oil production, so we will
# drop those states from our data
crude_oil_data.drop(['Arizona', 'Virginia'], inplace=True, axis=1)

# Print the remaining columns
print(crude_oil_data.columns)

# Convert date info to date/time format in order to extract features from dates
crude_oil_data['Date'] = pd.to_datetime(crude_oil_data['Month'])
print(crude_oil_data['Date'].head())

crude_oil_data.drop('Month', inplace=True, axis=1)
print(crude_oil_data.columns)

# Rename columns with long names to shorter versions
crude_oil_data = crude_oil_data.rename(columns={'Federal Offshore Gulf of Mexico Crude Oil': 'Mexico',
                                                'Federal Offshore Pacific Crude Oil': 'Pacific'})
print(crude_oil_data.columns)

# Extract year information
crude_oil_data['Year'] = crude_oil_data['Date'].dt.year
print(crude_oil_data['Year'].sample(10))

# Extract month information
crude_oil_data['Month'] = crude_oil_data['Date'].dt.month
print(crude_oil_data['Month'].sample(10))

# Having the months and years extracted will allow visualization of data on a monthly or yearly basis

# Now send the cleaned and prepared data to a new csv file
crude_oil_data.to_csv('crude_oil_data_processed.csv', index = False)

# Quick statistical description of data in dataset using describe function
print('\n')
print(crude_oil_data.describe())
