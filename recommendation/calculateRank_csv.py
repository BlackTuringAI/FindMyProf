import csv
import re
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

file_path='E:/FindMyProf/prof_data.csv'#教授数据文件的路径
save_path='E:/FindMyProf/result.csv'#结果文件的路径

def universityScore(university):
    #计算院校的分数，且院校属性占比40%
    weight1=0.4
    if university:
        university=int(university)
    else:
        return 0
    score1=float(university)*weight1
    return score1

def calculateSimilar(phrase1,phrase2):
    #计算学生专业与教授研究领域的匹配程度（相似性）
    tokens1 = word_tokenize(phrase1)
    tokens2 = word_tokenize(phrase2)
    # 使用NLTK的word_tokenize函数将短语分词，得到两个短语的词汇列表
    synsets1 = []
    synsets2 = []
    for token in tokens1:
        synsets1.extend(wordnet.synsets(token))
    # 对于短语1中的每个词，使用NLTK的wordnet.synsets函数获取其同义词集合，并将其添加到synsets1列表中
    for token in tokens2:
        synsets2.extend(wordnet.synsets(token))

    max_sim = -1
    # 初始化最大相似度为-1
    for synset1 in synsets1:
        for synset2 in synsets2:
            sim = synset1.path_similarity(synset2)
            # 使用synset1.path_similarity(synset2)计算两个同义词集合的路径相似度，并将结果存储在sim变量中

            if sim is not None and sim > max_sim:
                max_sim = sim
                # 如果计算得到的相似度不为None且大于最大相似度，则更新最大相似度的值
    return max_sim

def researchAreaScore(researchArea,tmp_department):#这里的researchArea暂用degree
    #计算研究领域属性的分数，研究领域属性占比37%
    weight2=0.37
    if researchArea is None:
        return 0
    else:
        phrase1=tmp_department
        phrase2=re.split("in ",researchArea)[1]#暂用degree值代替researchArea值，因此需取degree后面部分
        #计算分词相似度
        max_sim=calculateSimilar(phrase1,phrase2)
        score2=max_sim*weight2
    return score2

def evaluate_sentiment(comment):
    #评估关于教授的网上评论的好坏程度
    sid = SentimentIntensityAnalyzer()# 初始化情感分析器
    sentiment_scores = sid.polarity_scores(comment)# 获取评论的情感分数
    good_bad_score = (sentiment_scores['pos'] - sentiment_scores['neg']) / 2 + 0.5# 根据情感分数计算好坏程度
    good_bad_score = max(0, min(1, good_bad_score))# 限定好坏程度范围在0至1之间
    return good_bad_score

def webCommentScore(webComment):
    #计算网上评论的分数，其中网上评论属性的占比为16%
    weight3=0.16
    if webComment is None:
        return 0
    else:
        judge=evaluate_sentiment(webComment)
        score3=judge*weight3
    return score3

def educationScore(education):
    #计算教授的学术背景的分数，其中学术背景属性占比为7%
    weight4=0.07
    if education is None:
        return 0
    else:
        #score4=int(education)*weight4
        score4 = 1.0 * weight4#目前education
    return score4

def calculateRank(user_degree,name,university,researchArea,webComment,education):
    # 计算ranking值
    score1 = universityScore(university)
    score2 = researchAreaScore(researchArea, user_degree)
    score3 = webCommentScore(webComment)
    score4 = educationScore(education)
    score = score1 + score2 + score3 + score4
    return score

def getData(user_degree):
    university=1#目前所有教授均是hku，故设默认值为1
    tmp_comment=""#目前没有关于教授的网上评论，故设为空
    result={} #用于存储ranking结果

    with open(file_path, 'r') as file:#文件路径
        reader = csv.reader(file)  # 创建csv reader对象
        for i, row in enumerate(reader):  # 逐行读取csv文件的内容
            # 读取前32行内容
            if i == 0:
                continue
            else:
                rank = calculateRank(user_degree, row[1], university, row[2], tmp_comment, row[3])
                keyword=row[0]+"!"+row[1]
                result[keyword] = rank
            """elif i <= 32:
                #print(row)
                rank = calculateRank(user_degree, row[1], university, row[2], tmp_comment, row[3])
                keyword = row[0] + "!" + row[1]
                result[keyword] = rank
            else:
                break"""


    return result

def write_csv_file(ranks):
    with open(save_path, 'w+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID','English Name', 'ranking'])

        for key in ranks.keys():
            keyId=re.split("!",key)[0]
            value1=re.split("!",key)[1]
            value2 = ranks[key]
            value2 = round(value2, 3)
            writer.writerow([keyId, value1,value2])

def main(id,user_degree):
    result = getData(user_degree)
    print("已计算出结果")
    write_csv_file(result)
    print("已将" + "为ID：" + id + "的用户推荐的结果写入result.csv内！")

main("1234","Business Administration")#用于调试