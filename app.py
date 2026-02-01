# create webpage!

from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")

def home():

    return f"""
    <html>
    <head>
        <title>Valentine?</title>
        <style>
            body {{
                text-align: center;
                font-family: Arial;
                margin-top: 100px;
            }}

            #no-btn {{
                position: absolute;
                font-size: 20px;
                padding: 10px 30px;
            }}

            #yes-btn {{
                font-size: 20px;
                padding: 10px 30px;
                margin-right: 20px;
            }}
        </style>
    </head>

    <body>

        <img src="{url_for('static', filename='bob_minion.png')}" width="300">
        <h1>harry will you be my valentine?</h1>

        <a href="/yes">
            <button id="yes-btn">Yes!!!</button>
        </a>

        <a href="/no">
            <button id="no-btn">NO 💔</button>
        </a>

        <script>
            const noBtn = document.getElementById("no-btn");

            noBtn.addEventListener("mouseover", () => {{
                const x = Math.random() * (window.innerWidth - 100);
                const y = Math.random() * (window.innerHeight - 50);

                noBtn.style.left = x + "px";
                noBtn.style.top = y + "px";
            }});
        </script>
    </body>
    </html>
    """

@app.route("/yes")
def yes():
    return f"""
    <html>
    <body style="text-align:center; font-family:Arial; margin-top:100px;">
        
        <img src="{url_for('static', filename='b99.gif')}" width="500">
        <h1>YAY!! 🥰</h1>
    </body>
    </html>
    """

@app.route("/no")
def no():
    return f"""
    <html>
    <head>
        <title>Valentine?</title>
        <style>
            body {{
                text-align: center;
                font-family: Arial;
                margin-top: 100px;
            }}

            button {{
                transition: all 0.25s ease;
                margin: 20px;
            }}

            #no-btn {{
                font-size: 24px;
                padding: 15px;
            }}

            #yes-btn {{
                font-size: 24px;
                padding: 15px;
            }}
        </style>
    </head>

    <body>
        <h1>Are you sure????</h1>

        <button id="no-btn">No...</button>
        <button id="yes-btn">Yes, I'm sure.</button>

        <script>
            let noSize = 80;
            let yesSize = 24;

            const noBtn = document.getElementById("no-btn");
            const yesBtn = document.getElementById("yes-btn");

            // If they are NOT sure → go back home
            noBtn.addEventListener("click", () => {{
                window.location.href = "/";
            }});

            yesBtn.addEventListener("click", () => {{
                // Grow NO
                noSize += 15;
                noBtn.style.fontSize = noSize + "px";
                noBtn.style.padding = (noSize / 2) + "px";

                // Shrink YES
                yesSize -= 3;
                if (yesSize < 8) yesSize = 8;
                yesBtn.style.fontSize = yesSize + "px";
                yesBtn.style.padding = yesSize + "px";
                
            }});
        </script>
    </body>
    </html>
    """

@app.route("/not_sure")

def not_sure():

    return home()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)