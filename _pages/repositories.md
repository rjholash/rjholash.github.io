---
layout: page
permalink: /repositories/
title: repositories
description: Open-source code repositories for exercise physiology, muscle modeling, and research tools developed at the Digital Athlete Lab.
nav: true
nav_order: 4
---

{% assign github_user = site.data.repositories.github_user %}

<a class="github-profile-card" href="https://github.com/{{ github_user.username }}" aria-label="View {{ github_user.name }} on GitHub">
  <span class="github-profile-icon" aria-hidden="true"><i class="fa-brands fa-github"></i></span>
  <span class="github-profile-copy">
    <span class="github-profile-name">{{ github_user.name }}</span>
    <span class="github-profile-handle">@{{ github_user.username }}</span>
    <span class="github-profile-bio">{{ github_user.bio }}</span>
  </span>
  <span class="github-profile-meta">
    <span><i class="fa-solid fa-location-dot" aria-hidden="true"></i> {{ github_user.location }}</span>
    <span><i class="fa-solid fa-code-branch" aria-hidden="true"></i> {{ github_user.public_repos }} public repositories</span>
  </span>
</a>

## GitHub Repositories

These repositories contain code and resources for exercise physiology research, muscle modeling, data analysis tools, and educational materials developed at the Digital Athlete Lab.

<div class="repository-grid">
  {% for repo in site.data.repositories.github_repos %}
    <a class="repository-card" href="https://github.com/{{ repo.repository }}" aria-label="View {{ repo.name }} on GitHub">
      <span class="repository-card-heading">
        <i class="fa-solid fa-book-bookmark" aria-hidden="true"></i>
        <span>{{ repo.name }}</span>
      </span>
      <span class="repository-card-description">{{ repo.description }}</span>
      <span class="repository-card-meta">
        <span><i class="fa-solid fa-circle" aria-hidden="true"></i> {{ repo.language }}</span>
        <span>Updated {{ repo.updated | date: "%b %Y" }}</span>
      </span>
      <span class="repository-card-link">View on GitHub <i class="fa-solid fa-arrow-up-right-from-square" aria-hidden="true"></i></span>
    </a>
  {% endfor %}
</div>
