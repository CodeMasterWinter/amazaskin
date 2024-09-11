from django.shortcuts import render


def landing(request):

    context = {
        'page_title': 'Skin Revitalized'
    }

    return render(request, 'amazaskin/landing.html', context)


def about(request):

    context = {
        'page_title': 'Who We Are'
    }

    return render(request, 'amazaskin/about.html', context)
