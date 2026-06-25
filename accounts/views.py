from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Profile
from .profile_forms import ProfileForm
from marketplace.models import Product, Review
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from marketplace.recommendation import get_home_recommendations

def welcome(request):
    return render(request, "welcome.html")


from django.contrib.auth.models import User

def signup(request):

    error = None

    if request.method == "POST":

        form = SignupForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']

            if User.objects.filter(username=email).exists():

                error = "Email already registered."

            else:

                user = User.objects.create_user(
                    username=email,
                    email=email,
                    first_name=form.cleaned_data['first_name'],
                    password=form.cleaned_data['password']
                )

                Profile.objects.create(
                    user=user
                )

                return redirect('/login/')

    else:

        form = SignupForm()

    return render(
        request,
        "signup.html",
        {
            "form": form,
            "error": error
        }
    )

def login_view(request):

    error = None

    if request.method == "POST":

        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        if not email or not password:

            error = "Please enter both email and password."

        else:

            user = authenticate(
                request,
                username=email,
                password=password
            )

            if user is not None:

                login(request, user)

                return redirect('/home/')

            else:

                error = "Invalid email or password."

    return render(
        request,
        "login.html",
        {
            "error": error
        }
    )


def home(request):

    search = request.GET.get('search')
    category = request.GET.get('category')

    products = Product.objects.filter(
        is_sold=False
    ).exclude(
        seller=request.user
    )

    if search:

        products = products.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search)
        )

    if category:

        products = products.filter(
            category=category
        )

    recommended_products = get_home_recommendations(
        request.user
    )

    return render(
        request,
        'home.html',
        {
            'products': products,
            'recommended_products': recommended_products
        }
    )

def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def profile_setup(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect('/home/')

    else:
        form = ProfileForm(instance=profile)

    return render(
        request,
        "profile_setup.html",
        {"form": form}
    )


def seller_profile(request, user_id):

    seller = get_object_or_404(
        User,
        id=user_id
    )

    products = Product.objects.filter(
        seller=seller,
        is_sold=False
    )

    reviews = Review.objects.filter(
        seller=seller
    )

    total_rating = 0

    for review in reviews:
        total_rating += review.rating

    average_rating = 0

    if reviews.count() > 0:
        average_rating = round(
            total_rating / reviews.count(),
            1
        )

    return render(
        request,
        'seller_profile.html',
        {
            'seller': seller,
            'products': products,
            'reviews': reviews,
            'average_rating': average_rating
        }
    )


@login_required
def edit_profile(request):

    profile = request.user.profile

    if request.method == "POST":

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():

            form.save()

            return redirect('/my-profile/')

    else:

        form = ProfileForm(
            instance=profile
        )

    return render(
        request,
        "edit_profile.html",
        {
            "form": form
        }
    )

from django.contrib.auth.decorators import login_required

@login_required
def my_profile(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    return render(
        request,
        'my_profile.html',
        {
            'profile': profile
        }
    )