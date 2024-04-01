import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.security import OAuth2PasswordRequestForm
from jwt import DecodeError

from src.api.dependencies import user_service
from src.helper_functions.auth_handler import get_current_user, bcrypt_context, create_access_token, \
    create_refresh_token, decode_token
from src.schemas.user import RefreshInput, UserCreate, UserRegistration
from src.services.user import UserService

from sqlalchemy.exc import IntegrityError

auth_router = APIRouter(prefix="/v1/auth", tags=["auth"])



@auth_router.post(
    "/signup/",
    status_code=201,
    summary="Регистрация пользователя.",
)
async def add_user(
        user: UserRegistration,
        users_service: Annotated[UserService, Depends(user_service)],
):
    try:
        if user.password == user.confirm_password:
            user = UserCreate(
                username=user.username,
                password=user.password,
            )
            user_id = await users_service.create_entity(user)
            return user_id
        else:
            raise HTTPException(status_code=400, detail="Пароли не совпадают")
    except IntegrityError as e:
        if "duplicate key value" in str(e):
            raise HTTPException(status_code=400, detail="Пользователь с таким email уже существует")
        if "Key (role_id)=(1) is not present in table" in str(e):
            raise HTTPException(status_code=400, detail="Роль 1 не существует")
        elif "Key (role_id)=(2) is not present in table" in str(e):
            raise HTTPException(status_code=400, detail="Роль 2 не существует")
        else:
            raise HTTPException(status_code=400, detail="Неверные данные")



@auth_router.post(
    "/login/",
    status_code=200,
    summary="Вход в систему. можно использовать email",
)
async def login(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        users_service: Annotated[UserService, Depends(user_service)],
):
    try:
        user = await users_service.get_entity(username=form_data.username.lower())

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if not bcrypt_context.verify(form_data.password, user.hashed_password):
            raise HTTPException(status_code=404, detail="Неправильный пароль")
        print('bbb\n\n\n\n')
        data = {'id': user.id, 'role_id': user.role_id}

        try:
            token = create_access_token(data=data)
            refresh_token = create_refresh_token(data=data)
        except Exception as token_creation_error:
            # token creation error
            raise HTTPException(status_code=500, detail=f"Token creation error: {str(token_creation_error)}")
        return {'access_token': token, 'token_type': 'bearer', 'refresh_token': refresh_token}

    except HTTPException as e:
        # FastAPI error
        print(e)
        raise e

    except IntegrityError:
        # Database error
        raise HTTPException(status_code=500, detail="Internal Server Error")

    except Exception as e:
        # Other errors
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@auth_router.post(
    "/refresh/",
    status_code=200,
    summary="Обновление access token.",
)
async def refresh_token_router(
        request: RefreshInput = Body(...),
):
    try:
        refresh_token = request.refresh_token
        payload = decode_token(refresh_token)
        if not payload:
            raise HTTPException(status_code=400, detail="Invalid refresh token")

        current_time = datetime.datetime.utcnow()
        token_expiration = datetime.datetime.fromtimestamp(payload["exp"])
        if current_time > token_expiration:
            raise HTTPException(status_code=401, detail="Refresh token has expired")
        try:
            id: int = payload.get('id')
            role_id: int = payload.get('role_id')
            new_access_token_payload = {'id': id, 'role_id': role_id}
        except Exception as e:
            # Can't parse payload
            print(f"Unexpected error: {e}")
            raise HTTPException(status_code=500, detail="Can't parse payload")

        access_token = create_access_token(data=new_access_token_payload)

        return {"access_token": access_token, "token_type": "bearer"}
    except DecodeError:
        raise HTTPException(status_code=400, detail="Invalid token")




@auth_router.post(
    "/current-user/",
    status_code=200,
    summary="Возвращает пользователя.",
    description="Возвращает пользователя.",
)
async def get_user(
        user: Annotated[dict, Depends(get_current_user)],
):
    try:
        return user
    except HTTPException:
        raise HTTPException(status_code=401, detail="Invalid token")

