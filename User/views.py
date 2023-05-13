from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from .models import Profile
from django.contrib.auth.models import User


# Create your views here.


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("/product")

    form = NewUserForm()
    context = {"form": form}
    return render(request, "users/register.html", context)

@login_required
def profile(request):
     return render(request, "users/profile.html")

def create_profile(request):
    if request.method == "POST":
        user = request.user
        img = request.FILES['upload']
        phonenumber = request.POST.get('phonenumber')
        profile = Profile(user=user, img=img, phonenumber=phonenumber)
        profile.save()
    return render(request, "users/create_profile.html")


def sellerprofile(request, id):
    seller = User.objects.get(id=id)
    context = {
        "seller":seller
    }
    return render(request, "users/sellerprofile.html", context)













































