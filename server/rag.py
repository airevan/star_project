import langchain
from engine import CHAIN


def query_graph(query: str):

    return CHAIN.invoke({"query": query})
