class Solution(object):
    def zigZagArrays(self, n, l, r):
        MOD = 1000000007

        m = r - l + 1
        size = 2 * m

        U = [[0] * size for _ in range(size)]

        for j in range(m):
            for i in range(j):
                U[m + i][j] = 1

        for j in range(m):
            for i in range(j + 1, m):
                U[i][m + j] = 1

        def mat_mul(A, B):
            rows = len(A)
            cols = len(B[0])
            mid = len(B)

            C = [[0] * cols for _ in range(rows)]

            for i in range(rows):
                for k in range(mid):
                    if A[i][k] == 0:
                        continue

                    val = A[i][k]

                    for j in range(cols):
                        if B[k][j]:
                            C[i][j] = (C[i][j] + val * B[k][j]) % MOD

            return C

        p = n - 1

        vec = [[1] * size]

        while p:
            if p & 1:
                vec = mat_mul(vec, U)

            U = mat_mul(U, U)
            p >>= 1

        ans = 0

        for x in vec[0]:
            ans = (ans + x) % MOD

        return ans
        