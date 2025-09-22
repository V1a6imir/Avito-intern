from segmenter import get_space_positions, apply_spaces

tests = {
    "идунавокзал": "иду на вокзал",
    "айфон14про": "айфон 14 про",
    "куплюasusrog": "куплю asus rog",
    "сдаюновуюквартиру": "сдаю новую квартиру"
}

def test_segmenter(tests):
    for text, expected in tests.items():
        pred_positions = get_space_positions(text)
        predicted = apply_spaces(text, pred_positions)
        print("Текст      :", text)
        print("Ожидалось  :", expected)
        print("Предсказано:", predicted)
        print("✅" if predicted == expected else "❌")
        print("-" * 40)

if __name__ == "__main__":
    test_segmenter(tests)
