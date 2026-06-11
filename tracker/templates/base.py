{% load static %}
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <title>EnergyTracker</title>
    <link rel="stylesheet" href="{% static 'style.css' %}">
</head>
<body>

<nav>
    <div>
        <a href="{% url 'home' %}">Domů</a>
        <a href="{% url 'drinks_list' %}">Nápoje</a>
        <a href="{% url 'stats' %}">Statistiky</a>
        <a href="{% url 'add_record' %}">Přidat záznam</a>
    </div>

    <div>
        {% if user.is_authenticated %}
            <span style="color:white;">Ahoj, {{ user.username }}</span>
            <a href="{% url 'logout' %}" style="color:red;">Odhlásit</a>
        {% else %}
            <a href="{% url 'login' %}">Přihlášení</a>
            <a href="{% url 'register' %}">Registrace</a>
        {% endif %}
    </div>
</nav>

<div class="container">
    {% block content %}
    {% endblock %}
</div>

</body>
</html>l