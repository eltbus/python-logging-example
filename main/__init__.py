import contextlib
import logging
import logging.config
import pathlib
from typing import Annotated

from fastapi import FastAPI, Depends
import yaml

from .helpers.context import Context, ctx_context
from .led import leave_babe


logger = logging.getLogger(__name__)


def load_logger_config(filepath: pathlib.Path):
    with filepath.open("r") as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    load_logger_config(filepath=pathlib.Path(__file__).parent.parent / "logging_config.yaml")
    logger.debug("Applied logging configuration")
    yield


app = FastAPI(lifespan=lifespan)


def get_user():
    return "foo"


@app.get("/")
async def get_root(user: Annotated[str, Depends(get_user)]):
    ctx_context.set(Context(user=user))
    logger.debug(msg="get_root was called!")
    return leave_babe()
