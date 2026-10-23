name: Update contribution heatmap

"on":
  schedule:
    - cron: "17 6 * * *"
  workflow_dispatch: {}
  push:
    branches: [main]
    paths: [scripts/heatmap.py, scripts/portrait.py]

permissions:
  contents: write

jobs:
  heatmap:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      # Cài đặt thư viện xử lý ảnh chuyên sâu để chạy file portrait.py của tác giả
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pillow

      - name: Run Heatmap Script
        run: python3 scripts/heatmap.py

      - name: Run Portrait Script
        run: python3 scripts/portrait.py

      - name: Push changes back to repository
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@://github.com"
          git add contrib-heatmap.svg ascii-portrait.svg
          git diff --cached --quiet || { git commit -m "chore: refresh profile assets [skip ci]" && git push; }
