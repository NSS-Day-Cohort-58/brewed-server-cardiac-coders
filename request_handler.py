import json
from http.server import BaseHTTPRequestHandler

class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def do_GET(self):
        """Handles GET requests to the server """
        pass

    def do_POST(self):
        """Handles POST requests to the server """
        pass
    
    def do_PUT(self):
        """Handles PUT requests to the server """
        pass

    def do_DELETE(self):
        """Handles DELETE requests to the server """
        pass