# This code sourced from blog here https://blog.quantinsti.com/stock-market-data-analysis-python/
# Import yfinance package
import yfinance as yf

# Import matplotlib for plotting
import matplotlib.pyplot as plt


# Set the start and end date
start_date = '1990-01-01'
end_date = '2021-07-12'

# Set the ticker
ticker = 'IBM'

# Get the data
data = yf.download(ticker, start_date, end_date)

# Print 5 rows
#data.tail() #  didnt work
# print(data)

# Plot the adjusted close price
data['Adj Close'].plot(figsize=(10, 7))

# Define the label for the title of the figure
plt.title("Adjusted Close Price of %s" % ticker, fontsize=16)

# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)

# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)

# Show the plot
plt.show()
