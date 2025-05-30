from flask import Flask, url_for, redirect, render_template_string

app = Flask(__name__)

# Route for the homepage


@app.route('/')
def index():
    return 'Welcome to the homepage!'

# Route for login page


@app.route('/login')
def login():
    return 'Please log in.'

# Route with a variable part: username


@app.route('/user/<username>')
def profile(username):
    return f"User profile page of {username}"

# Route that redirects to the profile page using url_for


@app.route('/go-to-profile/<username>')
def go_to_profile(username):
    # Build the URL for the profile page dynamically
    profile_url = url_for('profile', username=username)
    return redirect(profile_url)

# Route that renders a template with links using url_for


@app.route('/links')
def links():
    # Using url_for inside a template string
    template = '''
    <h1>Useful Links</h1>
    <ul>
        <li><a href="{{ url_for('index') }}">Home</a></li>
        <li><a href="{{ url_for('login') }}">Login</a></li>
        <li><a href="{{ url_for('profile', username='Alice') }}">Alice's Profile</a></li>
    </ul>
    '''
    return render_template_string(template)


if __name__ == '__main__':
    app.run(debug=True)
