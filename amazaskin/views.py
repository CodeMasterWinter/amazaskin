from django.shortcuts import render


def landing(request):

    context = {
        'page_title': 'Skin Revitalized'
    }

    return render(request, 'amazaskin/landing.html', context)

