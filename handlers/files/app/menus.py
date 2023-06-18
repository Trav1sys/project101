menus = {
    'menu_main': {
        'title': 'Выберите один из пунктов меню:',
        'buttons': [
            {'text': 'Информация о вузе', 'callback': 'menu1_info'},
            {'text': 'Поступление', 'callback': 'menu_postuplenie'},
            {'text': 'Поддержка', 'callback': 'menu_support'}
        ]
    },
    'menu1_info': {
        'title': 'Бурятский институт инфокоммуникаций (филиал) Сибирского государственного университета телекоммуникаций и информатики в г. Улан-Удэ\n\nE-mail: bfsibguti@mail.ru\nТел: 8 (3012) 24-00-24\nФакс: 8 (3012) 43-16-44\nАдрес: 670031 г. Улан-Удэ ул. Трубачеева 152.',
        'message': 'Такой-то такой-то вуз',
        'buttons': [
            {'text': 'Назад', 'callback': 'menu_main'}
        ]
    },
    'menu_postuplenie': {
        'title': 'Поступление',
        'buttons': [
            {'text': 'Приемная комиссия', 'callback': 'priem'},
            {'text': 'Направления на высшее образование', 'callback': 'menu_NaprVishObr'},
            {'text': 'Направления на среднее профессиональное образование', 'callback': 'menu_NaprSrObr'},
            {'text': 'Назад', 'callback': 'menu_main'}
        ]
    },
    'priem': {
        'title': 'Приемная комиссия',
        'buttons': [
            {'text': 'График работы', 'callback': 'grafik'},
            {'text': 'Способы подачи документов', 'callback': 'podacha'},
            {'text': 'Назад', 'callback': 'menu_postuplenie'}
        ]
    },
    'grafik': {
        'title': 'График работы приемной комиссии:\nПонедельник\t9-00 – 17-00\nВторник\t9-00 – 17-00\nСреда\t9-00 – 17-00\nЧетверг\t9-00 – 17-00\nПятница\t9-00 – 16-00\n\nОбед\t12-00 – 13-00\nВыходные: Суббота и Воскресенье',

        'buttons': [
            {'text': 'Назад', 'callback': 'priem'}]
    },
    'podacha': {
        'title': 'Подача документов',

        'buttons': [
            {'text': 'Придти лично', 'callback': 'lichno'},
            {'text': 'Сервис поступление в вуз онлайн', 'callback': 'service'},
            {'text': 'Заказное письмо', 'callback': 'pismo'},
            {'text': 'По электронной почте', 'callback': 'email'},
            {'text': 'Подать прямо здесь', 'callback': 'menu_postuplenie'},
            {'text': 'Назад', 'callback': 'priem'}]
    },
    'lichno': {
        'title': 'Подойти лично в приемную комиссию по адресу г. Улан-Удэ, ул. Трубачеева, 152, каб 102. Проезд автобусом №77, 129, 82, 25',

        'buttons': [
            {'text': 'Назад', 'callback': 'podacha'}]
    },
    'service': {
        'title': 'Подача документов с использованием суперсервиса "Поступление в вуз онлайн", посредством федеральной государственной информационной системы "Единый портал государственных и муниципальных услуг (функций)".'
'Как получить услугу?\n'
'- Авторизуйтесь на портале (услуга доступна только для подтвержденной учетной записи)\n'
'- Заполните заявление\n'
'- Отправьте заявление и следите за уведомлениями от вузов\n'
'- Подайте согласие на зачисление в вуз\n'
'- Получите уведомление о зачислении в вуз',

        'buttons': [
            {'text': 'Назад', 'callback': 'podacha'}]
    },
    'pismo': {
        'title': 'Заказным письмом через операторов почтовой связи на адрес – 670031, Республика Бурятия, г. Улан-Удэ, Трубачеева, д.152',

        'buttons': [
            {'text': 'Назад', 'callback': 'podacha'}]
    },
    'email': {
        'title': 'По электронной почте БИИК СибГУТИ priem@biik.ru',

        'buttons': [
            {'text': 'Назад', 'callback': 'podacha'}]
    },




    'menu_NaprSrObr': {
        'title': 'Перечень направлений для приема в БИИК СИБГУТИ на среднее профессиональное',
        'message': 'Просмотрите направления и то, которое вас интересует, выберите в меню выше',
        'photo': r'C:\Users\Misha\PycharmProjects\project10\handlers\files\SredneeObr.jpg',
        'buttons': [
            {'text': 'Инфокоммуникационные сети и системы связи', 'callback': 'ISSS'},
            {'text': 'Монтаж, техническое обслуживание и ремонт электронных приборов и устройств', 'callback': 'MTOREPU'},
            {'text': 'Обеспечение информационной безопасности автоматизированных систем', 'callback': 'OIBAS'},
            {'text': 'Сетевое и системное администрирование', 'callback': 'SSA'},
            {'text': 'Информационные системы и программирование', 'callback': 'ISP'},
            {'text': 'Почтовая связь', 'callback': 'PS'},
            {'text': 'Экономика и бухгалтерский учет (по отраслям)', 'callback': 'EBU'},
            {'text': 'Главное меню', 'callback': 'menu_main'}
        ]
    },
    'menu_NaprVishObr': {
        'title': 'Перечень направлений для приема в БИИК СИБГУТИ на высшее образование',
        'message': 'Просмотрите направления и то, которое вас интересует, выберите в меню выше',
        'photo': r'C:\Users\Misha\PycharmProjects\project10\handlers\files\Vishka.jpg',
        'buttons': [
            {'text': 'Инфокоммуникационные технологии и системы связи', 'callback': 'IKTSS'},
            {'text': 'Информатика и вычислительная техника', 'callback': 'IVT'},
            {'text': 'Главное меню', 'callback': 'menu_main'}
        ]
    },
    'ISSS': {
        'title': 'Инфокоммуникационные сети и системы связи',
        'buttons': [
            {'text': 'Подайте информацию прямо здесь', 'callback': 'ISSS_db'},
            {'text': 'Назад', 'callback': 'menu_postuplenie'}, ]
    },
    'ISSS_db': {
        'title': 'Инфокоммуникационные сети и системы связи',
        'buttons': [
            {'text': 'Подайте информацию прямо здесь', 'callback': 'ISSS_db'},
            {'text': 'Назад', 'callback': 'menu_main'}, ]
    },
    'MTOREPU': {
        'title': 'Монтаж, техническое обслуживание и ремонт электронных приборов и устройств',
        'buttons': [
            {'text': 'Подайте информацию прямо здесь', 'callback': 'MTOREPU_db'},
            {'text': 'Назад', 'callback': 'menu_postuplenie'}, ]
    },
    'MTOREPU_db': {
        'title': 'Монтаж, техническое обслуживание и ремонт электронных приборов и устройств',
        'buttons': [
            {'text': 'Подайте информацию прямо здесь', 'callback': 'MTOREPU_db'},
            {'text': 'Назад', 'callback': 'menu_main'}, ]
    },
    'OIBAS': {
        'title': 'Обеспечение информационной безопасности автоматизированных систем',
        'buttons': [
            {'text': 'Подайте информацию прямо здесь', 'callback': 'OIBAS_db'},
            {'text': 'Назад', 'callback': 'menu_postuplenie'}, ]
    },
    'OIBAS_db': {
        'title': 'Обеспечение информационной безопасности автоматизированных систем',
        'buttons': [
            {'text': 'Подайте информацию прямо здесь', 'callback': 'OIBAS_db'},
            {'text': 'Назад', 'callback': 'menu_main'}, ]
    },
    'SSA': {
        'title': 'Сетевое и системное администрирование',
        'buttons': [
            {'text': 'Подайте информацию прямо здесь', 'callback': 'SSA_db'},
            {'text': 'Назад', 'callback': 'menu_postuplenie'}, ]
    },
    'SSA_db': {
        'title': 'Сетевое и системное администрирование',
        'buttons': [
            {'text': 'Подайте информацию прямо здесь', 'callback': 'SSA_db'},
            {'text': 'Назад', 'callback': 'menu_main'}, ]
    },
    'ISP': {
        'title': 'Информационные системы и программирование',
        'buttons': [
            {'text': 'Подайте информацию прямо здесь', 'callback': 'ISP_db'},
            {'text': 'Назад', 'callback': 'menu_postuplenie'}, ]
    },
    'ISP_db': {
        'title': 'Информационные системы и программирование',
        'buttons': [
            {'text': 'Подайте информацию прямо здесь', 'callback': 'ISP_db'},
            {'text': 'Назад', 'callback': 'menu_main'}, ]
    },
    'PS': {
        'title': 'Почтовая связь',
        'buttons': [
            {'text': 'Подайте информацию прямо здесь', 'callback': 'PS_db'},
            {'text': 'Назад', 'callback': 'menu_postuplenie'}, ]
    },
    'PS_db': {
        'title': 'Почтовая связь',
        'buttons': [
            {'text': 'Подайте информацию прямо здесь', 'callback': 'PS_db'},
            {'text': 'Назад', 'callback': 'menu_main'}, ]
    },
    'EBU': {
        'title': 'Экономика и бухгалтерский учет (по отраслям)',
        'buttons': [
            {'text': 'Подайте информацию прямо здесь', 'callback': 'EBU_db'},
            {'text': 'Назад', 'callback': 'menu_postuplenie'}, ]
    },
    'EBU_db': {
        'title': 'Экономика и бухгалтерский учет (по отраслям)',
        'buttons': [
            {'text': 'Подайте информацию прямо здесь', 'callback': 'EBU_db'},
            {'text': 'Назад', 'callback': 'menu_main'}, ]
    },
    'IVT': {
        'title': 'Информатика и вычислительная техника',
        'buttons': [
            {'text': 'Подайте информацию прямо здесь', 'callback': 'IVT_db'},
            {'text': 'Назад', 'callback': 'menu_postuplenie'}, ]
    },
    'IVT_db': {
        'title': 'Информатика и вычислительная техника',
        'buttons': [
            {'text': 'Подайте информацию прямо здесь', 'callback': 'IVT_db'},
            {'text': 'Назад', 'callback': 'menu_main'}, ]
    },

    'IKTSS': {
            'title': 'Инфокоммуникационные технологии и системы связи',
            'buttons': [
                {'text': 'Подайте информацию прямо здесь', 'callback': 'IKTSS_db'},
                {'text': 'Назад', 'callback': 'menu_postuplenie'},]
        },

    'IKTSS_db': {
            'title': 'Инфокоммуникационные технологии и системы связи',
            'buttons': [
                {'text': 'Подайте информацию прямо здесь', 'callback': 'IKTSS_db'},
                {'text': 'Назад', 'callback': 'menu_postuplenie'},]
        },
}