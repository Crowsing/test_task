from flask_wtf import FlaskForm
from wtforms import DecimalField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class ShopForm(FlaskForm):
    sum = DecimalField('Сумма оплаты', validators=[DataRequired()])
    currency = SelectField('Валюта оплаты', choices=['EUR', 'USD', 'RUB'])
    description = TextAreaField('Описание товара', validators=[DataRequired()])
    submit = SubmitField('Отправить форму')

