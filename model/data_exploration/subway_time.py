import pandas as pd
import math

subway_station_coordinates = [
    (50.3672376, 30.462403),  # Теремки
    (50.3739452, 30.4704367),  # Іподром
    (50.3814974, 30.4763541),  # Виставковий центр
    (50.3880966, 30.477066),  # Васильківська
    (50.3981921, 30.5028608),  # Голосіївська
    (50.4020389, 30.5033775),  # Деміївська
    (50.4126042, 30.5195308),  # Либідська
    (50.4148609, 30.5108583),  # Палац "Україна"
    (50.4248873, 30.5064695),  # Олімпійська
    (50.4248873, 30.5064695),  # Олімпійська
    (50.4368702, 30.514533),  # Льва Толстого
    (50.4446017, 30.522704),  # Майдан Незалежності
    (50.454814, 30.5164009),  # Почтова площа
    (50.469904, 30.5011797),  # Контрактова площа
    (50.469904, 30.5011797),  # Тараса Шевченка
    (50.469904, 30.5011797),  # Почайна
    (50.5076296, 30.4986306),  # Оболонь
    (50.5076296, 30.4986306),  # Мінська
    (50.4983493, 30.4929282),  # Теремки

    (50.4617005, 30.3521767),  # Академ
    (50.4544603, 30.364922),  # Житомирська
    (50.456142, 30.3826843),  # Святошин
    (50.4608005, 30.3951338),  # Нивки
    (50.4602382, 30.4129673),  # Берестейська
    (50.4550875, 30.435779),  # Шулявка
    (50.4531956, 30.4617059),  # Політехнічний інститут
    (50.4467623, 30.4702119),  # Вокзальна
    (50.4456808, 30.5109709),  # Університет
    (50.4456808, 30.5109709),  # Театральна
    (50.4468485, 30.5202937),  # Хрещатик
    (50.4466173, 30.5313004),  # Арсенальна
    (50.4471912, 30.5490244),  # Дніпро
    (50.4494321, 30.5628432),  # Гідропарк
    (50.4494321, 30.5628432),  # Лівобережна
    (50.4613889, 30.5900534),  # Дарниця
    (50.4613889, 30.5900534),  # Дарниця
    (50.4613889, 30.5900534),  # Чернігівська
    (50.4613889, 30.5900534),  # Лісова

    (50.4802668, 30.4214818),  # Сирець
    (50.4815716, 30.4089861),  # Дорогожичі
    (50.4715284, 30.458048),  # Лук'янівська
    (50.4558071, 30.4676093),  # Золоті ворота
    (50.4388722, 30.5119871),  # Палац спорту
    (50.4388722, 30.5119871),  # Кловська
    (50.4315464, 30.5213427),  # Печерська
    (50.4061982, 30.5458902),  # Дружби народів
    (50.4028598, 30.560897),  # Видубичі
    (50.401875, 30.579179),  # Осокорки
    (50.4024598, 30.634848),  # Позняки
    (50.4024598, 30.634848),  # Харківська
    (50.4080827, 30.6491124),  # Вирлиця
    (50.4145243, 30.666098),  # Бориспільска
    (50.4145243, 30.666098),  # Червоний хутір
]

HUMAN_VELOCITY = 3


def latitude_to_km(latitude):
    return 110.574 * latitude


def longitude_to_km(longitude):
    return 111.320 * 0.96 * longitude


def get_nearest_subway_time(latitude, longitude):
    min_diff = None
    for subway_station in subway_station_coordinates:
        latitude_diff = abs(subway_station[0] - latitude)
        longitude_diff = abs(subway_station[1] - longitude)

        latitude_diff_km = latitude_to_km(latitude_diff)
        longitude_diff_km = longitude_to_km(longitude_diff)

        general_diff = math.sqrt(latitude_diff_km**2 + longitude_diff_km**2)

        if min_diff is None or general_diff < min_diff:
            min_diff = general_diff

    return min_diff / HUMAN_VELOCITY * 60


columns = ['total_area', 'district_uk', 'room_count', 'latitude', 'longitude', 'price', 'currency']
df: pd.DataFrame = pd.read_csv('../../data/kyiv_flats_result.csv')

result = df.apply(lambda x: get_nearest_subway_time(x['latitude'], x['longitude']), axis=1)
df['subway_time'] = result
df.to_csv('../../data/kyiv_flats_result.csv')
