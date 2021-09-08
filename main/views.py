from .models import WishList
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {'title': "Wishlist | about project"})

def list_page(request, pk):
    # wishlist = WishList.objects.get(pk=pk)
    wishlist = get_object_or_404(WishList, pk=pk)
    return render(
        request, 'wish_list.html', 
        {
            'title': "Wishlist | wishlist", 
            'list': wishlist,
            'is_owner_list': wishlist.owner == request.user
            }
            )
