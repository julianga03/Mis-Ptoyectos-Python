import psutil
import platform

# Información sobre la CPU
cpu_info = platform.processor()
cpu_count = psutil.cpu_count(logical=False)

print('Información de la CPU:')
print(f'Modelo: {cpu_info}')
print(f'Núcleos físicos: {cpu_count}')
print(f'Núcleos lógicos: {psutil.cpu_count(logical=True)}')

print('\n')