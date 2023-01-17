#SBER-AI_ruBert-base example 
pip install datasets transformers
from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification
from transformers import XLNetForTokenClassification, YosoForTokenClassification,
from transformers import BertTokenizer, AlbertForTokenClassification, GPT2ForTokenClassification, BertForTokenClassification


model=BertForTokenClassification.from_pretrained('sberbank-ai/ruBert-base')

tokenizer=BertTokenizer.from_pretrained('sberbank-ai/ruBert-base', do_lower_case=False)

pipe = pipeline('ner', model=model, tokenizer=tokenizer)

pipe('Отдел тестирования Департамента разработки Информационное сообщение a. дополнить пункт 2.4.1.3 приложением N 61 (прилагается). Ответственным за контролем над исполнением вышеизложенного поручения назначить специалиста по информационной безопасности Поварихина Владимира. Привести вышеизложенное поручение в исполнение к 05.01.2016.Признать утратившими силу следующие организационно-распорядительные документы: приказ Генерального директора от 09.07.2021 N 398.Выполнить данное поручение до 20 ноя 18. Ответственность за исполнение задачи возложить на технического писателя Баруздина Глеба.пункт 5.1.2 дополнить абзацем четвертым следующего содержания: При официальной переписке с межгосударственными (международными) органами, компетентными органами и должностными лицами иностранных государств, иностранными гражданами и организациями используется отдельный бланк с продольным расположением реквизитов на двух языках - русском и английском (приложение N 61). Определить срок исполнения задачи вплоть до 0.Контроль над выполнением вышеуказанного поручения возложить на Контент менеджера Олабухина Этьена. b. Внести изменения в ОРД согласно прилагаемому Перечню.ПЕРЕЧЕНЬ ИЗМЕНЕНИЙ, ВНОСИМЫХ В ОРД Контроль над выполнением вышеуказанного поручения возложить на администратора вычислительной сети Турова Савву.Определить срок исполнения задачи вплоть до 20 декабря 03.Внести в Регламент, утвержденный приказом Генерального директора от 11.05.2016 N 276, изменение, исключив из пункта 1.11 слова а также деятельность Руководителя удаленного офиса.Ответственность за исполнение задачи возложить на Контент менеджера Роговцова Беньямина.Установить срок выполнения задачи до 19.08.22.Ответственным за исполнение настоящего приказа назначить администратора вычислительной сети Кондрашевсия {{Шейх-Хайдар}}Ивашов Александр Елизарович 15 августа 2004 года')


#Sber NER-RUS
tokenizer = AutoTokenizer.from_pretrained("sberbank-ai/bert-base-NER-reptile-5-datasets")

model = AutoModelForTokenClassification.from_pretrained("sberbank-ai/bert-base-NER-reptile-5-datasets")

NER = pipeline('ner', model=model, tokenizer=tokenizer)

NER("Отдел тестирования Департамента разработки Информационное сообщение a. дополнить пункт 2.4.1.3 приложением N 61 (прилагается). Ответственным за контролем над исполнением вышеизложенного поручения назначить специалиста по информационной безопасности Поварихина Владимира.")
