import requests
import numpy as np
import pandas as pd
import datetime
from datetime import timedelta
import json
from plotly.offline import plot
import plotly.graph_objects as go
from . import AlphaVantageAPIkey as API_key

def get_fred(query, start_date = None, end_date = None):
    fed_key = API_key.Fed()
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {'series_id': query,
              'api_key' : fed_key,
              'file_type' : 'json',
              'observation_start': start_date,
              'observation_end': end_date,
              }

    r = requests.get(url, params = params)
    
    return r.json()

def make_observation_chart(query, name, start_date = None, end_date = None):
    data = get_fred(query, start_date = start_date, end_date = end_date)
    data = data['observations']
    df = pd.DataFrame(data)
    x = df['date']
    y = df['value']
    fig = go.Figure()
    scatter = go.Scatter(x = x , y = y, name = name)
    fig.add_trace(scatter)
    fig.update_layout(
        title = name,
        xaxis_title = "Date",
        yaxis_title = "Spread (%)",
        showlegend = False,
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="#7f7f7f"
        ),    
    )
    fig.update_yaxes(zeroline = True, zerolinewidth = 2, zerolinecolor = 'red')
    plt_div = plot(fig, output_type = 'div', include_plotlyjs= False)
    return plt_div
