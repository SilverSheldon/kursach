import re


class Statistics:
    def __init__(self, symbol_count: dict, str_len: int, s: str):
        self.s = s  # строка после api/
        self.str_len = str_len  # длина строки
        self.symbol_count = symbol_count  # количество каждого символа

        # print("\xAB")  # это «
        # print("\xBB")  # это »
        # print("\x22")  # это "

        # Все левые: ^"| +"
        # Все правые: "$|" +

        self.original = self.s
        self.changed = re.sub(
            pattern=r'"$|" +',
            repl="\xBB ",
            string=re.sub(
                pattern=r'^"| +"',
                repl=" \xAB",
                string=self.s
            ).strip(" ")).strip(" ")
