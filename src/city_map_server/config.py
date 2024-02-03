from decouple import config


class AppConfig:
    db_user = config("DB_USER", default="dbuser")
    db_password = config("DB_PASSWORD", default="1234")
    db_database = config("DB_DATABASE", default="city_map")
    db_host = config("DB_HOST", default="localhost")
    db_port = config("DB_PORT", default="5432")

    @property
    def get_database_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@" \
               f"{self.db_host}:{self.db_port}/{self.db_database}"

    @property
    def get_sync_database_url(self):
        return f"postgresql+psycopg2://{self.db_user}:{self.db_password}@" \
               f"{self.db_host}:{self.db_port}/{self.db_database}"


app_config = AppConfig()
