# === ДЕНЬ 3–4: «БЕГСТВО В АД» (1–2 июля 1944) ===
label day34_start:
    scene black with fade
    play music theme_tense fadein 2.0

    n_narr "1 июля. Третий день прорыва. Мы ушли от Бобруйска — вглубь белорусских лесов. И даже тут слышен этот гул работающей артиллерии."
    n_narr "Немцы бегут. Бросают технику, раненых, даже знамёна. Но мы не даём им передышки."

    nvl hide
    nvl clear

    scene forest_swamp_morning with fade
    play sound distant_gunfire loop
    play sound crickets_sound

    ivan "След свежий. Колёса, гусеницы… и кровь."
    masha "Они везли офицеров. Может, даже штабников."

    n_narr "Маша — как лиса в лесу. Видит то, что скрыто от других."

    nvl hide
    nvl clear

    politruk "Если поймаем их — получим планы обороны Минска!"
    ivan "А если засада — потеряешь отряд."

    menu:
        "Что сделаем?"
        "Пойдем по их следам.":
            narr "Эта информация может помочь нашим солдатам."
            jump trail_pursuit

        "Будем придерживаться изначального плана.":
            narr "Нет смысла гнаться за призраками. Наша цель — Минск."
            $ avoided_ambush = True
            jump road_march

label trail_pursuit:
    scene abandoned_camp with fade
    play music cold_iron fadein 2.0 loop
    n_narr "След приводит к заброшенному лагерю. Палатки, кострище… и тела наших пленных."

    nvl hide
    nvl clear

    soldier "Расстреляны… в упор."
    n_narr "На земле — обломки касок, окровавленные бинты. Немцы ушли недавно."

    nvl hide
    nvl clear

    masha "Под палаткой — ящик."

    if not avoided_ambush:
        play sound machine_gun loop
        scene swamp_clearing with hpunch
        n_narr "Из кустов — очередь! Засада!"
        ivan "В укрытие!"

        nvl hide
        nvl clear

        n_narr "После ожесточенного боя мы всё же смогли отбиться и выйти из засады живыми."

        nvl hide
        nvl clear

    stop sound
    jump night_camp

# === МАРШ ПО ДОРОГЕ ===
label road_march:
    scene forest_road_dust with fade
    n_narr "Дорога пуста. Только дым от горящих деревень и следы гусениц."
    politruk "Так фашисты уходят из Беларуси — с огнём и пеплом."

    scene roadside_village with fade
    old_woman "Спасибо, хлопцы… Буду молиться за ваше здравие."
    n_narr "Она даёт кусок хлеба и иконку. Мы её поблагодарили и пошли дальше."

    jump night_camp

# === НОЧЬ У КОСТРА ===
label night_camp:
    scene forest_camp_night with fade
    stop music fadeout 2.0
    play sound crickets_sound loop
    play music theme_calm fadein 3.0

    n_narr "Ночь. Костёр потрескивает. Усталость — до костей."
    n_narr "Мы с Колей и Машей сели у костра."

    nvl hide
    nvl clear

    # Речь Маши — зависит от репутации ГГ
    if masha_rep >= 1:
        masha "Ты помнишь, что мы — люди. Даже здесь."
        masha "Я из Борок… Там, где сожгли деревню."
        masha "Загнали всех в сарай… маму, отца, сестрёнку…"
        masha "Больше никто не выжил. Я помню каждое лицо."
        kolya "А как ты смогла выбраться?"
        masha "Я выскочила первой. Слышала, как кричали дети…"

    else:
        masha "Я из Борок. Из той деревни, что стёрли с лица земли…"
        masha "Я помню их глаза. Так что не говори мне про необходимость."

    n_narr "Её слова — как нож в сердце. Но мы молчим. Завтра — снова в бой."
    show screen achievement_unlock("{size=14}Я наблюдала за глупостью человечества через прицел своей винтовки.{/size}", box_len=400, read_len=5.0)

    nvl hide
    nvl clear
    stop music fadeout 2.0

    # === УТРО 2 ИЮЛЯ ===
    scene black with dissolve
    scene forest_bridge_dawn with fade
    play music theme_tense fadein 2.0
    play sound distant_gunfire loop

    n_narr "2 июля. Рассвет. Мы вышли к мосту через болотистую реку."
    n_narr "Последний путь отступления врага. Если мост взорвут — котёл не замкнётся."

    nvl hide
    nvl clear

    ivan "Пулемёт на насыпи. Мины на подступах. И заряд под опорами — уже заложен."

    politruk "Если не возьмём за час — придут ястребы и сравняют всё."

    menu:
        "Атаковать сейчас":
            jump bridge_assault
        "Ждать артиллерию":
            jump bridge_artillery

# === АТАКА НА МОСТ ===
label bridge_assault:
    play sound machine_gun loop
    scene forest_bridge_dawn with vpunch

    n_narr "Пулемёт открывает огонь! Земля рвётся под ногами."
    kolya "А-а-а!" with hpunch

    nvl hide
    nvl clear

    n_narr "Коля застывает посреди поляны — парализован страхом."
    n_narr "У меня есть считанные мгновения на принятие решения."

    nvl hide
    nvl clear

    menu:
        "Спасти его":
            play sound grenade_throw
            n_narr "Я вытаскиваю его из-под огня."
            play sound alert
            n_narr "В моменте я чувствую, что ноги становятся ватными."
            play sound mgs_over
            n_narr "Резкая боль пронзает меня, в глазах темнеет…"
            $ kolya_saved = True
            nvl hide
            nvl clear
            jump coma
        "Подавить огонь":
            play sound grenade_throw
            n_narr "Граната в амбразуру. Коля остаётся стоять, дрожа."
            play sound explosion_loud
            $ kolya_saved = False
            nvl hide
            nvl clear

    stop sound
    jump bridge_victory

label coma:
    n_narr "Очнулся уже после боя."

    nvl hide
    nvl clear

    masha "Наконец-то очнулся. Мы уже думали, что тебя не спасти."

    n_narr "Я перевожу свой взгляд на дрожащего Колю."

    nvl hide
    nvl clear

    kolya "Спасибо тебе большое. Я не знаю, что на меня нашло."
    kolya "Все тело в одночасье оцепенело, я не мог пошевелиться."

    narr "Я понимаю. Самое главное, что мы остались в живых."

    masha "Не прыгай больше под пули, дурак!"
    masha "А ты, Коля, не стой как баран. Тебе повезло, что тебя спасли в этот раз!"
    kolya "Прости меня…"
    n_narr "Рана была несущественная. Через несколько часов мы продолжили путь."

    nvl hide
    nvl clear

    jump bridge_victory


label bridge_artillery:
    play sound artillery
    n_narr "Залп «Катюш»! Пулемёт уничтожен. Мост — цел."
    $ kolya_saved = True
    nvl hide
    nvl clear
    jump bridge_victory

# === ФИНАЛ ДНЯ ===
label bridge_victory:
    scene forest_bridge_dawn with fade
    stop music fadeout 2.0
    stop sound fadeout 2.0
    play music theme_calm loop

    n_narr "Мост захвачен. Котёл под Бобруйском — закрыт. Десятки тысяч врагов — в ловушке."
    politruk "Теперь — на Минск! На столицу!"

    nvl hide
    nvl clear

    ivan "Отдыхаем 20 минут — и марш."

    n_narr "Коля молча чистит винтовку. Его взгляд — пустой, безжизненный. Словно сама смерть чистит свою косу."

    nvl hide
    nvl clear

    scene black with fade
    n_narr "К вечеру 2 июля мы выходим к дороге на Минск. Впереди — столица."
    n_narr "Пятый день начнётся с атаки. Но сегодня… сегодня мы выжили."

    nvl hide
    nvl clear

    if kolya_saved:
        kolya "Слушай, извини за сегодняшнее."
        masha "Да ладно. Главное, что мы все остались живы."
        kolya "И ты меня прости, товарищ."
        narr "Хоть твоё спасение и стоило мне ранения, но твоя жизнь важнее."
        n_narr "После этого диалога мы пошли спать, в надежде, что завтрашний день будет лучше."
        nvl hide
        nvl clear
    stop music
    jump day5_start