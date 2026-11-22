---
layout: default
title: Selected Talks
permalink: /talks/
---

# Selected Talks

{% assign talks = site.data.talks | sort: "date" | reverse %}
{% for talk in talks %}
## {{ talk.title }}

**{{ talk.kind }} · {{ talk.event }} · {{ talk.date | date: "%d %B %Y" }}**

{% if talk.co_speakers %}With {{ talk.co_speakers }}.{% endif %}

{{ talk.summary }}

<p class="resource-links">
  <a href="{{ talk.url }}">Event</a>
  {% if talk.slides %}<a href="{{ talk.slides | relative_url }}">Presentation</a>{% endif %}
  {% if talk.recording %}<a href="{{ talk.recording }}">Recording</a>{% endif %}
</p>
{% endfor %}
