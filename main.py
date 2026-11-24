import os

TEXT = (
    "Every morning my sourdough starter rises at dawn and puffs up "
    "like a tough guy, then goes soft the minute things heat up "
    "\u2014 that's why I named him Clint Yeastwood."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
