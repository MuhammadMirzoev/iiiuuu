from flask import Flask, render_template
from data import db_session
from data.exponents import Exponents
from flask_sitemap import Sitemap
from flask import request
from function_.telegram import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
ext = Sitemap(app=app)


# О ВЫСТАВКЕ
@app.route("/index", methods=['POST', 'GET'])
@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@ext.register_generator
def index():
    yield 'index', {}


# ДЕЛОВАЯ ПРОГРАММА
@app.route("/work_program", methods=['POST', 'GET'])
def work_program():
    return render_template("work_program.html")


@app.route("/funder", methods=['POST', 'GET'])
def funder():
    return render_template("funder.html")


# ЭКСПОНЕНТЫ
@app.route("/exponents/<region>", methods=['POST', 'GET'])
def location(region='all'):
    session = db_session.create_session()
    if region == 'all':
        data = session.query(Exponents).all()
    else:
        data = session.query(Exponents).filter(Exponents.link == region)
    filter_region = set([el for el in session.query(Exponents.region, Exponents.link).all()])
    session.close()
    return render_template("exponents.html",
                           data=sorted(data, key=lambda x: (x.region, x.name)),
                           filter_region=sorted(filter_region, key=lambda x: x[0]))


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    check_post_method(request)
    return render_template("contact.html")


@app.route("/expert", methods=['POST', 'GET'])
def expert():
    return render_template("expert.html")


@app.route("/location", methods=['POST', 'GET'])
def exponents():
    return render_template("location.html")


@app.route("/test", methods=['POST', 'GET'])
def test():
    # session = db_session.create_session()
    # x = Exponents()
    # x.name = 'КФХ «Ангора»'
    # x.region = 'Республика Дагестан'
    # x.description = 'Меринос'
    # session.add(x)
    # session.commit()
    # session.close()
    return render_template("test.html")


def main():
    db_session.global_init()
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
