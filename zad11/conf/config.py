from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    """A class that represents the configuration settings of an application.

    :param sqlalchemy_database_url: SQLAlchemy database URL.
    :param secret_key: The secret key used for encryption.
    :param algorithm: The algorithm used for encryption.
    :param mail_username: Your email username.
    :param mail_password: Email password.
    :param mail_from: The sender's email address.
    :param mail_port: Mail server port.
    :param mail_server: The address of the e-mail server.
    :param redis_host: Redis host (default 'localhost').
    :param redis_port: Port Redis (default 6379).
    :param postgres_db: The name of the PostgreSQL database.
    :param postgres_user: PostgreSQL username.
    :param postgres_password: Password for the PostgreSQL database.
    :param postgres_port: A port of PostgreSQL.
    :param cloudinary_name: The name of your Cloudinary account.
    :param cloudinary_api_key: Cloudinary's API key.
    :param cloudinary_api_secret: Cloudinary's API secret key."""
    sqlalchemy_database_url: str
    secret_key: str
    algorithm: str
    mail_username: str
    mail_password: str
    mail_from: str
    mail_port: int
    mail_server: str
    redis_host: str = 'localhost'
    redis_port: int = 6379
    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_port: int
    cloudinary_name: str
    cloudinary_api_key: str
    cloudinary_api_secret: str

    class Config:
        """Configuration to load settings from the '.env' file.

    :param env_file: The name of the environment file.
    :param env_file_encoding: Encoding of the environment file (default 'utf-8')."""
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()