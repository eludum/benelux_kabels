from jinja2 import Environment, Template, FileSystemLoader
env = Environment(loader = FileSystemLoader(["."]))

t = env.get_template("index.html")
index = t.render(base_template="base.html")

t = env.get_template("projecten.html")
projects = t.render(base_template="base.html")

t = env.get_template("veiligheid.html")
safety = t.render(base_template="base.html")

t = env.get_template("contact.html")
contact = t.render(base_template="base.html")

with open("rendered/index.html", "w") as fh:
    fh.write(index)

with open("rendered/projecten.html", "w") as fh:
    fh.write(projects)

with open("rendered/veiligheid.html", "w") as fh:
    fh.write(safety)

with open("rendered/contact.html", "w") as fh:
    fh.write(contact)
