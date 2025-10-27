# === АУДИО ===
define artillery = "audio/artillery.mp3"
define rain = "audio/rain.mp3"
define machine_gun = "audio/machine_gun.mp3"
define birds_morning = "audio/birds_morning.mp3"
define theme_calm = "audio/theme_calm.mp3"
define crickets_sound = "audio/crickets_sound.mp3"
define distant_gunfire = "audio/distant_gunfire.mp3"
define grenade_throw = "audio/grenade_throw.mp3"
define child_crying = "audio/child_crying.mp3"
define distant_celebration = "audio/distant_celebration.mp3"
define incoming_shell_rising = "audio/incoming_shell_rising.mp3"
define explosion_loud = "audio/explosion_loud.mp3"
define theme_tense = "audio/theme_tense.mp3"
define wind_low = "audio/wind_low.mp3"

# === ПЕРСОНАЖИ ===
# === ПЕРСОНАЖИ ===
define n_narr = Character("Безымянный", color="#91d46a", kind=nvl)
define narr = Character("Безымянный", color="#91d46a")
define d_text = Character("Автор", color="#ffffff", kind=nvl)
define scene_narr = Character(None)

define ivan = Character("Иван", color="#b0e0e6")
define kolya = Character("Коля", color="#add8e6")
define politruk = Character("Политрук", color="#ff7f7f")
define masha = Character("Маша", color="#98fb98")
define soldier = Character("Рядовой", color="#ffffff")

# === ДОПОЛНИТЕЛЬНЫЕ ПЕРСОНАЖИ (жители, внук и др.) ===
define old_man = Character("Старик", color="#d3d3d3")
define old_woman = Character("Старуха", color="#f5deb3")
define grandson = Character("Внук", color="#90ee90")
define civil = Character("Неизвестный", color="#9dff00ff")
define old_narr = Character("Дед", color="#91d46a")  # пожилой ГГ в эпилоге A
define old_kolya = Character("Коля (в 2025)", color="#add8e6")  # если Коля дожил

# === ГЛОБАЛЬНЫЕ ФЛАГИ (добавьте ЭТО в начало script.rpy) ===
default avoided_ambush = False
default protected_masha = False
default saved_wounded = False
default saved_soldier = False
default spared_civilians = False
default kolya_saved = False
default chose_duty = False
default chose_comrades = False

# === ДИСКЛЕЙМЕР ===
label disclaimer:
    scene black with fade

    d_text "Этот проект представляет собой художественную визуальную новеллу,"
    d_text "Вдохновлённую историческими событиями операции «Багратион» в 1944 году."
    d_text "Он стремится к честному,"
    d_text "уважительному отображению трагических реалий войны и моральных дилемм, с которыми сталкивались люди."
    d_text "Все персонажи и события вымышлены. Игра содержит сцены насилия, травматичные эпизоды и описание военных действий."
    d_text "Рекомендуется проявлять осторожность при знакомстве с содержанием."

    menu:
        "Я понимаю и хочу продолжить":
            nvl hide
            nvl clear
            pass

        "Я не хочу продолжать (Выход из игры)":
            nvl hide
            nvl clear
            $ renpy.quit()

    return

# === ПРОЛОГ: СОН ===
label pre_history:
    scene black with fade
    play music theme_calm fadein 2.0
    scene village_morning with fade

    n_narr "Утренний свет. Я помню только этот свет. И запах свежего хлеба, которого не чувствовал уже давно."
    n_narr "Я помню обещание, данное ей: вернуться. Несмотря ни на что."
    n_narr "Она ждёт."

    nvl hide
    nvl clear

    stop music fadeout 3.0

    n_narr "Но это всего лишь сон… Всё вокруг начинает дрожать."

    nvl hide
    nvl clear

    scene black with dissolve
    play sound incoming_shell_rising fadein 2.0 loop    

    n_narr "Гул."
    n_narr "Я слышу его сквозь сон. Оглушающий, низкий, нарастающий. Он приближается."

    nvl hide
    nvl clear

    stop sound
    play sound explosion_loud
    scene black with hpunch

    scene trench_night with fade

    play music theme_tense fadein 1.0
    play sound rain loop

    scene_narr "Удар!"

    n_narr "Глаза распахиваются. В рот набилась земля. Чёрт…"

    nvl hide
    nvl clear

    return

# === НАЧАЛО: ПЕРВЫЙ ДЕНЬ ===
label start:
    call disclaimer
    call pre_history

    scene trench_night with fade

    narr "Ночь на 28 июня. Восточный берег реки Березина. Если переживу — запомню это."

    n_narr "Тяжёлые капли дождя барабанят по каске. Вдалеке — приглушённый гул артиллерии и частая дробь пулемётов."
    n_narr "Отряд сидит в укрытии, прижавшись к мокрой земле. До переправы — меньше часа."

    nvl hide
    nvl clear

    ivan "Всем внимание! До сигнала меньше часа. Проверить снаряжение, подогнать ремни. Отдыхаем, пока можем."

    kolya "Т-товарищ старшина… я…" with hpunch
    n_narr "Коля, молодой боец, явно нервничает. Его дыхание сбивается."

    nvl hide
    nvl clear

    ivan "Спокойно, солдат! Первый раз всегда страшно. Держись рядом."

    n_narr "Коля дрожит. Он сидит в неудобной воронке — слишком открытой. Нужно помочь ему… Лишних потерь нам точно не хватало."
    n_narr "Я аккуратно подхожу, кладу руку на его плечо и шепчу:"

    nvl hide
    nvl clear

    narr "Возьми позицию правее меня. Эта воронка лучше укроет."
    kolya "П-понял… спасибо, товарищ…"

    # === АРТПОДГОТОВКА ===
    n_narr "Внезапно небо озаряют яркие вспышки. Начинается артподготовка."
    n_narr "Земля дрожит под ногами. Воздух наполняется грохотом и свистом разрывов."

    play sound artillery loop
    scene river_crossing with vpunch

    n_narr "Первые лодки уже спускают на воду. Холодные брызги бьют в лицо."

    nvl hide
    nvl clear

    ivan "Вперёд! За мной! Держать строй!"

    n_narr "Подаётся сигнал. Начинается хаос. Мы бросаемся к лодкам."

    play sound machine_gun

    n_narr "Вода, на удивление, кристально чистая. Дыхание перехватывает. Вокруг — крики, свист пуль, взрывы мин, брызги."
    n_narr "Всё, что я могу сделать, — прижаться к борту лодки и надеяться, что мы доберёмся до западного берега."
    
    nvl hide
    nvl clear

    # === ПЕРЕПРАВА: МОМЕНТ ИСТИНЫ ===
    menu:
        "Помочь перевернувшейся лодке (рискованно)":
            narr "Там наши! Нельзя бросать!"
            n_narr "Я ныряю в воду, тащу раненого к берегу. Пули хлещут по поверхности."
            kolya "Держись! Я тебя вытащу!"
            n_narr "Мы выживаем — но теряем драгоценные минуты."

        "Следовать приказу — идти вперёд":
            narr "Приказ — зачищать плацдарм. Остальное — не моё решение."
            n_narr "Сердце рвётся, но я продолжаю. Война не ждёт."

    nvl hide
    nvl clear

    stop music fadeout 2.0
    stop sound fadeout 2.0

    scene western_bank with fade
    play music theme_tense

    n_narr "Спустя часы, казавшиеся вечностью, мы захватываем плацдарм. Мокрые, измученные… но живые."
    n_narr "На берегу — тела, обломки лодок, крики раненых. Но мы здесь. Мы переправились."

    nvl hide
    nvl clear

    # === УТРО: МАРШ ВГЛУБЬ ===
    scene black with dissolve
    scene dusty_road_day with fade

    n_narr "Утро сменяет ночь. Мы совершаем стремительный марш в поддержке техники. Жара и пыль поднимаются столбом. Слышно лишь рев моторов."

    nvl hide
    nvl clear

    politruk "Держать темп, товарищи! Каждая минута — это километры, отделяющие нас от фашистского зверя!"
    politruk "Именно наша скорость — ключ к успеху операции «Багратион»! Нельзя дать врагу подготовить оборону!"

    scene spearhead_view with dissolve

    n_narr "По главной дороге грохочут танки, мчатся конные части."

    nvl hide
    nvl clear

    politruk "Вот они, товарищи! Авангард прорыва — кавалерийско-механизированная группа Плиева!"
    politruk "Их задача — рвать оборону. Наша — не отставать и зачищать фланги."

    # === ВСТРЕЧА С ПАРТИЗАНАМИ ===
    scene forest_ambush with dissolve

    masha "Тихо! Сюда!"

    n_narr "Нас останавливает партизанка Маша. Её форма изорвана, но взгляд — твёрд."

    nvl hide
    nvl clear

    masha "Там застрял немецкий обоз. Два грузовика, охрана — тыловики. Шанс пополнить припасы."
    masha "У них медикаменты, патроны… даже хлеб. Нам это жизненно нужно."

    ivan "Это ловушка, Маша? Или…?"

    masha "Нет. Застряли в грязи после дождя. У них нет времени ждать подмогу."

    n_narr "Старшина смотрит на меня. Припасы нужны, но риск велик. Особенно после переправы."

    nvl hide
    nvl clear

    menu choice_convoy:
        "Атаковать немедленно (рискованно, но быстро)":
            narr "Припасы на исходе… Нам жизненно необходимо их пополнить."
            ivan "Хорошо. Берём в кольцо. Атака!"
            jump convoy_fight

        "Сообщить командованию по рации (безопасно, но без припасов)":
            narr "Риск неоправдан. Лучше передать координаты основным силам."
            politruk "Верное решение, солдат. Разумная предосторожность."
            jump convoy_report

# === БОЙ ЗА ОБОЗ ===
label convoy_fight:
    scene black with fade
    play sound machine_gun
    n_narr "Короткий, но ожесточённый бой. Солдаты вермахта застигнуты врасплох. Мы отбираем припасы."
    n_narr "В грузовиках — патроны, сухари, бинты. Даже консервы. Это спасёт десятки жизней."
    
    # Проверка: был ли спасён боец при переправе?
    n_narr "Тот, кого я вытащил из воды, улыбается сквозь боль: «Теперь у нас есть шанс дойти до дома»."
    
    nvl hide
    nvl clear
    jump end_of_day1

# === ПЕРЕДАЧА КООРДИНАТ ===
label convoy_report:
    n_narr "Передаём координаты обоза. Через полчаса — глухой взрыв вдалеке. Скорее всего, немцы сами уничтожили грузы при отступлении… или их перехватили другие."
    n_narr "Мы остаёмся с тем, что имеем, но избегаем потерь."
    n_narr "Коля смотрит на пустой мешок: «Надеюсь, завтра будет лучше…»"
    nvl hide
    nvl clear
    jump end_of_day1

# === ВЕЧЕР ПЕРВОГО ДНЯ ===
label end_of_day1:
    scene forest_camp with fade
    stop music
    play music theme_calm fadein 2.0
    play sound crickets_sound fadein 2.0 loop

    n_narr "К вечеру мы выходим на подступы к городу. Вдалеке гремят тяжёлые бои — идёт штурм."
    n_narr "Первый день прорыва закончен. Мы прошли 30 километров. Переправились через Березину. Выжили."

    nvl hide
    nvl clear

    # Рефлексия
    n_narr "Коля спит, прижавшись к винтовке. Иван точит нож. Политрук пишет письмо."
    n_narr "А я смотрю на закат и думаю: «Смогу ли я сохранить себя в этом аду?»"

    n_narr "Обещание всё ещё со мной. Но теперь оно звучит тише."

    scene black with fade
    n_narr "Первый день позади. Завтра — город. Завтра — снова бой."

    jump day2_sleep