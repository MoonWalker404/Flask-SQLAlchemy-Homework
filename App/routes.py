from flask import render_template, redirect, url_for, flash, request
from App import app, db
from App.forms import EditProfileForm
from App.models import User

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        user = User.query.first()  # Для простоты, работаем с первым пользователем
        user.name = form.name.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        user = User.query.first()  # Для простоты, работаем с первым пользователем
        form.name.data = user.name
        form.email.data = user.email
    return render_template('edit_profile.html', form=form)
