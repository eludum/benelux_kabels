from jinja2 import Environment, FileSystemLoader
env = Environment(loader = FileSystemLoader(["."]))

base = "base.html"
sites = ["index.html", "projecten.html", "veiligheid.html", "contact.html"]

projects_gallery = [{'1': 'Trekken van zware vermogen-kabels op kabelbaan in Tessenderlo.',
                '2': 'Trekken van zware vermogen-kabels op kabelbaan in Dendermonde.',
                '3': 'Trekken en vastleggen van zware vermogen-kabels, aarding in sleuf en kabelbaan in Tessenderlo.',
                '4': 'Trekken en vastleggen van zware vermogen-kabels, aarding in sleuf en kabelbaan in Tessenderlo.'},
               {'5': 'Trekken van FRECO kabels 4x240 mm in Amsterdam voor motoren.',
                '6': 'Trekken van FRECO kabels in Amsterdam.',
                '7': 'Trekken van verschillende secties kabels in Metalo Beerse.',
                '10': 'Grafen van een sleuf voor het trekken van verschillende vermogen kabels.'},
               {'11': 'Trekken van verschillende secties vermogen-kabels op kabelbaan in Metalo.',
                '12': 'Trekken en vastbinden van verschillende secties vermogen-kabels op kabelbaan in Metalo.',
                '16': 'Trekken en vastbinden van FRECO kabels op verticale kabelbaan in Amsterdam.',
                '21': 'Trekken en vastleggen van zware vermogen-kabels, aarding in sleuf en kabelbaan in Tessenderlo.'},
               {'17': 'De klant uit de nood helpen na een brand. Verschillende vermogen-kabels getrokken op kabelbaan.',
                '18': 'Een volledige bekabeling voor een project in Amsterdam is door onze werknemers mogelijk gemaakt.',
                '19': 'Trekken van  verschillende soorten kabels en secties voor een klant gelegen in Amsterdam.',
                '20': 'Trekken en vastbinden van FRECO kabels en signaalkabels in Amsterdam.'},
               {'23': 'Veilig afbakenen van een werkplaats en zorgen voor de algemene veiligheid.',
                '24': 'Trekken van verschillende soorten vermogen-kabels in Metalo.',
                '25': 'Trekken van verschillende soorten vermogen-kabels in Metalo.',
                '27': 'Trekken van EXAVB kabels voor een klant in Turnhout.'},
               {'28': 'Trekken van XGB kabels voor een medicatie magazijn in Tessenderlo.',
                '29': 'Trekken van verschillende vermogen-kabels op kabelbaan en caniveau.',
                '30': 'Trekken van EXAVB kabels voor een klant in Turnhout.',
                '31': 'Trekken van verschillende kabels op Arselor Mittal Gent.'},]

for site in sites:
    template = env.get_template(site)
    rendered_template = template.render(base_template=base, projects_gallery=projects_gallery)

    with open("rendered/" + site, "w") as fh:
        fh.write(rendered_template)
