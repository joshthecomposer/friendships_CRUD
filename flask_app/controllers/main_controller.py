from flask import flash, redirect, render_template, request
from flask_app import app
from flask_app.models import user, friendship

@app.route('/')
def index():
    return redirect('/friendships')

@app.route('/friendships')
def friendships():
    all_users = user.User.get_all_users()
    all_friendships = friendship.Friendship.get_all_friendships()
    return render_template('friendships.html', all_users=all_users, all_friendships=all_friendships)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name']
    }
    user.User.save(data)
    return redirect('/friendships')

@app.route('/create_friendship', methods=['POST'])
def create_friendship():
    if request.form['user'] == request.form['friend']:
        print('error user cannot be friends with themselves')
    else:
        data = {
            'user_id' : request.form['user'],
            'friend_id' : request.form['friend']
        }
        friendship.Friendship.create_friendship(data)
    return redirect('/friendships')
