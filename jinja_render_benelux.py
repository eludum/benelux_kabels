from jinja2 import Environment, Template, FileSystemLoader
env = Environment(loader = FileSystemLoader(["."]))

base = "base.html"
sites = ["index.html", "projecten.html", "veiligheid.html", "contact.html"]

for site in sites:
    template = env.get_template(site)
    rendered_template = template.render(base_template=base)

    with open("rendered/" + site, "w") as fh:
        fh.write(rendered_template)
