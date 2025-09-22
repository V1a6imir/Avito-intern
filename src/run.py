from pathlib import Path
import pandas as pd
from segmenter import get_space_positions

# === Универсальный путь к файлу ===
BASE_DIR = Path(__file__).resolve().parent.parent   # корень проекта
DATA_PATH = BASE_DIR / "data" / "dataset_1937770_3.txt"

# === Загружаем данные ===
df = pd.read_csv(
    DATA_PATH,
    sep=",",
    usecols=[0, 1],
    names=["id", "text_no_spaces"],
    header=0,
    engine="python"
)

# === Предсказания ===
results = []
for _, row in df.iterrows():
    text_id = row["id"]
    text = row["text_no_spaces"]
    positions = get_space_positions(text)
    results.append([text_id, str(positions)])

submission = pd.DataFrame(results, columns=["id", "predicted_positions"])

# === Сохраняем файл ===
OUT_PATH = BASE_DIR / "submission.csv"
submission.to_csv(OUT_PATH, index=False)

print(f"✅ submission.csv сохранён в {OUT_PATH}")
