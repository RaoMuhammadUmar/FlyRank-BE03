from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.supabase_client import supabase


security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    token = credentials.credentials

    try:
        response = supabase.auth.get_user(token)

        if response.user is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid or expired access token"
            )

        return response.user

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired access token"
        )