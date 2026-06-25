class Solution:
    def fullJustify(self, words: List[str], maxWidth: int):
        res = []
        line = []
        line_len = 0
        i = 0
        while i < len(words):
            word = words[i]
            if line_len + len(line) + len(word) > maxWidth:
                if len(line) == 1:
                    res.append(line[0] + " " * (maxWidth - line_len))
                else:
                    total_spaces = maxWidth - line_len
                    gaps = len(line) - 1
                    space, extra = divmod(total_spaces, gaps)

                    for j in range(extra):
                        line[j] += " " * (space + 1)
                    for j in range(extra, gaps):
                        line[j] += " " * space
                    res.append("".join(line))
                line = []
                line_len = 0
            line.append(word)
            line_len += len(word)
            i += 1
        last_line = " ".join(line)
        last_line += " " * (maxWidth - len(last_line))
        res.append(last_line)

        return res