import random
import plotly_express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import pandas as pd

df= pd.read_csv("110/data.csv")
data=df["average"].tolist()
populate_mean=statistics.mean(data)
fig=ff.create_displot([data],["average"],show_his=False)
fig.show()
print(data)