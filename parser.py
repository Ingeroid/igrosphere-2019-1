import os, re


def read_file(file_path):
    f = open(file_path + filename, "r")
    return f.readlines()


def filter_lines(regexp, lines):
    result = []
    for line in lines:
        while line != " ":
            if re.match(regexp, line):
                result.append(line)
            else:
                print(f"line {line} don't match")
            break
    return [line for line in lines if re.match(regexp, line)]


if __name__ == "__main__":
    filename = "\\coverage-error.log"
    file_path = os.getcwd()
    print(file_path + filename)
    regexp = r"\[\d\d\d\d\.\d\d\.\d\d \d\d:\d\d:\d\d\].+"
    lines = read_file(file_path)
    print("Author is s.rodionov")
    print(filter_lines(regexp, lines))
    lines = read_file(file_path)
    print(filter_lines(regexp, lines))