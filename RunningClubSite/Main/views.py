from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Main/home.html')


# Create your views here.
def about(request):
    return render(request, 'Main/about.html')


# Create your views here.
def news(request):
    return render(request, 'Main/news.html')


# Create your views here.
def records(request):
    return render(request, 'Main/records.html')
