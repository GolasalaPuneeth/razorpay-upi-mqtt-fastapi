from abc import ABC, abstractmethod

class PaymentHook(ABC):
    @abstractmethod
    def process_payment(self, payment_data):
        pass