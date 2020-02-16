# 访问项目Gutenberg（http://gutenberg.org/），并找一些你想分析的图书。
# 下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中
filename = 'alice.txt'
with open(filename,encoding='utf-8') as file_obj:
    article = file_obj.read()
    print(article.lower().count("not"))
  
    