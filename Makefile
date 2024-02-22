all: merge_json convert_notebook insert_file replace_file fix_title

merge_json:
	jsoncat subsets/[01]*.json --output subsets/all.json

convert_notebook:
	jupyter nbconvert --to html index.ipynb --no-input

insert_file:
	python insert_file.py index.html ga.script "mathjax" index2.html

replace_file:
	mv index2.html index.html

fix_title:
	sed -i .bak 's/<title>.*<\/title>/<title>Data Science Flashcards<\/title>/' index.html
