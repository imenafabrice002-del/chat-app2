from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)
messages = []
ADMIN_NAME = "Imena"

HTML = """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>IMENA</title>
<style>
body{font-family:sans-serif;max-width:500px;margin:auto;padding:15px;background:#0f172a}
h1{text-align:center;color:#FFD700;font-size:32px;letter-spacing:3px;margin:5px}
p.sub{text-align:center;color:white;margin:0 0 15px}
.box{background:white;padding:15px;border-radius:15px;min-height:300px}
.msg{background:#dcf8c6;padding:8px 12px;border-radius:10px;margin:8px 0;display:flex;justify-content:space-between;align-items:center}
.admin{color:#d4a017;font-weight:bold}
.del{background:red;color:white;border:none;border-radius:5px;padding:4px 8px}
form{display:flex;gap:8px;margin-top:10px;flex-wrap:wrap}
input{flex:1;padding:12px;border-radius:20px;border:1px solid #ccc}
button{padding:12px 20px;background:#FFD700;border:none;border-radius:20px;color:black;font-weight:bold}
</style></head>
<body>
<h1>👑 IMENA</h1>
<p class="sub">Chat App | Admin: Imena</p>
<div class="box">
{% for i,m in messages %}
<div class="msg"><span><b {% if m[0]==admin %}class="admin"{% endif %}>{{m[0]}}{% if m[0]==admin %} 👑{% endif %}:</b> {{m[1]}}</span>
{% if current==admin %}<a href="/delete/{{i}}?name={{current}}"><button class="del">X</button></a>{% endif %}
</div>
{% endfor %}
{% if not messages %}<p style="color:#888">Murakaza neza kuri IMENA! Ba uwa mbere wanditse.</p>{% endif %}
</div>
<form method="POST">
<input name="name" placeholder="Izina ryawe" value="{{current}}" required>
<input name="text" placeholder="Andika message..." required>
<button>Send</button>
</form>
<p style="text-align:center;color:#ccc;font-size:12px">Admin: Andika izina Imena kugirango ubone buto yo gusiba</p>
</body></html>
"""

@app.route("/", methods=["GET","POST"])
def home():
    current = request.args.get("name","")
    if request.method == "POST":
        name = request.form.get("name","")
        text = request.form.get("text","")
        if name and text:
            messages.append((name, text))
        return redirect(f"/?name={name}")
    return render_template_string(HTML, messages=list(enumerate(messages)), admin=ADMIN_NAME, current=current)

@app.route("/delete/<int:id>")
def delete(id):
    name = request.args.get("name","")
    if name == ADMIN_NAME and 0 <= id < len(messages):
        messages.pop(id)
    return redirect(f"/?name={name}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
