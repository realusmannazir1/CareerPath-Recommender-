import os
import shutil
import pickle

try:
    import joblib
    _use_joblib = True
except Exception:
    _use_joblib = False

MODEL_DIR = os.path.join(os.path.dirname(__file__), 'model')
FILES = ['scaler.pkl', 'model.pkl']

if not os.path.isdir(MODEL_DIR):
    raise SystemExit(f"Model directory not found: {MODEL_DIR}")

for fname in FILES:
    src = os.path.join(MODEL_DIR, fname)
    if not os.path.isfile(src):
        print(f"Skipping missing file: {src}")
        continue

    bak = src + '.backup'
    print(f"Backing up {src} -> {bak}")
    shutil.copyfile(src, bak)

    print(f"Loading {src}...")
    with open(src, 'rb') as f:
        obj = pickle.load(f)

    print(f"Re-saving {src} using {'joblib' if _use_joblib else 'pickle'}...")
    if _use_joblib:
        joblib.dump(obj, src)
    else:
        with open(src, 'wb') as f:
            pickle.dump(obj, f)

    print(f"Done for {src}\n")

print('All done. Created backups and re-saved available model files.')
