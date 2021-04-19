from flask import Flask, render_template, flash, request, url_for
from forms import RegistrationForm, AdminForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route("/", methods=['GET', 'POST'])
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash(f'The password is accepted', 'success')
            return render_template('register.html', title='Register', form=form), 200
        else:
            flash(f'The password is not accepted', 'danger')
            return render_template('register.html', title='Register', form=form), 403
    
    return render_template('register.html', title='Register', form=form), 200

@app.route("/", methods=['GET', 'POST'])
@app.route("/admin", methods=['GET', 'POST'])
def admin():
    form = AdminForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash(f'The password is accepted', 'success')
            return render_template('admin.html', title='Admin', form=form), 200
        else:
            flash(f'The password is not accepted', 'danger')
            return render_template('admin.html', title='Admin', form=form), 403
    
    return render_template('admin.html', title='Admin', form=form), 200

if __name__ == '__main__':
    app.run(debug=True)
