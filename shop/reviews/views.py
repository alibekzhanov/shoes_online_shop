from django.shortcuts import render


def review_list(request):
    return render(request, 'reviews/review_list.html')


def review_detail(request, id):
    return render(request, 'reviews/review_detail.html', {'id': id})


def create_review(request):
    return render(request, 'reviews/create_review.html')
