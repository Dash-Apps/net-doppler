.PHONY:dep_install


dep_install:
			pip install -r requirements.txt

devserver:
			python3 server.py