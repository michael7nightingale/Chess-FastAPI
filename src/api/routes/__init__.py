from .auth import auth_router
from .socks import router

__routes__ = (router, auth_router)
