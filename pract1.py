#!/usr/bin/python
# -*- coding: utf-8 -*-
import webapp

class urlApp(webapp.webApp):
    url = {}
    urlAcort = {}
    indx = 1

    def parse(self,request):
        method = request.split(' ',2)[0]
        recurso = request.split(' ',2)[1]
        if method == 'POST':
            body = request.split('\r\n\r\n',1)[1]
            body = body.split("=")[1].replace("+", " ")
        elif method == 'GET':
            body = ""
        return( method , recurso , body)

    def process(self, parsedRequest):
        (method, recurso, body) = parsedRequest

    # Relizamos el formulario
        form = '<form action = "" method = "POST">'
        form += 'Acorta la URL : <input type = "text" name = "valor">'
        form += '<input type = "submit" value= "Acorta"></form>'
        if method == "GET":
            recursoCorto = recurso.split('/',1)[1]
            if recurso == "/":
                returnCode = "200 OK"
                htmlAnswer = '<html><body><font color = "blue">' + form + "</font>"
                htmlAnswer += "URL almacenadas" +"<li>" +  str(self.url) +"</li></body></html>"
                return (returnCode , htmlAnswer)
            else:
                try:
                    if recursoCorto == self.url[body]:

                        redirrc = self.urlAcort[self.index]
                        returnCode = "302 URL Redirection"
                        htmlAnswer = "<html><body><meta http-equiv='refresh'content='1 url=" + redirrc + "'>"+"</body></html>"

                except ValueError :
                    returnCode = "404 Not Found"
                    htmlAnswer = "<html><body>Error : Not Found,  try again (Value error)</body></html> "
                    return (returnCode , htmlAnswer)

        elif method == "POST":

            if body == "":
                returnCode = "404 not found"
                htmlAnswer = "<html><body> Introduce una URL</body></html>"
                return (returnCode, htmlAnswer)

            else:
                body = body.split("%3A%2F%2F")[0] + "://" + body.split("%3A%2F%2F")[1]
                while body.find("%2F") != -1:
                    body = body.replace("%2F", "/")

                if body in self.url:
                    indx = self.url[body]
                    print str(self.url[body]) + " Estoy en el metodo post"

                else:
                    indx = self.indx
                    self.indx = self.indx + 1

                self.url[body] = indx
                self.urlAcort[self.indx] = body
                print str(self.url[body]) + " Estoy antes del return "
                returnCode = "200 OK"
                htmlAnswer = "<html><body>URL original : <a href ='"+ str(body)+"'>" + str(body)+"</a>"
                htmlAnswer += "<p> URL acortada :<a href ='"+str(body)+"'>" + str(indx) + "</a></p></body></html>"
                return (returnCode , htmlAnswer)



if __name__ == "__main__":
    testWebApp = urlApp("localhost",2312)
