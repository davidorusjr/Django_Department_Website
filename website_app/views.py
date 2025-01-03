from django.shortcuts import render
from django.core.mail import send_mail

# HOME PAGE
def index(request):
    return render(request, 'index.html', {})

# ABOUT US - OVERVIEW PAGE
def overview(request):
    return render(request, 'abt_us_overview.html', {})

# ABOUT US - PHILOSOPHY AND HISTORY PAGE
def philosophy(request):
    return render(request, 'abt_us_philosophy.html', {})

# ABOUT US - ADMISSION PAGE
def admission(request):
    return render(request, 'abt_us_admission.html', {})

def contact(request):
    if request.method == "POST":
        author = request.POST['author']
        email = request.POST['email']
        subject = request.POST['subject']
        comment = request.POST['comment']

        # SEND EMAIL FUNCTIONALITY
        send_mail(
            subject,  
            comment,
            email, 
            ['weirdolado@gmail.com'],  
            fail_silently=True
        )

        return render(request, 'contact.html', {'author': author, 'email': email, 'subject': subject, 'comment': comment})

    else:
        return render(request, 'contact.html', {})