def escape_quotes(line):
    return line.replace('"', r'\"')

def main():
    print("Enter your lines (press Enter on an empty line to finish):")
    lines = []
    while True:
        inp = input()
        if inp == "":
            break
        lines.append(inp)

    print("\nOutput:")
    for line in lines:
        if '"' in line:
            print(f'        "{escape_quotes(line)}",')
        else:
            print(f'        "{line}",')

if __name__ == "__main__":
    main()