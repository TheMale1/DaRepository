def calculate_half(number):
    half = number / 2
    return half
def calculate_double(number):
    double = number * 2
    return double

question = int(input("How much: "))
answer = calculate_half(question)
print(f"Half {question} is {answer}")


question = int(input("How much: "))
answer = calculate_double(question)
print(f"Double {question} is {answer}")
