from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def contact_view(request): 
    name=""
    email=""
    comment=""

    form=ContactForm(request.POST or None)
    if form.is_valid(): 
        name=form.cleaned_data.get("name")
        email=form.cleaned_data.get("email")
        comment=form.cleaned_data.get("comment")
        
        subject = "A Visitor Left A Message"
        comment=name+" with the email, " + email + ", sent the following message:\n\n" + comment; 
        
        send_mail(subject,comment, 'brandontetrick@gmail.com', [email])

        context = {'form': form}

        return render(request,'contact.html', context) 
    
    else: 
        context = {'form': form}
        return render(request, 'contact.html', context)


