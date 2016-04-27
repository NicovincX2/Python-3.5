# -*- coding: utf-8 -*-

import os
import requests
import json

d = {'name':[], 'max_atmosphering_speed':[], 'hyperdrive_rating':[]}

url = "http://swapi.co/api/starships/?page=1"

while url:
    r = requests.get(url)
    data = json.loads(r.text)
    for i in data['results']:
        d['name'].append(i['name'])
        d['max_atmosphering_speed'].append(i['max_atmosphering_speed'],)
        d['hyperdrive_rating'].append(i['hyperdrive_rating']),
    url = data['next']

import pandas as pd

df = pd.DataFrame(d)
df['max_atmosphering_speed'] = df['max_atmosphering_speed'].apply(lambda x: x.strip('km'))
df = df[(df['max_atmosphering_speed']!='n/a') & (df['hyperdrive_rating']!='n/a')]
df = df[(df['max_atmosphering_speed']!='unknown') & (df['hyperdrive_rating']!='unknown')]
df['max_atmosphering_speed'] = df['max_atmosphering_speed'].astype(float)
df['hyperdrive_rating'] = df['hyperdrive_rating'].astype(float)
df.head()

import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls
from random import random, randrange, seed
seed(123)

traces = []

for i in df.index:
    tr = Scatter(
        x=df.ix[i]['max_atmosphering_speed'], 
        y=df.ix[i]['hyperdrive_rating'],
        name=df.ix[i]['name'],
        marker=Marker(
        color='rgb(%s, %s, %s)' % (randrange(0,256), randrange(0,256), randrange(0,256)),
        size=0.001 * df.ix[i]['max_atmosphering_speed']/df.ix[i]['hyperdrive_rating']*20))
    traces.append(tr)

layout = Layout(
        title='Star Wars API - Spaceships',
        showlegend=False,
        xaxis=XAxis(
            showgrid=False,
            zeroline=False,
            title='Max. atmosphering speed [km/h]',
            tick0=-1,
            type='log'),
        yaxis=YAxis(
            showgrid=False,
            zeroline=False,
            title='Hyperdrive rating',),)

fig = Figure(data=traces, layout=layout)
py.iplot(fig, filename='SWAPI-Spaceships')
    
os.system("pause")