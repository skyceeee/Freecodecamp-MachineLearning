import random

# Global değişkenler
opponent_history = []
moves_counter = {}


def player(prev_play, opponent_history=opponent_history):
    if prev_play:
        opponent_history.append(prev_play)

    pattern_len = 3

    # Şablon tabanlı tahmin
    if len(opponent_history) >= pattern_len:
        pattern = "".join(opponent_history[-pattern_len:])
        if pattern not in moves_counter:
            moves_counter[pattern] = {"R": 0, "P": 0, "S": 0}
        if len(opponent_history) > pattern_len:
            next_move = opponent_history[-1]
            moves_counter[pattern][next_move] += 1

        # En sık görülen devam hamlesini tahmin et
        prediction_stats = moves_counter.get(pattern, {"R": 0, "P": 0, "S": 0})
        predicted_move = max(prediction_stats, key=prediction_stats.get)
    else:
        predicted_move = random.choice(["R", "P", "S"])

    # Kazandıracak hamleyi seç
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    return counter_moves[predicted_move]
