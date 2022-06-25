import pandas as pd

df = pd.read_excel("eu_countries.xlsx")
print(df.head())

def replace_gini(gini):
    if gini < 35:
        return "low_gini"
    elif 35 <= gini < 45:
        return "medium_gini"
    else:
        return "high_gini"

df["Gini_Index"] = df["Gini_Index"].astype("float")
df["Gini_Index"] = df["Gini_Index"].apply(lambda gini: replace_gini(gini))

dummy_gini = pd.get_dummies(df["Gini_Index"])

df = pd.merge(left=df, right=dummy_gini, left_index=True, right_index=True)
df = df.drop("Gini_Index", axis=1)

def replace_pop_density(pop_density):
    if pop_density < 50:
        return "low_pop_den"
    elif 50 <= pop_density < 200:
        return "moderate_pop_den"
    elif 200 <= pop_density < 1000:
        return "high_pop_den"
    else:
        return "very_high_pop_den"

df["Pop_Density"] = df["Pop_Density"].astype("int")
df["Pop_Density"] = df["Pop_Density"].apply(lambda den: replace_pop_density(den))

dummy_pop_den = pd.get_dummies(df["Pop_Density"])

df = pd.merge(left=df, right=dummy_pop_den, left_index=True, right_index=True)
df = df.drop("Pop_Density", axis=1)

def replace_gni_capita(gni):
    if gni < 1036:
        return "low_income"
    elif 1036 <= gni < 4045:
        return "lower_middle_income"
    elif 4045 <= gni < 12535:
        return "upper_middle_income"
    else:
        return "high_income"
    
df["GNI_Capita"] = df["GNI_Capita"].astype("int")
df["GNI_Capita"] = df["GNI_Capita"].apply(lambda gni: replace_gni_capita(gni))

dummy_gni = pd.get_dummies(df["GNI_Capita"])

df = pd.merge(left=df, right=dummy_gni, left_index=True, right_index=True)
df = df.drop("GNI_Capita", axis=1)

def replace_fertility_rate(rate):
    if rate < 1.3:
        return "very_low_fertility"
    elif rate < 2:
        return "below_replacement_fertility"
    elif 2 <= rate <= 2.2:
        return "replacement_fertility"
    elif 2.2 < rate < 5:
        return "above_replacement_fertility"
    else:
        return "high_fertility"
    
df["Fertility_Rate"] = df["Fertility_Rate"].astype("float")
df["Fertility_Rate"] = df["Fertility_Rate"].apply(lambda rate: replace_fertility_rate(rate))

dummy_rate = pd.get_dummies(df["Fertility_Rate"])

df = pd.merge(left=df, right=dummy_rate, left_index=True, right_index=True)
df = df.drop("Fertility_Rate", axis=1)

def replace_inflation_rate(rate):
    if rate <= 3:
        return "creeping_inflation"
    elif 3 < rate <= 10:
        return "walking_inflation"
    elif 10 < rate < 50:
        return "galloping_inflation"
    else:
        return "hyperinflation"
    
df["Inflation_Rate"] = df["Inflation_Rate"].astype("float")
df["Inflation_Rate"] = df["Inflation_Rate"].apply(lambda rate: replace_inflation_rate(rate))

dummy_infl_rate = pd.get_dummies(df["Inflation_Rate"])

df = pd.merge(left=df, right=dummy_infl_rate, left_index=True, right_index=True)
df = df.drop("Inflation_Rate", axis=1)
    
def replace_min_wage(wage):
    if wage > 1000:
        return "group_1_wage"
    else:
        return "group_2_wage"

df["Minimum_Wage"] = df["Minimum_Wage"].astype("int")
df["Minimum_Wage"] = df["Minimum_Wage"].apply(lambda wage: replace_min_wage(wage))

dummy_wage = pd.get_dummies(df["Minimum_Wage"])

df = pd.merge(left=df, right=dummy_wage, left_index=True, right_index=True)
df = df.drop("Minimum_Wage", axis=1)

df.to_csv("processed_eu_countries_3.csv")