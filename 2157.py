MAX_N = 300
MAX_K = 100000
MAX_UNISCORE = 10000

def check_and_extract_inputs(inputs):
    assert len(inputs) == 3 and all([i.isdigit() for i in inputs])
    n, m, k = map(int, inputs)
    assert 1 <= n and n <= MAX_N and 2 <= m and m <= n and 1 <= k and k <= MAX_K
    return n, m, k

def check_and_extract_path_infos(n, k):
    paths = []
    for _ in range(k):
        inputs = input().split()
        assert len(inputs) == 3 and all([i.isdigit() for i in inputs])
        i, j, s = map(int, inputs)
        assert 1 <= i and i <= n and 1 <= j and j <= n and i != j and 1 <= s and s <= MAX_UNISCORE
        if i < j:
            exists = False
            for idx in range(len(paths)):
                if paths[idx][0] == i - 1 and paths[idx][1] == j - 1:
                    exists = True
                    paths[idx][2] = max(paths[idx][2], s)
            if not exists:
                paths.append([i - 1, j - 1, s])

    return paths

def find_max_score(n, m, paths):
    d_list = [[0] + [-1 for y in range(n - 1)] for x in range(m)]
    for p_len in range(m - 1):
        for i in range(len(paths)):
            if d_list[p_len][paths[i][0]] != -1 and d_list[p_len + 1][paths[i][1]] < d_list[p_len][paths[i][0]] + paths[i][2]:
                d_list[p_len + 1][paths[i][1]] = d_list[p_len][paths[i][0]] + paths[i][2]

    if d_list[-1][-1] == -1:
        return 0
    else:
        return d_list[-1][-1]

if __name__ == "__main__":
    n, m, k = check_and_extract_inputs(input().split())
    paths = check_and_extract_path_infos(n, k)

    max_score = find_max_score(n, m, paths)
    print(max_score)