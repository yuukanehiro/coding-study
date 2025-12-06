
# 実行方法

```bash
cat in.txt | python main.py > result.txt
```

もしくは
```bash
python main.py < in.txt > result.txt
```

# diff expect.txt vs result.txt

```bash
diff expect.txt result.txt
```

## VScode

### macOS

- 「command & shift & p」を押す
- 「compare」と入力し、「File: Compare Active File With...」を選択
- out.txtとresult.txtを比較
