import requests
import logging

logging.basicConfig(level=logging.INFO)

ENDPOINT = "http://localhost:8000"


def test1():
    try:
        response = requests.get(f"{ENDPOINT}/health")
        logging.info(f"Test 1 Response: {response}")
        logging.info("Test 1 Complete")
    except Exception as e:
        logging.error(f"Test 1 Failed: {e}")


def test2():
    try:
        query = "I have this query"
        response = requests.post(
            f"{ENDPOINT}/chat", json=[{"role": "user", "content": query}]
        )
        response_text = response.json()
        logging.info(f"Test 2 Response: {response_text}")
        logging.info("Test 2 Complete")
    except Exception as e:
        logging.error(f"Test 2 Failed: {e}")


def test3():
    try:
        response = requests.post(
            f"{ENDPOINT}/retrieve_document", json={"doc_id": "123"}
        )
        response_text = response.json()
        logging.info(f"Test 3 Response: {response_text}")
        logging.info("Test 3 Complete")
    except Exception as e:
        logging.error(f"Test 3 Failed: {e}")


if __name__ == "__main__":
    test1()
    test2()
    test3()
