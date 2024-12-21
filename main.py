import logging

import uvicorn
from fastapi import FastAPI

import api.user
import log
from config import CONF

log.init_logger()
app = FastAPI()

app.include_router(api.user.router)

if __name__ == '__main__':
    logging.debug("Starting server")
    port = int(CONF['server']['port'])
    uvicorn.run("main:app", host="0.0.0.0", port=port)
    logging.debug("Server stopped")
