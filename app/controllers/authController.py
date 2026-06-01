from flask import render_template, redirect, request, url_for, flash, session
from app.database import get_connection
from app.auth import login_required, admin_required

def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        
        if user:
            session['username'] = user['username']
            session['role'] = user['role']
            if user['role'] == 'admin':
                return redirect(url_for('auth.admin_dashboard'))
            else:
                return redirect(url_for('auth.user_dashboard'))
        else:
            flash("Invalid username or password.", "error")
            return redirect(url_for('auth.login'))
    return render_template('login.html')

@admin_required
def admin_dashboard():
    return render_template('admin_dashboard.html')

@login_required
def user_dashboard():
    return render_template('user_dashboard.html')

def home():
    return render_template('home.html')

def about():
    return render_template('about.html')

def register():
    return render_template('register.html')