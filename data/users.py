from dataclasses import dataclass
from config.settings import settings

@dataclass(frozen=True)
class UserCredentials:
    email: str
    password: str
    tenant_slug: str

# Centralized credentials mapping to backend seed user data
DEMO_USER = UserCredentials(
    email=settings.ADMIN_EMAIL,
    password=settings.ADMIN_PASSWORD,
    tenant_slug="demo"
)
