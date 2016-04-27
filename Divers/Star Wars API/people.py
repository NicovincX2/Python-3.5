# -*- coding: utf-8 -*-

import os
import requests
import json
    
d = {'name':[], 'mass':[], 'height':[]}

url = "http://swapi.co/api/people/?page=1"

while url:
    r = requests.get(url)
    data = json.loads(r.text)
    for i in data['results']:
        d['name'].append(i['name'])
        d['mass'].append(i['mass'],)
        d['height'].append(i['height']),
    url = data['next']

import pandas as pd

df = pd.DataFrame(d)
df = df[(df['mass']!='unknown') & (df['height']!='unknown')]
df['mass'] = df['mass'].apply(lambda x: x.replace(',','.'))
df['mass'] = df['mass'].astype(float)
df['height'] = df['height'].astype(int)
df.head()

import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls
from random import random, randrange, seed
seed(123)

traces = []

for i in df.index:
    tr = Scatter(
        x=df.ix[i]['height'], 
        y=df.ix[i]['mass'],
        name=df.ix[i]['name'],
        marker=Marker(
        color='rgb(%s, %s, %s)' % (randrange(0,256), randrange(0,256), randrange(0,256)),
        size=df.ix[i]['mass']/df.ix[i]['height']*20))
    traces.append(tr)

layout = Layout(
        title='Star Wars API - People',
        showlegend=False,
        xaxis=XAxis(
            showgrid=False,
            zeroline=False,
            tick0=-1,
            title='Mass [kg]',),
        yaxis=YAxis(
            showgrid=False,
            zeroline=False,
            title='Height [cm]',))

fig = Figure(data=traces, layout=layout)
py.iplot(fig, filename='SWAPI-People')    
    
os.system("pause")