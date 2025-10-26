# === ДЕНЬ 3–4: «БЕГСТВО В АД» (1–2 июля 1944) ===
label day34_start:
    scene black with fade
    play music theme_tense fadein 2.0

    narr "1 июля. Третий день прорыва. Мы ушли от Бобруйска — вглубь белорусских лесов. И даже тут слышен этот гул.."
    n_narr "Немцы бегут. Бросают технику, раненых, даже знамёна. Но мы не даём им передышки."

    nvl hide
    nvl clear

    scene bg forest_swamp_morning with fade
    play sound distant_gunfire loop
    play sound crickets_sound

    ivan "След свежий. Колёса, гусеницы... и кровь."
    masha "Они везли офицеров. Может, даже штабников."

    n_narr "Маша — как лиса в лесу. Видит то, что скрыто от других."

    nvl hide
    nvl clear

    politruk "Если поймаем — получим планы обороны Минска!"
    ivan "А если засада — потеряешь отряд."

    menu:
        "Преследовать след":
            narr "Информация важнее риска."
            jump trail_pursuit

        "Держаться дороги":
            narr "Не гонимся за призраками. Наша цель — Минск."
            $ avoided_ambush = True
            jump road_march

# === ПОГОНЯ И ЛАГЕРЬ ===
label trail_pursuit:
    scene bg swamp_clearing with fade
    #МУЗЫКА ДЛЯ ЗВЕРСТВ
    n_narr "След приводит к заброшенному лагерю. Палатки, кострище… и тела наших пленных."

    soldier "Расстреляны… в упор."
    n_narr "На земле — обломки касок, окровавленные бинты. Немцы ушли недавно."

    masha "Под палаткой — ящик. И… документы."
    n_narr "В портфеле — карты Минска. И список партизан. Имя Маши — подчёркнуто красным."

    menu:
        "Сжечь документы — защитить Машу":
            n_narr "Я рву бумаги и бросаю в костёр."
            masha "…"  # Тихое: "Спасибо."
            $ protected_masha = True

        "Сохранить документы":
            n_narr "Сворачиваю карты. Маша отворачивается."
            $ protected_masha = False

    if not avoided_ambush:
        play sound machine_gun
        scene bg swamp_clearing with hpunch
        n_narr "Из кустов — очередь! Засада!"
        ivan "В укрытие!"

        nvl hide
        nvl clear

        menu:
            "Оставить раненых с санитаром":
                n_narr "Темп важнее. Санбат пришлёт помощь."
            "Остаться до эвакуации":
                n_narr "Час под снайперским огнём… но всех вывезли."
                $ saved_wounded = True

    jump night_camp

# === МАРШ ПО ДОРОГЕ ===
label road_march:
    scene bg forest_road_dust with fade
    n_narr "Дорога пуста. Только дым от горящих деревень и следы гусениц."
    politruk "Так фашисты прощаются с Беларусью — огнём и пеплом."

    scene bg roadside_village with fade
    old_woman "Спасибо, сыны… Пусть ангел хранит вас."
    n_narr "Она даёт кусок хлеба и иконку. Мы идём дальше."

    jump night_camp

# === НОЧЬ У КОСТРА ===
label night_camp:
    scene bg forest_camp_night with fade
    stop music fadeout 2.0
    play sound crickets_sound loop
    play music theme_calm fadein 3.0

    n_narr "Ночь. Костёр потрескивает. Усталость — до костей."

    # Речь Маши — зависит от милосердия ГГ
    if (saved_soldier or spared_civilians) and protected_masha:
        masha "Ты помнишь, что мы — люди. Даже здесь."
        masha "Я из Борок… Там, где сожгли деревню."
        masha "Загнали всех в сарай… маму, отца, сестрёнку…"
        masha "Я выскочила первой. Слышала, как кричали дети…"
        masha "Больше никто не выжил. Я помню каждое лицо."
    else:
        masha "Я из Борок. Из той деревни, что стёрли с земли…"
        masha "Я помню каждое лицо. Так что не говори мне про 'необходимость'."

    n_narr "Её слова — как нож в сердце. Но мы молчим. Завтра — снова в бой."

    nvl hide
    nvl clear
    stop music fadeout 2.0

    # === УТРО 2 ИЮЛЯ ===
    scene black with dissolve
    scene bg forest_bridge_dawn with fade
    play music theme_tense fadein 2.0
    play sound distant_gunfire loop

    narr "2 июля. Рассвет. Мы вышли к мосту через болотистую реку."
    n_narr "Последний путь отступления врага. Если мост взорвут — 'котёл' не замкнётся."

    ivan "Пулемёт на насыпи. Мины на подступах. И заряд под опорами — уже заложен."

    politruk "Если не возьмём за час — придут 'ястребы' и сровняют всё."

    menu:
        "Атаковать сейчас":
            jump bridge_assault
        "Ждать артиллерию":
            jump bridge_artillery

# === АТАКА НА МОСТ ===
label bridge_assault:
    play sound machine_gun
    scene bg forest_bridge_dawn with vpunch

    n_narr "Пулемёт открывает огонь! Земля рвётся под ногами."
    kolya "А-а-а!" with hpunch

    n_narr "Коля застывает посреди поляны — парализован страхом."

    menu:
        "Спасти его":
            play sound grenade_throw
            n_narr "Я вытаскиваю его из-под огня."
            $ kolya_saved = True
        "Подавить огонь":
            play sound grenade_throw
            n_narr "Граната в амбразуру. Коля остаётся стоять, дрожа."
            $ kolya_saved = False

    jump bridge_victory

label bridge_artillery:
    play sound artillery
    n_narr "Залп 'Катюш'! Пулемёт уничтожен. Мост — цел."
    $ kolya_saved = True
    jump bridge_victory

# === ФИНАЛ ДНЯ ===
label bridge_victory:
    scene bg forest_bridge_smoke with fade
    stop music fadeout 2.0
    stop sound fadeout 2.0

    n_narr "Мост захвачен. 'Котёл' под Бобруйском — закрыт. Десятки тысяч врагов — в ловушке."
    politruk "Теперь — на Минск! На столицу!"

    nvl hide
    nvl clear

    ivan "Отдыхаем 20 минут — и марш."

    n_narr "Коля молча чистит винтовку. Его взгляд — пустой, безжизненный. Словно сама смерть чистит свою косу."

    scene black with fade
    n_narr "К вечеру 2 июля мы выходим к шоссе на Минск. Впереди — огни столицы."
    n_narr "Пятый день начнётся с атаки. Но сегодня… сегодня мы выжили."

    jump day5_start