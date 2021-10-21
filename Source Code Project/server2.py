# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        queries = parse_qs(urlparse(self.path).query)
        self.log_message("%s", queries)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        s = queries.get("name")
        name = ""
        if s != None:
            name = s[0]
        #< converts to: &lt;
            name = name.replace("<", "&lt")
        #> converts to: &gt;
            name = name.replace(">", "&gt")
        # more than < and >, just write these 2 for demo

        self.wfile.write(bytes("<p>Input parameter: <text>%s<\text></p>" % name, "utf-8"))
        self.wfile.write(bytes("<p>This is a vulnerable web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
