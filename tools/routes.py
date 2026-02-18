from enum import Enum


base_url = "https://stellarburgers.education-services.ru"

class AppRoute(str, Enum):
    CONSTRUCTOR = base_url
    ORDER_FEED = f"{base_url}/feed"
    PERSONAL_ACCOUNT = f"{base_url}/account/profile"
    LOGIN = f"{base_url}/login"
    REGISTRATION = f"{base_url}/register"
    RECOVERY_PASSWORD = f"{base_url}/forgot-password"