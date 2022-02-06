# -*- coding: utf-8 -*-
import random
import psycopg2 as ps
import  json
from cryptography.fernet import Fernet
import os



class DbRand :



    #не работает
    def json(self):
        """
            :param file:   File.json
            :param key: - key

            :Description: writing words and topics in encrypted form to json file

        """



        with open('slowa.json', 'rb') as f:
            codind_slowa = f.read()

        file = open('key.key', 'rb')
        key = file.read()
        file.close()


        fernet = Fernet(key)  # это мы передаем ключ в переменную
        decrypted_text = fernet.decrypt(
            codind_slowa)  # расшифровываем файл и заносим весь файл в переменную decrypted_text

        # создали новый файл с расшифрованными данными
        with open('tempFile.json', 'wb') as f:
            f.write(decrypted_text)

        # через рандом мы с расшифрованного файла выписали слово и тему
        self.random_json_thems = random.choice(['Animals', 'Clothes', 'body_parts', 'kind_of_sport'])
        with open('tempFile.json', 'r') as f:
            data = json.loads(f.read())
            for i in data['slowa_i_tematy']:
                if i['temat'] == self.random_json_thems:
                    # print(i['slowa'])
                    all_slowa_json_out = i['slowa']

                    # рандом слово + рандом тема
                    self.slowa_json_random = random.choice(all_slowa_json_out)
                    self.randonSlowoJson = "".join(map(''.join, self.slowa_json_random))
                    print('slowa: ' + str(self.randonSlowoJson))  # слово
                    print('temat: ' + str(self.random_json_thems))  # тема

        self.random_thems = self.random_json_thems
        self.slowojoin = self.randonSlowoJson

        # а тыт мы сразу удаляем файл который мы расшифровали
        os.remove('tempFile.json')


    def dbrand(self):
        """
            :param self.random_thems:  list
            :param self.randomslowa:  tuple
            :param self.slowa_json:   json

            :Description: through random, a random topic is selected from the list, then the type is changed to string and a query is sent to the table
                            after, from the list, a random word is randomly selected, which the user will guess.
                            an encrypted json file is also created.

        """

        try:
            self.conn = ps.connect("host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
            self.rand =self.conn.cursor()

            self.slowa_zwierzeta = self.conn.cursor()
            self.slowa_ubrania  = self.conn.cursor()
            self.slowa_czesci_ciala = self.conn.cursor()
            self.slowa_rodzaj_sportu  = self.conn.cursor()






            self.random_thems = random.choice(['Animals', 'Clothes', 'body_parts', 'kind_of_sport'])
            # print(self.random_thems)

            self.rand.execute("SELECT "+ self.random_thems +" FROM slowa_do_gry")
            self.outputslowaisdb = self.rand.fetchall()
            # print(self.random_thems + str(self.outputslowaisdb))


            self.randomslowa = random.choice(self.outputslowaisdb)

            # убрал все лишнее потому что объект был типа tuple  и в окне игры не считовалось количество букв

            self.slowojoin = "".join(map(''.join, self.randomslowa))

            print(self.slowojoin)
            """"""""""""""""""""""""""""""""""""""""""""

            # слова из таблицы

            # zwierzęta
            self.slowa_zwierzeta.execute("SELECT Animals FROM slowa_do_gry")
            self.slowa_zwierzeta_is_file_tuple = self.slowa_zwierzeta.fetchall()

            # ubrania
            self.slowa_ubrania.execute("SELECT Clothes FROM slowa_do_gry")
            self.slowa_ubrania_is_file_tuple = self.slowa_ubrania.fetchall()

            # części_ciała
            self.slowa_czesci_ciala.execute("SELECT body_parts from slowa_do_gry")
            self.slowa_czesci_ciala_is_file_tuple = self.slowa_czesci_ciala.fetchall()

            # rodzajSportu
            self.slowa_rodzaj_sportu.execute("SELECT kind_of_sport from slowa_do_gry")
            self.slowa_rodzaj_sportu_is_file_tuple = self.slowa_rodzaj_sportu.fetchall()





            self.slowa_json = {
                'slowa_i_tematy' : [
                    {
                        'temat': 'Animals',
                        'slowa': self.slowa_zwierzeta_is_file_tuple
                    },
                    {
                        'temat': 'Clothes',
                        'slowa':  self.slowa_ubrania_is_file_tuple
                    },
                    {
                        'temat': 'body_parts',
                        'slowa': self.slowa_rodzaj_sportu_is_file_tuple
                    },
                    {
                        'temat': 'kind_of_sport',
                        'slowa': self.slowa_czesci_ciala_is_file_tuple
                    }

                ]

            }

            # запись в json наших данных
            with open('slowa.json', 'w') as f:
                json.dump(self.slowa_json, f )




            # это генерирует ключ и открывает файл "key.key" и записывает туда ключ
            key = Fernet.generate_key()
            file = open('key.key', 'wb')
            file.write(key)
            file.close()

            # это просто открывает ваш «key.key» и определяет ключ, хранящийся там, как «key»
            file = open('key.key', 'rb')
            key = file.read()
            file.close()

            # это открывает ваш json и считывает его данные в новую переменную с именем 'data'
            with open('slowa.json', 'rb') as f:
                data = f.read()

            # это шифрует данные, считанные из вашего json, и сохраняет их в «encrypted» .
            fernet = Fernet(key) # это мы передаем ключ в переменную
            encrypted = fernet.encrypt(data)

            # это записывает ваши новые зашифрованные данные в новый файл JSON
            with open('slowa.json', 'wb') as f:
                f.write(encrypted)






        except Exception as ex :
            print("error connect: " + str(ex))









        finally:
            self.slowa_ubrania.close()
            self.slowa_zwierzeta.close()
            self.slowa_czesci_ciala.close()
            self.slowa_rodzaj_sportu.close()
            self.conn.close()
            self.rand.close()






db = DbRand()
# db.json()





