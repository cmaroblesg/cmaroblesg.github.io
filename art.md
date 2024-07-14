---
layout: default
title: Digital Art
permalink: /art/
---

<ul class="post-list">
  {% for post in site.art %}
    <li class="post">
      <h2 class="post-title"><a href="{{ post.url }}">{{ post.title }}</a></h2>
      <time class="post-date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %-d, %Y" }}</time>
      <p class="post-excerpt">{{ post.excerpt }}</p>
      <hr class="post-separator"/>
    </li>
  {% endfor %}
</ul>
