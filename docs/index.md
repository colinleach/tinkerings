---
layout: home
---

This site collects various software-related links. The [GitHub site](https://github.com/colinleach/tinkerings) that hosts these Pages also has (or will have) some example code that I wrote while practicing.

See also the related [astro-Jupyter site](https://github.com/colinleach/astro-Jupyter) for entries specific to Jupyter notebooks and astronomy.


{% for topic in site.data.topics %}
## [{{ topic.name }}]({{ topic.path }})
{{ topic.description }}
 {% endfor %}
