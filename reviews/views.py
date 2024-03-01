from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm

# Create your views here.

# def review(request):
#     return render(request, "reviews/review.html")

# Extract form data and show thank you page
# def review(request):
#     if request.method == 'POST':
#         entered_username = request.POST['username']
#         print(entered_username)
#         return HttpResponseRedirect("/thank-you")
    
#     return render(request, "reviews/review.html")

# Manual form validation
# def review(request):
#     if request.method == 'POST':
#         entered_username = request.POST['username']

#         if entered_username == "":
#             return render(request, "reviews/review.html", {
#                 "has_error": True
#             })
        
#         print(entered_username)
#         return HttpResponseRedirect("/thank-you")
    
#     return render(request, "reviews/review.html", {
#         "has_error": False
#     })


# Use the ReviewForm (django form)
# def review(request):
#     myform = ReviewForm()

#     return render(request, "reviews/review.html", {
#         "form": myform
#     })

# Add form validation logic
def review(request):
    myform = ReviewForm()

    if request.method == 'POST':
        myform = ReviewForm(request.POST)

        if myform.is_valid():
            print(myform.cleaned_data)
            return HttpResponseRedirect("/thank-you")
        
    return render(request, "reviews/review.html", {
        "form": myform
    })

    return render(request, "reviews/review.html", {
        "form": myform
    })





def thank_you(request):
    return render(request, "reviews/thank_you.html")