import sys
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)

##################################
##################################
#### Initializing the DB #####
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payday.db'
db = SQLAlchemy(app) # Need a way to initialize a db automatically... perhaps within this script...

# Table for user info
class User(db.Model):
    user_name        = db.Column(db.String, nullable=False, primary_key=True, default='NU')
    current_balance  = db.Column(db.Float, nullable=False, default=-999999999.99)
    #"***don't run***"
    ##########################################################################
    ##########################################################################
    # REMOVE primary_key AND REINITALIZE DB ... CANNOT ADD DUPLICATE USER INFO
    ##########################################################################
    ##########################################################################

# Table for user's expense info
class Expenses(db.Model):
    expense_name     = db.Column(db.String, primary_key=True)
    monthly_amount   = db.Column(db.Float, nullable=False)
    mandatory        = db.Column(db.String, nullable=False) # Would like to make Bool...
    amount_mandatory = db.Column(db.Float, nullable=False)  # Want to make this optional in case the expense is NOT mandatory.
    date_created     = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    user_name        = db.Column(db.String, nullable=False, default="NU")

    def __repr__(self):
        return f'<Expense {self.expense_name}, monthly amount = {self.monthly_amount}, mandatory expense = {self.mandatory}, amount_mandatory = {self.amount_mandatory}>'

#with app.app_context():
#    db.create_all()

#################################
#################################

sys.exit(" ----- Fix primary_key issue first ----- \n Exiting program now...")

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        user_name        = request.form['user_name']
        current_balance  = request.form['current_balance']
        expense_name     = request.form['expense_name']
        monthly_amount   = request.form['monthly_amount']
        mandatory        = request.form['mandatory']
        amount_mandatory = request.form['amount_mandatory']

        new_expense = Expenses(expense_name=expense_name, 
                               monthly_amount=monthly_amount, 
                               mandatory=mandatory, 
                               amount_mandatory=amount_mandatory,
                               user_name=user_name)
        
        new_user    = User(user_name=user_name,
                           current_balance=current_balance)

        try:
            db.session.add(new_expense)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"There was an issue adding your expense: {e}" 
    else:
        expenses = Expenses.query.order_by(Expenses.date_created).all()
        return render_template("index.html", expenses=expenses)

@app.route('/delete/<string:expense_name>')
def delete(expense_name):
    expense_to_delete = Expenses.query.get_or_404(expense_name)

    try:
        db.session.delete(expense_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting your expense."

