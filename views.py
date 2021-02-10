from django.shortcuts import render, redirect

def index(request):



    return render(request, 'belt_reviewer_app/index.html')

def login(request):

    return render(request, 'belt_reviewer_app/login.html')

def add(request):

    return render(request, 'belt_reviewer_app/add.html')

def review(request):

    return render(request, 'belt_reviewer_app/review.html')

def user(request):

    return render(request, 'belt_reviewer_app/user.html')

