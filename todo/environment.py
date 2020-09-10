import logging
import sys
from pathlib import Path

from pydantic import BaseSettings, ValidationError

log = logging.getLogger(__name__)


class Environment(BaseSettings):
    project_path: Path = Path(__file__).parent.parent
    log_level: str = "DEBUG"

    todo_port: int

    db_protocol: str
    db_host: str
    db_port: str
    db_user: str
    db_pw: str
    db_name: str

    @property
    def db_uri(self) -> str:
        return f'{self.db_protocol}://{self.db_user}:{self.db_pw}@{self.db_host}:{self.db_port}/{self.db_name}'

    class Config:
        env_prefix = 'TOMUDO_'


try:
    env = Environment()
except ValidationError as e:
    log.error(e)
    sys.exit(-1)
