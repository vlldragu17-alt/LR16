from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>🌿 Магазин комнатных растений "Зеленый Слоник"</h1>
        <p>Добро пожаловать! У нас есть всё для вашего домашнего сада.</p>
        <hr>
        <p><a href='/about/'>📖 Об авторе</a> | <a href='/shop/'>🪴 О магазине</a></p>
    """)

def about(request):
    return HttpResponse("""
        <h1>👤 Об авторе</h1>
        <p>работу выполнил: <b>Колесник Алексей</b></p>
        <p>Группа: 89ТП</p>
        <br><a href='/'>⬅ На главную</a>
    """)

def shop_info(request):
    return HttpResponse("""
        <h1>🪴 О магазине</h1>
        <p><b>Тема:</b> Магазин комнатных растений.</p>
        <p><b>Ассортимент:</b></p>
        <ul>
            <li>Семена редких и экзотических цветов</li>
            <li>Керамические и пластиковые горшки</li>
            <li>Специализированный грунт и удобрения</li>
        </ul>
        <br><a href='/'>⬅ На главную</a>
    """)
