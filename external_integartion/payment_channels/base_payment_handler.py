from abc import ABC, abstractmethod

from external_integartion.payment_channels.api_client import APIClient


class BasePaymentHandler(ABC):
    class PaymentGatewayA(APIClient):

        @abstractmethod
        def prepare_payload(self, request_payload):
            pass

        @abstractmethod
        def process_payment(self, request):
            pass