class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        ans = []

        def dfs(index, expression, value, prev):

            if index == len(num):
                if value == target:
                    ans.append(expression)
                return

            for i in range(index, len(num)):

                if i > index and num[index] == "0":
                    break

                current = int(num[index:i + 1])

                if index == 0:

                    dfs(
                        i + 1,
                        expression + str(current),
                        current,
                        current
                    )
                
                else:

                    dfs(
                        i + 1,
                        expression + "+" + str(current),
                        value + current,
                        current
                    )

                    dfs(
                        i + 1,
                        expression + "-" + str(current),
                        value - current,
                        - current
                    )

                    dfs(
                        i + 1,
                        expression + "*" + str(current),
                        value - prev + prev * current,
                        prev * current
                    )

        dfs(0, "", 0, 0)

        return ans