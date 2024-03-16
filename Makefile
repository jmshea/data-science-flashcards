all: merge_json convert_homepage convert_terms add_ga add_og fix_title

merge_json:
	jsoncat subsets/[01]*.json --output subsets/all.json

convert_homepage:
	jupyter nbconvert --to html index.ipynb --no-input

convert_terms:
	jupyter nbconvert --to html terms.ipynb --no-input

add_ga:
	python insert_file.py index.html ga.script "mathjax" index2.html

add_og:
	python insert_file.py index.html og.html "title" index.html

fix_title:
	sed -i .bak 's/<title>.*<\/title>/<title>Data Science Flashcards<\/title>/' index.html
