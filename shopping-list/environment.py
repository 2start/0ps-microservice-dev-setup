import logging
import sys
from pathlib import Path

from pydantic import BaseSettings, ValidationError

log = logging.getLogger(__name__)


class Environment(BaseSettings):
    project_path: Path = Path(__file__).parent.parent
    log_level: str = "DEBUG"

    shopping_list_port: int
    todo_host: str
    todo_port: int

    @property
    def todo_uri(self):
        return f"http://{self.todo_host}:{self.todo_port}"

    class Config:
        env_prefix = 'TOMUDO_'


try:
    env = Environment()
except ValidationError as e:
    log.error(e)
    sys.exit(-1)
