# Importing data to use
import pandas as pd
df = pd.read_csv(r'C:\Users\Darren\Documents\Professional Development\Intro to data analytics UCD\Assignment\AnnualTicketSales.csv')
print(df.head())

# Show sorting - what 5 years had the highest number of tickets sold for the cinema in North America?
highest_tickets_sold = df.sort_values(["TICKETS SOLD"], ascending=[False])
print(highest_tickets_sold.head())

# Show sorting - what 5 years had the lowest number of tickets sold for the cinema in North America?
lowest_tickets_sold = df.sort_values(["TICKETS SOLD"], ascending=[True])
print(lowest_tickets_sold.head())

# Show setting an index, removing it while keeping its contents and removing it while dropping its contents.
df_ind = df.set_index("YEAR")
print(df_ind)
print(df_ind.reset_index())
print(df_ind.reset_index(drop=True))

# Show grouping and summary statistics - count of tv shows or movies per director.
netflix_show_data = pd.read_csv(r'C:\Users\Darren\Documents\Professional Development\Intro to data analytics UCD\Assignment\netflix_titles.csv')
nsd_grouped = netflix_show_data.groupby("director")["show_id"].count()
print(nsd_grouped)

# Show replacing missing values (blank) to none.
netflix_show_data.isna()
netflix_show_data.fillna(value=None)

# Show slicing, loc or iloc.
print(netflix_show_data.loc[0:20])