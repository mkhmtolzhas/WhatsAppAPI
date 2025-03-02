from fastapi import HTTPException

class GlobalException:
    class BadRequest(HTTPException):
        def __init__(self):
            super().__init__(status_code=400, detail="Bad Request")
        
    class NotFound(HTTPException):
        def __init__(self):
            super().__init__(status_code=404, detail="Not Found")
    
    class InternalServerError(HTTPException):
        def __init__(self):
            super().__init__(status_code=500, detail="Internal Server Error")
    
    class Forbidden(HTTPException):
        def __init__(self):
            super().__init__(status_code=403, detail="Forbidden")