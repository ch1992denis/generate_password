import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
strange_symbols = 'il1Lo'
chars = ''

# Количество паролей для генерации;
# Длину одного пароля;
# Включать ли цифры 0123456789?
# Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
# Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
# Включать ли символы !#$%&*+-=?@^_?
# Исключать ли неоднозначные символы il1Lo

quantity = int(input('Введите количество паролей для генерации:  '))
length = int(input('Введите количество символов вашего пароля:  '))
numbers = input('Включать ли цифры 0123456789? да/нет  ')
upper_letters = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? да/нет  ')
lower_letters = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? да/нет  ')
special_symbols = input('Включать ли символы !#$%&*+-=?@^_? да/нет  ')
similar_symbols = input('Исключать ли неоднозначные символы il1Lo? да/нет  ')

if numbers == 'да':
    chars += digits
if upper_letters == 'да':
    chars += uppercase_letters
if lower_letters == 'да':
    chars += lowercase_letters
if special_symbols == 'да':
    chars += punctuation
if similar_symbols == 'да':
    for c in strange_symbols:
        chars = chars.replace(c,'')

def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password
print()
print('Ваши пароли: ')

for i in range(quantity):
    print(generate_password(length, chars))

