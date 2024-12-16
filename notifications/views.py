from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import send_sms

class SendSMSView(APIView):
    def post(self, request):
        recipient = request.data.get('recipient')
        message = request.data.get('message')

        if recipient and message:
            send_sms.delay(recipient, message)
            return Response({'status': 'SMS is being sent'}, status=200)
        else:
            return Response({'error': 'Recipient and message are required'}, status=400)
