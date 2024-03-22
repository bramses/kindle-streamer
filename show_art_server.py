'''
a local server that displays art on a webpage full screen.
art is generated using the create_art function from create_Art.py
and is stored in the ./output/art folder.
we want to show the latest art generated on the server.
'''
from flask import Flask, send_file, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <html>
        <head>
            <style>
                #art {
                    transition: opacity 1s ease-in-out;
                }
            </style>
        </head>
        <body>
            <img id="art" src="/art" />
            <script>
                setInterval(function(){
                    var art = document.getElementById('art');
                    art.style.opacity = 0;
                    setTimeout(function() {
                        art.src = "/art?" + new Date().getTime();
                        art.onload = function() {
                            art.style.opacity = 1;
                        }
                    }, 1000);
                }, 3000);
            </script>
        </body>
    </html>
    """)

@app.route("/art")
def show_art():
    art_files = os.listdir("./output/art")
    if len(art_files) > 0:
        latest_art = sorted(art_files)[-1]
        return send_file(f"./output/art/{latest_art}")
    else:
        return "No art found."
    
if __name__ == "__main__":
    app.run(port=5000)