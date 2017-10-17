#!/usr/bin/env python

import itertools

COMBINATIONS = {
    1: {"18_inch": 6000, "36_inch": 0},
    2: {"18_inch": 4000, "36_inch": 600},
    3: {"18_inch": 2000, "36_inch": 1200},
    4: {"18_inch": 0,    "36_inch": 1800},
    5: {"18_inch": 9000, "36_inch": 0},
    6: {"18_inch": 7000, "36_inch": 600},
    7: {"18_inch": 5000, "36_inch": 1200},
    8: {"18_inch": 3000, "36_inch": 1800},
    9: {"18_inch": 1000, "36_inch": 2400}
}

SALES = {
    1: {"18_inch": 2200, "36_inch": 750},
    2: {"18_inch": 2350, "36_inch": 1050},
    3: {"18_inch": 3200, "36_inch": 1500},
    4: {"18_inch": 4550, "36_inch": 1800},
    5: {"18_inch": 4350, "36_inch": 1800},
    6: {"18_inch": 5600, "36_inch": 2100},
    7: {"18_inch": 4500, "36_inch": 1600},
    8: {"18_inch": 3850, "36_inch": 2000},
    9: {"18_inch": 4550, "36_inch": 2050},
    10: {"18_inch": 3650, "36_inch": 1850},
    11: {"18_inch": 2600, "36_inch": 1150},
    12: {"18_inch": 1900, "36_inch": 900}
}

INVENTORY_COST_FACTOR = {
    "18_inch": 2,
    "36_inch": 6,
}

FINAL_INVENTORY_COST_FACTOR = {
    "18_inch": 30,
    "36_inch": 100,
}

STOCK_OUT_COST_FACTOR = {
    "18_inch": 20,
    "36_inch": 60,
}

INVENTORY_REMAINING = {
    "18_inch": 2000,
    "36_inch": 700,
}


def calculate_cumulative_total_for_1_model(model, stock, choice, period):
    product = COMBINATIONS[choice][model]
    avaliable = stock + product
    inventory = avaliable - SALES[period][model]

    if inventory > 0:
        inventory_cost = inventory * INVENTORY_COST_FACTOR[model]
        stock_out_cost = 0
    elif inventory < 0:
        inventory_cost = 0
        stock_out_cost = abs(inventory) * STOCK_OUT_COST_FACTOR[model]
    else:
        inventory_cost = 0
        stock_out_cost = 0

    stock_end_period = inventory if inventory > 0 else 0

    period_cost = stock_out_cost + inventory_cost

    return stock_end_period, period_cost


def calculate_cumulative_total(stock_18, stock_36, choice, period):
    stock_end_period_18, period_cost_18 = calculate_cumulative_total_for_1_model("18_inch", stock_18, choice, period)
    stock_end_period_36, period_cost_36 = calculate_cumulative_total_for_1_model("36_inch", stock_36, choice, period)

    overtime_cost = 20000 if choice >= 5 else 0

    return stock_end_period_18, stock_end_period_36, period_cost_18 + period_cost_36 + overtime_cost


def calculate_one_combination(combination):
    stock_18 = INVENTORY_REMAINING["18_inch"]
    stock_36 = INVENTORY_REMAINING["36_inch"]

    total_cost = 0

    for period, choice in enumerate(combination, 1):
        stock_18, stock_36, cost = calculate_cumulative_total(stock_18, stock_36, choice, period)
        total_cost += cost
        #print stock_18, stock_36, cost, total_cost

    total_cost += stock_18 * (FINAL_INVENTORY_COST_FACTOR["18_inch"] - INVENTORY_COST_FACTOR["18_inch"])
    total_cost += stock_36 * (FINAL_INVENTORY_COST_FACTOR["36_inch"] - INVENTORY_COST_FACTOR["36_inch"])

    return total_cost


if __name__ == '__main__':
    # print calculate_cumulative_total_for_1_model("36_inch", INVENTORY_REMAINING_36, 3, 1)
    # calculate_one_combination((3, 2, 8, 8, 7, 8, 7, 8, 8, 8, 3, 3))
    # for x in itertools.product(*[range(1, 10)] * 10):
    #     pass

    best_combination = ()
    best_cost = 10000000000
    count = 0

    for a in range(2, 4):
        for b in range(5, 10):
            for c in range(5, 10):
                for d in range(5, 10):
                    for e in range(5, 10):
                        for f in range(5, 10):
                            for g in range(5, 10):
                                for h in range(5, 10):
                                    for i in range(5, 10):
                                        for j in range(5, 10):
                                            for k in range(1, 5):
                                                for l in range(2, 4):
                                                    combination = (a, b, c, d, e, f, g, h, i, j, k, l)
                                                    total_cost = calculate_one_combination(combination)
                                                    if total_cost < best_cost:
                                                        best_cost = total_cost
                                                        best_combination = combination

                                                    count += 1

    print best_cost, best_combination

    # for combination in ((3, 2, 8, 8, 7, 8, 7, 8, 8, 8, 3, 3), ) * (9 ** 7):
    #     calculate_one_combination(combination)
