from django.apps import AppConfig

# здесь формируеся конфигурация приложения. Например, под обработчики событий
class NewsPortalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news_portal'
    def ready(self): # это переопределенный метод
        import news_portal.signals
