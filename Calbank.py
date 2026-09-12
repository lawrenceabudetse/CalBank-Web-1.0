from flask import Flask, redirect, request, url_for, render_template, flash

cal = Flask(__name__)
cal.secret_key = "Qwerty1234"

class Bank:
    def __init__(self, _balance):
        self._balance = _balance

balance = Bank(0)

@cal.route('/home')
@cal.route('/')
def home():
    return render_template('CalBank.html')
     
@cal.route('/deposit', methods = ['POST', 'GET'])
def deposit():
    if request.method == 'POST':
        try:
            amount = float(request.form["amount"])
            if amount <= 0:
                flash("Amount To Deposit Must Be Greater Than Zero")
                return render_template('deposit.html')
        
            balance._balance += amount
            flash(f"Your deposit was successful.You deposited {amount} Your current balance is {balance._balance}")
            return redirect(url_for('home'))
        except ValueError:
            flash("Please Enter A Valid Numerical Value")
            return render_template('deposit.html')
    return render_template('deposit.html')

@cal.route('/withdraw', methods=['POST', 'GET'])
def withdraw():
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            if amount <= 0:
                flash("Amount To Withdraw Must Be Greater Than Zero ")
                return render_template('withdraw.html')   
            if amount > balance._balance:
                flash("Insufficient Fund, Please Recharge!")
                return render_template('withdraw.html') 
            balance._balance -= amount
            flash(f"Withdrawal Successful!. You have withdraw {amount}, current balance is {balance._balance}")
            return redirect(url_for('home'))
        except ValueError:
            flash("Please Enter A Valid Numerical Value")
            return render_template("withdraw.html")
    return render_template('withdraw.html')
@cal.route('/check_balance')
def check_balance():
    return render_template('check_balance.html', current_balance = balance._balance)    

if __name__ == "__main__":
    cal.run(host='0.0.0.0', port='5000', debug=True, use_reloader=False)
