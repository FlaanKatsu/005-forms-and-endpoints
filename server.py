from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/question", methods=['POST'])
def server():
    skibidi = request.form
    print(skibidi)
    bingus = f"""
<!doctype html>
    <title> Form Result </title>
        <style>
              .result {{
                 color: blue;
                 font-size: 2em;
              }}
        </style>
<h2 style='color:red;'>你好，{skibidi['unang pangalan']}<h2>
<body>
    <div>
        Our school cafeteria has really {skibidi['in1']} food. just thinking about it makes me wanna {skibidi['in2']}.  the spaggetti is {skibidi['in3']} and tastes like {skibidi['in4']}. One day, I swear my meatballs started to {skibidi['in5']}! The turkey talcos are totally {skibidi['in6']} and look like {skibidi['in7']}. My friend Lihua actually likes the meatloaf, even though it's {skibidi['in8']} and {skibidi['in9']}. I like to call it "mystery meatloaf", and think it's likely made from {skibidi['in10']}. My dad said he'd make my lunches, but the first day, he made me a {skibidi['in11']} sandwitch with {skibidi['in4']} soup! I think I'd take my chances with the cafeteria.
    </div>
</body>
    """
    return bingus

app.run(port=25565)
