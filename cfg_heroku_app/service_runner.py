import requests
from  flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/") 
def hello():
    return render_template("hello.html")

@app.route("/sendmail", methods=["POST"])
def send_simple_message():
    form_data = request.form
    name = form_data["name"]
    email = form_data["email"]
    send_to = "{0} <{1}>".format(name, email)
    email_text = "Hello {0}, this is a mail from me".format(name)
    response = requests.post(
        "https://api.mailgun.net/v3/sandbox33bfee0c9fd742409d6f660a09cf5baf.mailgun.org/messages",
        auth=("api", "key-8e5c3b15664a6986af1bddd5545fd169"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox33bfee0c9fd742409d6f660a09cf5baf.mailgun.org>",
              "to": send_to,
              "subject": "Hello David",
              "text": email_text})
    return "Mail sent - {0}".format(response.text)

app.run()