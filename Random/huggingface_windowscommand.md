# Install Embedding Service:  
**Command:** docker run -p 8080:80 --name embeddingservice --pull always ghcr.io/huggingface/text-embeddings-inference:cpu-1.7 --model-id BAAI/bge-large-en-v1.5  
**Model Name:** BAAI/bge-large-en-v1.5  
**Inference Service:** ghcr.io/huggingface/text-embeddings-inference:cpu-1.7  
**Support Model URL:** https://huggingface.co/docs/text-embeddings-inference/supported_models  

**Test Via HttpRequest**
![image](https://github.com/user-attachments/assets/527a6d14-e982-487b-b85e-4f68b1990e08)

**Python Code:** 
You can install it via pip as pip install --upgrade --quiet huggingface_hub, and then run:
```
from huggingface_hub import InferenceClient  
client = InferenceClient()  
embedding = client.feature_extraction("What is deep learning?", model="http://localhost:8080/embed")  
print(embedding)
```

# Install Vector Storage (Faiss)
```
pip install faiss-cpu
```
**Try Test Code**
```
import numpy as np
d = 64                           # dimension
nb = 100000                      # database size
nq = 10000                       # nb of queries
np.random.seed(1234)             # make reproducible
xb = np.random.random((nb, d)).astype('float32')
xb[:, 0] += np.arange(nb) / 1000.
xq = np.random.random((nq, d)).astype('float32')
xq[:, 0] += np.arange(nq) / 1000.

import faiss                   # make faiss available
index = faiss.IndexFlatL2(d)   # build the index
print(index.is_trained)
index.add(xb)                  # add vectors to the index
print(index.ntotal)
```
![image](https://github.com/user-attachments/assets/1e694feb-4f74-48d8-bb18-d098c072c08b)

**Inseart Content Into Vector Storage**

Set Content
```
news1 = """北京时间4月28日，NBA季后赛继续进行，湖人客场113-116不敌森林狼，总比分1-3落后。东契奇38分5三分，詹姆斯27分12篮板8助攻3抢断3盖帽，两人空砍65分。湖人上半场结束落后3分，第三节打出一波14-0反超，但末节遭遇森林狼逆转。爱德华兹轰下43分，在比赛中被詹姆斯倒地时压到左脚，险些受伤。 
 数据统计 湖人：东契奇38分5三分，詹姆斯27分12篮板8助攻3抢断3盖帽，八村垒23分5篮板5三分，里夫斯17分7篮板5三分，芬尼-史密斯6分8篮板6助攻，海耶斯2分3篮板.森林狼：爱德华兹43分9篮板6助攻，兰德尔25分7篮板，麦克丹尼尔斯16分11篮板，戈贝尔5分10篮板，里德12分4篮板，迪文琴佐8分，亚历山大-沃克5分"""

news2 = """
      首节之争步行者整体状态火热，首发方面除了3投0中的西亚卡姆外，其余四位首发合计13投11中可谓弹无虚发；雄鹿方面开局被动不说，刚刚复出不久的利拉德无对抗的情况下捂着跟腱位置伤退；次节雄鹿方面字母哥也受到限制，这一节只在最后时刻依靠罚球拿到2分，步行者攻防两端表现出彩带着11分领先进入下半场。
      休息归来步行者虽然没有继续扩大优势但一直控制局势，而雄鹿也在拉扯中被拖垮，第三节末和第四节初雄鹿4分钟里仅得5分，步行者送上一波17-5的攻势将分差拉大至20分以上奠定胜局。最终，步行者客场大胜雄鹿夺得赛点，总比分上3-1取得领先.
      双方数据
      步行者（3-1）：哈利伯顿17分8板15助、特纳23分5板3助4帽、内姆哈德20分3板2助、麦康纳15分3板6助、内史密斯14分5板、托平13分1板1助、沃克12分5板3助、西亚卡姆12分3板4助、谢泼德3分3板1助、布莱恩特3板1助、弗菲1板、布拉德利1板。
      雄鹿（1-3）：阿德托昆博28分15板6助、波特23分5板6助2断、波蒂斯14分3板1助、AJ-格林9分1板3助、希姆斯6分3板1助、大洛佩斯6分1板1助、特伦特6分1助2断、罗林斯5分1助、康诺顿3分2板1助、库兹马3分1助、利拉德2板2助、普林斯1板1助
      """

news3 = """ 
比赛上来，魔术利用主场之势率先进入状态取得领先，不过在首节后半段他们的命中率有所下滑，凯尔特人逐渐完成反超，次节双方的进攻表现都不算好，凯尔特人虽然保持微弱领先却无法拉开分差，半场结束时魔术落后5分；
易边再战，魔术继续紧咬比分，分差最小时仅剩1分，但他们始终无法完成反超，末节双方依旧打得难解难分，不过在91-91平后凯尔特人轰出一波10-1的攻势带走比赛，最终凯尔特人拿下魔术大比分3-1获得赛点。
双方数据
　　魔术（1-3）：班凯罗31分7板3助、小瓦格纳24分6板7助、约瑟夫12分3板6助、布莱克10分4板、卡特9分11板3助、波普8分2板4助2断2帽、艾萨克4分3板、加里-哈里斯1板、休斯坦1板
　　凯尔特人（3-1）：塔图姆37分14板3助3断、杰伦-布朗21分11板1助2断、波尔津吉斯19分5板1助、怀特18分7板7助、霍福德6分6板2助5帽、豪泽6分1板、普理查德1板2助、科内特1板1助
"""
```

Generate Embedding
```
embedding1 = client.feature_extraction(news1, model="http://localhost:8080/embed")
embedding2 = client.feature_extraction(news2, model="http://localhost:8080/embed")
embedding3 = client.feature_extraction(news3, model="http://localhost:8080/embed")

print(embedding1)
```

Create Index And Add Content
Notice: Use IDMap, we can get real Content from the embedding contents
```
indexDimension = len(embedding1[0])

newsIndex = faiss.IndexFlatL2(indexDimension)   # build the index
newsIndexIDMap = faiss.IndexIDMap(newsIndex)

newsIndexIDMap.add_with_ids(embedding1, [1])
newsIndexIDMap.add_with_ids(embedding2, [2])
newsIndexIDMap.add_with_ids(embedding3, [3])
```

Search Result

```
#Test Search Result
D,I = newsIndexIDMap.search(embedding2, 2)
print(D)
print(I)
```
![image](https://github.com/user-attachments/assets/739a9f47-dcca-4e36-adb2-a9581153fbf2)

Real Query
```
query = "NBA季后赛湖人与森林狼的比赛结果怎么样"
queryEmbedding = client.feature_extraction(query, model="http://localhost:8080/embed")
D,I = newsIndexIDMap.search(queryEmbedding, 2)
print(D)
print(I) # Index ID, Specified By User
```
![image](https://github.com/user-attachments/assets/d7899959-78a9-421c-8a42-decd54fb7e67)

**Build Prompt**

Build ID - News Map
```
newsDic = {
    1:news1,
    2:news2,
    3:news3
}

newsDic[I[0][0]]
```
![image](https://github.com/user-attachments/assets/ae1bb485-135b-4366-8821-b2cc85b48dfe)

Insert Into Prompt Template

No RAG Content
![image](https://github.com/user-attachments/assets/ba96d9cd-36de-44c6-be16-91e467bb2773)

Contain RAG Content
![image](https://github.com/user-attachments/assets/c9b9bfb1-8c93-4992-98aa-4e5d74f5c756)
