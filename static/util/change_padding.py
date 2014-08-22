import os

all_files = os.listdir('../ipython_blog')

all_file_names = [i for i in all_files if 'html' in i]

for file_name in all_file_names:
    file_content = open('../ipython_blog/' + file_name, 'r').read()
    file_content = file_content.replace('body {\n  overflow: visible;\n  padding: 8px;\n}\n', 'body {\n  overflow: visible;\n  padding: 0px;\n}\n')
    file_content = file_content.replace('<img src="', '<img src="/static/ipython_blog/files/')
    f = open('../ipython_blog/' + file_name, 'w')
    f.write(file_content)
