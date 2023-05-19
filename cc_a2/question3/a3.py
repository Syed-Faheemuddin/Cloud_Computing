from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# User class
class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password
        }

# Post class
class Post:
    def __init__(self, id, content, timestamp, user):
        self.id = id
        self.content = content
        self.timestamp = timestamp
        self.user = user

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'timestamp': self.timestamp,
            'user': self.user
        }

# In-memory data store for users and posts
users = []
posts = []

# UserController class
class UserController:
    # POST request to create a new user
    def create_user(self):
        data = request.get_json()
        id = len(users) + 1
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        user = User(id, username, email, password)
        users.append(user)
        return jsonify(user.to_dict())

    # GET request to retrieve a user by ID
    def get_user(self, user_id):
        user = self.find_user(user_id)
        if user is None:
            return {'error': 'User not found'}, 404
        return jsonify(user.to_dict())

    # Find user by ID
    def find_user(self, user_id):
        for user in users:
            if user.id == int(user_id):
                return user
        return None

# PostController class
class PostController:
    # POST request to create a new post
    def create_post(self):
        data = request.get_json()
        id = len(posts) + 1
        content = data.get('content')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user = data.get('user')
        post = Post(id, content, timestamp, user)
        posts.append(post)
        return jsonify(post.to_dict())

    # GET request to retrieve all posts
    def get_posts(self):
        return jsonify([post.to_dict() for post in posts])

# Create instances of controllers
user_controller = UserController()
post_controller = PostController()

# Routes for user-related operations
@app.route('/users', methods=['POST'])
def create_user():
    return user_controller.create_user()

@app.route("/users", methods=['GET')
def get_all_users():
    return jsonify(users.to_dict())

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    return user_controller.get_user(user_id)

# Routes for post-related operations
@app.route('/posts', methods=['POST'])
def create_post():
    return post_controller.create_post()

@app.route('/posts', methods=['GET'])
def get_posts():
    return post_controller.get_posts()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8002,debug=True)
