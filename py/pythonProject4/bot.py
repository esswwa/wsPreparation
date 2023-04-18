import pandas as pd
import joblib

#dt = pd.read_csv("C:\\Users\\Данил\\Desktop\\123.csv")
R_tree = joblib.load("C:\\Users\\Данил\\Desktop\\best_rf.pkl")


fillability = False
sub_type = -1
listing_type = -1
tom = -1
building_age = -1
total_floor_count = -1
floor_no = -1
room_count = -1
size = -1
address = -1
heating_type = -1
pred = -1


keywords_default = ["умолч", "случ"]
keywords_sub_type = ["квар", "многоэтажк", "общ", "особняк", "чердак", "частный", "сбор", "резеден", "вилл", "отель", "дач", "ферм"]
keywords_listing_type_sale = ["куп"]
keywords_listing_type_rent = ["ренд", "снять"]
keywords_tom = ["дней", "сут"]
keywords_building_age = ["лет", "год"]
keywords_total_floor_count = ["этажей"]
keywords_floor_no = ["этаж"]
keywords_room_count = ["комн"]
keywords_size = ["м^2", "метр"]
keywords_heating_type = ["кондиц", "солн", "гео", "мазут", "газ", "уголь", "обогр", "возд", "котел", "электр", "центр", "измер", "печь", "печь", "напол", "без"]

# квар, купить 20 дней 20 лет 20 этажей 20 этаж 20 комнат 20 метров уголь
def fill():
    return fillability


def list():
    fields = [sub_type, listing_type, tom, building_age, total_floor_count, floor_no,
              room_count, size, heating_type, pred]
    return fields

def list_to_str(fields):
    str1 = ' '.join(str(e) for e in fields)
    return str1


def analiz(tex):
        global sub_type
        global listing_type
        global tom
        global building_age
        global total_floor_count
        global floor_no
        global room_count
        global size
        global heating_type
        global fillability


        text = tex
        textList = text.split()


    #    for i in range(len(keywords_default)):
     #       if text.find(keywords_default[i]) != -1:
     #           sub_type = dt["sub_type"].value_counts().idxmax()
      #          listing_type = dt["listing_type"].value_counts().idxmax()
     #           tom = dt["tom"].value_counts().idxmax()
      #          building_age = dt["building_age"].value_counts().idxmax()
     #          total_floor_count = dt["total_floor_count"].value_counts().idxmax()
      #          floor_no = dt["floor_no"].value_counts().idxmax()
      #          room_count = dt["room_count"].value_counts().idxmax()
       #         size = dt["size"].value_counts().idxmax()
       #         heating_type = dt["heating_type"].value_counts().idxmax()

        for i in range(len(keywords_sub_type)):
            if text.find(keywords_sub_type[i]) != -1:
                sub_type = i

        for i in range(len(textList)):
            for j in range(len(keywords_tom)):
                if textList[i].find(keywords_tom[j]) != -1:
                    tom = textList[i - 1]

        for i in range(len(keywords_listing_type_sale)):
            if text.find(keywords_listing_type_sale[i]) != -1:
                listing_type = 1

        for i in range(len(keywords_listing_type_rent)):
            if text.find(keywords_listing_type_rent[i]) != -1:
                listing_type = 2

        for i in range(len(textList)):
            for j in range(len(keywords_building_age)):
                if textList[i].find(keywords_building_age[j]) != -1:
                    building_age_l = float(textList[i - 1])
                    if building_age_l == 0:
                        building_age = 0
                    elif building_age_l == 1:
                        building_age = 1
                    elif building_age_l == 2:
                        building_age = 4
                    elif building_age_l == 3:
                        building_age = 7
                    elif building_age_l == 4:
                        building_age = 10
                    elif building_age_l == 5:
                        building_age = 12
                    elif building_age_l >= 40:
                        building_age = 11
                    elif building_age_l >= 36:
                        building_age = 9
                    elif building_age_l >= 31:
                        building_age = 8
                    elif building_age_l >= 26:
                        building_age = 6
                    elif building_age_l >= 21:
                        building_age = 5
                    elif building_age_l >= 16:
                        building_age = 3
                    elif building_age_l >= 11:
                        building_age = 2
                    elif building_age_l >= 6:
                        building_age = 13

        for i in range(len(textList)):
            for j in range(len(keywords_total_floor_count)):
                if textList[i].find(keywords_total_floor_count[j]) != -1:
                    total_floor_count_l = float(textList[i - 1])
                    if total_floor_count_l == 1:
                        total_floor_count = 0
                    elif total_floor_count_l == 10:
                        total_floor_count = 1
                    elif total_floor_count_l == 2:
                        total_floor_count = 3
                    elif total_floor_count_l == 3:
                        total_floor_count = 5
                    elif total_floor_count_l == 4:
                        total_floor_count = 6
                    elif total_floor_count_l == 5:
                        total_floor_count = 7
                    elif total_floor_count_l == 6:
                        total_floor_count = 8
                    elif total_floor_count_l == 7:
                        total_floor_count = 9
                    elif total_floor_count_l == 8:
                        total_floor_count = 10
                    elif total_floor_count_l == 9:
                        total_floor_count = 11
                    elif total_floor_count_l >= 20:
                        total_floor_count = 4
                    elif total_floor_count_l >= 10:
                        total_floor_count = 2

        for i in range(len(textList)):
            for j in range(len(keywords_floor_no)):
                if textList[i].find(keywords_floor_no[j]) != -1:
                    floor_no_l = float(textList[i - 1])
                    if floor_no_l >= 20:
                        floor_no = 12
                    elif floor_no_l >= 10:
                        floor_no = floor_no_l - 9
                    elif floor_no_l >= 3:
                        floor_no = floor_no_l + 10
                    elif floor_no_l == 2:
                        floor_no = 11
                    elif floor_no_l == 1:
                        floor_no = 0

        for i in range(len(textList)):
            for j in range(len(keywords_room_count)):
                if textList[i].find(keywords_room_count[j]) != -1:
                    room_count = textList[i - 1]

        for i in range(len(textList)):
            for j in range(len(keywords_size)):
                if textList[i].find(keywords_size[j]) != -1:
                    size = textList[i - 1]

        for i in range(len(keywords_heating_type)):
            if text.find(keywords_heating_type[i]) != -1:
                heating_type = i

        if sub_type == -1:
            fillability = False
            return "Укажите пожалуйста тип помещения(квартира, дачный домик и т.д.)"

        else:
            fillability = True

        if listing_type == -1:
            fillability = False
            return "Укажите что вы хотите(снять или купить)"

        else:
            fillability = True

        if tom == -1:
            fillability = False
            return "Сколько дней висит объявление о продаже?"

        else:
            fillability = True

        if building_age == -1:
            fillability = False
            return "Сколько лет зданию?"

        else:
            fillability = True

        if total_floor_count == -1:
            fillability = False
            return "Сколько этажей в доме?"

        else:
            fillability = True

        if floor_no == -1:
            fillability = False
            return "На каком этаже находится квартира?"

        else:
            fillability = True

        if room_count == -1:
            fillability = False
            return "Сколько комнат в кватире"

        else:
            fillability = True

        if size == -1:
            fillability = False
            return "Укажите площадь квартиры(м^2)"

        else:
            fillability = True

        if heating_type == -1:
            fillability = False
            return "Укажите пожалуйста тип отопления(центральное, печь и т.д.)"

        else:
            fillability = True


        if fillability:
            data = {"sub_type": [sub_type], 'start_date': [18], 'end_date':[19],'listing_type': [listing_type], 'tom': [tom],
                    'building_age': [building_age], 'total_floor_count': [total_floor_count], 'floor_no': [floor_no],
                    'room_count': [room_count], 'size': [size],'address':[123], 'heating_type': [heating_type]}
            df_new = pd.DataFrame(data)
            pred = R_tree.predict(df_new)
            return "Прибизительная цена = " + str(pred)

if __name__ == "__main__":
    print("Список команд:\n/search - определение цены\n/help - справка\n/exit - выход")
    while True:
        command = input("Введите команду:\t")
        if command == "/search":
            print(analiz(input("введите что-нибудь")))
        elif command == "/help":
            print("Справка")
        elif command == "/exit":
            break
