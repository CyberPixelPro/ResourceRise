# Functions to generate html code from the data from mongodb

sub_html1 = """<div class="col">
                    <a href="/subject/{}">
                        <div class="card text-bg-primary mb-3 h-100" style="max-width: 18rem;">
                            <div id="card-body-pre"
                                class="d-flex align-items-center align-content-center justify-content-center">
                                <div class="card-body">
                                    <h5 class="card-title">{}</h5>
                                    <h6 class="card-subtitle mt-2">{}</h6>
                                </div>
                            </div>
                        </div>
                    </a>
                </div>"""

sub_html2 = """<div class="col">
                    <a href="/subject/{}">
                        <div class="card text-bg-primary mb-3 h-100 big-card1">
                            <div id="card-body-pre"
                                class="d-flex align-items-center align-content-center justify-content-center">
                                <div class="card-body">
                                    <h5 class="card-title">{}</h5>
                                    <h6 class="card-subtitle mt-2">{}</h6>
                                </div>
                            </div>
                        </div>
                    </a>
                </div>"""


def index_html_gen(subjects):
    subdiv1 = ""
    subdiv2 = ""

    for subject in subjects[:-2]:
        subdiv1 += sub_html1.format(
            subject["code"] + "-" + subject["name"], subject["name"], subject["code"]
        )
    for subject in subjects[-2:]:
        subdiv2 += sub_html2.format(
            subject["code"] + "-" + subject["name"], subject["name"], subject["code"]
        )

    return subdiv1, subdiv2


module_html = """<div class="col">
                    <a href="/module/{}">
                        <div class="card text-bg-primary mb-3">
                            <div id="card-body-pre"
                                class="d-flex align-items-center align-content-center justify-content-center">
                                <div class="card-body">
                                    <h5 class="card-title">Module {}</h5>
                                </div>
                            </div>
                        </div>
                    </a>
                </div>"""


def subject_html_gen(modules):
    html = ""
    for module in modules["modules"]:
        html += module_html.format(module + "-" + modules["name"], module.split("-")[1])
    return html


resource_html = """<div id="main-div" class="container-fluid">
        <div class="card text-center">
            <div class="card-header">
                <h4>{}</h5>
            </div>
            <div class="card-body">
                <div class="row row-cols-1 row-cols-md-1 g-1 subject-div">
                    {}
                </div>

            </div>
        </div>
    </div>"""

resource_inside_html = """<div class="col">
                    <a href="{}">
                        <div class="card text-bg-primary mb-3">
                            <div id="card-body-pre"
                                class="d-flex align-items-center align-content-center justify-content-center">
                                <div class="card-body">
                                    <h5 class="card-title">{}</h5>
                                </div>
                            </div>
                        </div>
                    </a>
                </div>"""


def module_html_gen(resources: dict):
    html = ""

    for key, val in resources.items():
        if key in ("_id", "name", "mid"):
            continue

        if key == "yt":
            html_inside = ""

            for i in val:
                html_inside += resource_inside_html.format(i[1], i[0].title())

            html += resource_html.format(key.upper(), html_inside)
        else:
            html_inside = ""

            for i in val:
                html_inside += resource_inside_html.format(
                    "/preview?url=" + i[1], i[0].title()
                )

            html += resource_html.format(key.upper(), html_inside)

    return html
