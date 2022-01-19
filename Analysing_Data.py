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

# Show replacing missing values (blank) to zero.
netflix_show_data.isna()
netflix_show_data.fillna(0)

# Show slicing, loc or iloc.
print(netflix_show_data.loc[0:20])
print(netflix_show_data.iloc[0:20, 0:10])

# Show iterrows - to iterate over rows and create a new column "name_length" which shows the number of characters in each title.
netflix_show_data = pd.read_csv(r'C:\Users\Darren\Documents\Professional Development\Intro to data analytics UCD\Assignment\netflix_titles.csv')
for lab, row in netflix_show_data.iterrows():
    netflix_show_data.loc[lab, "name_length"] = len(row["title"])
print(netflix_show_data)

# Show looping - for loop utilizing "car" list (list showing size of different parts of a car) and creating a sentence saying the 'car part' (element of the list) is 'x' cm.
car = [["driver side seat", 100.25],
         ["passenger seat", 96.0],
         ["backseat", 150.0],
         ["boot", 175.75]]

for x in car:
    print("the " + x[0] + " is " + str(x[1]) + " cm")

# Merge DataFrames
