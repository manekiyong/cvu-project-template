import os
import logging

from schema.document_schema import Document

# from elasticsearch import Elasticsearch

DB_HOST = os.environ.get("COMPONENT_A_DATABASE_HOST", "http://database:9200")
# DB_AUTH_USERNAME = os.environ.("ELASTIC_USERNAME", "username")
# DB_AUTH_PASSWORD = os.environ.("ELASTIC_PASSWORD", "password")

logging.basicConfig(level=logging.INFO)


class Database:
    def __init__(self) -> None:
        """
        Initialize database
        """
        # Example initalisation of ElasticSearch
        # self.db = Elasticsearch(
        #     DB_HOST,
        #     verify_certs=False,
        #     basic_auth=(DB_AUTH_USERNAME, DB_AUTH_PASSWORD),
        #     request_timeout=30,
        #     max_retries=10,
        #     retry_on_timeout=True,
        # )
        self.db = None

    def get_document(self, doc_id: str) -> Document:
        """
        Retrieve a document from database

        Args:
            doc_id: the unique identifier of the document

        Returns:
            Document: object with the title & the document's content
        """

        logging.info(f"Retrieved {doc_id} from Database")
        retrieved_document = Document(
            title="Title of Document", content="Content of Document"
        )
        return retrieved_document
