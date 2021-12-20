import math

import stripe
from rest_framework import mixins, status
from rest_framework.exceptions import NotAcceptable
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from stripe.error import StripeError

from .models import Ticket
from .serializers import TicketSerializer

stripe.api_key = "sk_test_8mXwGKRC39YbDsfVnWu6g1lo"


class TicketViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Ticket.objects.all()

    def create(self, request, *args, **kwargs):
        # TODO: Get event and ticket type to get the price
        print("Perform payment...")

        # Use an existing Customer ID if this is a returning customer
        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=1295,
                currency="eur",
                payment_method_types=["card"],
                application_fee_amount=math.ceil(1295 * 0.05),
                stripe_account="acct_1Ju0YsLpaIwDq3NC",
            )
            response = {
                "clientSecret": payment_intent.client_secret,
                "publishableKey": "pk_test_u3ZcmfHqRT2i7Nn4LwX52y0l",
            }
            print("Send confirmation email...")

            return Response(data=response, status=status.HTTP_200_OK)

        except Exception as e:
            print("Exception: ", e)
            raise NotAcceptable()
