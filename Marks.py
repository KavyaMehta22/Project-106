import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    Marks = []
    Days = []


    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks.append(float(row["Marks In Percentage"]))
            Days.append(float(row["Days Present"]))

    return {"x": Marks, "y": Days}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between Students' Marks and the Days Present :", correlation[0, 1])

def setup():
    data_path = "Student Marks.csv"
    dataSource  = getDataSource(data_path)

    findCorrelation(dataSource)

setup()
