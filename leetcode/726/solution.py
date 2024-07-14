class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse():
            nonlocal i
            if self.formula[i].isalpha() and self.formula[i].isupper():  # Element symbol
                start = i
                i += 1
                while i < self.n and self.formula[i].islower():  # Consume all lower case letters
                    i += 1
                element = self.formula[start:i]
                count = parse_count()
                return {element: count}
            elif self.formula[i] == '(':
                i += 1
                result = merge(parse())
                if self.formula[i] == ')':
                    i += 1
                    count = parse_count()
                    for key in result:
                        result[key] *= count
                return result
            else:
                raise ValueError("Invalid character at position " + str(i))

        def parse_count():
            nonlocal i
            if i < self.n and self.formula[i].isdigit():
                start = i
                while i < self.n and self.formula[i].isdigit():  # Consume all digits
                    i += 1
                return int(self.formula[start:i])
            else:
                return 1

        def merge(a, b=None):
            nonlocal result
            if b is None:
                result.update(a)
            else:
                for key in a:
                    if key not in b:
                        b[key] = 0
                    b[key] += a[key]
            return b or {}

        self.i = 0
        self.n = len(formula)
        result = {}
        merge(parse())
        return "".join(key + (str(result[key]) if result[key] > 1 else "") for key in sorted(result))