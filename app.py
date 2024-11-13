@app.route("/update_account/<int:id>", methods=["POST", "GET"])
def update_account(id):
    if 'user' not in session:
        return redirect(url_for('home'))

    # Get the account from the database
    account = Accounts.query.get(id)
    if not account:
        flash("Account not found.", "error")
        return redirect(url_for('home'))

    if request.method == "POST":
        account.account_name = request.form.get("account_name")
        account.balance = request.form.get("balance")

        try:
            db.session.commit()
            flash("Account updated successfully.", "success")
        except Exception as e:
            flash(f"Failed to update account: {e}", "error")
        return redirect(url_for('home'))

    return render_template("update_account.html", account=account)

