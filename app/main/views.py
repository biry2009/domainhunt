from flask import render_template, abort
from . import main
from app.models import Domain, Registrar, Price, Cheapest
from .. import config

@main.route('/')
def home_page():
    cheap_prices = Cheapest.query.all()

    return render_template("index.html", cheap_prices=cheap_prices)


@main.route('/about')
def about_page():
    title = "about"
    return render_template("about.html", title=title)


@main.route('/review')
def review_page():
    title = "review"
    return render_template("review.html", title=title)


# contact page route
@main.route('/contact')
def contact_page():
    title = "contact"
    return render_template("contact.html", title=title)


# domain extension route
@main.route('/tlds/<name>')
def domain_extension(name):
    domain = Domain.query.filter_by(name=name).first()
    if domain is None:
        abort(404)
    else:
        prices = Price.query.filter_by(domain_id=domain.id)

    objk =[]

    for price in prices:
        registrar_name = Registrar.query.filter_by(id=price.registrar_id).first().name
        obj = [{
            'registrar': registrar_name,
            'register': price.register,
            'renewal': price.renewal,
            'transfer': price.transfer,
            'whois': price.whois
               }]
        objk = objk + obj
    return render_template("tld_base.html", domain=domain, title=name, objk=objk)

