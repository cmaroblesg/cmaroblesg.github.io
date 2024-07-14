---
layout: home
title: Digital Art
permalink: /art/
---

<div class="post-list">
  {% for post in site.art %}
    <article class="post">
      <h2 class="post-title"><a href="{{ post.url }}">{{ post.title }}</a></h2>
      <h5><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %-d, %Y" }}</time></h5>
      <p>{{ post.excerpt }}</p>
    </article>
  {% endfor %}
</div>
