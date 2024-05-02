**令和２年国勢調査**

２０１５ー２０２０年、各市区町村の人口推移をグラフ化する

```
raw_data = pd.read_excel('https://www.e-stat.go.jp/stat-search/file-download?statInfId=000032142402&fileKind=0',
                  skiprows=9,
                  header=[1,2,3,4,5])
raw_data.head()
```

```
Unnamed: 0_level_0	Unnamed: 1_level_0	Unnamed: 2_level_0	Unnamed: 3_level_0	Unnamed: 4_level_0	Unnamed: 5_level_0	Unnamed: 6_level_0	男女	世帯の種類
Unnamed: 0_level_1	Unnamed: 1_level_1	Unnamed: 2_level_1	Unnamed: 3_level_1	Unnamed: 4_level_1	Unnamed: 5_level_1	Unnamed: 6_level_1	1	1
Unnamed: 0_level_2	Unnamed: 1_level_2	Unnamed: 2_level_2	Unnamed: 3_level_2	Unnamed: 4_level_2	Unnamed: 5_level_2	Unnamed: 6_level_2	0_総数	1_男	2_女	0_総数	1_一般世帯	2_施設等の世帯	0_総数	1_一般世帯	2_施設等の世帯
Unnamed: 0_level_3	Unnamed: 1_level_3	Unnamed: 2_level_3	Unnamed: 3_level_3	Unnamed: 4_level_3	Unnamed: 5_level_3	Unnamed: 6_level_3	人	人	人	...	1km2当たり	世帯	世帯	世帯	％	人	人	人
地域識別コード	2000年_都道府県	2000年_地域コード	2000年地域	2020年_都道府県	2020年_地域コード	地域名		Unnamed: 8_level_4	Unnamed: 9_level_4	...	Unnamed: 15_level_4	Unnamed: 16_level_4	Unnamed: 17_level_4	Unnamed: 18_level_4	Unnamed: 19_level_4	Unnamed: 20_level_4	Unnamed: 21_level_4	Unnamed: 22_level_4	Unnamed: 23_level_4	Unnamed: 24_level_4
0	a	00_全国	0	2000.0	00_全国	0	0001_全国	126146099	61349581	64796518	...	338.2	55830154	55704949	125205	53448685	2381469	4.45562	126146099	123162995	2983104
1	a	01_北海道	1000	2000.0	01_北海道	1000	0002_北海道	5224614	2465088	2759526	...	66.6	2476846	2469063	7783	2444810	32036	1.31037	5224614	5032739	191875
2	1	01_北海道	1100	2000.0	01_北海道	1100	0003_札幌市	1973395	918682	1054713	...	1760.0	969161	967372	1789	921837	47324	5.13366	1973395	1916478	56917
3	0	01_北海道	1101	2000.0	01_北海道	1101	0004_札幌市中央区	248680	112853	135827	...	5357.2	141429	141223	206	132006	9423	7.13831	248680	240498	8182
4	0	01_北海道	1102	2000.0	01_北海道	1102	0005_札幌市北区	289323	136596	152727	...	4551.3	139675	139449	226	133662	6013	4.49866	289323	282668	6655
5 rows × 25 columns
```

raw_dataを整形する

```
cl = raw_data.columns # マルチカラムを取得する
# 使用するデータを抽出する
df = pd.DataFrame({'prefecture': raw_data[cl[4]],
                   'city': raw_data[cl[6]],
                   'population_2020': raw_data[cl[7]],
                   'male': raw_data[cl[8]],
                   'female': raw_data[cl[9]],
                   'diff_value': raw_data[cl[11]],
                   'diff_rate': raw_data[cl[12]],})
```

'-'ハイフンをゼロ埋めし、object型からint型に変換する

```
df = df.replace('-', 0)
tmp = df.columns.to_list()
[pd.to_numeric(df[i], errors='coerce') for i in tmp[2:6]]
df['population_2015'] = df['population_2020'] - df['diff_value']
```
