import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/placement_data.csv")

# Placement Distribution
plt.figure(figsize=(6,4))

sns.countplot(
    x="Placed",
    data=df
)

plt.title("Placement Distribution")

plt.show()

plt.figure(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="CGPA",
    y="DSA",
    hue="Placed"
)

plt.title("CGPA vs DSA")

plt.show()

plt.figure(figsize=(8,6))

sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Feature Correlation")

plt.show()