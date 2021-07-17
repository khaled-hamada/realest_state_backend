from rest_framework import permissions
from rest_framework.views import APIView
from .models import Contact
from django.core.mail import send_mail
from rest_framework.response import Response



class ContactCreateView(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request , format = None):
        data = self.request.data

        try :
            send_mail(
                data['subject'], ## 1. subject
                "Name: "            ## 2. message or body
                +data['name']
                +"\nEmail: "
                +data['email']
                 + '\n\nMessage:\n'
                + data['message'],
                 data['email'],  # 3. sender
                ['enter your email here '], ##4. reciever
                fail_silently=False

            ) 
            contact = Contact(name=data['name'], email=data['email'],
                              subject=data['subject'], message=data['message'])
            contact.save()

            return Response({'success': 'Message sent successfully'})

        except Exception as ex:
            print(ex)
            return Response({"error : failed to send email"},status = 500 )
