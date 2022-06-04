def line_prepender(filename, line):
    with open(filename, 'r+', encoding="utf-8") as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)