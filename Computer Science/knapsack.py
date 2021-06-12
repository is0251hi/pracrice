from typing import NamedTuple


class Item(NamedTuple):
    name: str
    weight: int
    value: float

def knapsack(items, max_capacity):
    table = [[0 for _ in range(max_capacity+1)] for _ in range(len(items)+1)]
    for idx,item in enumerate(items):
        for capacity in range(1, max_capacity +1):
            previous_item_value = table[idx][capacity]
            if capacity >= item.weight:#品物がナップザックに入る
                value_freeting_weight_for_item = table[idx][capacity-item.weight]
                #以前のより価値が高いなら入れる
                table[idx+1][capacity] = max(value_freeting_weight_for_item + item.value, previous_item_value)
            else:
                table[idx+1][capacity] = previous_item_value
    for idx in range(len(items)+1):
        print(table[idx])
    solution = []
    capacity = max_capacity

    for idx in range(len(items),0,-1):
        if table[idx-1][capacity] != table[idx][capacity]:
            solution.append(items[idx-1])
            #品物が入ったなら重さを差し引く
            capacity -= items[idx-1].weight
    return solution


if __name__ == "__main__":
    items = [
        Item("a", 50, 500),
        Item("b", 2, 300),
        Item("c", 35, 400),
        Item("d", 3, 1000),
        Item("e", 15, 50),
        Item("f", 20, 800),
    ]
    print(knapsack(items,35))
