from re import findall


class FileCount:

    def __init__(self, file, string):
        self.f = file
        self.s = string

    def string_count(self):
        with open(self.f, encoding='utf-8') as f:
            result = len(findall(self.s, ''.join([i for i in f])))
        return f'String {self.s} appears {result} times in {self.f}'


class FileReplacement:

    def __init__(self, file, string_to_find, string_replacement):
        self.f = file
        self.s = string_to_find
        self.s2 = string_replacement

    def string_replacement(self):
        with open(self.f, encoding='utf-8') as f:
            result = ''.join([i for i in f]).replace(self.s, self.s2)
        with open(self.f, 'w', encoding='utf-8') as f:
            f.write(result)


def main():
    inpt = input().split()
    file, string = inpt[0], inpt[1]

    inpt2 = input().split()
    file2, string2, string3 = inpt2[0], inpt2[1], inpt2[2]

    print(FileCount(file, string).string_count())
    FileReplacement(file2, string2, string3).string_replacement()


if __name__ == '__main__':
    main()
