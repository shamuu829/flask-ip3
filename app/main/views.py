from flask import Flask
from flask import render_template,redirect,url_for
from . import main
from flask_login import login_required,current_user
from .forms import PitchForm
from .. models import User,Pitch,Comment
from ..import db

@main.route('/')
def index():
    pitches = Pitch.query.all()
    '''
    View the root page function
    '''
    title = "Pitches"
    return render_template('index.html', title = title,pitches=pitches)

@main.route('/new/pitch', methods = ['GET','POST'])
@login_required
def new_pitch():
    formpitch = PitchForm()
    if formpitch.validate_on_submit():
        pitch = Pitch(category = formpitch.category.data, content = formpitch.pitch.data)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
     
    return render_template('pitch.html',formpitch = formpitch) 

@main.route('/new/pickupline', methods = ['GET','POST'])
@login_required
def new_pickupline():
    formpitch = PitchForm()
    if formpitch.validate_on_submit():
        pitch = Pitch(category = formpitch.category.data, content = formpitch.pitch.data)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
     
    return render_template('Pickupline.html',formpitch = formpitch)   

@main.route('/new/interview', methods = ['GET','POST'])
@login_required
def new_interview():
    formpitch = PitchForm()
    if formpitch.validate_on_submit():
        pitch = Pitch(category = formpitch.category.data, content = formpitch.pitch.data)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
     
    return render_template('interview.html',formpitch = formpitch)   



@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):  
    '''
    View the root page function
    '''
    pass