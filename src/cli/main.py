import argparse
from .. import renderer, parser
from flask import Flask, render_template

app = Flask("")

p = argparse.ArgumentParser(description="Compile a YAML file into HTML, and run it using Flask.")
p.add_argument("filepath", help="Path to the YAML file to compile")
p.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
p.add_argument("-port", type=int, default=8080, help="Port to run the server on (default: 8080)")
args = p.parse_args()

data = parser.load_yaml(args.filepath)
html = renderer.render_page(data)

output_path = "templates/output.html"
if args.debug:
    app.debug = True

with open(output_path, "w") as f:
    f.write(html)

print("Finished generating HTML!")

if __name__ == '__main__':
    app.run("0.0.0", args.port)