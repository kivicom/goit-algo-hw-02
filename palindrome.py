from collections import deque

def is_palindrome(s):
    '''Перетворення рядка на нижній регістр та видалення пробілів'''
    formatted_string = ''.join(e for e in s.lower() if e.isalnum())

    # Створення двосторонньої черги з символів рядка
    char_deque = deque(formatted_string)

    # Порівняння символів з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Тестування функції
test_str = "A man, a plan, a canal: Panama"
print(f"Рядок '{test_str}' є паліндромом? {is_palindrome(test_str)}")

test_str = "Was it a car or a cat I saw"
print(f"Рядок '{test_str}' є паліндромом? {is_palindrome(test_str)}")

test_str = "No lemon, no melon"
print(f"Рядок '{test_str}' є паліндромом? {is_palindrome(test_str)}")
