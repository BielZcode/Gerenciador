#!/usr/bin/env python3
import os
import platform
import subprocess

def verificar_memoria():
    try:
        # Para sistemas baseados em Linux
        with open('/proc/meminfo', 'r') as meminfo:
            linhas = meminfo.readlines()
            mem_total = int(linhas[0].split()[1]) / 1024  # Em MB
            mem_livre = int(linhas[1].split()[1]) / 1024  # Em MB
            print(f"Memória Total: {mem_total:.2f} MB")
            print(f"Memória Livre: {mem_livre:.2f} MB")
    except FileNotFoundError:
        print("Informações de memória não disponíveis neste sistema.\n")

def verificar_cpu():
    try:
        # Para sistemas baseados em Linux
        with open('/proc/loadavg', 'r') as loadavg:
            carga = loadavg.readline().split()
            print(f"Carga da CPU (1 min): {carga[0]}")
            print(f"Carga da CPU (5 min): {carga[1]}")
            print(f"Carga da CPU (15 min): {carga[2]}")
    except FileNotFoundError:
        prin
