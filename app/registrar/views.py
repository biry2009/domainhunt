from flask import redirect, abort, render_template
from . import registrar
from app.models import Registrar

@registrar.route('/reviews/')
def reviews():
    title = 'Domain Registrars Reviews'
    return render_template("reviews.html", title=title)

# registrar route
@registrar.route('/review/<name>')
def review_registrar(name):
    regist = Registrar.query.filter_by(key=name).first()
    if regist is None:
        abort(404)
    else:
        title = str(name) + ' Review and Profile'
    return render_template("registrar.html", title=title)

# registrar coupon page route
#@registrar.route('coupon/<name>')
#def coupon_page(name):
#    pass


# redirect to registrar's page
@registrar.route('/link/<name>')
def link(name):
    registrar_name = Registrar.query.filter_by(key=name).first()
    godaddy_url = 'https://www.godaddy.com'
    namecheap_url = 'https://www.namecheap.com'
    onedomain_url = 'https://www.1and1.com'
    name_url = 'https://www.name.com'

    if registrar_name is None:
        abort(404)
    elif registrar_name.key == 'godaddy':
        return redirect(godaddy_url)
    elif registrar_name.key == 'namecheap':
        return redirect(namecheap_url)
    elif registrar_name.key == '1and1':
        return redirect(onedomain_url)
    elif registrar_name.key == 'name':
        return redirect(name_url)
    else:
        return render_template('index.html')