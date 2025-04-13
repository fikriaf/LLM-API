# LLM-API

Simple Python and Batch scripts to access various Large Language Models (LLMs) such as Qwen, LLaMA, and others via local APIs.

## 📁 File Structure

- `AI-110B.bat`  
  Batch script to run the Qwen 110B model or other compatible models via command line.

- `llama405B.py`  
  Python script for interacting with the LLaMA 405B model through an API endpoint.

- `qwen110b.py`  
  Python script for sending prompts to the Qwen 110B model.

- `qwen2-72b.py`  
  Python script for accessing the Qwen 2 72B model.

- `tes.py`  
  A basic testing script for interacting with the running model.

- `conversation_history.txt`  
  Log file storing the conversation history.

- `tes.txt`, `text.text`  
  Additional notes or output logs from test runs.

## 🚀 Usage

1. Make sure the LLM model server is running locally and is accessible via an HTTP API.
2. Run the Python script that matches the model you are using.
3. Enter a prompt as instructed in the terminal.
4. View the model’s response and (if configured) the conversation will be saved in `conversation_history.txt`.

## 🛠 Requirements

- Python 3.8 or later
- `requests` library (for making HTTP calls)
- A locally hosted LLM API server (e.g., LLaMA.cpp, Qwen, etc.)

To install the required library:

```bash
pip install requests
```
## ⚙ Notes

Some scripts may need customization depending on your local API URL and configuration.
