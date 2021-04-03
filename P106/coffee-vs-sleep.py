import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x = "sleep in hours", y = "Coffee in ml")
        fig.show()

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["sleep in hours"]))
            sleep.append(float(row["Coffee in ml"]))

        return{"x" : coffee, "y" : sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between hours of sleep and amount of coffee consumed :- /n--->", correlation[0,1])

def setup():
    data_path = "coffee-vs-sleep.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()