from flask import Flask, request
import joblib


pancakes = Flask(__name__)

#flask --app hello.py run
#curl --location 'http://127.0.0.1:5000/'


@pancakes.route('/', methods=['GET'])
def index():
	"""
	A very fancy animated webpage with vibrant colors and beautiful animations.
	"""
	return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vibrant Animation</title>
  <style>
	body {
	  margin: 0;
	  padding: 0;
	  background: linear-gradient(45deg, #ff0066, #ffcc00, #33cc33, #0099ff);
	  background-size: 600% 600%;
	  animation: gradientAnimation 16s ease infinite;
	  font-family: 'Arial', sans-serif;
	  display: flex;
	  justify-content: center;
	  align-items: center;
	  height: 100vh;
	  color: white;
	}
	@keyframes gradientAnimation {
	  0% { background-position: 0% 50%; }
	  50% { background-position: 100% 50%; }
	  100% { background-position: 0% 50%; }
	}
	.content {
	  text-align: center;
	}
	.title {
	  font-size: 3em;
	  margin-bottom: 20px;
	  animation: fadeIn 2s ease backwards;
	}
	.subtitle {
	  font-size: 1.5em;
	  animation: fadeIn 3s ease backwards;
	}
	@keyframes fadeIn {
	  from { opacity: 0; transform: translateY(20px); }
	  to { opacity: 1; transform: translateY(0px); }
	}
  </style>
</head>
<body>
  <div class="content">
	<div class="title">Welcome to Docker Session!</div>
	<div class="subtitle">Let's learn how to create docker container for my application.</div>
  </div>
</body>
</html>
'''


@pancakes.route('/hello', methods=['GET'])
def hello_name():
	name = request.args.get('name', 'World')
	return {"message": f"Hello, {name}!"}

# sample url can e like this:
# http://localhost:5000/hello?name=John

# curl request
# curl --location 'http://localhost:5000/hello?name=John'


clf = joblib.load('classifier.pkl')


@pancakes.route('/predict', methods=['POST'])
def predict():

	loan_req = request.get_json()

	if loan_req['Gender'] == "Male":
		Gender = 0
	else:
		Gender = 1

	if loan_req['Married'] == "Unmarried":
		Married = 0
	else:
		Married = 1

	if loan_req['Credit_History'] == "Uncleared Debts":
		Credit_History = 0	
	else:
		Credit_History = 1


	ApplicantIncome = loan_req['ApplicantIncome']

	LoanAmount = loan_req['LoanAmount']

	result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

	if result == 0:
		result = "Loan Rejected"
	else:
		result = "Loan Approved"

	return {"loan_approval_status": result}

""""
curl --location 'http://127.0.0.1:5000/predict' \
--header 'Content-Type: application/json' \
--data '{   "Gender": "Male",
   "Married": "Unmarried",
   "Credit_History": "Cleared Debts",
   "ApplicantIncome": 50000, 
   "LoanAmount": 500000000
   
   }'

   """