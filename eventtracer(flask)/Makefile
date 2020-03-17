SHELL:=/bin/bash

test:
	( \
	source ~/.virtualenvs/mate/ma_shop/eventtracer/bin/activate; \
	export FLASK_ENV=dev; \
	pytest; \
	)
run:
	( \
	source ~/.virtualenvs/mate/ma_shop/eventtracer/bin/activate; \
	export FLASK_ENV=prod; \
	python app.py \
	)
freeze:
	( \
	source ~/.virtualenvs/mate/ma_shop/eventtracer/bin/activate; \
	pip freeze > requirements.txt \
	)
shell:
	( \
	source ~/.virtualenvs/mate/ma_shop/eventtracer/bin/activate; \
	export FLASK_ENV=prod; \
	python; \
	)