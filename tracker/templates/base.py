<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EnergyTracker</title>

    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f9; color: #333; }
        nav { background-color: #2c3e50; padding: 15px; display: flex; justify-content: space-between; align-items: center; }
        nav a { color: white; text-decoration: none; margin: 0 10px; font-weight: bold; }
        nav a:hover { color: #1abc9c; }
        .container { max-width: 800px; margin: 30px auto; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }

        h1 { color: #2c3e50; }

        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { padding: 12px; border: 1px solid #ddd; text-align: left; }
        th { background-color: #2c3e50; color: white; }
        tr:nth-child(even) { background-color: #f9f9f9; }

        .btn { background-color: #1abc9c; color: white; padding: 10px 15px; border: none; border-radius: 5px; cursor: pointer; text-decoration: none; display: inline-block; }
        .btn:hover { background-color: #16a085; }

        .alert { padding: 15px; margin-bottom: 20px; border-radius: 5px; font-weight: bold; }
        .alert-ok { background-color: #d4edda; color: #155724; }
        .alert-danger { background-color: #f8d7da; color: #721c24; }

        .form-group { margin-bottom: 15px; }
        .form-group label { display: block; margin-bottom: 5px; font-weight: bold; }
        .form-group select, .form-group input {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
    </style>
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
            <span style="color: white; margin-right: 10px;">Ahoj, {{ user.username }}!</span>
            <a href="{% url 'logout' %}" style="color: #e74c3c;">Odhlásit se</a>
        {% else %}
            <a href="{% url 'register' %}">Registrace</a>
            <a href="/admin/">Přihlášení</a>
        {% endif %}
    </div>
</nav>

<div class="container">

    {% block content %}
    {% endblock %}

</div>

</body>
</html>