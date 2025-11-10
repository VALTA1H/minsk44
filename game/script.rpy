# === АУДИО ===
define artillery = "audio/artillery.opus"
define rain = "audio/rain.opus"
define machine_gun = "audio/machine_gun.opus"
define birds_morning = "audio/birds_morning.opus"
define theme_calm = "audio/theme_calm.opus"
define crickets_sound = "audio/crickets_sound.opus"
define distant_gunfire = "audio/distant_gunfire.opus"
define grenade_throw = "audio/grenade_throw.opus"
define child_crying = "audio/child_crying.opus"
define distant_celebration = "audio/distant_celebration.opus"
define incoming_shell_rising = "audio/incoming_shell_rising.opus"
define explosion_loud = "audio/explosion_loud.opus"
define theme_tense = "audio/theme_tense.opus"
define wind_low = "audio/wind_low.opus"
define alert = "audio/alert.opus"
define mgs_over = "audio/mgs_over.opus"

# === ПЕРСОНАЖИ ===
define n_narr = Character("Безымянный", color="#91d46a", kind=nvl)
define narr = Character("Безымянный", color="#91d46a")
define d_text = Character("Автор", color="#ffffff", kind=nvl)
define scene_narr = Character(None)

define ivan = Character("Иван", color="#b0e0e6")
define kolya = Character("Коля", color="#add8e6")
define politruk = Character("Политрук", color="#ff7f7f")
define masha = Character("Маша", color="#98fb98")
define masha_not_known = Character("Женщина", color="#98fb98")
define masha_lined = Character("Ж̶е̶н̶щ̶и̶н̶а̶ Маша", color="#98fb98")
define soldier = Character("Рядовой", color="#ffffff")
define hanz = Character("Немец",color="#b48282")

# === ДОПОЛНИТЕЛЬНЫЕ ПЕРСОНАЖИ (жители, внук и др.) ===
define civil = Character("Неизвестный", color="#9dff00ff")
define old_man = Character("Старик", color="#d3d3d3")
define old_woman = Character("Старуха", color="#f5deb3")
define grandson = Character("Внук", color="#90ee90")
define old_narr = Character("Дед", color="#91d46a")  # пожилой ГГ в эпилоге A
define old_kolya = Character("Коля (в 2025)", color="#add8e6")  # если Коля дожил

# === ГЛОБАЛЬНЫЕ ФЛАГИ (добавьте ЭТО в начало script.rpy) ===
default avoided_ambush = False
default saved_wounded = False
default saved_soldier = False
default spared_civilians = False
default kolya_saved = False
default chose_duty = False
default chose_comrades = False
define masha_rep = 0

label splashscreen:
    $ mouse_visible = False
    scene black
    $ renpy.pause(1.0, hard=True)
    show age_16 at truecenter with Dissolve(1.0)
    $ renpy.pause(2.0, hard=True)
    hide age_16 with Dissolve(1.0)
    $ renpy.pause(1.0, hard=True)
    show screen beta_version with Dissolve(1.0)
    $ renpy.pause(4.0, hard=True)
    hide screen beta_version with Dissolve(1.0)
    $ renpy.pause(1.0, hard=True)
    show halipov_ent with Dissolve(1.0)
    $ renpy.pause(2.0, hard=True)
    play sound mgs_over
    $ renpy.pause(2.0, hard=True)
    hide halipov_ent
    $ mouse_visible = True
    return

# === ПРОЛОГ: СОН ===
label pre_history:
    scene black with fade
    play music dramatic_theme fadein 5.0 loop

    n_narr "Заставил вас ждать, не так ли?"
    n_narr "Уже который год идёт кровопролитная война, которая решает наши судьбы."
    n_narr "Я помню, как в своей родной деревне проводил чудесное время со своей женой."
    n_narr "Те теплые майские дни. Те самые моменты, когда мы были счастливы."
    n_narr "Но потом началась война..."
    n_narr "Немцы, обманув западный мир и выставив себя миротворцами, начали преступную войну"
    scene poland with fade
    n_narr "Они заявили, что их обстреляли на границе поляки осенью 39-го года."
    n_narr "В то время как они обстреливали сами себя, чтобы выдать себя за жертву..."
    scene 1941_2 with fade
    n_narr "Душу улиц, на которых раньше жили люди, заменила глухая тишина"
    n_narr "Столько людей, семей, чьих-то домов и сёл просто пропали, как будто их никогда и не было"
    scene 1941_1 with fade
    n_narr "Сейчас весь наш великий народ ценой своих жизней и своего будущего дарит свет для будущих поколений, чтобы они никогда больше не познали ужасы и тяготы войн"
    n_narr "Сегодня, 28 июня, надеюсь, последнего года войны, мы форсируем реку Березину, чтобы не дать этим фрицам отступить и занять новые позиции"

    nvl hide
    nvl clear

    stop music fadeout 3.0

    return

# === НАЧАЛО: ПЕРВЫЙ ДЕНЬ ===
label start:
    call pre_history from _call_pre_history

    scene trench_night with fade
    play music high_tension fadein 5.0 loop
    ivan "Всем внимание! До сигнала меньше часа. Проверить снаряжение, подогнать ремни. Отдыхаем, пока можем."
    ivan "Сержант ..., подготовьте свою роту к наступлению. Убедитесь, что все знают свои задачи."
    
    narr "Так точно!"
    ivan "Также у нас появился новобранец: Захаров. Расскажи ему, что да как"
    narr "Есть!"

    narr "Итак, нужно найти этого новобранца"

    narr "Я оглядел окоп. Куда мог забиться зелёный юнец перед первым боем?"

    jump find_solider

    return

label find_solider:

    menu:
        "Где искать новобранца?"

        "Проверить у пулеметного гнезда.":

            narr "Здесь я не увидел никого нового, посмотрю в другом месте"
            jump find_solider

        "Заглянуть в землянку для отдыха.":

            narr "Вижу какого-то хилого мальчишку в форме, которая ему на пару размеров больше. Похоже, это он."
            jump kolya_meet

    return

label kolya_meet:

    n_narr "Подойдя к нему поближе, я коснулся его плеча"
    narr "Ты рядовой Захаров?"
    kolya "я.. Я!" with hpunch
    narr "Как звать тебя?"
    kolya "Захаров Николай Павлович" with hpunch
    narr "Мы сегодня форсируем реку. Твоя задача - держаться рядом со взводом. Задача ясна?"
    narr "Чуть что — обращайся. Здесь любая ошибка может стоить тебе жизни"
    kolya "так... Точно!" with hpunch

    n_narr "Коля, молодой боец, явно нервничает. Его дыхание сбивается."
    n_narr "Тяжёлые капли дождя барабанят по каске. Вдалеке — приглушённый гул артиллерии и частая дробь пулемётов."
    n_narr "Отряд сидит в укрытии, прижавшись к мокрой земле."

    kolya "А что будет дальше?"

    narr "Спокойно, Коля. Первый раз всегда страшно. Держись рядом."
    kolya "П-понял… спасибо, товарищ…"

    nvl hide
    nvl clear
    
    stop music
    play music theme_tense loop
    play sound artillery loop
    scene river_crossing with vpunch
    play sound machine_gun loop

    n_narr "Первые лодки уже спускают на воду. Холодные брызги бьют в лицо."
    n_narr "Вода, на удивление, кристально чистая. Слишком чистая для такого дня. Дыхание перехватывает. Вокруг — крики, свист пуль, взрывы мин, брызги."
    n_narr "Всё, что я могу сделать, — прижаться к борту лодки и надеяться, что мы доберёмся до западного берега."

    nvl hide
    nvl clear

    stop music fadeout 2.0
    stop sound fadeout 2.0

    scene western_bank with fade

    n_narr "Спустя часы, казавшиеся вечностью, мы захватываем плацдарм. Мокрые, измученные… но живые."
    n_narr "На берегу — тела, обломки лодок, крики раненых. Но мы здесь. Мы переправились."
    
    nvl hide
    nvl clear

    # === УТРО: МАРШ ВГЛУБЬ ===
    scene black with dissolve
    scene dusty_road_day with fade
    play music theme_calm fadein 5.0 loop

    n_narr "Утро сменяет ночь. Мы совершаем стремительный марш при поддержке техники. Жара и пыль поднимаются столбом. Слышно лишь рёв моторов."

    nvl hide
    nvl clear

    politruk "Держать темп, товарищи! Каждая минута — это километры, отделяющие нас от фашистского зверя!"
    politruk "Именно наша скорость — ключ к успеху операции по освобождению Минска! Нельзя дать врагу подготовить оборону!"

    scene spearhead_view with dissolve

    n_narr "По главной дороге грохочут танки, мчатся конные части."

    nvl hide
    nvl clear

    politruk "Вот они, товарищи! Авангард прорыва — кавалерийско-механизированная группа Плиева!"
    politruk "Их задача — рвать оборону. Наша — не отставать и зачищать фланги."

    stop music

    # === ВСТРЕЧА С ПАРТИЗАНАМИ ===

    scene forest_ambush with dissolve
    n_narr "Проходя мимо леса, мы услышали шум."
    n_narr "Не ожидая ничего хорошего, мы направили оружие в сторону источника шума"

    narr "Кто там, выходите с поднятыми руками!"

    n_narr "После чего слышится женский голос."

    masha_not_known "Свои! Не стреляйте!"

    n_narr "Из леса выходит молодая партизантка."
    n_narr "На вид, ей было лет 20-25."

    nvl hide
    nvl clear

    masha_lined "Я партизантка. Звать меня Машей."

    narr "И зачем ты пришла, Маша?"

    masha "Там застрял немецкий обоз. Два грузовика, охрана — тыловики. Шанс пополнить припасы."
    masha "У них медикаменты, патроны… даже хлеб. Нам это жизненно нужно."

    ivan "Это ловушка, Маша? Или…?"

    masha "Нет. Застряли в грязи после дождя. У них нет времени ждать подмогу."

    n_narr "Старшина смотрит на меня. Припасы нужны, но риск велик. Особенно после переправы."

    nvl hide
    nvl clear

    menu choice_convoy:
        "Атаковать немедленно":
            narr "Припасы никогда не будут лишними. Нам не помешает их пополнить."
            ivan "Хорошо. Берём в кольцо. Атака!"
            jump convoy_fight

        "Сообщить командованию по рации":
            narr "Риск неоправдан. Лучше передать координаты основным силам."
            politruk "Верное решение, солдат. Разумная предосторожность."
            jump convoy_report

# === БОЙ ЗА ОБОЗ ===
label convoy_fight:
    scene black with fade
    play sound machine_gun
    n_narr "Короткий, но ожесточённый бой. Солдаты вермахта застигнуты врасплох. Обоз наш. Мы отбираем припасы."
    n_narr "В грузовиках — патроны, сухари, бинты. Даже консервы. Это поможет десяткам людей."
    
    nvl hide
    nvl clear
    jump end_of_day1

# === ПЕРЕДАЧА КООРДИНАТ ===
label convoy_report:
    n_narr "Передаём координаты обоза. Через полчаса — глухой взрыв вдалеке. Скорее всего, немцы сами уничтожили грузы при отступлении… или их перехватили союзные войска."
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
    n_narr "А я смотрю на закат и думаю: «Как нам победить в этом аду?»"

    scene black with fade
    n_narr "Первый день позади. Завтра — город. Завтра — снова бой."

    jump day2_sleep