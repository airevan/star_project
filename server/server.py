import logging.config
from fastapi import FastAPI
import uvicorn
import logging
import sys
from logging import StreamHandler, FileHandler
from models import ChatBody
from rag import query_graph

logging.basicConfig(
    handlers=[
        StreamHandler(stream=sys.stdout),
        FileHandler("server.log", mode="a", encoding="utf-8"),
    ],
    level="DEBUG",
    format="%(asctime)s.%(msecs)03d [%(levelname)s] %(name) +25s - %(message)s",
    datefmt="%H:%M:%S",
)

logger = logging.getLogger(__name__)


app = FastAPI()


@app.get("/")
def root():
    return {"status": "server is running"}


@app.post("/chat")
def chat_func(body: ChatBody):
    all_messages = body.messages
    user_query = all_messages[0].content
    response = query_graph(user_query)
    print(response)
    return response


uvicorn.run(app, host="127.0.0.1", port=4242)
