''' Sadi Çetinkaya 05.03.2021
PI Works Test
Soru 4 - kodları
'''
import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)
df = pd.read_csv("country_vaccination_stats.csv")
df.loc[df['daily_vaccinations'].isnull(),'daily_vaccinations'] = df['country'].map(df.groupby('country')['daily_vaccinations'].min())
df.loc[df['daily_vaccinations'].isnull(),'daily_vaccinations'] = 0
print(df)
