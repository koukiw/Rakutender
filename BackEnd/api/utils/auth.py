from datetime import datetime, timedelta
import hashlib
import secrets
from uuid import UUID
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer
from jose import jwt
from models.user import User
from utils.db import session
import env

security = OAuth2PasswordBearer(tokenUrl="login")


def get_digest(password):
    salt_password = bytes(env.API_SALT + password, "utf-8")
    digest = hashlib.sha256(salt_password).hexdigest()
    for _ in range(10):
        digest = hashlib.sha256(bytes(digest, "utf-8")).hexdigest()
    return digest


def authenticate(username, password):
    user = User.query.filter(User.username == username).first()
    correct_password = secrets.compare_digest(get_digest(password), user.digest)
    if not (correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user


def create_tokens(user_id: str):
    access_payload = {
        "token_type": "access_token",
        "exp": datetime.utcnow() + timedelta(minutes=60),
        "user_id": user_id,
    }
    refresh_payload = {
        "token_type": "refresh_token",
        "exp": datetime.utcnow() + timedelta(days=90),
        "user_id": user_id,
    }

    access_token = jwt.encode(access_payload, env.API_SECRET_KEY, algorithm="HS256")
    refresh_token = jwt.encode(refresh_payload, env.API_SECRET_KEY, algorithm="HS256")

    user = User.query.filter(User.id == user_id).first()
    try:
        user.refresh_token = refresh_token
        session.commit()

    except:
        session.rollback()
        return {
            "access_token": "",
            "refresh_token": "",
            "token_type": "bearer",
        }

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


def get_current_user_from_token(token: str, token_type: str):
    payload = jwt.decode(token, env.API_SECRET_KEY, algorithms=["HS256"])

    if payload["token_type"] != token_type:
        raise HTTPException(status_code=403)

    user = User.query.filter(User.id == payload["user_id"]).first()

    if token_type == "refresh_token" and user.refresh_token != token:
        raise HTTPException(status_code=403)

    return user


async def get_current_user(token: str = Depends(security)):
    try:
        user = get_current_user_from_token(token, "access_token")
        return user
    except:
        raise HTTPException(status_code=403)


async def get_current_user_with_refresh_token(token: str = Depends(security)):
    try:
        user = get_current_user_from_token(token, "refresh_token")
        return user
    except:
        raise HTTPException(status_code=403)
