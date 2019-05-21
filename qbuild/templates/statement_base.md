{% if is_readme %}
{% if self.name() %}
# {% block name %}{% endblock %}


{% endif %}
{% if self.readme() %}
--------------------------------------------------

{% block readme %}{% endblock readme %}

--------------------------------------------------

{% endif %}
{% endif %}
{% if self.intro() %}
{% block intro %}{% endblock %}


{% endif %}
{% if has_initial %}
{% block initial %}
# پروژه اولیه

پروژه اولیه را از
[اینجا](%q_initial_url%)
دانلود کنید.
{% block structure %}
ساختار فایل‌های این پروژه به صورت زیر است:

```
{{ initial_structure }}
```

{% endblock structure %}
{% endblock %}


{% endif %}
{% if self.run() %}
# راه‌اندازی پروژه

{% block run %}{% endblock run %}


{% endif %}
{% if self.details() %}
# جزئیات

{% block details %}{% endblock %}


{% endif %}
{% if self.notes() %}
# نکات

{% block notes %}{% endblock notes %}


{% endif %}
