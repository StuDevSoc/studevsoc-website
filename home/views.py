from django.shortcuts import render, redirect
from django.views import generic
from blog.models import Post
from .models import Jumbotron, Project, Contact
from blog.models import Post
from django.utils import timezone
from .forms import ContactForm
from django.contrib import messages
# Home Page for SDS
def homeviews(request):
    posts = Jumbotron.objects.filter(status=1).order_by('-updated_on')
    features = Post.objects.filter(feature=1, status=1).order_by('-updated_on')
    projects = Project.objects.filter().order_by('-updated_on')
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            connect = form.save(commit=False)
            connect.sds_response = 0
            connect.date = timezone.now()
            connect.save()
            messages.success(request, 'Submited successfully')
            return redirect('home')
        else:
            messages.error(request,'Invalid Data<br>Please Input valid data , Check all the fields one more time')
    else:
        form = ContactForm()
    context = {'posts': posts,'features':features,'projects':projects,'form':form}
    return render(request, 'home.html', context)
