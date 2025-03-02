from fastapi import HTTPException

class WhatsAppException:
    class InvalidPhoneNumber(HTTPException):
        def __init__(self):
            super().__init__(status_code=400, detail="Invalid phone number")

    class InvalidMessage(HTTPException):
        def __init__(self):
            super().__init__(status_code=400, detail="Invalid message")
    
    class InvalidAudio(HTTPException):
        def __init__(self):
            super().__init__(status_code=400, detail="Invalid audio")

