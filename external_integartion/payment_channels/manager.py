from .payment_gateway_a.handler import PaymentGatewayA
from .payment_gateway_b.handler import PaymentGatewayB
from constants import PaymentGatewayEnum


class Manager:

    def __init__(self):
        self.default_gateway = PaymentGatewayA()
        self.manager_list = {
            PaymentGatewayEnum.PAYMENT_GATEWAY_A.value: PaymentGatewayA(),
            PaymentGatewayEnum.PAYMENT_GATEWAY_B.value: PaymentGatewayB()
        }

    def get_manager(self, code):
        return self.manager_list.get(code) if self.manager_list.get(code, None) else self.default_gateway