from django.shortcuts import render
from .models import Post

Months = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November', 12:'December'}

def newsMain(request, year, month):
    #User.objects.all().order_by(
    posts = []
    archives = []
    archivesDate = []

    for n in Post.objects.all().order_by('-date_posted'):


        if (Months[n.date_posted.month] + ' ' + str(n.date_posted.year)) not in archivesDate:
            archivesDate += [Months[n.date_posted.month] + ' ' + str(n.date_posted.year)]
            archives += [{
                            'Date':Months[n.date_posted.month] + ' ' + str(n.date_posted.year),
                            'Y':n.date_posted.year,
                            'M':n.date_posted.month
                        }]

        if str(n.date_posted.year) == year or len(year) == 0:
            if str(n.date_posted.month) == month or len(month) == 0:
                paragraphs = n.content.splitlines()
                post = {
                    'title': n.title,
                    'author': n.author,
                    'date_posted': n.date_posted,
                    'content': paragraphs
                }
                posts += [post]


    context = {
        'newsActive' : True,
        'posts' : posts,
        'archives' : archives
    }
    return render(request, 'Main/news.html',context)
