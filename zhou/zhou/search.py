from django.http import HttpResponse
from django.shortcuts import render
import jieba
import wordcloud
import snownlp
from baiduspider import BaiduSpider
import jiagu
from cnsenti import Sentiment
import imageio
zhezhao=imageio.imread('1.png')

# from cemotion import Cemotion



# 表单
from wordcloud import get_single_color_func


def search_form(request):
    return render(request, 'search_form.html')



# 接收请求数据
def search(request):

    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        spider = BaiduSpider()


        import imageio
        zhezhao = imageio.imread('1.png')  # 用imageio替代目前已经移除image的scipy库






        from wordcloud import STOPWORDS

        # 搜索网页
        keyword = request.GET['q']
        bad = float(request.GET['min'])
        good = float(request.GET['max'])
        test_list0 = spider.search_web(query=keyword, pn=1)
        test_list1 = spider.search_web(query=keyword, pn=2)
        test_list2 = spider.search_web(query=keyword, pn=3)
        test_list3 = spider.search_web(query=keyword, pn=4)
        test_list4 = spider.search_web(query=keyword, pn=5)
        test_list5 = spider.search_web(query=keyword, pn=6)
        test_list6 = spider.search_web(query=keyword, pn=7)
        test_list7 = spider.search_web(query=keyword, pn=8)



        txt_j0 = jieba.lcut(test_list0.__str__())
        txt_j1 = jieba.lcut(test_list1.__str__())
        txt_j2 = jieba.lcut(test_list2.__str__())
        txt_j3 = jieba.lcut(test_list3.__str__())
        txt_j4 = jieba.lcut(test_list4.__str__())
        txt_j5 = jieba.lcut(test_list5.__str__())
        txt_j6 = jieba.lcut(test_list6.__str__())
        txt_j7 = jieba.lcut(test_list7.__str__())
        txt_j = txt_j0 + txt_j1 + txt_j2 + txt_j3 + txt_j4 + txt_j5 + txt_j6 + txt_j7



        # 搜索普通网页

        test_com_list0 = spider.search_web(query=keyword, pn=1, time='day')
        test_com_list1 = spider.search_web(query=keyword, pn=2, time='day')
        test_com_list2 = spider.search_web(query=keyword, pn=3, time='day')
        test_com_list3 = spider.search_web(query=keyword, pn=4, time='day')
        test_com_list4 = spider.search_web(query=keyword, pn=5, time='day')
        test_com_list5 = spider.search_web(query=keyword, pn=6, time='day')
        test_com_list6 = spider.search_web(query=keyword, pn=7, time='day')
        test_com_list7 = spider.search_web(query=keyword, pn=8, time='day')
        txt_com_j0 = jieba.lcut(test_com_list0.__str__())
        txt_com_j1 = jieba.lcut(test_com_list1.__str__())
        txt_com_j2 = jieba.lcut(test_com_list2.__str__())
        txt_com_j3 = jieba.lcut(test_com_list3.__str__())
        txt_com_j4 = jieba.lcut(test_com_list4.__str__())
        txt_com_j5 = jieba.lcut(test_com_list5.__str__())
        txt_com_j6 = jieba.lcut(test_com_list6.__str__())
        txt_com_j7 = jieba.lcut(test_com_list7.__str__())
        txt_com_j = txt_com_j0+txt_com_j1+txt_com_j2+txt_com_j3+txt_com_j4+txt_com_j5+txt_com_j6+txt_com_j7

        #搜索本周
        test_week_list0 = spider.search_web(query=keyword, pn=1, time='week')
        test_week_list1 = spider.search_web(query=keyword, pn=2, time='week')
        test_week_list2 = spider.search_web(query=keyword, pn=3, time='week')
        test_week_list3 = spider.search_web(query=keyword, pn=4, time='week')
        test_week_list4 = spider.search_web(query=keyword, pn=5, time='week')
        test_week_list5 = spider.search_web(query=keyword, pn=6, time='week')
        test_week_list6 = spider.search_web(query=keyword, pn=7, time='week')
        test_week_list7 = spider.search_web(query=keyword, pn=8, time='week')
        txt_week_j0 = jieba.lcut(test_week_list0.__str__())
        txt_week_j1 = jieba.lcut(test_week_list1.__str__())
        txt_week_j2 = jieba.lcut(test_week_list2.__str__())
        txt_week_j3 = jieba.lcut(test_week_list3.__str__())
        txt_week_j4 = jieba.lcut(test_week_list4.__str__())
        txt_week_j5 = jieba.lcut(test_week_list5.__str__())
        txt_week_j6 = jieba.lcut(test_week_list6.__str__())
        txt_week_j7 = jieba.lcut(test_week_list7.__str__())
        txt_week_j = txt_week_j0 + txt_week_j1 + txt_week_j2 + txt_week_j3 + txt_week_j4 + txt_week_j5 + txt_week_j6 + txt_week_j7


        #搜索本月
        test_month_list0 = spider.search_web(query=keyword, pn=1, time='month')
        test_month_list1 = spider.search_web(query=keyword, pn=2, time='month')
        test_month_list2 = spider.search_web(query=keyword, pn=3, time='month')
        test_month_list3 = spider.search_web(query=keyword, pn=4, time='month')
        test_month_list4 = spider.search_web(query=keyword, pn=5, time='month')
        test_month_list5 = spider.search_web(query=keyword, pn=6, time='month')
        test_month_list6 = spider.search_web(query=keyword, pn=7, time='month')
        test_month_list7 = spider.search_web(query=keyword, pn=8, time='month')
        txt_month_j0 = jieba.lcut(test_month_list0.__str__())
        txt_month_j1 = jieba.lcut(test_month_list1.__str__())
        txt_month_j2 = jieba.lcut(test_month_list2.__str__())
        txt_month_j3 = jieba.lcut(test_month_list3.__str__())
        txt_month_j4 = jieba.lcut(test_month_list4.__str__())
        txt_month_j5 = jieba.lcut(test_month_list5.__str__())
        txt_month_j6 = jieba.lcut(test_month_list6.__str__())
        txt_month_j7 = jieba.lcut(test_month_list7.__str__())
        txt_month_j = txt_month_j0 + txt_month_j1 + txt_month_j2 + txt_month_j3 + txt_month_j4 + txt_month_j5 + txt_month_j6 + txt_month_j7
        # txt=test_list0.__str__()

        #搜索网页情态分析建立词库

        positivelist = []
        negativelist = []
        for each in txt_j:
            each_word=snownlp.SnowNLP(each)
            feeling=each_word.sentiments
            if feeling>good:
                positivelist.append(each)
            elif feeling<bad:
                negativelist.append(each)
            else:
                pass
        positive = " ".join(positivelist)
        negative = " ".join(negativelist)
        test_str = " ".join(txt_j)

        #普通网页情态分析建立词库
        positivelist_com = []
        negativelist_com = []
        for each in txt_com_j:
            each_word=snownlp.SnowNLP(each)
            feeling=each_word.sentiments
            if feeling>good:
                positivelist_com.append(each)
            elif feeling<bad:
                negativelist_com.append(each)
            else:
                pass
        positive_com = " ".join(positivelist_com)
        negative_com = " ".join(negativelist_com)
        test_day_str = " ".join(txt_com_j)

        # 本周网页情态分析建立词库
        positivelist_week = []
        negativelist_week = []
        for each in txt_week_j:
            each_word = snownlp.SnowNLP(each)
            feeling = each_word.sentiments
            if feeling > good:
                positivelist_week.append(each)
            elif feeling < bad:
                negativelist_week.append(each)
            else:
                pass
        positive_week = " ".join(positivelist_week)
        negative_week = " ".join(negativelist_week)
        test_week_str = " ".join(txt_week_j)

        # 本月网页情态分析建立词库
        positivelist_month = []
        negativelist_month = []
        for each in txt_week_j:
            each_word = snownlp.SnowNLP(each)
            feeling = each_word.sentiments
            if feeling > good:
                positivelist_month.append(each)
            elif feeling < bad:
                negativelist_month.append(each)
            else:
                pass
        positive_month = " ".join(positivelist_month)
        negative_month = " ".join(negativelist_month)
        test_month_str = " ".join(txt_month_j)


        #生成词库词云
        w = wordcloud.WordCloud(width=1000,height=1000,font_path='msyh.ttc',stopwords=['time','a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])
        w1=wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "blue",stopwords=['time','a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])
        w2=wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "red",stopwords=['time','a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','related','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])

        w.generate(test_str)


        w1.generate(positive)
        w2.generate(negative)


        w.to_file('statics/images/test.png')
        w1.to_file('statics/images/positive.png')
        w2.to_file('statics/images/negative.png')


        #生成普通网站词云
        w3=wordcloud.WordCloud(width=1000,height=1000,font_path='msyh.ttc',stopwords=['time','a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])
        w4=wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "blue",stopwords=['time','a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])
        w5=wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "red",stopwords=['time','a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','related','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])

        w3.generate(test_day_str)
        w4.generate(positive_com)
        w5.generate(negative_com)
        w4.to_file('statics/images/positive_com.png')
        w5.to_file('statics/images/negative_com.png')
        w3.to_file('statics/images/test_com.png')



        #生成本周网站词云
        w6=wordcloud.WordCloud(width=1000,height=1000,font_path='msyh.ttc',stopwords=['time','a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])
        w7=wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "blue",stopwords=['time','a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])
        w8=wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "red",stopwords=['time','a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','related','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])

        w6.generate(test_week_str)
        w7.generate(positive_week)
        w8.generate(negative_week)
        w7.to_file('statics/images/positive_week.png')
        w8.to_file('statics/images/negative_week.png')
        w6.to_file('statics/images/test_week.png')

        #生成本月网站词云
        w9=wordcloud.WordCloud(width=1000,height=1000,font_path='msyh.ttc',stopwords=['time','a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])
        w10=wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "blue",stopwords=['time','a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])
        w11=wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "red",stopwords=['time','a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z','related','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])

        w9.generate(test_month_str)
        w10.generate(positive_month)
        w11.generate(negative_month)
        w10.to_file('statics/images/positive_month.png')
        w11.to_file('statics/images/negative_month.png')
        w9.to_file('statics/images/test_month.png')

        # jiagu搜索网页情态分析建立词库

        positivelist_jiagu = []
        negativelist_jiagu = []
        for each in txt_j:
            sentiment = jiagu.sentiment(each)
            if sentiment[0] == 'positive' and sentiment[1] > good:
                positivelist_jiagu.append(each)
            elif sentiment[0] == 'negative' and sentiment[1] > (1-bad):
                negativelist_jiagu.append(each)
            else:
                pass
        positive_jiagu = " ".join(positivelist_jiagu)
        negative_jiagu = " ".join(negativelist_jiagu)

        # 普通网页情态分析建立词库
        positivelist_jiagu_day = []
        negativelist_jiagu_day = []
        for each in txt_com_j:
            sentiment = jiagu.sentiment(each)
            if sentiment[0] == 'positive' and sentiment[1] > good:
                positivelist_jiagu_day.append(each)
            elif sentiment[0] == 'negative' and sentiment[1] > (1-bad):
                negativelist_jiagu_day.append(each)
            else:
                pass
        positive_jiagu_day = " ".join(positivelist_jiagu_day)
        negative_jiagu_day = " ".join(negativelist_jiagu_day)

        # 本周网页情态分析建立词库
        positivelist_jiagu_week = []
        negativelist_jiagu_week = []
        for each in txt_week_j:
            sentiment = jiagu.sentiment(each)
            if sentiment[0] == 'positive' and sentiment[1] > good:
                positivelist_jiagu_week.append(each)
            elif sentiment[0] == 'negative' and sentiment[1] > (1-bad):
                negativelist_jiagu_week.append(each)
            else:
                pass
        positive_jiagu_week = " ".join(positivelist_jiagu_week)
        negative_jiagu_week = " ".join(negativelist_jiagu_week)

        # 本月网页情态分析建立词库
        positivelist_jiagu_month = []
        negativelist_jiagu_month = []
        for each in txt_week_j:
            sentiment = jiagu.sentiment(each)
            if sentiment[0] == 'positive' and sentiment[1] > good:
                positivelist_jiagu_month.append(each)
            elif sentiment[0] == 'negative' and sentiment[1] > (1-bad):
                negativelist_jiagu_month.append(each)
            else:
                pass
        positive_jiagu_month = " ".join(positivelist_jiagu_month)
        negative_jiagu_month = " ".join(negativelist_jiagu_month)

        # 生成词库词云

        w20 = wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                  width=1000, height=700, background_color='white', mode='RGBA',color_func=lambda *args, **kwargs: "red")
        w21 = wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "blue",
                                  stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                             'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'www',
                                             'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result', 'des',
                                             'result', 'Copyright', 'None', 'origin'])
        w22 = wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "red",
                                  stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                             'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'related',
                                             'www', 'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result',
                                             'des', 'result', 'Copyright', 'None', 'origin'])

        w20.generate(test_str)
        w21.generate(positive_jiagu)
        w22.generate(negative_jiagu)
        w21.to_file('statics/images/positive_jiagu.png')
        w22.to_file('statics/images/negative_jiagu.png')


        # 生成普通网站词云
        w23 = wordcloud.WordCloud(width=1000, height=1000, font_path='msyh.ttc',
                                  stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                             'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'www',
                                             'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result', 'des',
                                             'result', 'Copyright', 'None', 'origin'])
        w24 = wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "blue",
                                  stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                             'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'www',
                                             'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result', 'des',
                                             'result', 'Copyright', 'None', 'origin'])
        w25 = wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "red",
                                  stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                             'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'related',
                                             'www', 'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result',
                                             'des', 'result', 'Copyright', 'None', 'origin'])

        w23.generate(test_str)
        w24.generate(positive_jiagu_day)
        w25.generate(negative_jiagu_day)
        w24.to_file('statics/images/positive_jiagu_day.png')
        w25.to_file('statics/images/negative_jiagu_day.png')
        w23.to_file('statics/images/test_jiagu_day.png')

        # 生成本周网站词云
        w26 = wordcloud.WordCloud(width=1000, height=1000, font_path='msyh.ttc',
                                  stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                             'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'www',
                                             'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result', 'des',
                                             'result', 'Copyright', 'None', 'origin'])
        w27 = wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "blue",
                                  stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                             'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'www',
                                             'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result', 'des',
                                             'result', 'Copyright', 'None', 'origin'])
        w28 = wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "red",
                                  stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                             'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'related',
                                             'www', 'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result',
                                             'des', 'result', 'Copyright', 'None', 'origin'])

        w26.generate(test_week_str)
        w27.generate(positive_jiagu_week)
        w28.generate(negative_jiagu_week)
        w27.to_file('statics/images/positive_jiagu_week.png')
        w28.to_file('statics/images/negative_jiagu_week.png')
        w26.to_file('statics/images/test_jiagu_week.png')

        # 生成本月网站词云
        w29 = wordcloud.WordCloud(width=1000, height=1000, font_path='msyh.ttc',
                                  stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                             'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'www',
                                             'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result', 'des',
                                             'result', 'Copyright', 'None', 'origin'])
        w30 = wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "blue",
                                  stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                             'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'www',
                                             'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result', 'des',
                                             'result', 'Copyright', 'None', 'origin'])
        w31 = wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "red",
                                  stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                             'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                                             'related', 'www', 'baidu', 'com', 'http', 'url', 'type', 'title', 'link',
                                             'result', 'des', 'result', 'Copyright', 'None', 'origin'])

        w29.generate(test_str)
        w30.generate(positive_jiagu_month)
        w31.generate(negative_jiagu_month)
        w30.to_file('statics/images/positive_jiagu_month.png')
        w31.to_file('statics/images/negative_jiagu_month.png')
        w29.to_file('statics/images/test_jiagu_month.png')



        # senti搜索网页情态分析建立词库

        positivelist_senti = []
        negativelist_senti = []
        senti = Sentiment()
        for each in txt_j:
            sentiment = senti.sentiment_count(each)
            if sentiment['pos'] > sentiment['neg']:
                positivelist_senti.append(each)
            elif sentiment['pos'] < sentiment['neg']:
                negativelist_senti.append(each)
            else:
                pass
        positive_senti = " ".join(positivelist_senti)
        negative_senti = " ".join(negativelist_senti)


        # 普通网页情态分析建立词库
        positivelist_senti_day = []
        negativelist_senti_day = []
        for each in txt_com_j:
            sentiment = senti.sentiment_count(each)
            if sentiment['pos'] > sentiment['neg']:
                positivelist_senti_day.append(each)
            elif sentiment['pos'] < sentiment['neg']:
                negativelist_senti_day.append(each)
            else:
                pass
        positive_senti_day = " ".join(positivelist_senti_day)
        negative_senti_day = " ".join(negativelist_senti_day)


        # 本周网页情态分析建立词库
        positivelist_senti_week = []
        negativelist_senti_week = []
        for each in txt_week_j:
            sentiment = senti.sentiment_count(each)
            if sentiment['pos'] > sentiment['neg']:
                positivelist_senti_week.append(each)
            elif sentiment['pos'] < sentiment['neg']:
                negativelist_senti_week.append(each)
            else:
                pass
        positive_senti_week = " ".join(positivelist_senti_week)
        negative_senti_week = " ".join(negativelist_senti_week)


        # 本月网页情态分析建立词库
        positivelist_senti_month = []
        negativelist_senti_month = []
        for each in txt_week_j:
            sentiment = senti.sentiment_count(each)
            if sentiment['pos'] > sentiment['neg']:
                positivelist_senti_month.append(each)
            elif sentiment['pos'] < sentiment['neg']:
                negativelist_senti_month.append(each)
            else:
                pass
        positive_senti_month = " ".join(positivelist_senti_month)
        negative_senti_month = " ".join(negativelist_senti_month)


        # 生成词库词云

        w60 = wordcloud.WordCloud(width=1000, height=1000, font_path='msyh.ttc',
                                stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm',
                                           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'www', 'baidu',
                                           'com', 'http', 'url', 'type', 'title', 'link', 'result', 'des', 'result',
                                           'Copyright', 'None', 'origin'])
        w61 = wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "blue",
                                 stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                            'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])
        w62 = wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "red",
                                 stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                            'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'related','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])

        w60.generate(test_str)
        w61.generate(positive_senti)
        w62.generate(negative_senti)
        w61.to_file('statics/images/positive_senti.png')
        w62.to_file('statics/images/negative_senti.png')


        # 生成普通网站词云
        w63 = wordcloud.WordCloud(width=1000, height=1000, font_path='msyh.ttc',
                                 stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                            'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'www',
                                            'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result', 'des',
                                            'result', 'Copyright', 'None', 'origin'])
        w64 = wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "blue",
                                 stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                            'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])
        w65 = wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "red",
                                 stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                            'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'related','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])

        w63.generate(test_str)
        w64.generate(positive_senti_day)
        w65.generate(negative_senti_day)
        w64.to_file('statics/images/positive_senti_day.png')
        w65.to_file('statics/images/negative_senti_day.png')
        w63.to_file('statics/images/test_senti_day.png')

        # 生成本周网站词云
        w66 = wordcloud.WordCloud(width=1000, height=1000, font_path='msyh.ttc',
                                 stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                            'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'www',
                                            'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result', 'des',
                                            'result', 'Copyright', 'None', 'origin'])
        w67 = wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "blue",
                                 stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                            'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])
        w68 = wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "red",
                                 stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                            'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'related','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])

        w66.generate(test_week_str)
        w67.generate(positive_senti_week)
        w68.generate(negative_senti_week)
        w67.to_file('statics/images/positive_senti_week.png')
        w68.to_file('statics/images/negative_senti_week.png')
        w66.to_file('statics/images/test_senti_week.png')

        # 生成本月网站词云
        w69 = wordcloud.WordCloud(width=1000, height=1000, font_path='msyh.ttc',
                                 stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                            'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'www',
                                            'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result', 'des',
                                            'result', 'Copyright', 'None', 'origin'])
        w70 = wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "blue",
                                  stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                             'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])
        w71 = wordcloud.WordCloud(font_path='msyh.ttc', mask=zhezhao, \
                                width=1000, height=1000, background_color='black', mode='RGBA',
                                color_func=lambda *args, **kwargs: "red",
                                  stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
                                             'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                                             'related','www','baidu','com','http','url','type','title','link','result','des','result','Copyright','None','origin'])

        w69.generate(test_str)
        w70.generate(positive_senti_month)
        w71.generate(negative_senti_month)
        w70.to_file('statics/images/positive_senti_month.png')
        w71.to_file('statics/images/negative_senti_month.png')
        w69.to_file('statics/images/test_senti_month.png')



        # #cemotion效率太低
        #
        #
        # positivelist_cemotion = []
        # negativelist_cemotion = []
        # c = Cemotion()
        # for each in txt_j:
        #     if c.predict(each) > 0.9:
        #         positivelist_cemotion.append(each)
        #     elif c.predict(each) < 0.9:
        #         negativelist_cemotion.append(each)
        #     else:
        #         pass
        # positive_cemotion = " ".join(positivelist_cemotion)
        # negative_cemotion = " ".join(negativelist_cemotion)
        #
        # # 普通网页情态分析建立词库
        # positivelist_cemotion_day = []
        # negativelist_cemotion_day = []
        # for each in txt_com_j:
        #     if c.predict(each) > 0.9:
        #         positivelist_cemotion_day.append(each)
        #     elif c.predict(each) < 0.9:
        #         negativelist_cemotion_day.append(each)
        #     else:
        #         pass
        # positive_cemotion_day = " ".join(positivelist_cemotion_day)
        # negative_cemotion_day = " ".join(negativelist_cemotion_day)
        #
        # # 本周网页情态分析建立词库
        # positivelist_cemotion_week = []
        # negativelist_cemotion_week = []
        # for each in txt_week_j:
        #     if c.predict(each) > 0.9:
        #         positivelist_cemotion_week.append(each)
        #     elif c.predict(each) > 0.9:
        #         negativelist_cemotion_week.append(each)
        #     else:
        #         pass
        # positive_cemotion_week = " ".join(positivelist_cemotion_week)
        # negative_cemotion_week = " ".join(negativelist_cemotion_week)
        #
        #
        # # 本月网页情态分析建立词库
        # positivelist_cemotion_month = []
        # negativelist_cemotion_month = []
        # for each in txt_week_j:
        #     if c.predict(each) > 0.9:
        #         positivelist_cemotion_month.append(each)
        #     elif c.predict(each) > 0.9:
        #         negativelist_cemotion_month.append(each)
        #     else:
        #         pass
        # positive_cemotion_month = " ".join(positivelist_cemotion_month)
        # negative_cemotion_month = " ".join(negativelist_cemotion_month)
        #
        # # 生成词库词云
        #
        # w40 = wordcloud.WordCloud(width=1000, height=1000, font_path='msyh.ttc',
        #                           stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
        #                                      'm',
        #                                      'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'www', 'baidu',
        #                                      'com', 'http', 'url', 'type', 'title', 'link', 'result', 'des', 'result',
        #                                      'Copyright', 'None', 'origin'])
        # w41 = wordcloud.WordCloud(width=1000, height=1000, font_path='msyh.ttc',
        #                           stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
        #                                      'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'www',
        #                                      'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result', 'des',
        #                                      'result', 'Copyright', 'None', 'origin'])
        # w42 = wordcloud.WordCloud(width=1000, height=1000, font_path='msyh.ttc',
        #                           stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
        #                                      'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'related',
        #                                      'www', 'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result',
        #                                      'des', 'result', 'Copyright', 'None', 'origin'])
        #
        # w40.generate(test_str)
        # w41.generate(positive_cemotion)
        # w42.generate(negative_cemotion)
        # w41.to_file('statics/images/positive_cemotion.png')
        # w42.to_file('statics/images/negative_cemotion.png')
        # w40.to_file('statics/images/test.png')
        #
        # # 生成普通网站词云
        # w43 = wordcloud.WordCloud(width=1000, height=1000, font_path='msyh.ttc',
        #                           stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
        #                                      'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'www',
        #                                      'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result', 'des',
        #                                      'result', 'Copyright', 'None', 'origin'])
        # w44 = wordcloud.WordCloud(width=1000, height=1000, font_path='msyh.ttc',
        #                           stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
        #                                      'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'www',
        #                                      'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result', 'des',
        #                                      'result', 'Copyright', 'None', 'origin'])
        # w45 = wordcloud.WordCloud(width=1000, height=1000, font_path='msyh.ttc',
        #                           stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
        #                                      'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'related',
        #                                      'www', 'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result',
        #                                      'des', 'result', 'Copyright', 'None', 'origin'])
        #
        # w43.generate(test_str)
        # w44.generate(positive_cemotion_day)
        # w45.generate(negative_cemotion_day)
        # w44.to_file('statics/images/positive_cemotion_day.png')
        # w45.to_file('statics/images/negative_cemotion_day.png')
        # w43.to_file('statics/images/test_cemotion_day.png')
        #
        # # 生成本周网站词云
        # w46 = wordcloud.WordCloud(width=1000, height=1000, font_path='msyh.ttc',
        #                           stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
        #                                      'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'www',
        #                                      'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result', 'des',
        #                                      'result', 'Copyright', 'None', 'origin'])
        # w47 = wordcloud.WordCloud(width=1000, height=1000, font_path='msyh.ttc',
        #                           stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
        #                                      'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'www',
        #                                      'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result', 'des',
        #                                      'result', 'Copyright', 'None', 'origin'])
        # w48 = wordcloud.WordCloud(width=1000, height=1000, font_path='msyh.ttc',
        #                           stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
        #                                      'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'related',
        #                                      'www', 'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result',
        #                                      'des', 'result', 'Copyright', 'None', 'origin'])
        #
        # w46.generate(test_week_str)
        # w47.generate(positive_cemotion_week)
        # w48.generate(negative_cemotion_week)
        # w47.to_file('statics/images/positive_cemotion_week.png')
        # w48.to_file('statics/images/negative_cemotion_week.png')
        # w46.to_file('statics/images/test_cemotion_week.png')
        #
        # # 生成本月网站词云
        # w49 = wordcloud.WordCloud(width=1000, height=1000, font_path='msyh.ttc',
        #                           stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
        #                                      'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'www',
        #                                      'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result', 'des',
        #                                      'result', 'Copyright', 'None', 'origin'])
        # w50 = wordcloud.WordCloud(width=1000, height=1000, font_path='msyh.ttc',
        #                           stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
        #                                      'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'www',
        #                                      'baidu', 'com', 'http', 'url', 'type', 'title', 'link', 'result', 'des',
        #                                      'result', 'Copyright', 'None', 'origin'])
        # w51 = wordcloud.WordCloud(width=1000, height=1000, font_path='msyh.ttc',
        #                           stopwords=['time', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n',
        #                                      'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        #                                      'related', 'www', 'baidu', 'com', 'http', 'url', 'type', 'title', 'link',
        #                                      'result', 'des', 'result', 'Copyright', 'None', 'origin'])
        #
        # w49.generate(test_str)
        # w50.generate(positive_cemotion_month)
        # w51.generate(negative_cemotion_month)
        # w50.to_file('statics/images/positive_cemotion_month.png')
        # w51.to_file('statics/images/negative_cemotion_month.png')
        # w49.to_file('statics/images/test_cemotion_month.png')




        message = '你搜索的内容为: ' + request.GET['q'] + '<a href="Cloud">观看词云图</a>'+'，坏词：0~'+request.GET['min']+',好词：'+request.GET['max']+'~1.0'



    else:
        message = '你提交了空表单'
    return HttpResponse(message)

