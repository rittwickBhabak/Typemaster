# app.py
from myproject import app, db
from flask import Flask, render_template, redirect, flash, url_for, request, abort, session
from flask_login import login_user, login_required, logout_user
from myproject.models import User, PracticeLine, Exercise
from myproject.forms import LoginForm, RegistrationForm

@app.route('/')
def index():
    if session['current_user_id_typemaster'] is not None:
        return redirect(url_for('exercise'))
    return render_template('index.html')

@app.route('/dashboard')
@login_required
def dashboard():
    user_id = session['current_user_id_typemaster']
    level = User.query.get(user_id).level 
    passedText = []
    for i in range(level):
            ex = Exercise.query.filter_by(user_id=user_id,line_id=i).first()
            if ex is not None:
                passedText.append([i+1,PracticeLine[i],ex.speed,ex.error])
            else:
                passedText.append([i+1,PracticeLine[i],'--','--'])
    futureText = []
    for i in range(level,len(PracticeLine)):
        futureText.append([i+1,PracticeLine[i],'--','--'])
    return render_template('dashboard.html', passedText=passedText, futureText=futureText)
    

@app.route('/exercise', methods=['GET', 'POST'])
@login_required
def exercise():
    user = User.query.get(session['current_user_id_typemaster'])
    if request.method=="POST":
        lesson = user.level
        wpminput = request.form['wpm']
        typoinput = request.form['typo']
        exerciseId = int(request.form['exerciseId']) - 1
        practiceText = PracticeLine[user.level]
        status = 'Pass'
        clas = 'success'
        new_ex = Exercise(session['current_user_id_typemaster'],exerciseId,wpminput,typoinput)
        update_check = Exercise.query.filter_by(user_id=session['current_user_id_typemaster'],line_id=exerciseId).first()
        if update_check is not None:
            update_check.speed = wpminput
            update_check.error = typoinput
            db.session.add(update_check)
            db.session.commit()
            print('UPDATE-----------------------------------------')
        else:
            db.session.add(new_ex)
            db.session.commit()
            print('CREATE-----------------------------------------')
        if float(wpminput) <10:
            msg = 'Too slow. WPM must be greater than 10'
            status = 'Fail'
            clas='danger'
        if int(typoinput) >=3:
            msg = 'Too many typo. Typo must be less than 3'
            status = 'Fail'
            clas='danger'
        if status=='Pass':
            # update user level
            user = User.query.get(session['current_user_id_typemaster'])
            print('ExerciseId:========================================================== ',exerciseId)
            if user.level<len(PracticeLine) and user.level==exerciseId:
                print('User level will increace in this block')
                user.level = user.level + 1
                db.session.add(user)
                db.session.commit()
                lesson = lesson + 1

            msg = f"WPM: {wpminput} and TYPO: {typoinput}"
        print('Current level of user is: ', user.level)
        return render_template('transitionpage.html', msg=msg, status=status, clas=clas, exerciseId= exerciseId+1)
    
    else:
        practiceText = PracticeLine[user.level]
        return render_template('exercise.html', practiceText=practiceText, lesson = user.level+1)

@app.route('/customexercise/<int:exerciseid>',methods=['GET','POST'])
@login_required
def customexercise(exerciseid):
    level = User.query.get(session['current_user_id_typemaster']).level
    if level>=exerciseid:
        return render_template('exercise.html', practiceText=PracticeLine[exerciseid], lesson = exerciseid+1)
    else:
        return render_template('exercise.html', practiceText=PracticeLine[level], lesson = level+1)



@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data 
        email = form.email.data 
        username = form.username.data 
        password = form.password.data 
        confirm_password = form.pass_confirm.data 
        print(name,email,username,password,confirm_password)
        user_mail_check = User.query.filter_by(email=email).first()
        user_name_check = User.query.filter_by(username=username).first()
        name = name.strip()
        email = email.strip()
        username = username.strip()
        check_pass = password.strip()
        passlen = len(password)
        if name=='' or email=='' or username=='' or password=='':
            flash('Name, email, username, password can not be blank', 'danger')
            return render_template('register.html', form=form)
        if (user_mail_check is not None) or (user_name_check is not None) or not password==confirm_password:
            flash('Username and email both must be unique and password should match with confirm passowrd','danger')
            return render_template('register.html', form=form)
        if passlen<8 or check_pass=='':
            flash('Password can not be less than 8 character', 'danger')
            return render_template('register.html', form=form)

        db.session.add(User(name,email,username,password))
        db.session.commit()
        flash('Registration successful', 'success')
        return redirect(url_for('login'))
        
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data 
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            session['current_user_id_typemaster'] = user.id
            flash('Welcome '+user.name, 'primary')
            return redirect(url_for('index'))
        else:
            flash('Some error occoured', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    session['current_user_id_typemaster'] = None
    flash('See you soon', 'success')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)