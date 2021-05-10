with open('mybib.bib', 'r') as _file:
    filecontent = _file.read()

bibentries = filecontent.split('@')[1:]

for be in bibentries:
    dic = {}
    _str = '---\n'
    for nline, line in enumerate(be.lstrip("\n").rstrip('\n').split(',\n')):
        line = line.strip()
        if nline == 0:
            pubkey = line.split('{')[1]
        else:
            if line[0] == '_':
                try:
                    key, value = line.split("=")
                except ValueError:
                    print(line)
                key, value = key.strip(), value.strip()
                dic[key[1:]] = value.strip('{').strip('}').strip('\n').strip('}')
    for key, value in dic.items():
        _str += "{}: {}\n".format(key, value)
    _str += '---\n'

    # Header finished

    _str += '{}\n\n'.format(dic['excerpt'].rstrip('"').lstrip('"'))
    with open('{}.md'.format(pubkey), 'w') as _file:
        _file.write(_str)
