new_dict_ = [
    {
        "id": "1",
        "date": "01.10.2023",
        "items": [
            {"name": "name1", "price": 10, "quantity": 1},
            {"name": "name2", "price": 10, "quantity": 2},
            {"name": "name3", "price": 10, "quantity": 3},
        ],
    },
    {
        "id": "2",
        "date": "05.10.2023",
        "items": [
            {"name": "name1", "price": 100, "quantity": 4},
            {"name": "name2", "price": 100, "quantity": 5},
            {"name": "name3", "price": 100, "quantity": 6},
        ],
    },
    {
        "id": "3",
        "date": "25.10.2023",
        "items": [
            {"name": "name1", "price": 1000, "quantity": 2},
            {"name": "name2", "price": 1000, "quantity": 3},
            {"name": "name3", "price": 1000, "quantity": 9},
        ],
    },
    {
        "id": "4",
        "date": "25.11.2023",
        "items": [
            {"name": "name1", "price": 5000, "quantity": 7},
            {"name": "name2", "price": 5000, "quantity": 8},
            {"name": "name3", "price": 5000, "quantity": 9},
        ],
    },
    {
        "id": "5",
        "date": "26.11.2023",
        "items": [
            {"name": "name1", "price": 10000, "quantity": 7},
            {"name": "name2", "price": 10000, "quantity": 8},
            {"name": "name3", "price": 10000, "quantity": 9},
        ],
    },
    {
        "id": "6",
        "date": "26.12.2023",
        "items": [
            {"name": "name1", "price": 5, "quantity": 7},
            {"name": "name2", "price": 1, "quantity": 8},
            {"name": "name3", "price": 1, "quantity": 9},
        ],
    },
]


# def interesting_func(any_list: list[dict]) -> list[dict]:
#     """возвращает словарь, содержащий информацию о средней стоимости заказа
#     и количестве заказов за каждый месяц"""
#     new_dictionary = {}
#     average_order_value = 0
#     order_count = 0
#     for one_dict in any_list:
#         date_format = one_dict['date'].split('.')
#         date = date_format[2] + '-' + date_format[1]
#         order_value = lambda one_dict: one_dict["price"] * one_dict["quantity"]
#
#     return order_value


def order_amount(any_list):
    new_list = []
    counter = 0
    for one_dict in any_list:
        order_sum = 0
        counter += 1
        date_format = one_dict['date'].split('.')
        date = date_format[2] + '-' + date_format[1]
        for small_dict in one_dict["items"]:
            order_sum += small_dict["price"] * small_dict["quantity"]
        new_list.append([date, order_sum])
    return new_list


print(order_amount(new_dict_))


# corr_dict = {
#     1: ["2023-10", 60],
#     2: ["2023-10", 1500],
#     3: ["2023-10", 14000],
#     4: ["2023-11", 120000],
#     5: ["2023-11", 240000],
#     6: ["2023-12", 52],
# }



corr_list = [['2023-10', 60], ['2023-10', 1500], ['2023-10', 14000],
             ['2023-11', 120000], ['2023-11', 240000], ['2023-12', 52]]


final_dict = {}
summ_counter = 0
# some_set = ('2023-10', '2023-11', '2023-12')

# some_list = [item for item in corr_list if item[0]]
# fucking_date = '2023-10'
# fucking_summ = 0
# for item in corr_list:
#     if item[0] == fucking_date:
#         fucking_summ += item[1]
#     fucking_date = item[0]
#     summ_counter = item[1]
#     counter_two = 1
#
#     if item[0] in some_set:
#         summ_counter += item[1]
#
#     final_dict[value[0]] = value[1]
#
# print(summ_counter)