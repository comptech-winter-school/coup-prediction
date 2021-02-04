from django.shortcuts import render

import os
import json
import pandas as pd
from plotly.offline import plot
import plotly.express as px


# Create your views here.
def main_page(request):
    return render(request, 'CoupPredictionApp/main.html')


def datasets_page(request):
    return render(request, 'CoupPredictionApp/Review.html')


def index(request):
    response = open(os.path.dirname(os.path.realpath(__file__)) + '/geo.json', "r")
    counties = json.load(response)

    df = pd.read_csv(os.path.dirname(os.path.realpath(__file__)) + '/population.csv')
    fig = px.choropleth(df, geojson=counties, locations='country', color='pop_num',
                        color_continuous_scale='emrld',
                        range_color=(0, df['pop_num'].max()),
                        scope="world",
                        featureidkey="properties.geounit",
                        labels={'pop_num': 'Population'}
                        )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return render(request, 'CoupPredictionApp/main.html', context={'plot_div': plot(fig, output_type='div')})
