from flask import Flask

# Create new application
app = Flask(__name__)

# Debugging is okay for now
app.debug = True

# Serves the main application
@app.route('/auth/requestToken')
def handleAuthTokenRequest():
    return ''

# Run the server if this file is run directly
if __name__ == '__main__':
    app.run()
