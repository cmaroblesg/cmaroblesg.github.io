---
layout: page
title: Docs
permalink: /docs/
---
In this section you could find some important documents related to my career as a researcher as well as a business professional.

* **Curriculum Vitae:** [CV-CesarRobles](/documents/CV/CV_CesarRobles.pdf){:target="_blank"}
* **Master Dissertation:** [Masters_Dissertation](/documents/Dissertations/Masters_Thesis.pdf){:target="_blank"}
* **PhD Dissertation:** [PhD_Dissertation](/documents/Dissertations/Doctorate_Thesis.pdf){:target="_blank"}

<table>
  {% for row in site.data.authors %}
    {% if forloop.first %}
    <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}

    {% tablerow pair in row %}
      {{ pair[1] }}
    {% endtablerow %}
  {% endfor %}
</table>
