#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly
import plotly.express as px

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)


# In[2]:


df = pd.read_csv('https://raw.githubusercontent.com/jwilber/Bob_Ross_Paintings/master/data/bob_ross_paintings.csv', index_col=0)


# In[3]:


df.head()


# In[4]:


app.layout = html.Div([
    
    html.Div([
        dcc.Graph(id='barplot_kleuren')
    ])
    
    html.Div([
        html.Label(['Kies het aantal kleuren:'],
                  style={'font-weight':'bold'}),
    
    html.P(),
    dcc.RangeSlider(
    id='slider1',
    marks={
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: '10',
        11: '11',
        12: '12',
        13: '13',
        14: '14',
        15: '15',
        },
        step=1,
        min=1,
        max=15,
        value=[8,9],
        dots=True
        allowCross=False,
        disabled=False,
        pushable=2,
        updatemode='mouseup',
        included=True,
        vertical=False,
        verticalHeight=900,
        className='None',
        tooltip={'always visible':False,
                'placement': 'bottom'},
        ),
    ]),
])


# In[ ]:


@app.callback(
        Output('barplot_kleuren','figure'),
        [Input('slider1','value')]
)

def update_graph(hoeveelheid_kleuren)
    
    dff=df[(df['num_colors']>=hoeveelheid_kleuren[0])&(df['num_colors']<=hoeveelheid_kleuren[1])]
    
    fig = px.bar(dff, x="value")
    
    return(fig)

