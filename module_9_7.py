def is_prime(func):
    def wrapper(*args):
        original_result = func(*args)
        if original_result % 2 != 0:
            print("Простое")
        else:
            print("Состовное")
        return original_result
    return wrapper


@is_prime
def sum_three(a, b, c):
    result_ = a + b + c
    return result_


result = sum_three(2, 3, 6)
print(result) 
