import matplotlib
import pandas as pd

import matplotlib.pyplot as plt

crude_oil_data = pd.read_csv('crude_oil_data_processed.csv')
print('\n{}'.format(crude_oil_data.head(5)))

# Convert data on dates from csv into datetime format
crude_oil_data['Date'] = pd.to_datetime(crude_oil_data['Date'])
print('\n{}'.format(crude_oil_data['Date'].head()))

# Plot a simple line plot to show data variation over time
crude_oil_data.plot(x='Date', y='U.S. Crude Oil ',
                    figsize=(12, 8), color='brown')
plt.ylabel('Production')
plt.title('U.S. Crude Oil Production')
# plt.show()

# View summary descriptive statistics using a boxplot (specify the column of interest)
crude_oil_data.boxplot('U.S. Crude Oil ', figsize=(12, 8))
plt.ylabel('Production')
plt.title('U.S. Crude Oil Production')
# plt.show()

# Box plot for single state production
crude_oil_data[['California']].boxplot(figsize=(12, 8))
plt.ylabel('Production')
plt.title('California Crude Oil Production')
# plt.show()

# Comparative box plot
crude_oil_data[['Alaska', 'California']].boxplot(figsize=(12, 8))
plt.ylabel('Production in Alaska, California')
plt.title('Alaska, California Crude Oil Production')
# plt.show()

# Boxplots that show production over time
crude_oil_data.boxplot(column=['U.S. Crude Oil '], by=['Year'],
                        figsize=(12, 8))
plt.ylabel('Production')
# plt.show()

# Group data based on the year column
year_data = crude_oil_data.groupby('Year', as_index=False).sum()
print('\n{}'.format(year_data[['Year', 'U.S. Crude Oil ']]))

# Bar plot of the data by year
colors = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9']
year_data.plot.bar(x='Year', y='U.S. Crude Oil ',
                    figsize=(12, 8), color=colors,
                    legend=False)
plt.ylabel('Production')
plt.title('U.S. Crude Oil Production')
# plt.show()

# Mean data
mean_prod_data = crude_oil_data.mean()[1:-3] # Sliced out data not interested in (date, year, etc.)
print('\nMean data:\n{}'.format(mean_prod_data))

# Sort the mean data
mean_prod_data = mean_prod_data.sort_values(ascending=False)
print('\nSorted mean data:\n{}'.format(mean_prod_data))

# Making another dataframe to make later steps easier
mean_prod_df = pd.DataFrame(mean_prod_data).reset_index()
mean_prod_df.columns = ['State', 'Production']
print('\n{}'.format(mean_prod_df.head(10)))

# Bar plot of production across states
plt.figure(figsize=(12, 8))
plt.bar(mean_prod_df['State'], mean_prod_df['Production'],
        width=0.85)
plt.title('US Oil Mean-Production June 2008 to June 2018')

plt.xticks(rotation=90)
plt.xlabel('State')
plt.ylabel('Production')
plt.show()

# Visualize production across states with probability density distribution
mean_prod_df['Production'].plot.kde(figsize=(12, 8))
plt.title('US Oil Mean-Production June 2008 to June 2018')
plt.xlabel('Oil Production')
plt.show()

# Scatter plot of Texas oil production vs general US oil production
plt.figure(figsize=(12, 8))
plt.scatter(crude_oil_data['Texas'], crude_oil_data['U.S. Crude Oil '], c='g')
plt.xlabel('US Production')
plt.ylabel('Texas Production')
plt.show()

# The strong linearity of the relationship between Texas and the US production
# levels indicates a strong correlation (when Texas is doing well, the US is
# also doing well at large)

# Scatter plot of California oil production vs general US oil production
plt.figure(figsize=(12, 8))
plt.scatter(crude_oil_data['California'], crude_oil_data['U.S. Crude Oil '], c='g')
plt.xlabel('US Production')
plt.ylabel('California Production')
plt.show()

# Scatter plot of Michigan oil production vs general US oil production
plt.figure(figsize=(12, 8))
plt.scatter(crude_oil_data['Michigan'], crude_oil_data['U.S. Crude Oil '], c='g')
plt.xlabel('US Production')
plt.ylabel('Michigan Production')
plt.show()
