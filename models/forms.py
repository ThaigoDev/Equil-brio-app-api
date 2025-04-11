from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class CadastroForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    descricao = TextAreaField('Descrição', validators=[DataRequired()])
    categoria = SelectField('Categoria', choices=[
        ('limpeza', 'Limpeza'),
        ('eletricista', 'Eletricista'),
        ('pintura', 'Pintura'),
        ('outros', 'Outros')
    ], validators=[DataRequired()])
    submit = SubmitField('Cadastrar Serviço')
