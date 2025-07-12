from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    bot_token: SecretStr = Field(..., env="BOT_TOKEN")
    # creator: SecretStr = Field(..., env="CREATOR_ID")

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

config = Settings()