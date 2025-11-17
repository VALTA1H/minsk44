label day2_sleep:
    scene black with fade
    n_narr "Сон был коротким и тревожным. Неудивительно, после вчерашних то событий"
    n_narr "Но утро пришло без солнца. Только дым и гул артиллерии на горизонте."
    n_narr "Мы сейчас отправляемся в сторону Бобруйска, чтобы помочь в зачистке города."

    nvl hide
    nvl clear

    jump day2_start

label day2_start:
    scene city_ruins_morning with fade
    play music theme_tense fadein 2.0
    play sound distant_gunfire loop

    n_narr "К полудню мы добрались до места назначения."
    n_narr "Сегодня 30 июня. Мы стоим на окраине почти освобождённого города - Бобруйска. Вчера здесь бушевал ад."
    n_narr "Теперь — мёртвая тишина, нарушаемая лишь треском горящих балок и стонами раненых. Воздух пропитан запахом гари, пыли и крови."
    n_narr "Вчера, к десяти часам утра, город был наш. Но победа далась страшной ценой."
    n_narr "Говорят, под Бобруйском фашисты потеряли пятьдесят тысяч своих. «Котёл» ликвидирован."

    nvl hide
    nvl clear

    voice "audio/voice/ivan/ivan-06.opus"
    ivan "Внимание! Враг отступил, но оставил «крыс» — снайперов и миномётчиков. Двигаемся осторожно, по укрытиям!"
    voice "audio/voice/politruk/politruk_6.opus"
    politruk "Помните, товарищи! Этот город — наша земля. Каждый дом, каждая улица — свидетель зверств оккупантов. Наша задача зачистить его до конца!"

    n_narr "Мы продвигаемся вглубь. Нас встречают обугленные, обстрелянные дома. На дороге — следы крови и сгоревшая техника."
    n_narr "Проходим мимо разрушенного здания. На асфальте неподалеку виднеется надпись мелом: «ДЕТИ». Сердце сжимается."

    nvl hide
    nvl clear

    scene city_courtyard with dissolve
    civil "Кто-нибудь, помогите!"

    n_narr "Из подвала одного из домов выбегает мужчина лет сорока. Его лицо покрыто сажей, руки в ожогах и ссадинах, глаза полны отчаяния."

    nvl hide
    nvl clear

    civil "Мой брат… он ранен! Вчера, когда начался штурм, его ранило и теперь он не может идти!"
    voice "audio/voice/ivan/ivan-07.opus"
    ivan "Где он? Проведи наc к нему."
    civil "Там, в подвале соседнего дома. Но… там ещё и фриц… Раненый… Они вместе, как в ловушке."

    n_narr "Старшина Иван переглядывается со мной. Ситуация сложная. Раненый враг — это опасность и отвестенность за соотечественника."

    nvl hide
    nvl clear

    menu choice_wounded_enemy:
        "Идти спасать обоих":
            narr "Раненый — не враг. Он уже не опасен."
            n_narr "Мы осторожно спускаемся в полутёмный подвал. На полу лежат двое: наш парень и немец."
            n_narr "Немец смотрит на нас с ненавистью, но силы держать винтовку у него нет. Наш раненый стонет от боли."
            n_narr "И тут немец на ломаном русском с сильным немецким акцентом говорит:"

            nvl hide
            nvl clear

            hanz "Те дети, которых мы оставить в живых.. Они все будут должны служить и восхвалять нашего фюрреру!"
            n_narr "Не обращая внимания на его возгласы, мы продолжаем операцию по спасению."            
            n_narr "Я бросаю свой бинт местному жителю: «Перевяжи его. Быстро!»"
            n_narr "Иван приказывает: «Забираем своего. Немца оставляем. Пусть медсанбат разбирается»."
            $ showed_mercy = True

        "Забрать только нашего":
            narr "Наша задача — сохранить своих. Остальное — не наше дело."
            n_narr "Мы забираем гражданского. Местный житель помогает нам вынести его на улицу."
            
            show kolya scared at center with dissolve
            n_narr "В подвале остаётся стон раненого немца. Коля смотрит вниз с ужасом, но молчит."
            hide kolya
            
            n_narr "Иван коротко командует: «Закройте вход. Пусть сидит там, пока не подохнет или пока его не найдут»."
            $ showed_mercy = False

    nvl hide
    nvl clear

    scene city_street_ruins with dissolve
    play sound machine_gun
    scene city_street_ruins with hpunch

    n_narr "Продолжаем движение. Внезапная очередь заставила нас всех спрятаться по углам. Пули свистят над головами."
    n_narr "Огонь ведётся из здания бывшего почтамта. Пулемёт простреливает всю улицу. Продвижение невозможно."

    nvl hide
    nvl clear

    show masha tension 2 at left
    with easeinleft
    with hpunch

    voice "audio/voice/masha/loud_masha_5_2.opus"
    masha "Я знаю это здание! Слева — разрушенная лестница на второй этаж, а справа - подвал, выходящий во двор."

    voice "audio/voice/masha/loud_masha_6.opus"
    masha "Могу провести в обход с тыла, но нужно удостовериться в безопасности."

    n_narr "Старшина Иван смотрит на меня. Время решать."

    nvl hide
    nvl clear

    menu choice_post_office:
        "Бросить гранату в окно":
            narr "Нет времени на обходы. Нужно подавить огневую точку сейчас."
            play sound grenade_throw
            n_narr "Я вырываю гранату из подсумка и метаю её в разбитое окно второго этажа."
            play sound explosion_loud
            scene city_street_ruins with vpunch
            n_narr "Взрыв. Облако пыли и дыма. Огонь прекратился."
            n_narr "Мы врываемся внутрь… В подвале, под завалами, слышен детский плач."
            hide masha
            nvl hide
            nvl clear

            jump day2_basement

        "Пойти на обход с Машей":
            show screen achievement_unlock("{size=14}Только идиот доверит свою жизнь оружию.{/size}", box_len=300, read_len=3.0)
            narr "Лучше не рисковать. Вдруг там гражданские…"
            voice "audio/voice/masha/loud_masha_7.opus"
            show masha tension 2 at left
            masha "За мной. И чтоб тише воды…"
            scene black with dissolve 
            n_narr "Мы пробираемся по завалам во двор, затем — в подвал здания."
            n_narr "Из темноты на нас смотрят две пары испуганных глаз. Старуха прижимает к себе ребёнка."
            n_narr "Рядом с ними — деревянный ящик с красным крестом."
            $ masha_rep += 1
            nvl hide
            nvl clear
            hide masha

            jump day2_basement_peaceful

label day2_basement_peaceful:
    scene city_basement with fade
    stop sound
    play sound child_crying

    n_narr "Подвал наполнен сыростью и страхом. На полу, прижавшись к углу, сидит старуха с ребенком на руках."
    n_narr "Ящик с медикаментами стоит в углу. На нём — следы немецких сапог. Видимо, его готовили к эвакуации."

    nvl hide
    nvl clear
    jump choice_med

label day2_basement:
    scene city_basement with fade
    stop sound
    play sound child_crying

    n_narr "Подвал наполнен сыростью и страхом. Старуха, чудом оставшаяся в живых, дрожит, прикрывая ребёнка своим телом."
    n_narr "Ящик с медикаментами стоит в углу. На нём — следы немецких сапог. Видимо, его готовили к эвакуации."

    nvl hide
    nvl clear
    jump choice_med

label choice_med:
    show masha neutral at left
    with easeinleft
    menu choice_medicine:
        "Что сделать с ящиком?"
        "Забрать всё содержимое":
            narr "Война не щадит никого. Наши раненые — в первую очередь."
            n_narr "Я беру ящик. Старуха тихо всхлипывает, но не сопротивляется."
            
            show kolya mad at right with dissolve
            n_narr "Маша отводит взгляд. Коля сжимает губы."
            hide kolya
            
        "Взять только бинты и перевязочные пакеты":
            narr "Они тоже люди. Оставим им хоть что-то."
            n_narr "Я вынимаю из ящика только самое необходимое для полевого госпиталя — бинты и пакеты."
            n_narr "Старуха кивает, её глаза полны слёз благодарности."
            show masha happy at left
            n_narr "Маша кладёт руку мне на плечо и шепчет:"
            voice "audio/voice/masha/loud_masha_8.opus"
            masha "Спасибо"
            $ masha_rep +=1

    stop sound
    nvl hide
    nvl clear

    hide masha 

    scene destroyed_house with dissolve
    n_narr "Пока отряд отдыхает, я замечаю полуразрушенный дом с выгоревшим фасадом. А за ним здание с обугленной дверью где вырезана шестиконечная звезда, вырезанная топором."
    n_narr "Маша, увидев это, замирает. Её лицо становится каменным."

    nvl hide
    nvl clear

    scene ghetto with dissolve
    play music warum volume 0.5 loop
    show masha scared at left
    with easeinleft
    with hpunch

    voice "audio/voice/masha/loud_masha_9.opus"
    masha "{bt=1}Здесь был концентрационный {sc=3}{color=#E10600}лагерь… концлагерь{/color}{/sc}. Тут держали евреев.{/bt}"
    
    voice "audio/voice/masha/loud_masha_10.opus"
    show masha scared at left
    masha "{bt=1}Осенью сорок первого… их всех согнали сюда. А потом… потом большую часть{para}повели в сарай на окраине деревни.{/bt}"
    
    voice "audio/voice/masha/loud_masha_11.opus"
    masha "{bt=1}Говорят, крики были слышны в соседних сёлах."
    
    voice "audio/voice/masha/loud_masha_12.opus"
    masha "А потом — тишина…"
    
    voice "audio/voice/masha/loud_masha_13.opus"
    masha "{bt=1}И черные облака.{/bt}"

    n_narr "Она не плачет. Её боль глубже слёз. Она — память о тех, кого уже не вернуть."
    n_narr "Я кладу руку на обгоревшую дверь. {b}Три года{/b} оккупации. Тысячи убитых мирных жителей. Сотни расстрелянных семей." 
    n_narr "Лучше пока что об этом не думать. Они ответят за все что они сделали!"

    nvl hide
    nvl clear

    hide masha

    scene city_square_evening with fade
    stop music fadeout 2.0
    stop sound fadeout 2.0
    play music theme_calm fadein 2.0
    play sound distant_celebration

    n_narr "К вечеру город полностью в наших руках. Остатки немецкого гарнизона уничтожены или взяты в плен."
    n_narr "Жители, прятавшиеся в подвалах, выходят на улицы. Их лица — смесь радости, боли и неверия."

    nvl hide
    nvl clear

    voice "audio/voice/ivan/ivan-08.opus"
    ivan "Молодцы, ребята! Но расслабляться рано. Получен приказ: преследовать отступающего врага. Направление — Минск."
    voice "audio/voice/politruk/politruk_7.opus"
    politruk "Минск ждёт нас! Путь к столице открыт!"

    n_narr "Мы смотрим на руины. Сегодня мы освободили город. Завтра — снова в бой."
    n_narr "Нужно помнить. Помнить о Бобруйске. Помнить о всех городах и деревнях Беларуси. Об их мёртвых улицах и живой боли его жителей."

    nvl hide
    nvl clear
    stop sound
    scene black with fade
    n_narr "День второй позади. Впереди — леса, болота и погоня за отступающим врагом."
    nvl hide
    nvl clear
    jump day3_start