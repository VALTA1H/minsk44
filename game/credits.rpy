define supporter_screen_speed = 40.0  
transform credits_scroll(speed):
    ypos 1080
    linear speed ypos -7450
style titres_list_white_text:
    size 30
    color "#fff"
    xalign 0.5
    yalign 0.5
style titres_list_black_text:
    size 30
    color "#000"
    xalign 0.5
    yalign 0.5
screen support(bg = "black"):
    style_prefix "credits"
    if titres_white:
        add "white"
    else:
        add "black"
    frame at credits_scroll(supporter_screen_speed):
        background None
        xalign 0.5
        vbox:
            
            if titres_white:
                style_prefix "titres_list_black"
            else:
                style_prefix "titres_list_white"
            spacing 200
            null height 20
            vbox:
                spacing 40 align(0.5, 0.5)
                text _("Автор сценария:") size 40 bold True
                text "Арсений Дерновский & Коджакулак Алтай"
            vbox:
                spacing 40 align(0.5, 0.5)
                text _("Художник:") size 40 bold True
                text "Footer Heart"
            vbox:
                spacing 40 align(0.5, 0.5)
                text _("Дизайнер:") size 40 bold True
                text "Арсений Дерновский & Коджакулак Алтай"
            vbox:
                spacing 40 align(0.5, 0.5)
                text _("Озвучка:") size 40 bold True
                text "Маша - Александра Дерновская"
                text "Политрук - Александр Хаев"
                text "Коля - Александра Дерновская"
                text "Иван - Александра Дерновская"
            vbox:
                spacing 40 align(0.5, 0.5)
                text _("Программист:") size 40 bold True
                text "Арсений Дерновский"
            null height 200
            vbox:
                spacing 40 align(0.5, 0.5)
                text _("Музыка:") size 40 bold True
                vbox:
                    spacing 10 xalign 0.5 yalign 0.5
                    text "Caged Heart"
                    text "Breathlessy"
                    text "Cold Iron"
                    text "Concord"
                    text "Friendship"
                    text "High Tension"
                    text "Jitter"
                    text "Letting my heart speak"
                    text "Main Theme"
                    text "Moment of Decesion"
                    text "Nocturne"
                    text "Painful History"
                    text "Shadow of the Truth"
                    text "Tension"
                    text "Theme Calm"
                    text "Theme Tense"
                    text "Warum"
                    text "Wiosna"
            null height 100
            vbox:
                spacing 40 align(0.5, 0.5)
                vbox:
                    spacing 10 align(0.5, 0.5)
                    text _("Спасибо за поддержку:") size 40 bold True
                    hbox:
                        spacing 10 xalign 0.5
                vbox:
                    spacing 10 xalign 0.5 yalign 0.5
                    text "Халипов Сергей Сергеевич"
                    text "Захарова Анастасия Сергеевна"
            null height 100
            vbox:
                spacing 40 align(0.5, 0.5)
                text _("Особая благодарность:") size 40 bold True
                vbox:
                    spacing 10 xalign 0.5 yalign 0.5
                    text "Александр Хаев"
                    text "Александра Дерновская"
                    text "Footer Heart"
                    text "Наталья Дерновская"
                    text "Антон Семенченко"
            null height 500
            text _("Создано с помощью Ren'Py") size 40 bold True
            null height 1100
            add "gui/title.png"
style credits_hbox:
    spacing 40
    ysize 30
style credits_label:
    xalign 0.5
style credits_text:
    xalign 0.5
default titres_white = False  

label game_credits:
    $ _game_menu_screen = None
    $ renpy.config.skipping = None
    $ _skipping = False
    $ renpy.pause(0.6, hard=True)
    show screen support
    if persistent.seen_titres:
        pause supporter_screen_speed
    else:
        $ renpy.pause(supporter_screen_speed, hard=True)
    $ persistent.seen_titres = True
    $ renpy.pause(2.0, hard=True)
    stop music fadeout 4.0
    hide screen support with Dissolve(4.0)
    $ _game_menu_screen = "save_screen"
    $ _skipping = True
    
    return
