# Visualise some of the project data using matplotlib/seaborn.

# Importing data from a CSV file saved locally on my laptop into Python as a Pandas DataFrame.
import pandas as pd
df = pd.read_csv(r'C:\Users\Darren\Documents\Professional Development\Intro to data analytics UCD\Assignment\AnnualTicketSalesv2.csv')
print(df.head())

import matplotlib.pyplot as plt
plt.plot(df["YEAR"], df["TICKETS SOLD IN BILLIONS"])
xlab = 'Year [in years]'
ylab = 'Total Box Office Ticket Sales [in billions]'
title = 'Total Box Office Ticket Sales 1995 - 2021'

plt.xlabel('Year [in years]')
plt.ylabel('Total Box Office Tickets Sales [in billions]')
plt.title('Total Box Office Tickets Sales 1995 - 2021')
plt.show()
