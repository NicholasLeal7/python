import subprocess
import time

def connection():    
    # Caminho para o executável do Chrome
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

    # Executa o Chrome com o modo de depuração ativado
    subprocess.run([chrome_path, '--remote-debugging-port=9222'])

    

import asyncio

async def main():
    connection()
    await asyncio.sleep(5)
    print('... Mundo')

asyncio.run(main())  # Python 3.7+
