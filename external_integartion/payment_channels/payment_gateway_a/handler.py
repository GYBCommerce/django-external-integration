from abc import abstractmethod

from external_integartion.payment_channels.api_client import APIClient
from external_integartion.payment_channels.base_payment_handler import BasePaymentHandler


class PaymentGatewayA(BasePaymentHandler, APIClient):

    def prepare_payload(self, request_payload):
        pass

    def process_payment(self, request) -> bool:
        # Here you have to find the way to integrate Payment gateway A
        return True