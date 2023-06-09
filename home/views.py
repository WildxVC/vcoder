from django.shortcuts import render,reverse
from .models import Contact
from blog.models import Post,BlogComment
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User



# Create your views here.
def home(request):
    newpost = Post.objects.order_by("timestamp").last()
    secondpost= Post.objects.order_by("-timestamp")[1]
    thirdpost =Post.objects.order_by("-timestamp")[2]
    context={'newpost': newpost,'secondpost':secondpost,'thirdpost':thirdpost}
    return render(request,"home/home.html",context)

def about(request):
    return render(request,"home/about.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']

        if len(name)<2 or len(email)<4 or len(phone)<10 or len(desc)<3:
            messages.error(request, 'Please fill the form correctly')
        else:      
            contact = Contact(name= name , email=email,phone= phone,desc=desc)
            contact.save()
            messages.success(request, 'Your form has been successfully filled.')
    return render(request,"home/contact.html")    

def search(request):
    query= request.GET['query']
    if len(query)>50 or len(query)<1:
        allPost= Post.objects.none()
    else:
        allPostTitle = Post.objects.filter(title__icontains=query)
        allPostContent = Post.objects.filter(content__icontains=query)
        allPost = allPostTitle.union(allPostContent)
    context = {'allpost': allPost, 'query':query}
    if allPost.count()==0:
        messages.warning(request, 'No search results found ! Please refine your query.')

    return render(request,'home/search.html',context)

def login_view(request):
    
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            messages.success(request,'You have been successfully logged in !')
            # return HttpResponseRedirect(reverse("home"))
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
        # Otherwise, return login page again with new context
        else:
            messages.error(request, 'Invalid credentials. Please try again !')
            return render(request, "home/login.html")

    else:
        return render(request,"home/login.html")  

def signup(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]
        password = request.POST["confirm"]
        email= request.POST["email"]
        first= request.POST["first"]
        last= request.POST["last"]
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already exists! Try a different username.')
            return render(request, 'home/signup.html')
        else:    
            user = User.objects.create_user(username,email, password)
            user.first_name = first
            user.last_name = last
            user.save()
            messages.success(request,'Your account has been successfully created !')
            # return render(request, 'home/home.html')
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        return render(request,"home/signup.html")

def logout_view(request):
    
    logout(request)
    messages.success(request,'You have been logged out !')
    # return render(request, "home/login.html")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))    