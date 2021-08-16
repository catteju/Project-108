import csv
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("Data1.csv")

fig = ff.create_distplot([df["AvgRating"]], ["Average Rating"], show_hist=False)

fig.show()
