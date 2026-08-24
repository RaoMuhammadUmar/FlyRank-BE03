from fastapi import APIRouter, Depends, HTTPException
from app.models import AuthRequest
from app.supabase_client import supabase
from app.dependencies import get_current_user


router = APIRouter()


# -------------------------
# SIGNUP
# -------------------------

@router.post("/auth/signup", status_code=201)
def signup(request: AuthRequest):

    if not request.email or not request.password:
        raise HTTPException(
            status_code=400,
            detail="Email and password are required"
        )

    try:
        response = supabase.auth.sign_up({
            "email": request.email,
            "password": request.password
        })

        return {
            "message": "User created successfully",
            "user": response.user
        }

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Unable to create user"
        )


# -------------------------
# LOGIN
# -------------------------

@router.post("/auth/login")
def login(request: AuthRequest):

    if not request.email or not request.password:
        raise HTTPException(
            status_code=400,
            detail="Email and password are required"
        )

    try:
        response = supabase.auth.sign_in_with_password({
            "email": request.email,
            "password": request.password
        })

        return {
            "message": "Login successful",
            "access_token": response.session.access_token,
            "refresh_token": response.session.refresh_token
        }

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid login credentials"
        )


# -------------------------
# LOGOUT
# PROTECTED
# -------------------------

@router.post(
    "/auth/logout",
    status_code=204,
    dependencies=[Depends(get_current_user)]
)
def logout():

    try:
        supabase.auth.sign_out()

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Unable to logout"
        )

    return None


# -------------------------
# PUBLIC ROUTE
# -------------------------

@router.get("/public/info")
def public_info():

    return {
        "message": "Welcome stranger! This info is public."
    }


# -------------------------
# PROTECTED PROFILE
# -------------------------

@router.get("/protected/profile")
def protected_profile(
    current_user=Depends(get_current_user)
):

    return {
        "message": "Access granted",
        "user": {
            "id": current_user.id,
            "email": current_user.email,
            "created_at": current_user.created_at
        }
    }


# -------------------------
# PROTECTED DASHBOARD
# STAGE 4 CHECKPOINT
# -------------------------

@router.get("/protected/dashboard")
def protected_dashboard(
    current_user=Depends(get_current_user)
):

    return {
        "message": "Welcome to your protected dashboard",
        "user_id": current_user.id
    }