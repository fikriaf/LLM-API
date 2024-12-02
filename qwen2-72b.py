from gradio_client import Client, file
import time

client = Client("Qwen/Qwen2-72B-Instruct", max_workers=128000)

hist = []

while True:
    tny = input("you: ")
    result = client.predict(
        query=tny,
        history=hist,
        system="You are a helpful assistant.",
        api_name="/model_chat",
    )

    # Update history
    hist.extend(result[1])

    # Get the last response
    last_response = result[1][-1][1]

    # Display the response per token (character in this case)
    for char in last_response:
        print(char, end='', flush=True)
        time.sleep(0.001)  # Sleep to mimic streaming effect

    print()  # New line after the response is complete
