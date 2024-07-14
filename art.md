---
layout: default
title: Digital Art
permalink: /art/
---

<ul class="post-list">
  {%- assign date_format = site.date_format | default: "%b %-d, %Y" -%}
  {% for post in site.art %}
    <li class="post">
      <h2 class="post-title"><a href="{{ post.url }}">{{ post.title }}</a></h2>
      <p class="post-meta">
        <time class="post-date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %-d, %Y" }}</time></p>
      <p class="post-excerpt">{{ post.excerpt }}</p>
    </li>
  {% endfor %}
</ul>