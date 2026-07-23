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
            session['id'] = user['id']
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
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('admin_dashboard.html', users=users)

@login_required
def user_dashboard():
    return render_template('user_dashboard.html')

def home():
    return render_template('home.html')

def about():
    return render_template('about.html')

def register():
    if request.method == "POST":
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return redirect(url_for('auth.register'))

        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO users (first_name, last_name, username, email, password, role) VALUES (%s, %s, %s, %s, %s, 'user')",
                (first_name, last_name, username, email, password)
            )
            connection.commit()
            cursor.close()
            connection.close()
            flash("Account created! Please sign in.", "success")
            return redirect(url_for('auth.login'))
        except Exception as e:
            print(e)
            flash("Username or email already exists.", "error")
            return redirect(url_for('auth.register'))

    return render_template('register.html')


def habits():
    if 'id' not in session:
        return redirect(url_for('auth.login'))
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM habits WHERE user_id = %s", (session['id'],))
    habits = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('habits.html', habits=habits)


def add_habit():
    if 'id' not in session:
        return redirect(url_for('auth.login'))
    name = request.form.get('habitName')
    identity = request.form.get('habitIdentity')
    icon = request.form.get('habitIcon')
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO habits (user_id, name, identity, icon) VALUES (%s, %s, %s, %s)",
        (session['id'], name, identity, icon)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('auth.habits'))



def delete_habit(habit_id):
    if 'id' not in session:
        return redirect(url_for('auth.login'))
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM habits WHERE id = %s AND user_id = %s", (habit_id, session['id']))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('auth.habits'))

def edit_habit(habit_id):
    if 'id' not in session:
        return redirect(url_for('auth.login'))
    connection = get_connection()
    cursor = connection.cursor()
    if request.method == "POST":
        name = request.form.get('habitName')
        identity = request.form.get('habitIdentity')
        icon = request.form.get('habitIcon')
        cursor.execute(
            "UPDATE habits SET name=%s, identity=%s, icon=%s WHERE id=%s AND user_id=%s",
            (name, identity, icon, habit_id, session['id'])
        )
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('auth.habits'))
    cursor.execute("SELECT * FROM habits WHERE id=%s AND user_id=%s", (habit_id, session['id']))
    habit = cursor.fetchone()
    cursor.close()
    connection.close()
    return render_template('edit_habit.html', habit=habit)

def logout():
    session.clear()
    return redirect(url_for('auth.login'))