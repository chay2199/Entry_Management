from datetime import datetime
# For SMS using TWILIO
from twilio.rest import TwilioRestClient

from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect

from .forms import CheckInForm
from django.http import HttpResponse
from .models import CheckIn


def home(request):
    return render(request, 'home.html')


def checkin(request):
    form = CheckInForm(request.POST)
    if form.is_valid():
        now = datetime.now()
        check_in = now.strftime("%H:%M:%S")
        post = form.save(commit=False)
        post.checkTime = check_in
        post.save()
        host_email = form.cleaned_data['host_email']
        host_phone = form.cleaned_data['host_phone']
        visitor_name = form.cleaned_data['visitor_name']
        visitor_email = form.cleaned_data['visitor_email']
        visitor_phone = form.cleaned_data['visitor_phone']

        message = ("Visitor's CheckIn Details\nName: {}, Phone: {}, Email: {}, "
                   "CheckIn Time: {}").format(visitor_name, visitor_phone,
                                              visitor_email, check_in)
        subject = "Visitor's CheckIn Details"

        # For SMS using TWILIO
        # from_ = host_phone
        # to = host_phone
        # client = TwilioRestClient(
        #     settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        # client.messages.create(
        #     body=message, to=to, from_=from_)

        try:
            send_mail(subject, message, from_email=visitor_email,
                      recipient_list=[host_email], fail_silently=False,)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('check_out')
    return render(request, "details.html", {'form': form})


def success_view(request):
    return render(request, "check_out.html")


def checkout(request):
    now = datetime.now()
    outTime = now.strftime("%H:%M:%S")
    latest_details = CheckIn.objects.values_list()[len(CheckIn.objects.values_list())-1]
    visitor_name = latest_details[1]
    visitor_email = latest_details[2]
    visitor_phone = latest_details[3]
    host_name = latest_details[4]
    host_email = latest_details[4]
    checkTime = latest_details[7]
    address = "SummerGeeks"
    message = ("Visitor's CheckOut Details\nName: {}, Phone: {}, Email: {}, "
               "CheckIn Time: {}, CheckOut Time: {}\nHost's Name: {}, "
               "Address: {}").format(visitor_name, visitor_phone,
                                     visitor_email, checkTime, outTime,
                                     host_name, address)
    subject = "Visitor's CheckOut Details"
    try:
        send_mail(subject, message, from_email=host_email,
                  recipient_list=[visitor_email], fail_silently=False, )
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    return render(request, 'home.html')
