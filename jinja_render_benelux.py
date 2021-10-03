from jinja2 import Environment, Template, FileSystemLoader
env = Environment(loader = FileSystemLoader(["."]))

t = env.get_template("index.html")
print(t.render(base_template="base.html"))

t = env.get_template("projecten.html")
print(t.render(base_template="base.html"))

t = env.get_template("veiligheid.html")
print(t.render(base_template="base.html"))

t = env.get_template("contact.html")
print(t.render(base_template="base.html"))

