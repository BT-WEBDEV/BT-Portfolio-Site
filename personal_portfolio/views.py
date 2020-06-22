from django.shortcuts import render

def home_view (request): 
    return render(request, "index.html")

def experience_view (request): 
    return render(request, "experience.html")

def skills_view (request): 
    return render(request, "skills.html")

def education_view (request): 
    return render(request, "education.html")

def interests_view (request): 
    return render(request, "interests.html")
