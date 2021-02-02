# coding: utf-8
import random
import time
import python.main as main
import python.greedy as greedy


def solve(hunts, guilds, method='bellman'):
    start = time.time() * 1000
    if method == 'greedy':
        G, s, t, f = greedy.make_graph(hunts, guilds)
        ans = greedy.min_cost_flow_greedy(G, s, t, f)
    elif method == 'bellman':
        G, s, t, f = main.make_graph(hunts, guilds)
        ans = main.min_cost_flow_bellman_ford(G, s, t, f)
    else:
        G, s, t, f = main.make_graph(hunts, guilds)
        ans = main.min_cost_flow_dijkstra(G, s, t, f)
    duration = time.time() * 1000 - start
    return ans, duration


def write(sin, ans, problem_name, duration, N, M):
    print(f'problem: {problem_name}\tans: {ans}\tduration:{duration:.0f} ms (N={N}\tM={M})')
    with open(f'../input/{problem_name}.in', 'w') as f:
        f.write(sin)
    with open(f'../output/{problem_name}.out', 'w') as f:
        f.write(f'{ans}\n')


def make_random_hunts_guilds(N, M, seed):
    random.seed(seed)

    sin = ''
    hunts = []
    enemies = 0
    for i in range(M):
        xi = random.randint(-1000, 1000)
        yi = random.randint(-1000, 1000)
        ei = random.randint(1, 100)
        enemies += ei
        hunts.append([xi, yi, ei])
        sin += f'{xi} {yi} {ei}\n'

    capacity = int(enemies * (1 + random.random()))
    guilds = []
    for i in range(N):
        vi = random.randint(-1000, 1000)
        wi = random.randint(-1000, 1000)
        ci = random.randint(1, 100)
        guilds.append([vi, wi, ci])
        sin += f'{vi} {wi} {ci}\n'

    return hunts, guilds, sin


def make_random(seed, M, N, name='random'):
    random.seed(seed)
    sin = f'{M} {N}\n'

    hunts, guilds, sin_tmp = make_random_hunts_guilds(N, M, seed)
    sin += sin_tmp

    ans_g, duration_g = solve(hunts, guilds, method='greedy')
    ans_b, duration_b = solve(hunts, guilds, method='bellman')
    ans_d, duration_d = solve(hunts, guilds, method='dijkstra')
    print('greedy  \t', end='')
    write(sin, ans_g, name, duration_g, N, M)
    print('bellman \t', end='')
    write(sin, ans_b, name, duration_b, N, M)
    print('dijkstra\t', end='')
    write(sin, ans_d, name, duration_d, N, M)


if __name__ == '__main__':
    for seed in range(1, 11):
        M = random.randint(1, 10)
        N = random.randint(1, 10)
        make_random(seed, M, N, f'small{seed:02}')
    for seed in range(1, 11):
        M = random.randint(1, 100)
        N = random.randint(1, 100)
        make_random(seed, M, N, f'medium{seed:02}')
    for seed in range(1, 11):
        M = 100
        N = 100
        make_random(seed, M, N, f'large{seed:02}')
