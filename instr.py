win_x, win_y = 200, 100
win_width, win_height = 1000, 600

txt_hello = 'Добро пожаловать в программу по определению состояния здоровья!'
txt_next = 'Начать'
txt_instruction = 'Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья. Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке. У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд; затем в течение 45 секунд испытуемый выполняет 30 приседаний. После окончания нагрузки испытуемй ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд, а потом - за последние 15 секунд первой минуты периода восстановления. Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.' 
txt_title = 'Здоровье'
txt_name = 'Введите ФИО:'
txt_hintname = "ФИО"
txt_hintage = "0"
txt_test1 = 'Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер. Результат запишите в соответствующее поле.'
txt_test2 = 'Выполните 30 риседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания", чтобы запустить счетчик приседаний. '
txt_test3 = 'Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд. Нажмите кнопку "Начать финальный тест", чтобы запустить таймер. Зеленым обозначены секунды, в течение которых необходимо проводить измерения, черным - минуты  без замера пульсаций. Результаты запишите в соответствующие поля.
txt_sendresults = 'Отправить результаты'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Начать первый тест'
txt_starttest2 = 'Начать делать приседания'
txt_starttest3 = 'Начать финальный тест'

txt_age = 'Полных лет:'
txt_finalwin = 'Результаты'
txt_index = 'Индекс Руфье:'
txt_workheart = 'Работоспособность серца:'
txt_res1 = 'низкая. Срочно обратитесь к врачу!'
txt_res2 = 'удовретворительная. Обратитесь к врачу!'
txt_res3 = 'средняя. Возможно, стоит дополнительно обследоваться у врача.'
txt_res4 = 'выше среднего'
txt_res5 = 'высокая'
class TestWin(QWidget):
    def __init__(self):
        pass