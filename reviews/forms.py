from django import forms

# Create our Django form

# class ReviewForm(forms.Form):
#     user_name = forms.CharField()

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=50)


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name", max_length=20,
#                                 error_messages={
#                                     "required": "The name cannot be empty",
#                                     "max_length": "Please enter a shorter name"
#                                 })


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your name", max_length=20,
                                error_messages={
                                    "required": "The name cannot be empty",
                                    "max_length": "Please enter a shorter name"
                                })
    review_text = forms.CharField(
        label="Your feedback", widget=forms.Textarea, max_length=100)
    rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)
