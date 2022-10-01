from payment_channels.manager import Manager


class ExternalIntegrationServices:

    def get_payment_gateway(self, code):
        return Manager().get_manager(code=code)