import uuid

class UuidGenerator:
    def generate_id(self):
        u1 = str(uuid.uuid4())
        return u1

# UID : UuidGenerator = UuidGenerator()
# print(UID.generate_id())

# {'close_by': None, 'close_reason': None, 'closed_at': None, 'created_at': 1773416728, 'customer_id': None, 'description': 'sample', 'entity': 'qr_code', 'fixed_amount': False, 'id': 'qr_SQlRDZoVmnVKG6', 'image_content': 'upi://pay?cu=INR&mc=5817&mode=19&pa=nexiopayopcpriv128573.rzp@rxairtel&tn=PaymentToNEXIOPAYOPCPRIVATELIMITED&tr=SQlRDZoVmnVKG6qrv2', 'image_url': 'https://rzp.io/rzp/ABmzfFj', 'name': None, 'notes': [], 'payment_amount': None, 'payments_amount_received': 9100, 'payments_count_received': 64, 'status': 'active', 'tax_invoice': [], 'type': 'upi_qr', 'usage': 'multiple_use'}