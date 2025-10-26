import seaborn as sns
df = sns.load_dataset("titanic")
df.to_csv("titanic_raw.csv", index=False)