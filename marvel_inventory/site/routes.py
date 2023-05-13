from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from marvel_inventory.forms import CharacterForm
from marvel_inventory.models import Character, db
from marvel_inventory.helpers import random_joke_generator



site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    print("ooga booga in the terminal")
    return render_template('index.html')


@site.route('/profile', methods = ['GET', 'POST'])
@login_required
def profile():
     my_character =CharacterForm()


     try:
        print('I try')
        if request.method == "POST" and my_character.validate_on_submit():
            name = my_character.name.data
            description = my_character.description.data
            comics_appeared_in = my_character.comics_appeared_in.data
            super_power = my_character.super_power.data
            date_created = my_character.date_created.data 
            if my_character.dad_joke.data:
                random_joke = my_character.dad_joke.data
            else:
                random_joke = random_joke_generator() 
        
            user_token = current_user.token

            character = Character(name, description, comics_appeared_in, super_power, date_created, random_joke, user_token)

            db.session.add(character)
            db.session.commit()

            return redirect(url_for('site.profile'))
     except:
        raise Exception("Character not created, please check your form and try again!")
    
     

     characters = Character.query.filter_by(user_token=current_user.token).all()

    
     return render_template('profile.html', form=my_character, characters = characters )
     

