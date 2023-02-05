from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from blog import tokens

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "login")

def get_current_user(data : str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = f"Unable to process the credentials",
        headers = {"WWW-Authenticae" : "Bearer"}
    )
    return tokens.verify_token(data, credentials_exception)
   