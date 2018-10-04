{% block intro %}{% endblock %}

{% block initial %}{% if has_initial %}# پروژه اولیه

پروژه اولیه را از
[اینجا](%q_initial_url%)
دانلود کنید.{% block structure %} ساختار فایل‌های این پروژه به صورت زیر است:

```
{{ initial_structure }}
```
{% endblock structure %}{% endif %}{% endblock %}
{% block details_ %}# جزئیات
{% block details %}{% endblock %}
{%endblock details_ %}
{% block notes_ %}# نکات
{% block notes %}{% endblock notes %}
{% endblock notes_ %}
