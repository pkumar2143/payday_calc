from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payday1.db'
db = SQLAlchemy(app) # Need a way to initialize a db automatically... perhaps within this scrip...

class Todo(db.Model):
    expense_name     = db.Column(db.String, primary_key=True)
    monthly_amount   = db.Column(db.Float, nullable=False)
    mandatory        = db.Column(db.String, nullable=False) # Would like to make Bool...
    amount_mandatory = db.Column(db.Float, nullable=False) # Want to make this optional in case the expense is NOT mandatory.
    date_created     = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f'<Expense {self.expense_name}, monthly amount = {self.monthly_amount}, mandatory expense = {self.mandatory}, amount_mandatory = {self.amount_mandatory}>'

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        expense_name = request.form['expense_name']
        monthly_amount = request.form['monthly_amount']
        mandatory = request.form['mandatory']
        amount_mandatory = request.form['amount_mandatory']
        #return mandatory
        new_expense = Todo(expense_name=expense_name, monthly_amount=monthly_amount, mandatory=mandatory, amount_mandatory=amount_mandatory)

        try:
            db.session.add(new_expense)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding your expense"
        
        #return "Hello"
    else:
        expenses = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", expenses=expenses)

@app.route('/delete/<string:expense_name>')
def delete(expense_name):
    expense_to_delete = Todo.query.get_or_404(expense_name)

    try:
        db.session.delete(expense_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting your expense."

