import pandas as pd #convention
import csv
# standard waay to do something
# pd.

# pandas is short for "panel data"
# is built on top of numpy ("numerical
# python")
# 2 main reasons to use pandas for
# data science
# 1.really great built-in functionality
# for indexing,cleaning,statistics,
# etc.
# 2.label-based indexing (in addition
# to position-based indexing)

# there are 2 main objects in pandas
# powerful list)
# 1.Series:1D data (like a more
# powerful list)
# 2.DataFrame:2D data ( like a more
# powerful 2D list)

# let's start with Series
populations = [ 26.8, 21.1, 7.9, 2.6]
cities = ["Shanghai", "Beijing", "Hangzhou", "zibo"]
pop_ser = pd.Series(populations, index=cities)
print(pop_ser)

pop_ser.name ="Population"
print(pop_ser)

# indexing/slicing(:)
# we can user a label to get a value
print(pop_ser["Beijing"])
print()
print(pop_ser[["Beijing","zibo"]])
print()
print(pop_ser["Beijing":"zibo"])
print()
# start and stop labels are included
# we can still do position-based indexing
# with Series (use .iloc[])
# iloc -> integer location
print(pop_ser.iloc[1]) # asme output as
# print (pop_ser["Beijing"])
print("*",pop_ser.iloc[[2,3]])

print("**",pop_ser.iloc[1:4])
# summary statistics
print("average population:",pop_ser.mean())
print("standard deviation population:",pop_ser.std())
print()
#we can add new data to to a Series
# very similar to how you add a new
# key:value pair to a dictionary
pop_ser["Liuzhou"]=2.1
print(pop_ser)
print (len(pop_ser))
print(pop_ser.shape)
#
#
pop_ser2=pd.Series(dtype=float)
print(pop_ser2)
pop_ser2["Liuzhou"]=2.1
print(pop_ser2)


#let's start DataFrames
#colum for city
pop_data=[
    ["Shanghai",26.8,"large"],
    ["Beijing",21.1,"large"],
    ["Hangzhou",7.9,"medium"],
    ["Zibo",2.6,"small"]
]
header=["city","population","class"]
pop_df=pd.DataFrame(pop_data,columns=header)
print(pop_df)


pop_ser3=pop_df["population"]
print(type(pop_ser3))
print(pop_ser3)

pop_ser4=pop_df.iloc[:,1]

print(pop_ser4)

print(pop_df.iloc[0,1])
pop_df=pop_df.set_index("city")

print(pop_df)

print(pop_df.loc["Hangzhou"]["population"])
print(pop_df["population"]["Hangzhou"])


regions_df=pd.read_csv("regions.csv",index_col=0)
print(regions_df)
print()

merged_df1=pop_df.merge(regions_df,on=["city"])
print(merged_df1)

merged_df=pop_df.merge(regions_df,on=["city"],how="outer")
print(merged_df)

merged_df.to_csv("merged.csv")


grouped_by_class=merged_df.groupby("class")

mean_pop_ser=grouped_by_class["population"].mean()

mean_pop_ser.name="Mean Population"
print(mean_pop_ser)


large_df=grouped_by_class.get_group("large")
print(large_df)

large_df2= \
    merged_df[merged_df["class"]=="large"]
print(large_df2)


print(merged_df["class"].value_counts())

merged_df= \
    merged_df.sort_values("population",
                          ascending=False)
print(merged_df)


print(merged_df.isnull())
print()
print(merged_df.isnull().sum())
print()
print(merged_df.isnull().sum().sum())

