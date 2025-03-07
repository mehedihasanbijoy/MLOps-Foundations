# Install Requirements
pip install -r requirements.txt


# FLASK FUNDAMENTALS:
    ## HTML Methods:
        - GET: To fetch data from the server (e.g. displaying a webpage). Read-only (does not change data) and idempotent (repeated calls have the same effect).
        - POST: To send data to the server to create a new resource (e.g. submitting a form / adding new item). Not idempotent.
        - PUT: To fully update an existing resource by replacing all fields. Idempotent (repeated calls with the same data don’t change the outcome).
        - PATCH: To partially update an existing resource by modifying specific fields. Not idempotent.
        - DELETE: To remove a resource from the server. Idempotent (deleting an already deleted resource has no effect).
        - HEAD: To retrieve only headers (no body). e.g. checking if a resource exists before making a GET request.
        - OPTIONS: To retrieve the HTTP methods allowed on a resource. e.g. checking what action can be performed on an endpoint.
    
    ## Render Template:
        - Renders an HTML template and injects dynamic data into it.
        - Separates Python logic from HTML (avoiding hardcoding HTML in Python files).
        - Supports Jinja2 templating (allows loops, conditions, and variables).
        
    ## Redirect:
        - Redirects the user to another URL
        - After form submissions, avoid duplicate form submissions.
        - Redirect users to different pages dynamically.
        
    ## Request:
        - Handles incoming HTTP request data (form data, query parameters, JSON, headers, etc.).
        - Access form input fields.
        - Read query parameters from URLs.
        - Handle file uploads.
        
    ## Session:
        - Stores user data across requests (e.g., login sessions).
        - Keep users logged in across pages.
        - Store temporary user preferences.
        
    ## Flash:
        - Displays temporary messages to users (e.g., error messages, success messages).
        - Show feedback messages after form submissions.
        - Notify users about errors or confirmations.
        
    ## Make Response:
        - Allows custom HTTP responses (set headers, cookies, etc.).
        - Modify response headers.
        - Attach cookies.
