from flask import Flask, request, jsonify, send_from_directory
import random
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

well_known_dir = os.path.join(app.root_path, '.well-known')

FNAME, LNAME, ID = 'NIKHILESH', 'BELULKAR', 2
animals = ['Giraffe', 
           'Snake', 
           'Lion', 
           'Tiger', 
           'Gorilla', 
           'Fox', 
           'Kangaroo', 
           'Squirrel', 
           'Elephant', 
           'Crocodile']


@app.route('/.well-known/<path:filename>')
def well_known(filename):
    return send_from_directory(well_known_dir, filename)


@app.route('/submit-verification-information', methods=['POST'])
def verify_information():
    user_information = request.get_json()
    fname = user_information["first_name"]
    lname = user_information["last_name"]
    idnumber = user_information["id_number"]

    if fname.upper()==FNAME and lname.upper()==LNAME and idnumber == ID:
        new_password = random.choice(animals)+str(random.randint(0,100))
        robj = {"return_string":"Your new password is "+new_password}
        return jsonify(robj)
    
    return {}
    
if __name__ == "__main__":
    app.run(debug=False)