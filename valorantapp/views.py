from django.shortcuts import render

from valorantapp.model import Blog, Characters, Weapons


# Create your views here.


def Menu(request):
    return render(request, "Exam.html")


def Info(request):
    return render(request, "exam2.html")


def gallery(request):
    return render(request, 'exam3.html')


def safety(request):
    return render(request, 'exam4.html')


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {
        'blogs': blogs

    })



def characters(request):
    characters = Characters.objects.all()
    return render(request, 'characters.html', {
        'characters': characters
    })


def weapons(request):
    weapons = Weapons.objects.all()
    return render(request, 'weapons.html', {
        'weapons': weapons
    })


def Weapons_1(request, id):
    weaponss = Weapons.objects.get(id=id)
    return render(request, 'Weapons_1.html', {
        'weaponss': weaponss
    })


def Characters_1(request, id):
    characterss = Characters.objects.get(id=id)
    return render(request, 'Characters_1.html', {
        'characterss': characterss
    })


def blog_1(request, id):
    blogs = Blog.objects.get(id=id)
    return render(request, 'blog_1.html', {
        'blog': blogs
    })