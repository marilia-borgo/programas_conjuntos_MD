'''
usando o conceito de busca binaria e recursao
da induçäo finita
'''

def binary_search(arr, low, high, target):
    if high >= low:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, high, target)
    else:
        return -1


arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
target = 11
result = binary_search(arr, 0, len(arr) - 1, target)

if result != -1:
    print(f"Elemento {target} encontrado no index {result}.")
else:
    print("Elemento não encontrado mno array")