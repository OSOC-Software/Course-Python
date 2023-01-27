# Fizz Buzz

def fizzbuzz():
    num = 1
    while num <= 100:
        if(num % 3 == 0 and num % 5 != 0):
            print("fizz")
        elif(num % 5 == 0 and num % 3 != 0): 
            print("buzz")
        elif(num % 3 == 0 and num % 5 == 0):
            print("fizz buzz")
        else:
            print(num)
        num += 1    

# fizzbuzz()

# Anagramas

def anagramas(text1:str, text2):
    son_anagramas = False
    if(len(text1) == len(text2)):
        print('iguales')
        text1 = text1.lower()
        text2 = text2.lower()
        print(text1,text2)
        for element in text2: 
            if(element in text1):
                son_anagramas = True
            else:
                son_anagramas = False
            print(element)
    else:
        print('No son iguales')    
    print(f"¿ Son anagramas ? {son_anagramas} ! ")

def anagramas2(a:str,b:str):
    if a.lower() == b.lower():
        return False
    return sorted(a.lower()) == sorted(b.lower())

# anagramas("JUAN", "jUaN")
# print(f"¿Son anagramas? {anagramas2('roma', 'AMOR')}")

# Fibonacci

def fibonacci(limit):
    prev = 0
    next = 1
    fib = 0
    for i in range(1, limit):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

# fibonacci(10)

# Num Primo

def num_primo(limit):
    for num in range(1, limit):    
        if(num >= 2 ):
            is_divisible = False
            for index in range(2, num):
                if num % index == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(num)

# num_primo(10)


# Invertir Cadenas

def invertir_cadenas(text):
    text_len = len(text)
    reverse = ""
    for index in range(0, text_len):
        reverse += text[text_len - index - 1]
    return reverse

print(invertir_cadenas("Hola Mundo"))