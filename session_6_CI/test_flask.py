import pytest
import numpy as np
from hello import pancakes



# purpose of fixture is to create resources that can be shared across tests

# pytest fixture for connecting to a database
#@pytest.fixture
#def db_connection():
#	# Simulate a database connection
#	connection = "Database connection established"
#	yield connection
#	# Teardown code
#	connection = None
#	print("Database connection closed")


## use the fixture in a test
#def test_db_connection(db_connection):
#	assert db_connection == "Database connection established"


#@pytest.fixture
#def create_something():
#	return "something"


#def testing_wednesday(create_something):
#	assert create_something == "something"



@pytest.fixture
def client():
	"""Create a test client for the Flask application."""
	return pancakes.test_client() # test_client() is a method provided by Flask to create a test client for the application.


def test_my_first_flask_function(client):

	response = client.get('/hello')

	assert response.status_code == 200, "Expected status code 200, got {}".format(response.status_code)

	assert response.json == {"message": "Hello, World!"}, "Expected JSON response does not match actual response."


def test_main_predict_function(client):

		payload1 = { "Gender": "Male", "Married": "Unmarried", "Credit_History": "Cleared Debts", "ApplicantIncome": 50000, "LoanAmount": 500000000 }

		response = client.post('/predict', json=payload1)

		assert response.status_code == 200, "Expected status code 200, got {}".format(response.status_code)
		assert response.json == {"loan_approval_status": "Loan Rejected"}, "Expected loan rejected status does not match actual status."

		payload2 = { "Gender": "Male", "Married": "Unmarried", "Credit_History": "Cleared Debts", "ApplicantIncome": 50000, "LoanAmount": 5 }

		response = client.post('/predict', json=payload2)
		assert response.status_code == 200
		assert response.json == {"loan_approval_status": "Loan Approved"}, "payload2 failed"

		for _ in range(100):
			rng_payload = { "Gender":  np.random.choice(["Male", "Female"]),
							"Married": np.random.choice(["Married", "Unmarried"]),
							"Credit_History": np.random.choice(["Cleared Debts", "Uncleared Debts"]),
							"ApplicantIncome": np.random.randint(1000, 100000),
							"LoanAmount": np.random.randint(1000, 1000000) }
			
			response = client.post('/predict', json=rng_payload)
			assert response.status_code == 200, f"Expected status code 200, got {response.status_code} for payload: {rng_payload}"
			assert response.json in [{"loan_approval_status": "Loan Approved"}, {"loan_approval_status": "Loan Rejected"}], \
				f"Unexpected response for payload: {rng_payload}. Response: {response.json}"

#======================================================================= warnings summary =======================================================================
#test_flask.py::test_main_predict_function
#  /Users/shivam13juna/Documents/virtual_envs/appy/lib/python3.9/site-packages/sklearn/base.py:493: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
#    warnings.warn(

#-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html