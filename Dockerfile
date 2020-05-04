FROM tiangolo/uwsgi-nginx-flask:python3.7

RUN pip install scikit-learn pandas dill flask gunicorn
