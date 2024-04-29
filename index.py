from queue import Queue
import random
import time

def generate_request(q):
    '''Функція для генерації нової заявки'''
    request_id = random.randint(100, 999)
    print(f"Генеруємо нову заявку: {request_id}")
    q.put(request_id)


def process_request(q):
    '''Функція для обробки заявки'''
    if not q.empty():
        request_id = q.get()
        print(f"Обробляємо заявку: {request_id}")
    else:
        print("Черга пуста. Немає заявок для обробки.")

# Створюємо чергу заявок
queue = Queue()

# Головний цикл програми
try:
    while True:
        generate_request(queue)  # Генеруємо нові заявки
        process_request(queue)   # Обробляємо заявки
        time.sleep(1)            # Затримка для імітації часу обробки
except KeyboardInterrupt:
    print("Програма завершила роботу.")
