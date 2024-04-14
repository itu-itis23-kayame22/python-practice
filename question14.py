raw_list = [1, 1, 2, 4, 6, 6, 7, 7, 7, 8]

def remover(raw_list):
    return list(set(raw_list))

result = remover(raw_list=raw_list)
print(result)