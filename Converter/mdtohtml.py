import re
import sys

def converter(file, output):

    with open(file, 'r') as f:
        lines = f.readlines()

    headers = re.compile(r'^(#+)\s*(.*)')
    bold = re.compile(r'(\*\*|__)(.*?)\1')
    italic = re.compile(r'(\*|_)(.*?)\1')
    numerate = re.compile(r'^(\d+\.)\s(.*)')

    html_lines = []
    countL = False

    html_lines.append("<html>")
    html_lines.append("<body>")

    for i, line in enumerate(lines):
        line = line.rstrip("\n")

        # Headers
        hM = headers.match(line)
        if hM:
            quantity = len(hM.group(1)) # numero de '#' no nível do header
            title = hM.group(2) # o que vem depois do '#' 
            line = f'<h{quantity}>{title}</h{quantity}>'

        # Bold / Italic
        line = bold.sub(r'<strong>\2</strong>', line)
        line = italic.sub(r'<em>\2</em>', line)

        # Lists
        nM = numerate.match(line)
        if nM:
            text = nM.group(2)

            if not countL:
                html_lines.append("<ol>")
                countL = True

            html_lines.append(f"<li>{text}</li>")

            # Fecha lista se a próxima linha não for item
            next_line = lines[i + 1].rstrip("\n") if i + 1 < len(lines) else ""
            if not numerate.match(next_line):
                html_lines.append("</ol>")
                countL = False

            continue

        html_lines.append(line)

    html_lines.append("</body>")
    html_lines.append("</html>")

    with open(output, "w") as f:
        f.write("\n".join(html_lines))

    return output

def find_tags_h1(file):

    with open(file, 'r') as f:
        html_text = f.read()

    h1_re = re.compile(r'<h1>.*?</h1>')

    h1_count = len(h1_re.findall(html_text))
    print(f"Número de H1 no HTML: {h1_count}")

def find_tags_li(file):

    with open(file, 'r') as f:
        html_text = f.read()

    li_re = re.compile(r'<li>.*?</li>')

    li_count = len(li_re.findall(html_text))
    print(f"Número de LI no HTML: {li_count}")

def main(args):

    if len(args) != 3:
        print('Usage: python conversor.py <input_file> <output_file>')
        return 1
    
    input_file = args[1]
    output_file = args[2]
    converter(input_file, output_file)
    find_tags_li(output_file)

if __name__ == '__main__':
    main(sys.argv)