import json, pathlib
nb = json.loads(pathlib.Path('model/model.ipynb').read_text(encoding='utf-8'))
for i, cell in enumerate(nb['cells']):
    if cell['cell_type']=='code':
        src=''.join(cell['source'])
        if 'read_csv' in src or 'status' in src or 'url' in src:
            print('--- cell', i, '---')
            print(src)
