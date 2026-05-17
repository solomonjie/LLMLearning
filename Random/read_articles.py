import pandas as pd
import json

df = pd.read_excel('data/文章整理.xlsx')

articles = []
for i in range(len(df)):
    articles.append({
        'index': i + 1,
        'title': df.iloc[i, 0],
        'content': df.iloc[i, 1],
        'source': df.iloc[i, 2]
    })

# Print all articles for analysis
print("=" * 80)
print("完整文章列表")
print("=" * 80)

for article in articles:
    print(f"\n{'=' * 80}")
    print(f"文章 {article['index']}")
    print(f"{'=' * 80}")
    print(f"标题: {article['title']}")
    print(f"来源: {article['source']}")
    print(f"\n内容:")
    print(article['content'][:1000] + "..." if len(article['content']) > 1000 else article['content'])