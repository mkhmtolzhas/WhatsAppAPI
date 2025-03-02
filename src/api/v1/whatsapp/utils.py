from re import fullmatch

class WhatsAppUtils:
    @staticmethod
    def is_valid_phone_number(phone_number: str) -> bool:
        return bool(fullmatch(r"^\+7\d{10}$", phone_number))
    
