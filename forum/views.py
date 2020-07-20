from django.shortcuts import render

# Create your views here.
def forumpage(request):
    return render(request, 'forum/index.html')