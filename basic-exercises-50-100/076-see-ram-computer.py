import psutil


def see_ram_computer():
    memory = psutil.virtual_memory()
    total_ram = memory.total / (1024 ** 3)  # Convert bytes to GB
    return total_ram


memory = see_ram_computer()
print(f"Total RAM: {memory:.2f} GB")
