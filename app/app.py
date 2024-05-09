Sure! Here's a basic outline of a Python Flask API code that could be used to implement the credit check and pre-qualification process for loan applicants:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/credit-check', methods=['POST'])
def credit_check():
    data = request.json
    
    # Perform credit check and pre-qualification logic here
    
    # Calculate loan eligibility and interest rate range based on credit score and financial history
    
    # Generate pre-qualification outcome and explanation
    
    # Return pre-qualification result to the applicant
    return jsonify({'result': pre_qualification_result, 'explanation': pre_qualification_explanation})

if __name__ == '__main__':
    app.run()
```

In the above code, we define a Flask app and create a single route `/credit-check` to handle POST requests. Inside the `credit_check` function, we can access the JSON data sent in the request using `request.json`. You can perform the credit check and pre-qualification logic based on the provided data and calculate the loan eligibility and interest rate range.

Finally, you can generate the pre-qualification outcome and explanation and return it to the applicant as a JSON response using `jsonify`.

This is just a basic structure to get you started. You will need to add your own logic for credit check and pre-qualification, as well as handle data storage, authentication, and any other additional requirements specific to your project.