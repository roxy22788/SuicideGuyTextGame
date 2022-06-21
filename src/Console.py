import sys
import time
import os

def escrever(texto):
  for letra in texto:
    sys.stdout.write(letra)
    sys.stdout.flush()
    time.sleep(0.04)

def limparConsole():
  os.system('cls' if os.name == 'nt' else 'clear')