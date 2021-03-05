''' Sadi Çetinkaya 05.03.2021 
PI Works Test 
Soru 5 - kodları 
''' 
import pandas as pd 
pd.set_option("display.max_rows", None, "display.max_columns", None) 
df = pd.read_csv("country_vaccination_stats.csv")
df = df.groupby('country')['daily_vaccinations'].median()
print(df.nlargest(3))
