from fastapi import Header, HTTPException
from app.supabase_client import supabase


def get_current_user(
    authorization: str = Header(None)
):
    # Check whether Authorization header exists
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Access token required"
        )

    # Check Bearer format
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Access token required"
        )

    # Extract token
    token = authorization[7:].strip()

    # Make sure token is not empty
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Access token required"
        )

    # Ask Supabase to verify the token
    try:
        response = supabase.auth.get_user(token)

        if not response.user:
            raise HTTPException(
                status_code=401,
                detail="Invalid or expired token"
            )

        return response.user

    except HTTPException:
        raise
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.supabase_client import supabase


security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Access token required"
        )

    try:
        response = supabase.auth.get_user(token)

        if not response.user:
            raise HTTPException(
                status_code=401,
                detail="Invalid or expired token"
            )

        return response.user

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )