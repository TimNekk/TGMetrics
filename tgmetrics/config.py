from dataclasses import dataclass

from environs import Env


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str
    port: int
    uri: str = ""

    def __post_init__(self) -> None:
        self.uri = f"postgresql://{self.user}:{self.password}" \
                   f"@{self.host}:{self.port}/{self.database}"


@dataclass
class Config:
    db: DbConfig


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME'),
            port=env.int('DB_PORT'),
        )
    )
