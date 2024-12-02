from threading import Thread
from pylatexenc.latex2text import LatexNodes2Text
from gradio_client import Client
import time
import sys

client = Client("Qwen/Qwen1.5-110B-Chat-demo", max_workers=128000)

def latex_to_text(latex_string):
    # Replace special characters to avoid loss during conversion
    latex_string = latex_string.replace('%', '__PERCENT__').replace(' & ', '__DAN__').replace(' { ', '__KURAWALleft__').replace(' } ', '__KURAWALright__')
    text = LatexNodes2Text().latex_to_text(latex_string)
    
    # Restore special characters to their original symbols
    text = text.replace('__PERCENT__', '%').replace('__DAN__', ' & ').replace('__KURAWALleft__', ' { ').replace('__KURAWALright__', ' } ')
    return text

def show_loading():
    while loading_flag:
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.2)
        sys.stdout.write("\b\b\b   \b\b\b")
        sys.stdout.flush()
        time.sleep(0.5)
        
def save_history(items):
    with open('conversation_history.txt', 'w', encoding="UTF-8") as file:
        for item in items:
            file.write(repr(item) + '\n')
def load_history():
    hist = []
    try:
        with open('conversation_history.txt', 'r') as file:
            loaded_data = [eval(line.strip()) for line in file]
        for item in loaded_data:
            hist.append(item)
    except Exception as e:
        print(e)
        pass
    return hist
def delete_history(leng):
    with open('conversation_history.txt', 'r') as file:
        lines = file.readlines()
    modified_lines = lines[leng:]
    with open('conversation_history.txt', 'w') as file:
        file.writelines(modified_lines)
    with open('conversation_history.txt', 'r') as cek:
        liness = cek.readlines()
    print(f"\nMengapus history Success. History Now: {len(liness)}\n")
        
loading_flag = False

while True:
    print("\nyou:")
    tny = sys.stdin.read().replace("\n", "\\n")

    # Start loading animation thread
    loading_flag = True
    loading_thread = Thread(target=show_loading)
    loading_thread.start()
    
    while True:
        hist = load_history()
        try:
            result = client.predict(
                query=tny,
                history=hist,
                system="Your name is Vultr. You are a helpful assistant.",
                api_name="/model_chat"
            )
            break
        
        except Exception as e:
            print(e)
            delete_history(10)
            pass
    # Stop loading animation
    loading_flag = False
    loading_thread.join()
    
    # Update history
    new_hist = result[1]
    hist.extend(new_hist)
    
    save_history(new_hist)
    
    print("\nRespon:\n")
    # Get the last response
    last_response = latex_to_text(new_hist[-1][1])
    
    # Display the response per token (character in this case)
    for char in last_response:
        print(char, end='', flush=True)
        time.sleep(0.001)
    
    print()
