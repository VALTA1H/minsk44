label day3_start:
    scene black with fade
    play music theme_tense fadein 2.0

    n_narr "1 июля. Третий день прорыва. Мы ушли от Бобруйска — вглубь белорусских лесов. И даже тут слышен этот гул работающей артиллерии."
    n_narr "Немцы бегут. Бросают технику, раненых, даже знамёна. Но мы не даём им передышки."

    nvl hide
    nvl clear

    scene forest_swamp_morning with fade
    play sound distant_gunfire loop
    play sound crickets_sound
    show ivan neutral at left with dissolve
    voice "audio/voice/ivan/ivan-09.opus"
    ivan "След свежий. Колёса, гусеницы… и кровь."
    hide ivan
    show masha tension 2 at right
    with easeinright

    voice "audio/voice/masha/loud_masha_14.opus"
    masha "Они везли офицеров. Может, даже штабников."

    n_narr "Маша — как лиса в лесу. Видит то, что скрыто от других."

    nvl hide
    nvl clear

    show politruk neutral at center with dissolve
    voice "audio/voice/politruk/politruk_8.opus"
    politruk "Если поймаем их — получим планы обороны Минска!"
    hide politruk with dissolve
    show ivan mad at left with dissolve
    voice "audio/voice/ivan/ivan-10.opus"
    ivan "А если засада — потеряешь отряд."
    hide ivan

    hide masha

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

    voice "audio/voice/soldier/soldier_2.opus"
    soldier "Расстреляны… в упор."
    n_narr "На земле — обломки касок, окровавленные бинты. Немцы ушли недавно."

    nvl hide
    nvl clear

    show masha alarm at left
    with easeinleft
    voice "audio/voice/masha/loud_masha_15.opus"
    masha "Под палаткой — ящик."

    if not avoided_ambush:
        play sound machine_gun loop
        scene swamp_clearing with hpunch
        n_narr "Из кустов — очередь! Засада!"
        show ivan mad at center
        voice "audio/voice/ivan/ivan-11.opus"
        ivan "В укрытие!"
        hide ivan

        nvl hide
        nvl clear

        n_narr "После ожесточенного боя мы всё же смогли отбиться и выйти из засады живыми."

        nvl hide
        nvl clear

    stop sound
    hide masha
    jump night_camp

label road_march:
    scene forest_road_dust with fade
    n_narr "Дорога пуста. Только дым от горящих деревень и следы гусениц."
    show politruk neutral at center with dissolve
    voice "audio/voice/politruk/politruk_9.opus"
    politruk "Так фашисты уходят из Беларуси — с огнём и пеплом."
    hide politruk with dissolve

    scene roadside_village with fade
    voice "audio/voice/old_woman/old_woman_1.opus"
    old_woman "Спасибо, хлопцы… Буду молиться за ваше здравие."
    n_narr "Она даёт кусок хлеба и иконку. Мы её поблагодарили и пошли дальше."

    jump night_camp

label night_camp:
    scene forest_camp_night with fade
    stop music fadeout 2.0
    play sound crickets_sound loop
    play music theme_calm fadein 3.0

    n_narr "Ночь. Костёр потрескивает. Усталость — до костей."
    n_narr "Мы с Колей и Машей сели у костра."

    nvl hide
    nvl clear

    if masha_rep >= 1:
        show kolya neutral at left:
            linear 0.5 matrixcolor BrightnessMatrix(-0.3) * TintMatrix("#e2582236")
        show masha neutral at right:
            linear 0.5 matrixcolor BrightnessMatrix(-0.3) * TintMatrix("#e2582236")
        with ease
        
        voice "audio/voice/masha/loud_masha_16.opus"
        masha "Ты помнишь, что мы — люди. Даже здесь."
        
        voice "audio/voice/masha/loud_masha_17.opus"
        show masha scared at right:
            linear 0.5 matrixcolor BrightnessMatrix(-0.3) * TintMatrix("#e2582236")
        masha "Я из Борок… Там, где сожгли деревню."
        
        voice "audio/voice/masha/loud_masha_18.opus"
        masha "Загнали всех в сарай… маму, отца, сестрёнку…"
        
        voice "audio/voice/masha/loud_masha_19.opus"
        masha "Больше никто не выжил. Я помню каждое лицо."
        
        show kolya neutral at left:
            matrixcolor BrightnessMatrix(-0.3) * TintMatrix("#e2582236")
        voice "audio/voice/kolya/kolya_06.opus"
        kolya "А как ты смогла выбраться?"
        
        voice "audio/voice/masha/loud_masha_20.opus"
        masha "Я выскочила первой."
        
        voice "audio/voice/masha/loud_masha_21.opus"
        masha "Слышала, как кричали дети…"

    else:
        show kolya neutral at left:
            linear 2.0 matrixcolor BrightnessMatrix(-0.3) * TintMatrix("#e2582236")
        show masha angry at right:
            linear 2.0 matrixcolor BrightnessMatrix(-0.3) * TintMatrix("#e2582236")
        with ease
        
        voice "audio/voice/masha/loud_masha_22.opus"
        masha "Я из Борок. Из той деревни, что стёрли с лица земли…"
        voice "audio/voice/masha/loud_masha_23.opus"
        masha "Я помню их глаза. Так что не говори мне про необходимость."

    n_narr "Её слова — как нож в сердце. Но мы молчим. Завтра — снова в бой."
    show screen achievement_unlock("{size=14}Я наблюдала за глупостью человечества через прицел своей винтовки.{/size}", box_len=400, read_len=5.0)

    nvl hide
    nvl clear
    hide kolya
    hide masha
    stop music fadeout 2.0
    jump day4_start