from flask import Flask, request, jsonify
import random

app = Flask(__name__)


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


@app.route('/submit-verification-information', methods=['POST'])
def verify_information():
    user_information = request.get_json()
    fname= user_information["first_name"]
    lname= user_information["last_name"]
    idnumber= user_information["id_number"]

    if fname.upper()==FNAME and lname.upper()==LNAME and idnumber == ID:
        new_password = random.choice(animals)+str(random.randint(0,100))
        robj = {"return_string":"Your new password is "+new_password}
        return jsonify(robj)
    

if __name__ == "__main__":
    app.run(debug=False)