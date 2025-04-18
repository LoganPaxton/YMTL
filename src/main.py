from parser import load_yaml
from renderer import render_page
from flask import render_template, Flask

app = Flask(import_name="app")
app.debug = True

@app.route("/")
def root():
    return render_template("output.html")

if __name__ == '__main__':
    data = load_yaml("examples/sample.yaml")
    html = render_page(data)

    with open("templates/output.html", "w") as f:
        f.write(html)
    
    print("Finished generating HTML!")

    app.run(host="0.0.0.0", port=8080)