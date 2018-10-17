
run:
	export FLASK_ENV=development && FLASK_APP=call_records/api.app flask run;

test:
	export FLASK_ENV=qa && pytest --cov=call_records/api --pyargs ./call_records/tests/ -v;

install:
	pip install -r requirements.txt

db_init_dev:
	export FLASK_ENV=development && FLASK_APP=call_records/api.migrate flask db init

db_migrate_dev:
	export FLASK_ENV=development && FLASK_APP=call_records/api.migrate flask db migrate

db_upgrade_dev:
	export FLASK_ENV=development && FLASK_APP=call_records/api.migrate flask db upgrade

db_upgrade_qa:
	export FLASK_ENV=qa && FLASK_APP=call_records/api.migrate flask db upgrade
