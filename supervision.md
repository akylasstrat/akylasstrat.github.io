---
layout: default
title: Supervision
permalink: /supervision/
---

# Supervision

## Current PhD Students

{% for student in site.data.students %}
### {{ student.name }}

**{{ student.degree }} · {{ student.affiliation }} · Since {{ student.start_year }}**

{{ student.topic }}.

My role: {{ student.role }}. Primary supervisor: {{ student.primary_supervisor }}.
{% endfor %}
