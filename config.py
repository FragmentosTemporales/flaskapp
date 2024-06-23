from pydantic_settings import BaseSettings

class Setting(BaseSettings):

    flask_env : str

    jwt_secret_key : str
    jwt_access_token_expires_hours : int
    jwt_access_token_expires_days : int
    secret_key : str

    postgres_user : str
    postgres_password : str
    postgres_db : str
    postgres_host : str
    postgres_port : str

    class Config:
        env_file='.env'

settings = Setting() 