# Заполнить двумерный массив A(M*N) элементами из текстового файла
# Первый столбец упорядочить по возрастанию методом вставки, используя рабочий одномерный массив B(M)
max_num = 16
# Алгоритм сортировки вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

M = [[] for i in range(max_num)]
with open("lab5.txt", "rt") as f:
    for i in range(max_num):
        for n in range(max_num):
            M[i].append(f.read(1))
print("Массив, полученый из файла/n")
for i in M:
    print(i)
print("Массив первого столбца\n")
B = [M[i][0] for i in range(max_num)]
print(B)
B = insertion_sort(B)
print("Отсортированный массив первого столбца\n")
print(B)
for i in range(max_num):
    M[i][0] = B[i]
print("Результат работы программы\n")
for i in M:
    print(i)