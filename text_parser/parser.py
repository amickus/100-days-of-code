#!/usr/bin/env Python3


def read_file(filename):
    f = open(filename, 'rU')
    all_text = f.read().splitlines()
    return all_text
    f.close()


def create_h(all_text):
    print(all_text)
    filename = all_text[0] + '.h'
    f = open(filename, 'w')
    f.truncate()
    f.write('\textern const char* NAME_names[];\n')
    f.write('\ttypedef enum {\n')
    for i in all_text[1:]:
        f.write('\t\t' + i + ',\n')
    f.write('\t} ' + all_text[0].upper()
            + ';\n')
    f.close()

# Same as create_h


def create_c(all_text):
    print(all_text)
    filename = all_text[0] + '.c'
    with open(filename, 'w') as f:
        f.write('A string to write')


def main():
    all_text = read_file("text.txt")
    create_h(all_text)
    create_c(all_text)


if __name__ == '__main__':
    main()
