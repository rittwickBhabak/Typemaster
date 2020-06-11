# app.py
from myproject import app, db
import random
import json
from flask import Flask, render_template, redirect, flash, url_for, request, abort, session
from flask_login import login_user, login_required, logout_user
from myproject.models import User, PracticeLine, Exercise, TestLines, TestResults
from myproject.forms import LoginForm, RegistrationForm

@app.route('/')
def index():
    if session.get('current_user_id_typemaster', None) is not None:
        return redirect(url_for('exercise'))
    return render_template('index.html')

@app.route('/weakkeys')
@login_required
def weakkeys():
    user = User.query.get(session['current_user_id_typemaster'])
    weakkeysObj = json.loads(user.weakKeys.replace("'",'"'))
    obj = []
    for key,value in weakkeysObj.items():
        obj.append([chr(int(key)),value])
    return render_template('weakkeys.html', weakKeys = obj)

def update_weakkeys(user_id, update_list):
    pass

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
    
@app.route('/analytics')
@login_required
def analytics():
    user_id = session['current_user_id_typemaster']
    testresults = TestResults.query.filter_by(user_id=user_id)
    result = []
    for ind,r in enumerate(testresults):
        print(str(int(r.speed)*2)+','+str(int(r.accuracy)*2))
        result.append([ind+1,int(r.speed)*2,int(r.accuracy)*2])
    return render_template('analytics.html', result = result)

@app.route('/testresult', methods=['POST'])
def testresult():
    if request.method=='POST' and session.get('current_user_id_typemaster',None) is not None:
        user_id = session['current_user_id_typemaster']
        speed = request.form['wpm']
        weakkeys = request.form['weakkeys']
        accuracy = request.form['accuracy']
        update = json.loads(weakkeys)
        user = User.query.filter_by(id = user_id).first()
        print(user.weakKeys)
        weakkeys = json.loads(user.weakKeys.replace("'",'"'))
        for key,values in weakkeys.items():
            weakkeys[key] += int(update[key])
        user.weakKeys = str(weakkeys)
        db.session.add(user)
        db.session.commit()
        db.session.add(TestResults(user_id,speed, accuracy))
        db.session.commit()
    if request.method=='POST':
        speed = request.form['wpm']
        accuracy = request.form['accuracy']

    
    msg = f"Your current speed is {speed} and accuracy is {accuracy}. You can increase your speed and accuracy amazingly using our app. Practice our lessons 10minutes daily and imporve your speed and accuracy. It's free."
    return render_template('testresult.html', msg=msg)

@app.route('/test')
def typetest():
    text = TestLines[random.randint(0,len(TestLines)-1)]
    return render_template('typetest.html', practiceText = text)

@app.route('/editprofile')
def editprofile():
    return render_template('editprofile.html')

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

@app.route('/dashboard/test-results')
@login_required
def testresults():
    user_id = session['current_user_id_typemaster']
    testresults = TestResults.query.filter_by(user_id=user_id)
    result = []
    for ind,r in enumerate(testresults):
        result.append([ind+1,r.speed,r.accuracy])
    return render_template('logtestresults.html', result = result)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return redirect(url_for('index'))
@app.errorhandler(405)
def method_not_allowed(e):
    # note that we set the 404 status explicitly
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(port=9999,debug=True)