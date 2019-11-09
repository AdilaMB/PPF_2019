"""
Create by abarrio
Date: 01/11/2019
Manager to text mining.


import io
from matplotlib.backends.backend_agg import FigureCanvasAgg
from wordcloud import WordCloud
from django.http import HttpResponse, response
from random import sample
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
"""

"""Method for mananger to visualization type 
#def manager_visualizator(request):

def numbers_to_visualization(argument):
    switcher = {
        1: heatmap(),
        2: wordcloud(),
        3: plot()
        }

    return HttpResponse("")


 Visualization of "HeatMap long format" is when each line represents an observation. You have 3 columns: individual, 
variable name, and value (x, y and z). You can plot a heatmap from this kind of data

def heatmap(request):
    # Create a dataset (fake)
    url = 'https://python-graph-gallery.com/wp-content/uploads/mtcars.csv'
    df = pd.read_csv(url)
    df = df.set_index('model')
    del df.index.name
    # data = sns.clustermap(df)

    #Pinto la figura
    plt.figure()

    # Standardize or Normalize every column in the figure
    # Standardize:
    # data = sns.clustermap(df, standard_scale=1)
    # Normalize
    fig = sns.clustermap(df, z_score=1)

    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    png_output = io.BytesIO(fig)
    fig.set_canvas(plt.gcf().canvas)

    canvas = plt.savefig('figura.png', facecolor = fig.get_facecolor())
    response = HttpResponse(png_output.getvalue(), content_type='images/figura.png')

    #return f"<img src='data:image/png;base64,{data}'/>"

    response = HttpResponse(png_output.getvalue(), canvas)
    return response


def plot(request):
    # Creamos los datos para representar en el gráfico
    x = range(1, 11)
    y = sample(range(20), len(x))

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()

    # Creamos los ejes
    axes = f.add_axes([0.15, 0.15, 0.75, 0.75])  # [left, bottom, width, height]
    axes.plot(x, y)
    axes.set_xlabel("Eje X")
    axes.set_ylabel("Eje Y")
    axes.set_title("Mi gráfico dinámico")

    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    # Creamos la respuesta enviando los bytes en tipo imagen png
    response = HttpResponse(buf.getvalue(), content_type='image/png')

    # Limpiamos la figura para liberar memoria
    f.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    response['Content-Length'] = str(len(response.content))

    #return render('list/search.html', context_instance=RequestContext(response))
    #return HttpResponse(html)

    # Devolvemos la response
    return response


Visualization of WordCloud
def wordcloud(request):
    # Create a list of word
    text = (
        "Python Python Python Matplotlib Matplotlib Seaborn Network Plot Violin Chart Pandas Datascience Wordcloud "
        "Spider Radar Parrallel Alpha Color Brewer Density Scatter Barplot Barplot Boxplot Violinplot Treemap Stacked "
        "Area Chart Chart Visualization Dataviz Donut Pie Time-Series Wordcloud Wordcloud Sankey Bubble")

    # Create the wordcloud object
    wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.margins(x=0, y=0)

    return HttpResponse(wordcloud)
    """