from app import app
from flask import render_template, redirect, session
from app.forms import ShopForm
from app.models import Shop
from app import db
from app.redirect_by_currency import RedirectByCurrency


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ShopForm()
    redirect_by_currency = RedirectByCurrency()
    if form.validate_on_submit():
        purchase = Shop(sum=form.sum.data, currency=form.currency.data, description=form.description.data)

        db.session.add(purchase)
        db.session.commit()
        if purchase.currency == 'EUR':
            session['by_eur'] = redirect_by_currency.pay(purchase.sum, purchase.currency, purchase.id)
            return redirect('/')
        elif purchase.currency == 'USD':
            url = redirect_by_currency.bill(purchase.sum, purchase.currency, purchase.id)
            return redirect(url, code=302)
        else:
            session['by_rub'] = redirect_by_currency.invoice(purchase.sum, purchase.currency, purchase.id)
            return redirect('/')
    by_eur = session.pop('by_eur', None)
    by_rub = session.pop('by_rub', None)
    return render_template('purchase_of_goods/index.html', form=form, by_eur=by_eur, by_rub=by_rub)




