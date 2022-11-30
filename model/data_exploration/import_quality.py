import pandas as pd
import numpy as np
df = pd.read_csv('../../data/kyiv_flats_result.csv')
quality = [60,
           10,
           20,
           35,
           32,
           30,
           57,
           50,
           301,
           10,
           70,
           665,
           55,
           75,
           63,
           44,
           40,
           46,
           25,
           40,
           44,
           35,
           65,
           25,
           20,
           20,
           20,
           50,
           43,
           40,
           10,
           80,
           80,
           907,
           75,
           25,
           66,
           40,
           15,
           71,
           20,
           37,
           405,
           5,
           76,
           69,
           65,
           80,
           15,
           20,
           20,
           40,
           83,
           42,
           56,
           66,
           70,
           46,
           39,
           43,
           50,
           67,
           85,
           32,
           90,
           82,
           77,
           88,
           74,
           80,
           40,
           15,
           25,
           15,
           26,
           26,
           26,
           58,
           77,
           75,
           26,
           80,
           85,
           83,
           26,
           20,
           20,
           50,
           27,
           58,
           20,
           20,
           40,
           30,
           45,
           45,
           20,
           50,
           35,
           20,
           66,
           65,
           70,
           25,
           85,
           30,
           78,
           68,
           25,
           35,
           60,
           76,
           40,
           35,
           45,
           25,
           64,
           50,
           76,
           50,
           40,
           50,
           48,
           50,
           64,
           42,
           59,
           78,
           30,
           85,
           83,
           44,
           30,
           75,
           40,
           55,
           60,
           50,
           47,
           30,
           40,
           43,
           30,
           44,
           58,
           60,
           50,
           66,
           40,
           20,
           20,
           20,
           20,
           25,
           26,
           22,
           23,
           77,
           21,
           35,
           25,
           35,
           25,
           22,
           ]

quality_np = np.zeros(len(df.index))

for idx, qual in enumerate(quality):
    quality_np[idx] = qual

df['quality'] = quality_np
df.to_csv('kyiv_flats_result.csv', index=False)