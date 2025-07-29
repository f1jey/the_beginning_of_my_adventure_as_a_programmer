help = print("список команд : \n'привет', \n'можно я тебя обниму?', \n'назови случайную цифру', \n'сгенерируй пароль', \n'задай мне вопрос', \n'реши пример', \n'улыбнись'(команда с подвохом...), \n'stop' " )
command = input("Введите команду : ").lower()
counter = 0
import random
import string

while command.lower() != "stop":
     if command.lower() == '!help':
          print("список команд : \n'привет', \n'можно я тебя обниму?', \n'назови случайную цифру', \n'сгенерируй пароль', \n'задай мне вопрос', \n'реши пример', \n'улыбнись'(команда с подвохом...), \n'stop' " )
     
     elif command.lower() == "привет":
          print("привет, долгорослик !")
     
     elif command.lower() == "можно я тебя обниму?":
          counter += 1
          if counter >= 5:
               print("Ого, как ты любишь обниматься. Можно-можно)")
          else:
               print("конечно можно!! *крепко обнимает*")
     
     elif command.lower() == "назови случайную цифру":
          while True:
               print("какие рамки ?")
               ran_num1 = int(input("с какой цифры ?"))
               ran_num2 = int(input("по какую цифру ?"))
               result = print(random.randint(ran_num1, ran_num2)) 
               command = input('Напишите "еще" для нового пароля или "выход" для выхода: ').lower()
               if command.lower() != "еще":
                    break
     
     elif command.lower() == "сгенерируй пароль":
          print("сколько символов?")
          quantity = int(input("сколько символов должен составлять пароль ? "))
          print("символы?")
          symbols = input("какие символы должен составлять пароль: цифры или буквы ? ")
          while True:
               if symbols == "цифры":
                    password = ''.join(random.choices(string.digits, k=quantity))
                    print(password)
                    command = input('Напишите "еще" для нового пароля или "выход" для выхода: ').lower()
                    if command.lower() != "еще":
                         break
               elif symbols == "буквы":
                    password = ''.join(random.choices(string.ascii_letters, k=quantity))
                    print(password)
                    command = input('Напишите "еще" для нового пароля или "выход" для выхода: ').lower()
                    if command.lower() != "еще":
                         break
               elif symbols == "цифры и буквы" or "буквы и цифры":
                    password = ''.join(random.choices(string.ascii_letters + string.digits, k=quantity))
                    print(password)
                    command = input('Напишите "еще" для нового пароля или "выход" для выхода: ').lower()
                    if command.lower() != "еще":
                         break
               else:
                    print("неизвестный запрос.")
                    command = input('Напишите "еще" для нового пароля или "выход" для выхода: ').lower()
                    if command.lower() != "еще":
                         break
     
     elif command.lower() == "задай мне вопрос":
          while True:
               question = random.choice(["как дела?", "сколько раз ты сегодня какала?", "как тебя зовут?", "я считаюсь твоим другом?", "Ты интроверт или экстраверт?", "Есть ли у тебя хобби?", "Любишь ли ты животных?", "У тебя есть любимый фильм?", "Чай или кофе?", "Где бы ты хотел(а) побывать?", "Какой у тебя любимый цвет?", "Ты больше сова или жаворонок?", "Часто ли ты слушаешь музыку?", "Ты любишь дождь?", "Веришь ли ты в удачу?", "Какой у тебя любимый день недели?", "Что тебе помогает расслабиться?", "Ты больше любишь тишину или шум?"])
               print(question)
               answer = input(": ").lower()
               if any(char in answer for char in '13579'):
                    print("ЧТОО?!?! НЕЧЕТНОЕ ЧИСЛОО?! ТЫ ЧТО МЕНЯ НЕ ЛЮБИШЬ?!")
               else:
                    bot_answer = random.choice(["круто!", "я тоже!", "ого!", "прикольно!", "вау!", "ничего себе!", "понимаю!", "интересно!", "хехех", "жесть", "необычно"])  
                    print(bot_answer)
               command = input('Напишите "еще" для нового пароля или "выход" для выхода: ').lower()
               if command.lower() != "еще":
                    break
     
     elif command.lower() == "реши пример":
          while True:
               num_fst = int(input("Введите первое число : "))
               num_snd = int(input("Введите второе число : "))
               operator = input("Введите оператор (+, -, *, /): ")
               if operator == "+":
                    result = num_fst + num_snd
                    print(f"{num_fst} + {num_snd} = {result}")
               elif operator == "-":
                    result = num_fst - num_snd
                    print(f"{num_fst} - {num_snd} = {result}")
               elif operator == "*":
                    result = num_fst * num_snd
                    print(f"{num_fst} * {num_snd} = {result}")
               elif operator == "/":
                    if num_snd != 0:
                         result = num_fst / num_snd
                         print(f"{num_fst} : {num_snd} = {result}")
                    else:
                         result = "Ошибка: низя делить на ноль!"
               else:
                    result = "Ошибка: неверный оператор!"
               print(result)
               command = input('Напишите "еще" для нового пароля или "выход" для выхода: ').lower()
               if command.lower() != "еще":
                    break
     
     elif command.lower() == "улыбнись":
             counter += 1
             if counter >= 3:
                    print("*бабах* bruuh bro...")
                    break
             else:
               print(";з *робот нежно улыбается с убийственным взглядом смотря на вас*^^")
     
     else:
          print("Я не знаю такой команды :[")
     command = input("Введите команду : ").lower()
else:
     print("пока, долгорослик!")

        
            