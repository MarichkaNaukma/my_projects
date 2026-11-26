import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path

PHOTOS_DIR = Path(__file__).parent / "photos"

RESULTS = {
    0: ("Звичайна Лєна", "lena_normal.png", "Ти basic, bro. Нема шо про тебе сказати, нпсішка"),
    1: ("Весела Лєна", "lena_happy.png", "Шоб не плакать я сміялась, да?"),
    2: ("Сонна Лєна", "lena_sleepy.png", "Тобі явно варто чучуть вздрємнуть"),
    3: ("Зла Лєна", "lena_angry.png", "Шо ти агришся??? Я щас сама заагрусь >:("),
    4: ("Лєна-філософ", "lena_filos.png", "Бути, чи не бути...🤔"),
    5: ("Сігма-Лєна", "lena_sigma.png", "+1000 aura moment"),
    6: ("Лєна crash out", "lena_crashout.png", "Та нашо тобі те навчання, нерви тіки портиш"),
    7: ("Ділова Лєна", "lena_busy.png", "Ой-ой, глянь яка важна птиця"),
    8: ("Кокєтка Лєна", "lena_flirty.png", "Знаєш, може в тебе і є шанс зі мною, красуне))"),
    9: ("Тру Лєна", "lena_true.png", "Н-ні, це... ТИ СПРАВЖНЯ ЛЄНА 😱😱😰😰"),
}

QUESTIONS = [{"text": "1. Як ся маєш?", "options": [("Та нічо, нормально", 0), ("Все прекрасно", 1), ("Я хочу спать", 2), ("Всі довкола тупі, бісить", 3), 
                                                ("Не все в цьому світі так однозначно", 4), ("*дуже круте мовчання*", 5), ("Я вже не вивожу, вбийте мене😭😭", 6), 
                                                ("В мене занадто багато справ щоб балакати з тобаю", 7), ("Було чудово, а як тебе побачила стало ще краще))", 8), 
                                                ("норма льно", 9),],},
    {"text": "2. Шо ти робиш першим ділом зранку?", "options": [("Та нічого особливого, вмиваюсь, снідаю", 0), 
                                                ("Смачно їм і пританцьовуючи йду на пари :D", 1), 
                                                ("Сплю далі", 2), ("Кидаю в стєнку той будильник", 3), ("Роздумаю над сенсом свого буття", 4), 
                                                ("Прокинувшись, роблю воркаут на 3 години", 5), 
                                                ("Згадую що в мене куча дедлайнів і хочу випригнути з вікна", 6),
                                                ("Я з важним ліцом іду робити свої важні справи", 7),
                                                ("Їду в тіндер переписуваться з хлопаком/дівчиною", 8), ("Ну просипаюсь, водичку п'ю, ну лекції там, пари", 9),],},
    {"text": "3. Тобі скасували всі пари на день. Шо будеш робити?", "options": [("Буду щасливо займатись своїми справами", 0), 
                                                ("СКАСУВАЛИ ПАРИ??? ЄЄЄ БОЙЙЙ!!! БУДЕ ГУЛЯНКА!!!!", 1), 
                                                ("Буду спать", 2), ("Буду в тредсах сратись з усіма, бо я можу", 3), 
                                                ("А чи справді ми вільні лише коли немає пар? Чи навчання наше - наше прокляття?", 4), 
                                                ("Якщо я захочу сама ці пари і скасую", 5), 
                                                ("Б'юсь головою об стінку бо сьогодні дедлайн", 6), ("Нема пар? Пфф, я завжди зайнята", 7),
                                                ("Піду на побачення)))", 8), ("Домашку робить, мабуть", 9),],},
    {"text": "4. Що ти зазвичай носиш дома?", "options": [("Щось зручне, худі і штани", 0), ("Шось яскраве", 1), 
                                                ("Піжаму", 2), ("Шось без цих довбаних бірок", 3), ("А чи одяг несе в собі якийсь сенс?", 4), 
                                                ("Сонцезахисні окуляри, щоб ніхто не бачив моє обличчя", 5), 
                                                ("Шо перше попалось під руку. Я просто хочу вижити цей день", 6), ("Строгий костюм dah", 7),
                                                ("Обтягуюче плаття, хочу завжди бути готовою))", 8), ("Футболка, штани спортівні, носки і тапки", 9),],},
    {"text": "5. Тебе ігнорять в повідомленнях, як вчинеш?", "options": [("Почекаю, може людина зайнята", 0), 
                                                ("Буду розповідати про все на світі, я навіть не помічу, що мене ігнорять", 1), 
                                                ("Я не сиджу в месенджерах, я сплю", 2), ("Буду агресивно надзванювати, бо як ця тварюка сміє???", 3), 
                                                ("Коли ж ігнорування стало нас турбувати? Я пороздумую над цим", 4), 
                                                ("Мені всеодно", 5), ("Мені нема часу, в мене все горить", 6), ("Я занадьо зайнята своїми справами", 7),
                                                ("Почну фліртувати))", 8), ("Та пофіг якось, нічо страшного", 9),],},
    {"text": "6. Ти випадково наступила жіночці на ногу. Твоя реакція?", "options": [("Вибачусь і забуду", 0), 
                                                ("Вибачусь і запрпоную сходити по каву, бо це весело", 1), 
                                                ("Я сонно щось буркну", 2), ("Якого фіга її нога взагалі тут опинилась???", 3), 
                                                ("Чи короткочасна була її біль? Чи запам'ятає вона мене на все життя?", 4), 
                                                ("Я просто холодно глянула і жінка швидкими кроками пішла від мене", 5), 
                                                ("Я панічно вибачаюсь по тисячу разів", 6), ("Я швидко вибачаюсь і біжу по справам", 7),
                                                ("Роблю їй комплімент і пропоную разом повечеряти", 8), ("Сказать -Ой, перепрошую-", 9),],},
    {"text": "7. Ну шо, як тест?", "options": [("Непоганий", 0), ("Тест - супер!!!", 1), 
                                                ("Сорі, я проспала. Був якийсь тест?", 2), ("Та закрийся і покажи результат", 3), 
                                                ("А чи справді тест визначає мене, чи я визначаю тест?", 4), 
                                                ("Норм *стоїть nonchalant*", 5), ("ААаа, давай швидче, мені вже задали куча нових завдань😭😢", 6), 
                                                ("Непогано, але я була зайнята іншим, тому повністю оцінити не можу", 7),
                                                ("Дівчино, а ви вільні сьогодні ввечері?)))", 8), ("Хз, мейбі", 9),],},]

class PersonalityTest:
    def __init__(self, root):
        self.root = root
        self.root.title(f"Тест: Яка ти Лєна?")
        self.current_question = 0 
        self.scores = [0] * 10

        # Головний заголовок
        self.title_label = tk.Label(
            root, 
            text="ЯКА ТИ ЛЄНА????", 
            font=("Arial", 20, "bold"),
            wraplength=450
        )
        self.title_label.pack(pady=(40, 10))

        # Опис тесту
        self.intro_label = tk.Label(
            root, 
            text="Чи задумувались ви колись, яка ви Лєна? Ні? Позорисько! Пройди цей тест і дізнайся!", 
            font=("Arial", 14),
            wraplength=400,
            justify="center"
        )
        self.intro_label.pack(pady=20)

        self.small_label = tk.Label(
            root, 
            text="(Розпочавши цей тест, ваша душа автоматично переходить в мою власність, не дякуйте ❤)", 
            font=("Arial", 5),
            wraplength=400,
            justify="left"
        )
        self.small_label.pack(pady=20)
        # Кнопка «Почати»
        self.start_btn = tk.Button(
            root, 
            text="Пігнали", 
            font=("Arial", 13, "bold"),
            padx=20,
            pady=10,
            command=self.start_test
        )
        self.start_btn.pack(pady=30)
        self.question_label = None
        self.selected_option = tk.IntVar(value=-1)
        self.btn_frame = None
        self.next_btn = None
        self.radio_buttons = []

    def start_test(self):
        self.title_label.destroy()
        self.intro_label.destroy()
        self.start_btn.destroy()
        self.small_label.destroy()

        self.question_label = tk.Label(self.root, text="", wraplength=450, font=("Arial", 14, "bold"))
        self.question_label.pack(pady=20)

        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.pack(pady=10, fill="x", padx=20)

        self.next_btn = tk.Button(self.root, text="Далі", font=("Arial", 12), command=self.next_question)
        self.next_btn.pack(pady=20)

        self.load_question()

    def load_question(self):
        for rb in self.radio_buttons:
            rb.destroy()
        self.radio_buttons.clear()
        
        q_data = QUESTIONS[self.current_question]
        self.question_label.config(text=f"{q_data['text']}")
        self.selected_option.set(-1)
        
        for idx, (opt_text, score_index) in enumerate(q_data["options"]):
            rb = tk.Radiobutton(
                self.btn_frame, 
                text=opt_text, 
                variable=self.selected_option, 
                value=score_index,
                font=("Arial", 11),
                anchor="w",
                justify="left"
            )
            rb.pack(fill="x", pady=5)
            self.radio_buttons.append(rb)

    def next_question(self):
        chosen = self.selected_option.get()
        if chosen == -1:
            return
        
        self.scores[chosen] += 1
        
        self.current_question += 1
        if self.current_question < len(QUESTIONS):
            self.load_question()
        else:
            self.show_result()
    def show_result(self):
        # Очищаємо екран
        self.question_label.destroy()
        self.btn_frame.destroy()
        self.next_btn.destroy()
        
        # Визначаємо індекс з найбільшою кількістю балів
        winner_idx = self.scores.index(max(self.scores))
        result_title, image_filename, desc = RESULTS[winner_idx]
        
        # Заголовок результату
        title_label = tk.Label(self.root, text=f"Твій результат:\n{result_title}!", font=("Arial", 16, "bold"))
        title_label.pack(pady=15)
        title_desc = tk.Label(self.root, text=f"{desc}", font=("Arial", 13, "bold"))
        title_desc.pack(pady=30)
        # Відображення картинки через Pillow
        try:
            pil_img = Image.open(PHOTOS_DIR / image_filename)
            pil_img = pil_img.resize((100, 100))
            self.img_tk = ImageTk.PhotoImage(pil_img)  # Зберігаємо посилання в self!
            
            img_label = tk.Label(self.root, image=self.img_tk)
            img_label.pack(pady=10)
        except Exception as e:
            err_label = tk.Label(self.root, text=f"[Картинка {image_filename} не знайдена]", fg="red")
            err_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalityTest(root)
    root.mainloop()
