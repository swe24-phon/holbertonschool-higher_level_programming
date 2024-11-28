""" http.server example """
import http.server
import json

PORT = 8005


class MyHandler(http.server.BaseHTTPRequestHandler):
    """ Custom handler class """
    def do_GET(self):
        """ Handle GET requests """
        if self.path == '/data':
            # Sample dataset
            sample_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            # Set the response code and headers
            self.send_response(200)  # HTTP status code 200 (OK)
            self.send_header('Content-Type', 'application/json')  # Set content type to JSON
            self.end_headers()  # End headers
            # Write the JSON data as a response
            self.wfile.write(json.dumps(sample_data).encode('utf-8'))  # Convert dict to JSON and encode to bytes
        else:
            # Handle other paths
            self.send_response(404)  # HTTP status code 404 (Not Found)
            self.end_headers()  # End headers
            self.wfile.write(b'{"error": "Not found"}')  # Write error message

if __name__ == "__main__":
    # Create an HTTP server instance
    httpd = http.server.HTTPServer(('localhost', PORT), MyHandler)
    print(f"Serving on port {PORT}")  # Print server status
    httpd.serve_forever()  # Start the server