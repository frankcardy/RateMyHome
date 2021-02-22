from django.shortcuts import get_object_or_404, render
from .models import Review, Home

# Create your views here.
#Gets a list of the latest 9 reviews and renders it using 'reviews/list.html'
def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)

#Gets a review given its ID and renders it using 'review_detail.html'
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review} )


#Gets all the homes sorted by name and passes it to home_list.html to be rendered
def home_list(request):
    home_list = Homes.objects.order_by('-name')
    context = {'home_list':home_list}
    return render(request, 'reviews/home_list.html', context)


#Gets a home from the DB given its ID and renders it using home_detail.html
def home_detail(request, home_id):
    home = get_object_or_404(Home, pk=home_id)
    return render(request, 'reviews/home_detail.html', {'home': home})
