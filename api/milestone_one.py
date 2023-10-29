from fastapi import FastAPI, Body 

app = FastAPI()

# Get a list of all transactions that comprise the total balance
@app.get("/api/transactions")
def get_transactions():
    transactions = []

    return {"msg": transactions}

# Post transactions
@app.post("/api/transactions")
def post_transactions(new_transaction = Body()):
    print(new_transaction)
    return {"msg": new_transaction}

# Update transactions
@app.put("/api/transactions")
def put_transactions(update_transaction = Body()):
    print(f"The transaction has been updated {update_transaction}")
    return {"msg": update_transaction}

# Get a list of all accounts receivables (i.e pending purchaes)
# Pending transactions is a field in the transaction table
@app.get("/api/transaction_info/pending_purchases")
def get_accounts_receivables():
    pending_purchases = []
    # Example of a curl command to test this api
    # curl 'http://api/transactions/pending_purchases/?pending_purchases=True'
    return {"msg": pending_purchases}


#Get a list of all the customer 
@app.get("/api/customers")
def get_customers():
    customers = []

    return {"msg": customers}

# Get a list of customers that are devs
# The dev is a SQL subclass of customer 
@app.get("/api/customers/devs")
def get_devs():
    devs = []
    return {"msg": devs}
# Create the dev
@app.post("/api/customers/devs")
def post_devs(new_dev = Body()):
    print(new_dev)
    return {"msg": new_dev}

# Update dev by customer id
@app.put("/api/customers/devs/{customer_id}")
def put_devs(customer_id: int, update_dev = Body()):
    print(f"The dev has been updated {update_dev}")
    return {"msg": update_dev}

# Delete the dev by customer id
@app.delete("/api/customers/devs/{customer_id}")
def delete_devs(customer_id: int):
    print(f"The dev has been deleted {customer_id}")
    return {"msg": customer_id}

# Get a list of all the customers that are business owners
# The business owner is a SQL subclass of customer
@app.get("/api/customers/business_owners")
def get_business_owners():
    business_owners = []
    return {"msg": business_owners}

# Create the business owner
@app.post("/api/customers/business_owners")
def post_business_owners(new_business_owner = Body()):
    print(new_business_owner)
    return {"msg": new_business_owner}

# Update business owner by customer id
@app.put("/api/customers/business_owners/{customer_id}")
def put_business_owners(customer_id: int, update_business_owner = Body()):
    print(f"The business owner has been updated {update_business_owner}")
    return {"msg": update_business_owner}

# Delete the business owner by customer id
@app.delete("/api/customers/business_owners/{customer_id}")
def delete_business_owners(customer_id: int):
    print(f"The business owner has been deleted {customer_id}")
    return {"msg": customer_id}

# Get all Debit Cards
@app.get("/api/debit_cards")
def get_debit_cards():
    debit_cards = []

    return {"msg": debit_cards}

# Create a Debit Card
@app.post("/api/debit_cards")
def post_debit_cards(new_debit_card = Body()):
    print(new_debit_card)
    return {"msg": new_debit_card}

# Update a Debit Card by paymentId
@app.put("/api/debit_cards/{paymentId}")
def put_debit_cards(paymentId: int, update_debit_card = Body()):
    print(f"The debit card has been updated {update_debit_card}")
    return {"msg": update_debit_card}

# Delete a Debit Card by paymentId
@app.delete("/api/debit_cards/{paymentId}")
def delete_debit_cards(paymentId: int):
    print(f"The debit card has been deleted {paymentId}")
    return {"msg": paymentId}


# Get all Credit Cards
@app.get("/api/credit_cards")
def get_credit_cards():
    credit_cards = []

    return {"msg": credit_cards}

# Create a Credit Card
@app.post("/api/credit_cards")
def post_credit_cards(new_credit_card = Body()):
    print(new_credit_card)
    return {"msg": new_credit_card}

# Update a Credit Card by paymentId
@app.put("/api/credit_cards/{paymentId}")
def put_credit_cards(paymentId: int, update_credit_card = Body()):
    print(f"The credit card has been updated {update_credit_card}")
    return {"msg": update_credit_card}

# Delete a Credit Card by paymentId
@app.delete("/api/credit_cards/{paymentId}")
def delete_credit_cards(paymentId: int):
    print(f"The credit card has been deleted {paymentId}")
    return {"msg": paymentId}