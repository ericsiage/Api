from website.models import Note
from flask import Blueprint, render_template, request, flash
from flask.helpers import flash
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST']) #ruta que recibe metodos de GET Y POST
@login_required #decorador
def home():
    if request.method == 'POST': #si recibe el methodo post
        note = request.form.get('note')
        #flashmessages
        if len(note) < 1:
            flash('Note is toom short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id) #else - agregar notas de ese usuario
            db.session.add(new_note) 
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user)


