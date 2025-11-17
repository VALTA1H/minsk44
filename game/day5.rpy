label day5_start:
    scene black with fade
    play music theme_tense fadein 2.0

    n_narr "3 июля 1944 года. Пятый день прорыва."
    n_narr "С утра мы отправились в сторону Минска."

    nvl hide
    nvl clear

    if kolya_saved:
        n_narr "Хоть вчера я и получил ранение, сегодня было идти проще, чем я ожидал."

    else:
        n_narr "Коля после вчерашних событий почти постоянно смотрел вдаль и не разговаривал."

    n_narr "День. Мы стоим на окраине Минска. Город — в дыму, но колокола звонят. Люди выходят на улицы."

    nvl hide
    nvl clear

    scene minsk_outskirts_morning with fade
    play sound distant_celebration loop
    play sound birds_morning loop

    n_narr "Первые жители бегут к нам — с плачем, с хлебом, с цветами."

    nvl hide
    nvl clear

    old_man "Спасибо… спасибо, хлопцы! Мы ждали… ждали вас каждый день!"

    voice "audio/voice/old_woman/loud_old_woman_2.opus"
    old_woman "Мои дети… они живы? Вы видели их?"
    n_narr "На её лице — надежда и страх. Мы не знаем, что ответить."

    nvl hide
    nvl clear

    voice "audio/voice/politruk/politruk_12.opus"
    politruk "Товарищи! Минск — столица Беларуси! Сегодня мы освободим её до конца!"
    voice "audio/voice/ivan/ivan-14.opus"
    ivan "Но немцы засели в центре. Особенно — на площади Свободы."

    show masha tension 2 at center # Сфокусирована на боевой задаче
    with easeoutleft

    voice "audio/voice/masha/loud_masha_27.opus"
    masha "Там, где был Дом торговли… теперь — их последний опорный пункт. Пулемёт на третьем этаже."

    n_narr "Я смотрю на разрушенные дома, обгоревшие трамваи… и вдруг — замечаю что-то в стороне."

    nvl hide
    nvl clear
    hide masha

    jump pows_camp_ruins

label pows_camp_ruins:
    scene minsk_pows_camp_ruins with fade
    stop sound
    play sound wind_low loop
    play music caged_heart loop fadein 2.0
    n_narr "Забор из колючей проволоки. Обгоревшие бараки. И… детская игрушка — обугленная кукла у ворот."

    nvl hide
    nvl clear

    soldier "Лагерь для наших пленных. Немцы сожгли его при отступлении."
    n_narr "На земле — обрывки документов. Фотографии. Имена…"

    nvl hide
    nvl clear

    n_narr "Одна из фотографий — молодой парень в форме. На обороте: Любе, жди меня. Вернусь — поженимся."
    n_narr "Он не вернулся."

    nvl hide
    nvl clear

    voice "audio/voice/kolya/kolya_013.opus"
    kolya "Зачем они это делали? Зачем так много зла?"
    voice "audio/voice/ivan/ivan-15.opus"
    ivan "Чтобы мы помнили. Чтобы никогда не допустили этого снова."

    n_narr "Я поднимаю куклу. Кладу в карман — рядом с письмом."

    stop music fadeout 2.0

    nvl hide
    nvl clear

    jump freedom_square_approach

label freedom_square_approach:
    scene minsk_freedom_square_ruins with fade
    play music theme_tense fadein 2.0
    play sound distant_gunfire

    n_narr "Площадь Свободы. Когда-то здесь гуляли люди. Теперь — руины и смерть."
    n_narr "В здании бывшего Дома торговли — пулемёт. Он простреливает всю площадь."

    nvl hide
    nvl clear

    voice "audio/voice/politruk/politruk_13.opus"
    politruk "Это последний очаг сопротивления в центре! Берём его — и Минск свободен!"

    voice "audio/voice/ivan/ivan-16.opus"
    ivan "Группа А — слева по развалинам. Группа Б — за мной. Искатель — прикрываешь."

    n_narr "Мы занимаем позиции. Воздух — густой от пыли и страха."

    nvl hide
    nvl clear

    play sound machine_gun
    scene minsk_freedom_square_ruins with vpunch

    n_narr "Пулемёт открывает огонь! Кирпичи летят в щепки!"
    voice "audio/voice/ivan/ivan-17.opus"
    ivan "Вперёд! Не дать им перезарядиться!"

    nvl hide
    nvl clear

    n_narr "Иван бросается вперёд — как всегда, первым. Его каска отлетает."
    n_narr "И вдруг — короткая очередь. Он падает."

    nvl hide
    nvl clear

    voice "audio/voice/kolya/kolya_014.opus"
    kolya "СТАРШИНА!!!"

    n_narr "Иван лежит у подножия лестницы. Кровь на гимнастёрке. Но он смотрит на меня — и кивает в сторону окна."

    voice "audio/voice/ivan/ivan-18.opus"
    ivan "Выпол… няй… приказ…"

    nvl hide
    nvl clear

    menu:
        "Выполнить приказ — уничтожить пулемёт":
            narr "Минск должен быть свободен. Даже ценой его жизни."
            n_narr "Я хватаю гранату. Бросок в окно. Взрыв. Пулемёт замолкает."
            n_narr "Я подбегаю к Ивану. Его глаза уже не видят."
            n_narr "Он умирает один. Но город — свободен."
            $ chose_duty = True
            nvl hide
            nvl clear
            show screen achievement_unlock("{size=14}Не стоит понимать доброту за слабость, грубость за силу, а подлость за умение жить.{/size}", box_len=400, read_len=5.0)
            jump minsk_liberated

        "Спасти Ивана — броситься к нему":
            narr "Он — не просто командир. Он — брат."
            n_narr "Я бросаюсь к нему. Пули вспарывают землю. Одна — в плечо. Вторая — в грудь."
            n_narr "Я падаю рядом. Его рука сжимает мою. Прости… — шепчет он."
            n_narr "Последнее, что я вижу — Коля, бросающийся в атаку с криком: ЗА СТАРШИНУ!"
            $ chose_comrades = True
            nvl hide
            nvl clear
            show screen achievement_unlock("{size=14}Жизнь можно начать с чистого листа, но почерк изменить невозможно.{/size}", box_len=400, read_len=5.0)
            jump minsk_liberated

label minsk_liberated:
    scene minsk_freedom_square_evening with fade
    stop music fadeout 3.0
    play sound distant_celebration
    play music theme_calm

    if chose_duty:
        n_narr "К вечеру площадь зачищена. Минск — свободен."
        n_narr "Жители несут цветы к зданию Дома торговли. Кто-то поёт «Священную войну»."
        n_narr "Коля стоит у тела Ивана. В его глазах — слёзы и ярость."

        nvl hide
        nvl clear

        voice "audio/voice/kolya/kolya_015.opus"
        kolya "Он заслужил похоронить его не на чужбине… а здесь. В освобождённом городе."

    elif chose_comrades:
        n_narr "Очнулся я в госпитале. Минск — свободен."
        n_narr "Коля сидит у койки. В глазах — гордость и боль."

        nvl hide
        nvl clear

        voice "audio/voice/kolya/kolya_016.opus"
        kolya "Ты спас его честь. И свою. Мы похоронили его на площади — как героя."

    voice "audio/voice/politruk/politruk_14.opus"
    politruk "Сегодня — великий день! Беларусь свободна!"
    n_narr "Но в этом празднике — горечь. Слишком много имён, что не вернутся домой."

    scene black with fade

    if chose_duty:
        nvl hide
        nvl clear

        scene black with fade

        n_narr "Ночью город не спит. Люди обнимаются, плачут, поют."
        n_narr "Я стою у разрушенного фонтана."

        nvl hide
        nvl clear

        n_narr "Я выжил. Но смогу ли я защитить страну?"
    elif chose_comrades:
        n_narr "Я не вернулся домой. Но, может, именно поэтому другие вернулись."

    nvl hide
    nvl clear

    scene black with dissolve
    n_narr "Через 80 лет… кто вспомнит нас? Кто сохранит память?"

    nvl hide
    nvl clear

    stop music
    jump epilogue_setup

label epilogue_setup:
    if chose_duty:
        jump epilogue_a
    elif chose_comrades:
        jump epilogue_b
    else:
        jump epilogue_a

label epilogue_a:
    nvl clear
    scene minsk_memorial_1944 with fade
    play music theme_calm fadein 3.0

    n_narr "4 июля 1944 года. Минск."
    n_narr "Коля и Маша стоят у импровизированного памятника — груда камней с красной звездой."
    show masha neutral at center # Скорбь/нейтралитет
    with easeoutleft

    voice "audio/voice/kolya/kolya_017.opus"
    kolya "Он заслужил покой в освобождённом городе."
    voice "audio/voice/masha/loud_masha_28.opus"
    masha "Мы будем помнить. Все."

    nvl hide
    nvl clear
    hide masha

    scene black with dissolve
    d_text "80 лет спустя…"

    nvl hide
    nvl clear

    scene minsk_memorial_2025_day with fade
    stop music fadeout 2.0
    play sound birds_morning

    grandson "Дед… ты гордишься собой?"
    narr "Я горжусь теми, кто не вернулся. А я… я просто выжил."

    grandson "Но благодаря тебе у нас есть сегодняшний день."
    grandson "И я обещаю — мы сохраним эту память и сделаем нашу Беларусь сильной."

    nvl hide
    nvl clear

    d_text "Внук кладёт цветы к мемориалу. На граните — тысячи имён. Среди них — Иван, Маша, Коля…"
    d_text "Современный Минск — живой, чистый, благоустроенный."
    d_text "Аллея Победы. Дети играют. Студенты читают. Жизнь продолжается!"

    nvl hide
    nvl clear
    scene black with fade
    d_text "Памяти всех, кто пал в боях за Беларусь. 1941–1944."
    pause 5.0

    jump game_end

label epilogue_b:
    nvl clear
    scene black with fade
    play music theme_tense fadeout 2.0
    play sound wind_low

    n_narr "3 июля 1944 года. Последнее мгновение."
    n_narr "Тьма. Боль. И крик Коли: ЗА СТАРШИНУ!"

    n_narr "Потом — тишина…"

    nvl hide
    nvl clear

    scene black with dissolve
    nvl clear

    n_narr "80 лет спустя…"

    nvl hide
    nvl clear

    scene minsk_memorial_2025_day with fade
    play sound birds_morning

    grandson "Ты когда-нибудь его видел?"
    voice "audio/voice/kolya/kolya_018.opus"
    kolya "Каждый день: в своих снах, в зеркале, в лицах молодых солдат!"

    d_text "Внук стоит у Мемориала «Минск — Город-герой». На чёрном граните — тысячи имён."
    d_text "Его палец останавливается на одном:"

    d_text "БЕЗЫМЯННЫЙ…"

    d_text "Рядом — ухоженная аллея с фонарями и скамейками. На табличке: «Героям, чьи имена неизвестны, но подвиг — вечен»."

    d_text "Солнце садится. Ветер шелестит листвой. Где-то играет гармонь."

    nvl hide
    nvl clear
    scene black with fade
    d_text "Он не вернулся. Но благодаря ему — вернулись другие!"
    pause 5.0

    jump game_end
label game_end:
    stop audio fadeout 2.0
    stop sound fadeout 2.0
    play music letting_my_heart_speak fadein 2.0
    $ mouse_visible = False
    scene black
    $ renpy.pause(1.544, hard=True)
    show age_16 at truecenter with Dissolve(0.3) 
    # 1.844
    $ renpy.pause(2.0, hard=True)
    hide age_16 with Dissolve(1.0)
    $ renpy.pause(1.5, hard=True)
    show screen end_credit with Dissolve(0.3)
    # 6.644
    $ renpy.pause(4.5, hard=True)
    hide screen end_credit with Dissolve(2.0)
    $ renpy.pause(1.3, hard=True)
    show halipov_ent with Dissolve(0.3)
    #14.444
    $ renpy.pause(2.099, hard=True)
    play sound mgs_over 
    #16.7
    $ renpy.pause(3.757, hard=True)
    hide halipov_ent with Dissolve(2.0)
    # 22.3
    $ mouse_visible = True
    jump game_credits