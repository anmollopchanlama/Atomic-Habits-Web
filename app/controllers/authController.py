from flask import render_template, redirect, request, url_for, flash

def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "admin" and password == "admin":
            flash("Logged in successfully!", "success")
            return redirect(url_for('auth.home'))
        flash("Invalid username or password.", "error")
        return redirect(url_for('auth.login'))
    return render_template('login.html')

def home():
    return render_template('home.html')

def about():
    return render_template('about.html')

def register():
    return render_template('register.html')