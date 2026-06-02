import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_dataset():

    df = pd.read_csv(
        "data/placement_data.csv"
    )

    return df


def placement_distribution():

    df = get_dataset()

    fig, ax = plt.subplots()

    sns.countplot(
        x="Placed",
        data=df,
        ax=ax
    )

    ax.set_title(
        "Placement Distribution"
    )

    return fig


def cgpa_vs_dsa():

    df = get_dataset()

    fig, ax = plt.subplots()

    sns.scatterplot(
        data=df,
        x="CGPA",
        y="DSA",
        hue="Placed",
        ax=ax
    )

    ax.set_title(
        "CGPA vs DSA"
    )

    return fig