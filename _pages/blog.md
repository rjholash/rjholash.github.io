---
layout: default
permalink: /blog/
title: Stories
nav_title: Stories
nav: true
nav_order: 1
page_class: stories-page
pagination:
  enabled: true
  collection: posts
  permalink: /page/:num/
  per_page: 5
  sort_field: date
  sort_reverse: true
  trail:
    before: 1 # The number of links before the current page
    after: 3 # The number of links after the current page
---

<main class="stories-index">
  <header class="stories-header">
    <p class="eyebrow">Research · Students · Teaching</p>
    <h1>Stories from the lab</h1>
    <p>Updates and perspectives on muscle physiology, digital health, student research, and learning through experience.</p>
  </header>

  {% if site.display_categories.size > 0 %}
    <nav class="stories-categories" aria-label="Story categories">
      {% for category in site.display_categories %}
        <a href="{{ category | slugify | prepend: '/blog/category/' | relative_url }}">{{ category | replace: '-', ' ' | capitalize }}</a>
      {% endfor %}
    </nav>
  {% endif %}

  {% if page.pagination.enabled %}
    {% assign postlist = paginator.posts %}
  {% else %}
    {% assign postlist = site.posts %}
  {% endif %}

  <section class="stories-list" aria-label="Recent stories">
    {% for post in postlist %}
      {% assign read_time = post.content | number_of_words | divided_by: 180 | plus: 1 %}
      <article class="story-entry">
        <div class="story-entry__meta">
          <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%b %d, %Y' }}</time>
          {% if post.categories.size > 0 %}
            <div class="story-entry__categories">
              {% for category in post.categories limit: 2 %}
                <a href="{{ category | slugify | prepend: '/blog/category/' | relative_url }}">{{ category | replace: '-', ' ' }}</a>
              {% endfor %}
            </div>
          {% endif %}
        </div>
        <div class="story-entry__content">
          <h2>
            {% if post.redirect == blank %}
              <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
            {% elsif post.redirect contains '://' %}
              <a href="{{ post.redirect }}" target="_blank" rel="noopener">{{ post.title }} <span aria-hidden="true">↗</span></a>
            {% else %}
              <a href="{{ post.redirect | relative_url }}">{{ post.title }}</a>
            {% endif %}
          </h2>
          {% if post.description %}<p>{{ post.description }}</p>{% endif %}
          <span class="story-entry__read-time">{{ read_time }} min read</span>
        </div>
        <span class="story-entry__arrow" aria-hidden="true">→</span>
      </article>
    {% endfor %}
  </section>

  {% if page.pagination.enabled %}{% include pagination.liquid %}{% endif %}
</main>
