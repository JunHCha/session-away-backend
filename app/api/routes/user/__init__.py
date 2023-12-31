from fastapi import APIRouter

from app.api.schemas import UserRead, UserUpdate
from app.core.auth.backend import auth_backend, fastapi_users_component

app_router = APIRouter()


app_router.include_router(
    fastapi_users_component.get_oauth_router(
        auth_backend.google_oauth_client,
        auth_backend.auth_backend,
        state_secret="SECRET",  # TODO: 정확한 사용법을 확인 후 수정
        associate_by_email=True,
    ),
    prefix="/oauth/google",
)
app_router.include_router(fastapi_users_component.get_reset_password_router())
app_router.include_router(
    fastapi_users_component.get_users_router(
        user_schema=UserRead, user_update_schema=UserUpdate
    )
)
