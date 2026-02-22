name: Auto Label PR

on:
  pull_request:
    types: [opened]

jobs:
  label:
    runs-on: ubuntu-latest
    steps:
      - name: Add label
        uses: actions-ecosystem/action-add-labels@v1
        with:
          labels: |
            needs-review
