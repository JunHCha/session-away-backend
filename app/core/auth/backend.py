import uuid

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, CookieTransport
from httpx_oauth.clients.google import GoogleOAuth2

from app.core.config import get_app_settings
from app.db.tables import User
from app.depends.auth import get_database_strategy, get_user_manager

SETTINGS = get_app_settings()

cookie_transport = CookieTransport(cookie_max_age=SETTINGS.auth_session_expire_seconds)

auth_backend = AuthenticationBackend(
    name="database",
    transport=cookie_transport,
    get_strategy=get_database_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

google_oauth_client = GoogleOAuth2(
    SETTINGS.google_client_id, SETTINGS.google_client_secret
)