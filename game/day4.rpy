label day4_start:
    scene black with dissolve
    scene forest_bridge_dawn with fade
    play music theme_tense fadein 2.0
    play sound distant_gunfire loop

    n_narr "2 июля. Рассвет. Мы вышли к мосту через болотистую реку."
    n_narr "Последний путь отступления врага. Если мост взорвут — котёл не замкнётся."

    nvl hide
    nvl clear

    ivan "Пулемёт на насыпи. Мины на подступах. И заряд под опорами — уже заложен."

    voice "audio/voice/politruk/politruk_10.opus"
    politruk "Если не возьмём за час — придут ястребы и сравняют всё."

    menu:
        "Атаковать сейчас":
            jump bridge_assault
        "Ждать артиллерию":
            jump bridge_artillery

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

    show masha scared at left:
        ease 0.25 zoom 1.5 yoffset 512
    with easeinleft
    voice "audio/voice/masha/masha_24.opus"
    masha "Наконец-то очнулся. Мы уже думали, что тебя не спасти."

    n_narr "Я перевожу свой взгляд на дрожащего Колю."
    show masha scared at right:
        ease 0.25 zoom 1.0 yoffset 0
    with easeinright

    nvl hide
    nvl clear

    kolya "Спасибо тебе большое. Я не знаю, что на меня нашло."
    kolya "Все тело в одночасье оцепенело, я не мог пошевелиться."

    narr "Я понимаю. Самое главное, что мы остались в живых."

    show masha angry at left
    with easeinleft
    voice "audio/voice/masha/masha_25.opus"
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

label bridge_victory:
    scene forest_bridge_dawn with fade
    stop music fadeout 2.0
    stop sound fadeout 2.0
    play music theme_calm loop

    n_narr "Мост захвачен. Котёл под Бобруйском — закрыт. Десятки тысяч врагов — в ловушке."
    voice "audio/voice/politruk/politruk_11.opus"
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
        scene forest_camp_night
        kolya "Слушай, извини за сегодняшнее."
        show masha at right:
            linear 2.0 matrixcolor BrightnessMatrix(-0.3) * TintMatrix("#e2582236")
        with easeinright
        voice "audio/voice/masha/masha_26.opus"
        masha "Да ладно. Главное, что мы все остались живы."
        kolya "И ты меня прости, товарищ."
        narr "Хоть твоё спасение и стоило мне ранения, но твоя жизнь важнее."
        n_narr "После этого диалога мы пошли спать, в надежде, что завтрашний день будет лучше."
        nvl hide
        nvl clear
    stop music
    jump day5_start