from bisect import bisect_left, insort
from collections import Counter

def max_kills(n, m, swords, b_list, c_list):
    '''
    I'am in a dungeon and i have 
    n swords 
    facing m monsters

    damage of ith sword - ai 
    hp of ith monster - bi 

    after killing a monster with a sword of damage x 
    it disapper 

    and if ci > 0 
    we will get a new sword of damage max(x , ci)

    to find - maximum no of monsters we can kill 
    at most we can kill 1 monster with one sword 
    '''

    '''
    we need to figure out which sword we should use to kill which monster 

    we should probably try to kill a monster which gives atleast a reward so that we can get a new sword 
    '''

    # lets get the monsters which give atleast a reward 
    reward = [(b_list[i], c_list[i]) for i in range(m) if c_list[i] > 0]
    no_reward = [(b_list[i], c_list[i]) for i in range(m) if c_list[i] == 0]

    # lets sort sword in order of low to high dmg and monster in low to high health 
    swords.sort()
    reward.sort()
    no_reward.sort()

    # frequency map for sword damages
    freq = Counter(swords)
    unique_swords = sorted(freq.keys())

    def find_and_use(b):
        """
        Find smallest sword >= b.
        If found, decrement its count, remove from list if count hits 0.
        Return that sword's damage, else None.
        """
        idx = bisect_left(unique_swords, b)
        if idx == len(unique_swords):
            return None
        dmg = unique_swords[idx]
        freq[dmg] -= 1
        if freq[dmg] == 0:
            freq.pop(dmg)
            unique_swords.pop(idx)
        return dmg

    def add_sword(x):
        """
        Insert sword of damage x (if new, insert into sorted list)
        """
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
            insort(unique_swords, x)

    kill = 0

    # for reward giving monsters , we are guaranteed to get a new sword after killing them 
    for b, c in reward:
        used = find_and_use(b)
        if used is not None:
            new_sword = max(used, c)
            add_sword(new_sword)
            kill += 1

    # killing non-reward monsters , our sword will disappear after kill
    for b, _ in no_reward:
        used = find_and_use(b)
        if used is not None:
            kill += 1

    return kill


t = int(input().strip())
for _ in range(t):
    n, m = map(int, input().split())
    swords = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))
    print(max_kills(n, m, swords, b_list, c_list))
