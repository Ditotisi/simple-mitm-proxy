
from mitmproxy import http


def request(flow: http.HTTPFlow):
    # Get the actual IP address of the connected client
    client_ip = flow.client_conn.peername[0]

    # Inject the original client IP
    flow.request.headers["X-True-Client-IP"] = "UNKNOWN"
    flow.request.headers["X-IS-EXTERNAL-REQUEST"] = "true"

