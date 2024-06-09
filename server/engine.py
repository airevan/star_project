import os
from langchain_community.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain
from langchain_openai import ChatOpenAI

os.environ["NEO4J_URI"] = "bolt://localhost:7687"
os.environ["NEO4J_USERNAME"] = "neo4j"
os.environ["NEO4J_PASSWORD"] = "Neo4j@123"


def get_query_chain():

    graph = Neo4jGraph()
    llm = ChatOpenAI(model="gpt-4", temperature=0)
    chain = GraphCypherQAChain.from_llm(
        graph=graph, llm=llm, verbose=True, validate_cypher=True
    )
    return chain


CHAIN = get_query_chain()
