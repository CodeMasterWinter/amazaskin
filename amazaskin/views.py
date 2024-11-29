from django.shortcuts import render


# Create your views here.
def shop(request):

    context = {
        'page_title': "Shop the Range",
    }

    return render(request, 'shop.html', context)