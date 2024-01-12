from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponseForbidden

def review_list(request):
    reviews = Review.objects.all()
    for review in reviews:
        review.showtime = f"{int(review.showtime/60)}시간 {review.showtime%60}분"
    context = {
        "reviews" : reviews,
    }
    return render(request, 'review_list.html', context)

def review_detail(request, pk):
    # GET으로 접근시에, 없는 레코드에 접근시 404오류 반환
    review = get_object_or_404(Review, pk=pk)
    if review:
        review.showtime = f"{int(review.showtime/60)}시간 {review.showtime%60}분"
    context = {
        "review" : review
    }
    return render(request, 'review_detail.html', context)

def review_new(request):
    # Page에 처음 접속했을 때(get), 제출할 때(post)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    context = {
        "form" : form
    }
    return render(request, 'review_edit.html', context)

def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect('review_detail', pk=review.pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        "form" : form
    }
    return render(request, 'review_edit.html', context)

def review_delete(request, pk):
    if request.method != "POST":
        return HttpResponseForbidden()
    Review.objects.get(pk=pk).delete()
    return redirect("/")

def review_order(request, criteria):
    reviews = Review.objects.all().order_by(criteria)
    for review in reviews:
        review.showtime = f"{int(review.showtime/60)}시간 {review.showtime%60}분"
    context = {
        "reviews" : reviews,
    }
    return render(request, 'review_list.html', context)