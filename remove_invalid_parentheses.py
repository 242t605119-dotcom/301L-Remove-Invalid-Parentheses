class Solution:
    def removeInvalidParentheses(self, s):
        def is_valid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        result = []
        visited = {s}
        queue = [s]
        found = False

        while queue:
            current = queue.pop(0)

            if is_valid(current):
                result.append(current)
                found = True

            if found:
                continue

            for i in range(len(current)):
                if current[i] != '(' and current[i] != ')':
                    continue

                next_string = current[:i] + current[i + 1:]

                if next_string not in visited:
                    visited.add(next_string)
                    queue.append(next_string)

        return result
