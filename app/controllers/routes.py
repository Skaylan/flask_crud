from flask import render_template, request, redirect, flash, session, url_for
from app import app
from app.models.forms.register_form import RegisterForm
from app.models.forms.login_form import LoginForm
from app.models.forms.add_item_form import AddItemForm
from app.models.tables.user import User
from app.models.tables.item import Item
from app.models.db_config import *
from app.controllers.config import *
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('user_page'))
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.password.data == form.confirm_password.data:
                hashed_password = generate_password_hash(form.password.data)
                try:
                    new_user = User(form.name.data, form.username.data.lower(), form.email.data.lower(), hashed_password)
                    db.session.add(new_user)
                    db.session.commit()
                    db.session.close()
                    flash('Usuario criado com sucesso!', category='success')
                except Exception as error:
                    print(error.__cause__)
                    if str(error.__cause__) == 'UNIQUE constraint failed: user.username':
                        flash('Nome de Usuario já existe', category='error')
                    elif str(error.__cause__) == 'UNIQUE constraint failed: user.email':
                        flash('Email já cadastrado!', category='error')
                        
            else:
                flash("Senhas não coincidem!", category='error')
    
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect('user_page')
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data.lower()
            password = form.password.data
            
            user_info = User.query.filter_by(username=username).first()
            if user_info == None:
                flash(f'Usuario informado não existe!', category='error')
            else:
                checked_password = check_password_hash(user_info.password_hash, password)
                if checked_password == False:
                    flash('Senha Incorreta!')
                elif username == user_info.username and checked_password == True:
                    session['user'] = username
                    session['id'] = user_info.id
                    return redirect(url_for('user_page'))
                    
        
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('id', None)
    session.pop('_flashes', None)
    return redirect(url_for('index'))


@app.route('/user_page', methods=['GET', 'POST'])
def user_page():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    form = AddItemForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            id = int(session['id'])
            title = str(form.title.data)
            desc = str(form.description.data)    
            try:
                new_item = Item(title=title, description=desc, owner_id=id, completed=False)
                db.session.add(new_item)
                db.session.commit()
                db.session.close()
                flash('Adicionado com Sucesso!', category='success')
                return redirect(url_for('user_page'))
            except Exception as error:
                print(error.__class__)
            
    # items = Item.query.filter_by(owner_id=session['id']).all().order_by(Item.posted_at.desc())
    items = Item.query.filter_by(owner_id=session['id']).order_by(Item.created_at.desc()).all()
    return render_template('user_page.html', form=form, items=items)



@app.route('/delete_item', methods=['POST'])
def delete_item():
    if request.method == 'POST':
        item_id = request.form['item_id']
        
        try:
            delete = Item.query.filter_by(id=item_id).first()
            db.session.delete(delete)
            db.session.commit()
            db.session.close()
        except Exception as error:
            print(error.__class__)
            
    return redirect(url_for('user_page'))


@app.route('/edit_item', methods=['POST'])
def edit_item():
    if request.method == 'POST':
        
        id = request.form['item_id']
        title = request.form['title']
        description = request.form['description']
        
        item = Item.query.filter_by(id=id).first()
        item.title = title
        item.description = description
        db.session.commit()
        db.session.close()
        return redirect(url_for('user_page'))
        
        
    return redirect(url_for('user_page'))


@app.route('/complete_task', methods=['POST'])
def complete_task():
    if request.method == 'POST':
        id = request.form['complete_task_id']
        complete_value = request.form['complete_value']
        
        if complete_value == 'False':
            try:
                item = Item.query.filter_by(id=id).first()
                item.completed = True
                db.session.commit()
                db.session.close()
            except Exception as error:
                print(error.__cause__)
        
    return redirect(url_for('user_page'))
