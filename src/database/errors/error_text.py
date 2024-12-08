class ErrorForms:
    error_message = "This is a static variable"
    could_not_verify= "could not verify"
    login_required="Basic auth='Login required'"
    token_missing ="'Token is missing!'"
    envalid_credential = "Invalid credentials"


class ErrorNumber:
    bad_request = 400
    unauthorized = 401
    forbidden = 403
    not_found = 404
    method_not_allowed = 405
    internal_server_error = 500
    service_unavailable = 503
    