"""
Create by abarrio
Date: 01/11/2019
Manager to text mining.
"""

from os import path

from django.template.loader import render_to_string
from wordcloud import WordCloud
from os import path
from django.http import HttpResponse

import seaborn as sns
import pandas as pd
import numpy as np


"""Method for mananger to visualization type """
def manager_visualizator(request):

    def numbers_to_months(argument):
        switcher = {
            1: heatmap(),
            2: wordcloud()
            }

    return HttpResponse("")


""" Visualization of HeatMap"""
def heatmap(request):
    # Create a dataset (fake)
    if 'Stand' in request.GET:
        url = 'https://python-graph-gallery.com/wp-content/uploads/mtcars.csv'
        df = pd.read_csv(url)
        df = df.set_index('model')
        del df.index.name
        data = sns.clustermap(df)
        html = render_to_string('list/mg_visualization.html', data)

    # Standardize or Normalize every column in the figure
    # Standardize:
    #sns.clustermap(df, standard_scale=1)
    # Normalize
    #sns.clustermap(df, z_score=1)

    return HttpResponse(html)

"""Visualization of WordCloud"""
def wordcloud(request):

    text = request.data()

    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)
    return HttpResponse(wordcloud)