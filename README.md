# sd_ti_merge

Stable Diffusion の Textual Inversion 埋め込みをマージできます。

## マージスクリプト

マージする全ての埋め込みのトークンサイズと次元数が一致している必要があります。(後述する情報表示スクリプトでも確認できます)

```bash
python ./merge.py emb1.pt emb2.pt ... emb.pt -o output.pt --ratios 1 1 ... 1
```

のようにマージするモデル、出力先、混ぜる割合を指定できます。 

- `--ratios` は指定しなかった場合、すべて等しい割合でマージされます。指定する場合は特に合計値を意識する必要はなく、単純に割合だけ考えて大丈夫です。

`ti_A` と `ti_B` を 2:3 でマージする場合はこんな感じです。

```bash
python ./merge.py path/to/ti_A.pt path/to/ti_B.pt -o path/to/output.pt --ratios 0.4 0.6
```

## 情報表示スクリプト

TI に入っている情報を見ることが出来ます。

```bash
python ./info.py path/to/ti.pt
```

のようにすると、

```
Model: {'emb_params': tensor([[-0.0165,  0.0029,  0.0104,  ...,  0.0131, -0.0015, -0.0038],
        [-0.0164,  0.0102,  0.0066,  ...,  0.0060,  0.0098,  0.0109],
        [-0.0164,  0.0101,  0.0076,  ...,  0.0061,  0.0055,  0.0089],
        ...,
        [-0.0138, -0.0084, -0.0020,  ...,  0.0048,  0.0108,  0.0097],
        [-0.0136, -0.0096,  0.0006,  ...,  0.0080,  0.0124,  0.0089],
        [-0.0094, -0.0046,  0.0009,  ...,  0.0137,  0.0160,  0.0206]])}
Token size: 16 tokens
Dimension: 1024 (SDv2.x)
```

のように出てきます。`Token size` で示されているのがそのモデルのトークンサイズ、`Dimension` で示されているのが次元数であり、これが一致しないモデル同士はマージできません。`Dimension` は SDv1 系なら768、SDv2 系なら 1024 であり、v1 系と v2 系の TI をマージすることはできません。

