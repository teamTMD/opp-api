# Modules: 

## User Authentication Module: 
* User Login: 
    * Receives user credentials
    * Verifies credentials against data stored on database
    * Generates and returns authentication tokens upon successful verification
    * If authentication fails, passes information to the front end to notify the user of incorrect login information 
## User Registration: 
* If user is not already registered: 
    * Requests user-provided information from front-end 
    * Validates that data is not already stored in database (ie. user already exists)
    * If new user, validates and stores new user data on database
    * Issues authentication token for newly registered user
## Data Processing Module: 
* Data Validation: 
    * Checks for Credit or Debit
## Transaction Logging Module:
* Receives card details and transaction amount
* Processes payment based on credit/debit requirements
* Logs transaction details including User ID, Merchant ID, amount, and balances
* Initiates payment processing logic
## Payment Gateway Module: 
* Receives card details and processes based on Debit/Credit
   * Debit Card:
     * Prior to processing purchase, validate that debit cards have enough funds to cover the cost of a purchase by checking current balance in the back end database
      * Instantly processed and do not have to wait for an arbitrary amount of time to clear the banking system, this amount should be instantly deducted from the database
   * Credit Card:
        * Credit card purchases have a minimum of two calendar days while in processing. For at least the first two days of being processed, credit card purchases are considered to be "in-processing" and thus should not be deducted from balance amount in database. Once two days have passed, that credit card purchase is considered "processed" and should be processed by the database and deducted from the account
* Validate all card numbers before processing against Lund algorithm 
## Balances Module:
* Manages balances after completed and pending transactions
* Keeps track of funds received and disbursed
* Calculates balances for a certain time period
## Security Module:
* Implements algorithms to encrypt data that is exchanged over the network
## Notification Module:
* Sends notifications to users and merchants about transaction status.
## Card Tokenization Module:
* Tokenizes and securely stores card information using Lund Algorithm
* Reduces the risk associated with storing sensitive card data by using encryption
## API and Integration Module:
* Defines APIs for seamless integration with third-party systems.
* Allows merchants to integrate the payment system into their applications
