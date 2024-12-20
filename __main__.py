from os import (
    sep,
    environ,
)
from typing import Type, Tuple
from dotenv import load_dotenv

from pydantic import BaseModel
from pydantic_settings import (
    SettingsConfigDict,
    BaseSettings,
    PydanticBaseSettingsSource,
)

DOT_ENV_FILE_NAME = environ.get("DOT_ENV_FILE_NAME", None)
if DOT_ENV_FILE_NAME:
    env_file_path = "." + sep + DOT_ENV_FILE_NAME
    load_dotenv(  # Sometimes python caches the .env, especially in vscode
    dotenv_path = env_file_path,
    override=True,
)
else:
    env_file_path = None

class SubModel(BaseModel):
    FOO: str = "foo from initial value"
    BAR: int = 1

print(f".env file path is:\n{env_file_path}")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=env_file_path,
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        env_ignore_empty=True,
        env_parse_none_str="none",
        env_parse_enums=True,
        extra="ignore",
        load_dotenv=True,
        override=True,
    )
    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return (init_settings, dotenv_settings, env_settings, file_secret_settings)


    ORIGIN: str = "From Initial Value"
    OTHER_SETTING: SubModel = SubModel()


print(f"Loaded config:\n {Settings().model_dump()}" )
