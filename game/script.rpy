label disclaimer:
    scene black with fade
    
    d_text "Этот проект является художественной визуальной новеллой, основанной на исторических событиях операции «Багратион» в 1944 году."
    d_text "Он не преследует целей пропаганды, а ставит своей задачей честное и реалистичное отображение суровых условий и моральных дилемм войны."
    d_text "Все персонажи и их поступки являются вымышленными. Игра содержит сцены насилия и трагические моменты."
    
    menu:
        "Хочу продолжить игру":
            nvl hide
            nvl clear
            pass 
        
        "Не хочу продолжать (Выход из игры)":
            nvl hide
            nvl clear
            $ renpy.full_quit()     
    return

define artillery = "audio/artillery.mp3"
define rain = "audio/rain.mp3"
define machine_gun = "audio/machine_gun.mp3"
define birds_morning = "audio/birds_morning.mp3"
define theme_calm = "audio/theme_calm.mp3"
define incoming_shell_rising = "audio/incoming_shell_rising.mp3"
define explosion_loud = "audio/explosion_loud.mp3"
define theme_tense = "audio/theme_tense.mp3"

define n_narr = Character("Безымянный", color="#91d46a", kind=nvl)
define narr = Character("Безымянный", color="#91d46a")
define d_text = Character("Автор",color="#ffffff", kind=nvl) 
define scene_narr = Character(None,)

define ivan = Character("Иван", color="#b0e0e6")
define kolya = Character("Коля", color="#add8e6")
define politruk = Character("Политрук", color="#ff7f7f")
define masha = Character("Маша", color="#98fb98")
define soldier = Character("Рядовой", color="#ffffff")

label pre_history:
    scene black with fade
    play music theme_calm fadein 2.0
    scene bg bedroom_morning with fade 
    
    n_narr "Утренний свет. Я помню только этот свет. И запах свежего хлеба, который давно не чувствовал."
    n_narr "Я помню обещание, которое дал ей. Вернуться. Несмотря ни на что."
    n_narr "Она ждет."
    
    nvl hide
    nvl clear

    stop music fadeout 3.0
    
    n_narr "Но это сон... Все неожиданно начинает дрожать."

    nvl hide
    nvl clear
    
    scene black with dissolve
    play sound incoming_shell_rising fadein 2.0 loop
    
    n_narr "Гул."
    n_narr "Я слышу его сквозь сон. Этот оглушающий гул. Низкий. Нарастающий. Он всё ближе."

    nvl hide
    nvl clear
    
    stop sound 
    play sound explosion_loud 
    scene black with hpunch
    
    scene bg trench_night with fade 
    
    play music theme_tense fadein 1.0
    play sound rain loop
    
    scene_narr "Удар!" 
    
    n_narr "Глаза открываются рывком. В рот набилась земля. Чёрт..."

    nvl hide
    nvl clear
    
    return

label start:
    call disclaimer 
    call pre_history 
    
    scene bg trench_night with fade 

    narr "Ночь на 28 июня. Восточный берег реки Березина. Если переживу, отмечу это."

    n_narr "Тяжёлые капли дождя барабанят по каске. Вдалеке слышен приглушённый гул артиллерии и стук пулеметов."
    n_narr "Отряд сидит в укрытии, прижавшись к мокрой земле."

    nvl hide
    nvl clear

    ivan "Всем внимание. До сигнала меньше часа. Проверить снаряжение, подогнать ремни. Отдыхаем, пока можем."

    kolya "Т-товарищ старшина... я..." with hpunch
    n_narr "Коля, молодой боец, заметно нервничает, его дыхание сбивается."

    nvl hide
    nvl clear

    ivan "Спокойно, солдат! Первый раз всегда страшно. Держись рядом."

    n_narr "Коля, молодой боец, дрожит. Он сидит в невыгодной воронке. Слишком заметен, надо ему помочь... Будто нам лишних потерь еще не хватало."
    n_narr "Аккуратно подойдя к Коле и положив руку на его плечо, я шепчу:"

    nvl hide
    nvl clear
    
    narr "возьми позицию правее меня, эта воронка лучше укроет." 
    kolya "П-понял... спасибо, товарищ..."

    n_narr "Внезапно небо озаряется яркими вспышками. Начинается артподготовка."
    n_narr "Первые лодки уже спускают на воду. Холодные брызги летят в лицо."

    nvl hide
    nvl clear

    ivan "Вперёд! За мной! Держать строй!"
    
    n_narr "Сигнал. Начинается хаос. Мы бросаемся в лодку."
    
    scene bg river_crossing
    play sound machine_gun
    
    n_narr "Вода, на удивление, кристально чистая, Дыхание перехватывает. Вокруг крики, свист пуль, взрывы мин, брызги."
    n_narr "Всё, что я могу сделать — это прижаться к борту лодки в надежде, что мы сможем проплыть к западному берегу."

    nvl hide
    nvl clear
    
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene bg western_bank with fade 
    play music theme_tense 
    n_narr "Спустя часы, казавшиеся вечностью, мы захватили плацдарм. Мокрые, уставшие, но живые."
    
    nvl hide
    nvl clear

    scene black with dissolve
    scene bg dusty_road_day with fade
    
    n_narr "Утро сменило ночь. Мы совершаем стремительный марш при поддержке техники. Жара и пыль поднимается столбом. Слышен лишь рев моторов."

    nvl hide
    nvl clear

    politruk "Держать темп, товарищи! Каждая минута — это километры, отделяющие нас от фашистского зверя!"
    politruk "Именно наша скорость — ключ к успеху «Багратиона»! Нельзя дать им подготовить оборону!"
    
    scene bg spearhead_view with dissolve 

    n_narr "На главной дороге грохочут танки и несётся кавалерия."

    nvl hide
    nvl clear

    politruk "Вот они, товарищи! Авангард прорыва! Кавалерийско-механизированная группа Плиева!"
    politruk "Их дело — рвать оборону, наше — не отставать и зачищать фланги."
  
    scene bg forest_ambush with dissolve 
    
    masha "Тихо! Сюда!"
    
    n_narr "Нас останавливает партизанка, Маша. Она указывает на лесную дорогу."

    nvl hide
    nvl clear

    masha "Там застрял немецкий обоз. Два грузовика, охрана — тыловики. Шанс восполнить припасы."

    ivan "Это ловушка, Маша? Или...?"
    
    masha "Нет. Застряли в грязи. У них нет времени ждать."
    
    n_narr "Старшина смотрит на меня. Припасы нужны, но риск велик."

    nvl hide
    nvl clear
    
    menu choice_convoy:
        "Атаковать немедленно (Рискованно, но быстро)":
            narr "Припасы на исходе... Нам жизненно необходимо их восполнить."
            ivan "Хорошо. Берём в кольцо. Атака!"
            jump convoy_fight
        
        "Сообщить командованию по рации (Безопасно, но потеря припасов)":
            narr "Риск неоправдан. Лучше передать информацию основным силам."
            politruk "Верное решение, солдат. Разумная предосторожность."
            jump convoy_report

label convoy_fight:
    scene black with fade
    play sound machine_gun
    n_narr "Начинается короткий, но ожесточенный бой. Солдаты вермахта были застигнуты врасплох. Мы отвоевали припасы."
    nvl hide
    nvl clear
    jump end_of_day1

label convoy_report:
    n_narr "Передаём координаты обоза. Через полчаса слышим отдалённый взрыв. Скорее всего, немцы сами уничтожили обоз при отступлении, или его перехватили другие."
    n_narr "Мы остались с тем, что имели, но избежали потерь."
    nvl hide
    nvl clear
    jump end_of_day1

label end_of_day1:
    scene black with fade
    n_narr "К вечеру мы выходим на подступы к городу."
    n_narr "Вдалеке слышны тяжелые бои — идет штурм."
    n_narr "Первый день прорыва закончен."
    nvl hide
    nvl clear
    jump day_2.sleep