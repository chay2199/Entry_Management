# Entry Manager
This is an application which can capture the Name, email address, phone no of the visitor and
the same information for the host on the front end.
At the back end, once the user enters the information in the form, the backend stores all of
the information with time stamp of the entry.
This triggers an email and an SMS to the host informing him of the details of the visitor.
There is a provision of the checkout time which the guest can provide once he
leaves. This also triggers an email to the guest with the complete form which includes:

1. Name
2. Phone
3. Check-in time,
4. Check-out time,
5. Host name
6. Address visited.

Note: This application is just a prototype. It doesn't actually send the sms and emails(the actual service is expensive), 
it just shows them on the console. You can use apps like TWILIO and EmailGun etc to actually send sms and emails. Infact a
few lines of SMS code using TWILIO is commented out just for a reference.

# Installation
This is a django application. To install and run the app, follow the steps given below:
1. `pip install django` (install django-version > 2)
2. `cd entry_management`
3. `python manage.py runserver`
4. Open 127.0.0.1:8000 on your web-browser.

# Approach
1) First the visitor has to signup or login.
2) He can then checkin at the portal, as soon as he checks in the timestamp is noted.
3) The user has to fill a form with his/her details and the of the host he/she wants to visit. After which the details of 
   the vistior is send to the host using an email/sms. (Please check console/terminal at this stage)
4) The portal keeps on showing a checkout button. Once the visitor checks out. He is emailed the details of his visit. (Again check console/terminal)

## Sample Image

![Example_Image](https://raw.githubusercontent.com/chay2199/Entry_Management/master/Screenshot%20from%202019-11-24%2006-32-40.png)
