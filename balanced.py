def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or pairs[char] != stack.pop():
                return False
    return not stack

# Тестування функції
test_strings = [
    "( ){[ ]( )( ){} }",
    "( ( ( )",
    "( }",
    "( ){ [1](1 + 3)( ){ }}"
]

for test_string in test_strings:
    result = "Симетрично" if is_balanced(test_string) else "Несиметрично"
    print(f"{test_string}: {result}")
