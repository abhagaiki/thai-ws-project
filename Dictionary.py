import Article
import Encyclopedia
import News
import Novel

article_word = Article.dictionary
encyclopedia_word = Encyclopedia.dictionary
news_word = News.dictionary
novel_word = Novel.dictionary

content = [article_word,encyclopedia_word,news_word,novel_word]
dictionary={}

for i in range(len(content)):
    for word in content[i]:
        if word not in dictionary:
            dictionary[word] = word




    


    
        
        
        

