# -*- coding: utf-8 -*-
DATA_FILE = 'data.in'

# more index more strength
CARDS_STRENGHT = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
CARDS_J_STRENGHT = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def read_file():
    f = open(DATA_FILE, "r")
    return f.readlines()

def get_hands():
    hands = {}
    for line in read_file():
        hands[line.split(" ")[0].strip()] = int(line.split(" ")[1].strip())
    return hands

def hand_type(bid):
    # 6 Five of a kind -> AAAAA
    # 5 Four of a kind -> AA8AA
    # 4 Full house -> 23332
    # 3 Three of a kind -> TTT98
    # 2 Two pair -> 23432
    # 1 One pair -> A23A4
    # 0 High card -> 23456
    map_counter = {}
    for b in bid:
        if b not in map_counter:
            map_counter[b] = 1
        else:
            map_counter[b] = map_counter[b] + 1
    if (len(map_counter)) == 1: # AAAAA
        return 6
    elif (len(map_counter)) == 2: # AA8AA | 23332
        for value in map_counter.values():
            if value == 4:
                return 5
        return 4
    elif (len(map_counter)) == 3: # TTT98 | 23432
        for value in map_counter.values():
            if value == 2:
                return 2
        return 3
    elif (len(map_counter)) == 4: # A23A4
        return 1
    elif (len(map_counter)) == 5: # 23456
        return 0
    return -1 # BOOOM!!!

def get_map_ranks_bids(hands_ranks):
    map_ranks_bids = {}
    for key, value in hands_ranks.items():
        if value in map_ranks_bids:
            map_ranks_bids[value].append(key)
        else:
            map_ranks_bids[value] = [key]
    return map_ranks_bids

def get_ordered_map_rank_bid(map):
    ordered_rank_bid = {}
    for k in sorted(map.keys(), reverse = True):
        ordered_rank_bid[k] = map[k]
    return ordered_rank_bid

def get_ordered_bids(bids, cards_strenght):
    # sum elements and compared
    strengths_bids = {}
    for bid in bids:
        strenght = ""
        for b in bid:
            ix = str(cards_strenght.index(b))
            if len(ix) < 2:
                ix = '0'+ix
            strenght += ix
        strengths_bids[bid] = strenght
    
    ordered = dict(sorted(strengths_bids.items(), key=lambda item: item[1], reverse = True))
    return ordered

def calculate_ranks(rank_bid, total_ranks, cards_strenght):
    bid_rank = {}
    for value in rank_bid.values():
        if len(value) == 1:
            bid_rank[value[0]] = total_ranks
            total_ranks -= 1
        else:
            for bid in get_ordered_bids(value, cards_strenght):
                bid_rank[bid] = total_ranks
                total_ranks -= 1
    return bid_rank

def hands_with_joker(hands):
    result = {}
    for key, value in hands.items():
        card_max_value = -1
        for el in key:
            if CARDS_J_STRENGHT.index(el) > card_max_value:
                card_max_value = CARDS_J_STRENGHT.index(el)
        new_key = key + "-" + key.replace("J", CARDS_J_STRENGHT[card_max_value])
        result[new_key]=value
    return result


def part_one():
    total_winnings = 0
    hands = get_hands()
    hands_ranks = {}
    for bid in hands.keys():
        hands_ranks[bid] = hand_type(bid)

    # order ranks, ONLY bid - unique rank
    map_rank_bid = get_map_ranks_bids(hands_ranks)
    # reorder map to rank - bids
    ordered_rank_bid = get_ordered_map_rank_bid(map_rank_bid)
    bid_2_rank = calculate_ranks(ordered_rank_bid, len(hands_ranks), CARDS_STRENGHT)

    for bid, rank in hands.items():
        total_winnings += rank * bid_2_rank[bid]
    print("PART ONE total winnings:", total_winnings)

def part_two():
    total_winnings = 0
    hands = hands_with_joker(get_hands())
    hands_ranks = {}
    for bid in hands.keys():
        bid_replace_joker = bid.split("-")[1]
        bid_no_joker =  bid.split("-")[0]
        hands_ranks[bid_no_joker] = hand_type(bid_replace_joker)
    print("PART TWO  total winnings:",  total_winnings)


if __name__ == "__main__":
    part_one()
    part_two()