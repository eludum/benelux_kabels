from jinja2 import Environment, FileSystemLoader
env = Environment(loader = FileSystemLoader(["."]))

base = "base.html"
sites = ["index.html", "projecten.html", "veiligheid.html", "contact.html"]

projects_gallery = [{'1': 'Trekken van zware vermogen-kabels op kabelbaan in Tessenderlo.',
                '2': 'Trekken van zware vermogen-kabels op kabelbaan in Dendermonde.',
                '3': 'Trekken en vastleggen van zware vermogen-kabels, aarding in sleuf en kabelbaan in Tessenderlo.',
                '4': 'Trekken en vastleggen van zware vermogen-kabels, aarding in sleuf en kabelbaan in Tessenderlo.'},
               {'1': 'Trekken van zware vermogen-kabels op kabelbaan in Tessenderlo.',
                '2': 'Trekken van zware vermogen-kabels op kabelbaan in Dendermonde.',
                '3': 'Trekken en vastleggen van zware vermogen-kabels, aarding in sleuf en kabelbaan in Tessenderlo.',
                '4': 'Trekken en vastleggen van zware vermogen-kabels, aarding in sleuf en kabelbaan in Tessenderlo.'},
               {'1': 'Trekken van zware vermogen-kabels op kabelbaan in Tessenderlo.',
                '2': 'Trekken van zware vermogen-kabels op kabelbaan in Dendermonde.',
                '3': 'Trekken en vastleggen van zware vermogen-kabels, aarding in sleuf en kabelbaan in Tessenderlo.',
                '4': 'Trekken en vastleggen van zware vermogen-kabels, aarding in sleuf en kabelbaan in Tessenderlo.'},
               {'1': 'Trekken van zware vermogen-kabels op kabelbaan in Tessenderlo.',
                '2': 'Trekken van zware vermogen-kabels op kabelbaan in Dendermonde.',
                '3': 'Trekken en vastleggen van zware vermogen-kabels, aarding in sleuf en kabelbaan in Tessenderlo.',
                '4': 'Trekken en vastleggen van zware vermogen-kabels, aarding in sleuf en kabelbaan in Tessenderlo.'},
               {'1': 'Trekken van zware vermogen-kabels op kabelbaan in Tessenderlo.',
                '2': 'Trekken van zware vermogen-kabels op kabelbaan in Dendermonde.',
                '3': 'Trekken en vastleggen van zware vermogen-kabels, aarding in sleuf en kabelbaan in Tessenderlo.',
                '4': 'Trekken en vastleggen van zware vermogen-kabels, aarding in sleuf en kabelbaan in Tessenderlo.'},]

for site in sites:
    template = env.get_template(site)
    rendered_template = template.render(base_template=base, projects_gallery=projects_gallery)

    with open("rendered/" + site, "w") as fh:
        fh.write(rendered_template)
