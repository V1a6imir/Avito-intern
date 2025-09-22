from wordfreq import word_frequency

def segment(text, lang="ru", max_word_len=20):
    """DP-сегментатор с использованием wordfreq"""
    n = len(text)
    dp = [0.0] * (n + 1)
    back = [-1] * (n + 1)
    dp[0] = 1.0

    for i in range(1, n + 1):
        for j in range(max(0, i - max_word_len), i):
            word = text[j:i].lower()
            prob = word_frequency(word, lang)
            if prob > 0:
                score = dp[j] * (prob + 1e-9)
                if score > dp[i]:
                    dp[i] = score
                    back[i] = j

    words, i = [], n
    while i > 0:
        j = back[i]
        if j == -1:
            return [text]
        words.append(text[j:i])
        i = j
    return list(reversed(words))


def get_space_positions(text):
    """Возвращает индексы символов, после которых ставим пробелы"""
    words = segment(text)
    positions, pos = [], 0
    for w in words[:-1]:
        pos += len(w)
        positions.append(pos)
    return positions


def apply_spaces(text, positions):
    """Показывает текст с пробелами"""
    result, last = [], 0
    for pos in positions:
        result.append(text[last:pos])
        last = pos
    result.append(text[last:])
    return " ".join(result)
