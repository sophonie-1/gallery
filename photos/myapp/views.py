from django.shortcuts import render,redirect
from .models import PhotoModel,Category
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def register_view(request, *args, **kwargs):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('gallery')
    return render(request,'myapp/register_view.html',{'form': form})

def login_view(request, *args, **kwargs):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('gallery')
        else:
            form=LoginForm()
    return render(request,'myapp/login_view.html',{'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def gallery(request):
    categories = Category.objects.all()
    context={
        'categories': categories,
        'photos': PhotoModel.objects.all(),
    }

    return render(request, 'myapp/gallery.html',context)
@login_required(login_url='/login')
def viewphoto(request,pk):
    photo = PhotoModel.objects.get(id=pk)
    print(photo)
    context = {
        'photo': photo,
    }
    return render(request, 'myapp/viewphoto.html', context)

@login_required(login_url='/login')
def addphoto(request):
    categories=Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        description = data.get('description')
        image= request.FILES.get('image')
        print(data["category"])
        if data["category"] != 'none':
            category = Category.objects.get(id=data["category"])
        elif data['create-category'] != '':
            category,created = Category.objects.get_or_create(name=data['create-category'])
        else:
            category = None
        photo=PhotoModel.objects.create(
            description=description,
            image=image,
            category=category,
        )
        return redirect('gallery')

    return render(request, 'myapp/addphoto.html',{'categories':categories})
@login_required(login_url='login')
def list_photo_with_associated_category(request,pk):
    category=Category.objects.get(id=pk)
    photos=PhotoModel.objects.filter(category=category)
    return render(request,'myapp/list_photo.html',{'photos':photos})

@login_required(login_url='login')
def abantu(request):
    user=User.objects.all()
    return render(request,'myapp/abantu.html',{'user':user})