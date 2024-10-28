from src.config.chain import chain_with_history

def run():
    print(chain_with_history.invoke({"input": "Hello"}, config={"configurable": {"session_id": "foo"}}))

if __name__ == "__main__":
    run()