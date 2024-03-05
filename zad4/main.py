from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
import json
from threading import Thread
from datetime import datetime



html_files={"message":r"C:\Users\pawel\Desktop\Nowy folder (6)\message.html",
            "index":r"C:\Users\pawel\Desktop\Nowy folder (6)\index.html",
            "error":r"C:\Users\pawel\Desktop\Nowy folder (6)\error.html",
            "save":r"C:\Users\pawel\Desktop\Nowy folder (6)\storage\data.json",
            "logo":r"C:\Users\pawel\Desktop\Nowy folder (6)\storage\logo.png"}


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open(html_files["index"], "rb") as file:
                self.wfile.write(file.read())
        elif self.path=="/message.html":
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            with open(html_files["message"], "rb") as file:
                self.wfile.write(file.read())
        elif self.path=="/logo":
            self.send_response(200)
            self.send_header("Content-type","htpp/text")
            self.end_headers()
            with open(html_files["logo"],"rb") as file:
                self.wfile.write((file.read()))
        else:
            self.send_error(404, "błą")
def run_serwer():
    serwer=("",3000 )
    htt=HTTPServer(serwer,RequestHandler)
    htt.serve_forever()
def echo_serwer():
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("localhost", 5000))
        s.listen(1)
        conn, addr= s.accept()
        with conn:
            while True:
                data=conn.recv(1024)
                if not data:
                    break
            save(data.decode())
def save(data):
    with open (html_files[save], "a") as file:
        json.dump(data, file)
        file.write("\n")


if __name__ == '__main__':
    http_thread = Thread(target=run_serwer)
    http_thread.start()

echo_serwer_thender= Thread(target=echo_serwer)
echo_serwer_thender.start()