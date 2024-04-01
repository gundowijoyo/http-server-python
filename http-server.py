#kita membutuhkan dua liblary di bawah ini
import os 
from http.server import BaseHTTPRequestHandler,HTTPServer
#'kita buat objek class di baaah ini'
class FileServerAll(BaseHTTPRequestHandler):
  def list_directory(self,path):
         try:
    #lanjut kita buat daftar file yg ada di dlm path
              files = os.listdir(path)
              #'kita buat daftar file make html
              html = "<ul>"
              for file in files:
                  html += f"<li><a href='{file}'>{file}</a></li>"
              html+= "</ul>"
              return html 
         except Exception as e:
               return f"Error: {str(e)}"
              
  def do_GET(self):
        try:
              
              path = '.'+self.path
              #kita buat kondisi jika path kita folder tampilin isi file ke browser
              if os.path.isdir(path):
                  html = self.list_directory(path)
                  self.send_response(200)
                  self.send_header("Content-type","text/html")
                  self.end_headers()
                  self.wfile.write(bytes(html,"utf-8"))
              else:
                      #jika path isinya file html.maka pas fi klik akan ngejalanin html
                      with open(path,"rb") as file:
                          content = file.read()
                          self.send_response(200)
                          self.send_header("Content-type","text/html")
                          self.end_headers()
                          self.wfile.write(content)
  #jika respon 404 maka tampil not fund
        except FileNotFoundError:
            self.send_error(404, 'File Not Found: %s' % self.path)
            #jika respon 500 internal server nya error
        except Exception as e:
            self.send_error(500, 'Internal Server Error: %s' % str(e))
            
def run(serverClass=HTTPServer, handle=FileServerAll, port=8000):
    serverAdd = ("", port)
    http = serverClass(serverAdd, handle)
    print(f'Server running on port {port}...')
    http.serve_forever()
       
if __name__ == "__main__":
    run()
