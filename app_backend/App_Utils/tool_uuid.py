import uuid

class UuidGenerator:
    def generate_id(self):
        u1 = str(uuid.uuid4())
        return u1

UID : UuidGenerator = UuidGenerator()
print(UID.generate_id())