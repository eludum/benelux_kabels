from jinja2 import Environment, FileSystemLoader
env = Environment(loader = FileSystemLoader(["."]))

base = "_base.html"
sites = ["index.html", "projecten.html", "veiligheid.html", "producten.html", "contact.html"]

projects_gallery = [{'1': 'Trekken van zware vermogen-kabels op kabelbaan in Tessenderlo.'}]

products_gallery= [{'1': 'kabelrol'}]

for site in sites:
    template = env.get_template(site)
    rendered_template = template.render(base_template=base, projects_gallery=projects_gallery, products_gallery=products_gallery)

    with open("rendered/" + site, "w") as fh:
        fh.write(rendered_template)
