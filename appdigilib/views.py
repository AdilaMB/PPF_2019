"""
Create by abarrio
Date: 08/04/2019
Manager for the articles.
"""
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import requires_csrf_token, ensure_csrf_cookie
from django.http import HttpResponse
from appdigilib.forms import *
from django.db.models import Q
from appdigilib.models import Article, Category, AnaliticTask, Image, DataSource


""" Method to render the main page:
    Input: @request
    Check which items are to be shown depending on the selections made in the view
    Returns: @list of articles
"""
@requires_csrf_token
@ensure_csrf_cookie
def show_list(request):

    images = Image.objects.all().order_by('article')                            # Save all the images of the articles
    if request.method == 'POST':                                                # Check if the POST method comes from the search
        articles, tasks, categories, dataSources = search(request)              #Search articles by selected categories and tasks
        html = render_to_string('list/render.html', {'articles': articles,
                                                     'categories': categories,  # load all the data from the left menu
                                                     'tasks': tasks,
                                                     'images': images,
                                                     'dataSources': dataSources
                                                     })

    else:
        articles = Article.objects.all().order_by('published_date')             # Show all articles without having searched
        dataSources = DataSource.objects.all()
        categories = Category.objects.all()                                     # Save all categories for left menu
        tasks = AnaliticTask.objects.all()                                      # Save all analytical tasks for left menu
        html = render_to_string('list/index_list.html',{'articles': articles,                                # List the items in the main interface
                                                        'categories': categories,                            # load all the data from the left menu
                                                        'tasks': tasks,
                                                        'images': images,
                                                        'dataSources': dataSources})



    return HttpResponse(html)
    """return render(request, 'list/index_list.html',
                  {'articles': articles,                                # List the items in the main interface
                   'categories': categories,                            # load all the data from the left menu
                   'tasks': tasks,
                   'images': images,
                   'dataSources': dataSources}
                  )"""

"""Method to update the articles depending on the category marked in the view:
    Input: Ajax @peticion of the view with the check marked.
    Check for each item, if it has at least one category of the list, else, 
    remove it from the list of items to display.
    Returns: The list of items to be displayed
"""
#@requires_csrf_token
def update_article_category(request):

    if request.method == 'POST':                                                            #I check if the request is safe
        check_category = request.POST.getlist('lista[]')                                    #I save the list of categories that sent the request
        all_articles = []                                                                   #will store the items that I will show
        articles_show = list(Article.objects.all().prefetch_related('categories'))          #Total of current articles

        #I check if the article has at least one of the categories that are marked,
        # I add it in @all_articles
        for x in range(0, len(articles_show)):
            for y in range(0, len(check_category)):

                # Auxiliary method that says if a category is in an article
                if serach_category(articles_show[x], check_category[y]):
                    all_articles.append(articles_show[x])
                    break
    else:
        all_articles = Article.objects.all().values(Article.title, Article.author)

    html = render_to_string('list/render.html', {'articles': all_articles})
    return HttpResponse(html)


"""Method to update the articles depending on the analytical tasks marked in the view:
    Input: Ajax @peticion of the view with the check marked.
    Check for each item, if it has at least one analytical task from the list, else, 
    remove it from the list of items to display
    Return: The list of items to be displayed
"""
#@requires_csrf_token
def update_article_task(request):

    if request.method == 'POST':                                                            #I check if the request is safe
        task_checked = request.POST.getlist('lista[]')                                      #I save the list of Task that sent the request

        all_articles = []                                                                   #will store the items that I will show
        articles_show = list(Article.objects.all().prefetch_related('tasks'))               #Total of current articles

        #For each article I check if it has at least one task marked,
        # I add it in @all_articles
        for x in range(0, len(articles_show)):
            for y in range(0, len(task_checked)):

                if search_task(articles_show[x], task_checked[y]):                     #Auxiliary method that says if a task is in an article
                    all_articles.append(articles_show[x])
                    break
    else:
        all_articles = Article.objects.all().values(Article.title, Article.author)

    html = render_to_string('list/render.html', {'articles': all_articles})
    return HttpResponse(html)


"""Auxiliary method that searches if an article has a certain category.
     Input: @a article, @a category
     Returns True if that item has this category, False otherwise.
"""
def serach_category(s_article, s_category):

    list_cat_art = list(s_article.categories.all())             #All categories of the article that comes as an entry


    for c in range(0, len(list_cat_art)):                      #Search if the entry category exists in the article
        if list_cat_art[c].category == s_category:
          return True
    return False


"""Auxiliary method that searches if an article has a certain analytical task.
     Input: @an article, @a task
     Returns True if that article has that task, False otherwise
"""
def search_task(s_article, s_task):

    list_task_art = list(s_article.tasks.all())                   #Task list of the input article

    for t in range(0,len(list_task_art)):                         #Search if the task exists in the article
        if list_task_art[t].task == s_task:
            return True
    return False


"""Method to search for articles, giving a phrase and match the left menu check
    Input: @text
    Returns: @ List of articles that contain the text in the Title or Author
"""
def search(request):

    search_query = request.POST.get('my_form')
    list_task_serch = request.POST.getlist('list_task_search[]')
    lista_cat_buscar = request.POST.getlist('list_cat_search[]')
    dataSources = DataSource.objects.all()
    all_articles = []

    if search_query:
        articles = list(Article.objects.filter(                         # Query to search by title and author
            Q(title__contains= search_query) |
            Q(author__contains =search_query)))

        if articles:                                                    #Search in the articles of the query if they have the task marked
            for x in range(0, (len(articles)-1)):
                print(articles[x])
                for y in range(0, len(list_task_serch)):
                    print(list_task_serch[y])
                    if search_task(articles[x], list_task_serch[y]):    #Auxiliary method that says if a task is in an article
                        all_articles.append(articles[x])
                        articles.remove(articles[x])                    #I am deleting the articles that match so as not to search for them by categories
                        break
        if articles:                                                    #The remaining items, see if they have the category marked
            for x in range(0, len(articles)):
                for z in range(0, len(lista_cat_buscar)):
                    print(lista_cat_buscar[z])
                    if serach_category(articles[x], lista_cat_buscar[z]):
                        all_articles.append(articles[x])
                        break

    return all_articles, list_task_serch, lista_cat_buscar, dataSources


"""Method to visualize the details of the article
     Input: a selected article
     Return: All the data of the article in an html to be shown
"""
def details(request):
    if request.method == 'POST':                                             #If the details were requested
        id = request.POST.get('id_article')

        data_article = Article.objects.get(pk = id)                         #I get the object of the article
        categories = data_article.categories.all().only('category')         #I get the Category of the article as an object
        categories = list(categories.values('category'))                    #To the Category object, I ask for the values
        task = data_article.tasks.all().only('task')                        #I get the tasks of the article as an object
        task = list(task.values('task'))                                    #To the Task object, I ask for the values

        title = data_article.title
        author = data_article.author
        year = data_article.published_date
        doi = data_article.doi
        images = data_article.image

    return render(request, 'list/modal.html',  #Create the body of the modal with the respective data
                  {'categories': categories, 'year': year, 'doi':doi,
                   'task': task, 'images': images,
                   'title': title, 'author': author
                   })


"""Method to insert an image in my static directory"""
def add_image(request):
    categories = Category.objects.all()                         #Save all categories for left menu
    tasks = AnaliticTask.objects.all()                          #Save all task for left menu

    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)          #Form with the files

        if form.is_valid():
            form.save(commit=True)
            return redirect('post_list')                        #Show the initial page after saving the form
        else:
            return redirect('error')                            #The form is not valid
    else:
        form = ImagenForm
    return render(request, 'list/article.html',
                  {'form': form,
                   'categories': categories,
                   'tasks': tasks}
                  )


"""Auxiliary method that shows a standard error"""
def error(request):
    return HttpResponse("Something is wrong.")


"""
                                ---Work section with Visualization---
"""
#def heatmap(request):
    # Create a dataset (fake)
    #if 'Stand' in request.GET:
        #url = 'https://python-graph-gallery.com/wp-content/uploads/mtcars.csv'
        #df = pd.read_csv(url)
        #df = df.set_index('model')
        #del df.index.name
        #data = sns.clustermap(df)
    #print(1)

    # Standardize or Normalize every column in the figure
    # Standardize:
    #sns.clustermap(df, standard_scale=1)
    # Normalize
    #sns.clustermap(df, z_score=1)

    #return render(request, 'list/search.html')