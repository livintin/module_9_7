def is_prime(func):
    def wrapper(*args):
        original_result = func(*args)
        if original_result > 1:
            for i in range(2, (original_result // 2) + 1):
                if (original_result % i) == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")
        return original_result

    return wrapper


@is_prime
def sum_three(a, b, c):
    result_ = a + b + c
    return result_


result = sum_three(2, 3, 6)
print(result)
