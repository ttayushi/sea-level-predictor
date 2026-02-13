import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")

    fig, ax = plt.subplots()
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years = pd.Series(range(1880, 2051))
    ax.plot(years, res.intercept + res.slope * years, 'r')

    recent = df[df["Year"] >= 2000]
    res2 = linregress(recent["Year"], recent["CSIRO Adjusted Sea Level"])
    years_recent = pd.Series(range(2000, 2051))
    ax.plot(years_recent, res2.intercept + res2.slope * years_recent, 'g')

    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    fig.savefig("sea_level_plot.png")
    return fig
