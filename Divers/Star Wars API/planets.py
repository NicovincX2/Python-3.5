# -*- coding: utf-8 -*-

import os
import requests
import json

d = {'name':[], 'diameter':[], 'population':[]}

url = "http://swapi.co/api/planets/?page=1"

while url:
    r = requests.get(url)
    data = json.loads(r.text)
    for i in data['results']:
        d['name'].append(i['name'])
        d['diameter'].append(i['diameter'],)
        d['population'].append(i['population']),
    url = data['next']

import pandas as pd

df = pd.DataFrame(d)
df = df[(df['diameter']!='unknown') & (df['population']!='unknown')]
df['diameter'] = df['diameter'].astype(int)
df['population'] = df['population'].astype(int)
df.head()


import plotly.plotly as py
from random import random, randrange, seed
seed(456)

traces = []

for i in df.index:
    tr = Scatter(
        x=df.ix[i]['diameter'], 
        y=df.ix[i]['population'],
        name=df.ix[i]['name'],
        marker=Marker(
        color='rgb(%s, %s, %s)' % (randrange(0,256), randrange(0,256), randrange(0,256)),
        size=0.001*df.ix[i]['diameter']))
    traces.append(tr)

layout = Layout(
        title='Star Wars API - Planets',
        xaxis=XAxis(
            showgrid=False,
            zeroline=False,
            title='Diameter [km]',
            tick0=-1,
            type='log'),
        yaxis=YAxis(
            showgrid=False,
            zeroline=False,
            title='Population',
            type='log'))

fig = Figure(data=traces, layout=layout)
py.iplot(fig, filename='SWAPI-Planets')

os.system("pause")
