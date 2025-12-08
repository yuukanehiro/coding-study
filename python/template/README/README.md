
# 実行方法

```bash
cat in.txt | python3 main.py > out.txt
```

もしくは
```bash
python3 main.py < in.txt > out.txt
```

# diff expect.txt vs out.txt

```bash
diff expect.txt out.txt
```

## VScode

### macOS

- 「command & shift & p」を押す
- 「compare」と入力し、「File: Compare Active File With...」を選択
- out.txtとexpect.txtを比較
