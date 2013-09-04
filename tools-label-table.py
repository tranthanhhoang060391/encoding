import json

def get_data(filename):
    return json.loads(open(filename, "r").read())

def create_table():
    data = get_data("encodings.json")
    table = ""
    labelsseen = []
    for set in data:
        table += " <tbody>\n  <tr><th colspan=2><a href=#" + set["heading"].lower().replace(" ", "-") + ">" + set["heading"] + "</a>\n"
        for encoding in set["encodings"]:
            rowspan = ""
            label_len = len(encoding["labels"])
            if label_len > 1:
                rowspan = " rowspan=" + str(label_len)

            table += "  <tr>\n   <td" + rowspan + "><span>" + encoding["name"] + "</span>"
            i = 0
            labels = encoding["labels"]
            labels.sort()
            for label in labels:
                if label in labelsseen:
                    raise NameError("Duplicate label: " + label)
                labelsseen.append(label)
                if i > 0:
                    table += "  <tr>"
                else:
                    table += "\n   "
                table += "<td>\"<code title>" + label + "</code>\"\n"
                i += 1
    print table

create_table()