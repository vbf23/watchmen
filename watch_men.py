from flask import Flask, request, render_template_string, make_response
from datetime import datetime

app = Flask(__name__)

index_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Interaction Page</title>
</head>
<body>
    <h1>User Information</h1>
    <p>IP Address: {{ ip_address }}</p>
    <p>Timestamp: {{ timestamp }}</p>
    <p>Cookie Information: {{ cookie_info }}</p>
    <p>Visit Count: {{ visit_count }}</p>
</body>
</html>
"""

@app.route("/")
def index():
    ip_address = request.remote_addr
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get or initialize the visit count from the cookie
    visit_count = int(request.cookies.get('visit_count', 0))
    visit_count += 1

    # Set the updated visit count in the response cookie
    response = make_response(render_template_string(index_template, ip_address=ip_address, timestamp=timestamp, cookie_info=request.headers.get("Cookie", "No cookies"), visit_count=visit_count))
    response.set_cookie('visit_count', str(visit_count), max_age=60 * 60 * 24 * 7)  # Expires in 7 days

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
