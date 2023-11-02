# Description of Potential Errors and Status Codes

Below are the following status codes that will be generated across the various requests. The status code will let us know if know if our request was successful or not with additional information. We expect to encounter the below status codes when running requests to our server.

* Status Code 200 OK: 
    - Additional Info: This means that the request was successful.

* Status Code 400 Bad Request: 
    - Potential Error: Bad request data, missing parameters, invalid input format
    - Additional Info: Our request was not successful, and the server cannot process it.

* Status Code 401 Unauthorized: 
    - Potential Error: Missing invalid headers or authentication credentials
    - Additional Info: The client did not provide valid credentials and needs to do so.

* Status Code 403 Forbidden:
    - Potential Error: User is missing necessary permissions to access the resource.
    - Additional Info:  The client does not have permission to access the requested resource. 

* Status Code 404 Not Found: 
    - Potential Error: The requested info does not exist on the server.
    - Additional Info: The requested resource could not be found on the server. 

* Status Code 500 Internal Server Error:
    - Potential Error: Server-side bug or database errors.
    - Additional Info: An error occurred on the server.
