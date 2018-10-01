import plotly.graph_objs as go
from sqlalchemy import create_engine 
import pandas as pd

engine = create_engine("mysql+mysqlconnector://root:X8sjwait46@localhost/ujiantitanic?host=localhost?port=3306")
conn = engine.connect()

parentCategory = conn.execute("SELECT * FROM titanic").fetchall()
dfTitanic = pd.DataFrame(parentCategory)
dfTitanic.columns = parentCategory[0].keys()

childCategory = conn.execute("SELECT * FROM titanicoutcalc").fetchall()
dfStd = pd.DataFrame(childCategory)
dfStd.columns = childCategory[0].keys()

listGoFunc = {
    'bar': go.Bar,
    'violin': go.Violin,
    'box': go.Box
}

def getPlot(typeCategory, xCategory):
    return [
        listGoFunc[typeCategory]
        (
            x = dfTitanic[xCategory],
            y = dfTitanic['fare'],
            text = dfTitanic['fare'],
            opacity = 0.7,
            name = 'Fare',
            marker = dict(color='blue'),
            legendgroup = 'Fare'
        ),
        listGoFunc[typeCategory](
            x = dfTitanic[xCategory],
            y = dfTitanic['age'],
            text = dfTitanic['age'],
            opacity = 0.7,
            name = 'Age',
            marker = dict(color='orange'),
            legendgroup = 'Age'
        )
    ]
    