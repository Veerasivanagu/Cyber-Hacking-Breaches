import json, pathlib
path = pathlib.Path('model/model.ipynb')
nb = json.loads(path.read_text(encoding='utf-8'))
print('=== training-related cells ===')
for i, cell in enumerate(nb['cells']):
    if i < 40 and cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        if any(x in source for x in ['TfidfVectorizer', 'RandomForestClassifier', 'train_test_split', 'rfc']):
            print('--- cell', i, '---')
            print(source)

