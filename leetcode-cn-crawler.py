import os
import requests
import json
from sqlalchemy import Column, String, create_engine, Integer, TEXT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from sqlalchemy.ext.declarative import declarative_base

f_config = open('config.json', 'r')
user_config = json.load(f_config)

DB_PATH = user_config["database"]
USERNAME = user_config["username"]
PASSWORD = user_config["password"]

ROOT_PATH = os.getcwd()
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

requests.packages.urllib3.disable_warnings()  # 为了避免弹出一万个warning，which is caused by 非验证的get请求
leetcode_url = 'https://leetcode-cn.com/'
sign_in_url = 'https://leetcode-cn.com/accounts/login/'
submissions_url = 'https://leetcode-cn.com/submissions/'
problems_url = "https://leetcode-cn.com/api/problems/all/"
question_url = "https://leetcode-cn.com/problems/"
tag_url = "https://leetcode-cn.com/tag/"

category = {
    'Algorithms': "算法",
    'LCCI': "程序员面试金典",
    'LCOF': "剑指OFFER",
    'Database': "数据库",
    'Shell': "Shell",
    'Concurrency': "多线程"
}
diff = {
    'Easy': "简单",
    'Medium': "中等",
    'Hard': "困难"
}
for key in category:
    path = category[key]
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
Base = declarative_base()


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    frontend_id = Column(TEXT, nullable=False)
    title_en = Column(TEXT, nullable=False)
    title_cn = Column(TEXT, nullable=False)
    content_en = Column(TEXT, nullable=False)
    content_cn = Column(TEXT, nullable=False)
    simple_url = Column(TEXT, nullable=False)
    difficulty = Column(TEXT, nullable=False)
    category_title = Column(TEXT, nullable=False)
    tag = Column(TEXT, nullable=False)


engine = create_engine('{}?check_same_thread=False?charset=utf8'.format(DB_PATH), echo=True)
Base.metadata.create_all(engine, checkfirst=True)
DBSession = sessionmaker(bind=engine)


def login(username, password):
    client = requests.session()
    client.encoding = "utf-8"

    client.get(sign_in_url, verify=False)
    login_data = {'login': username, 'password': password}
    result = client.post(sign_in_url, data=login_data, headers=dict(Referer=sign_in_url))

    if result.ok:
        print("Login Successfully!")  # Login Successfully!
    else:
        print("Login Failed!")
    return client


def get_question_list(client):
    headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}
    response = client.get(problems_url, headers=headers, timeout=10)
    # print(response)  # <Response [200]>
    # print(response.content.decode('utf-8'))  # My Personal Information

    information_json = json.loads(response.content.decode('utf-8'))  # Attention for this loads 's'
    # print(information_json['user_name']) # Personal UserName
    # Smaple Information of Problems:
    # {'stat': {'question_id': 1000093, 'question__title': '寻宝', 'question__title_slug': 'xun-bao', 'question__hide': False, 'total_acs': 323, 'total_submitted': 1862, 'total_column_articles': 15, 'frontend_question_id': 'LCP 13', 'is_new_question': False}, 'status': None, 'difficulty': {'level': 3}, 'paid_only': False, 'is_favor': False, 'frequency': 0, 'progress': 0}
    # print(information_json)
    ac_easy = information_json['ac_easy']
    ac_medium = information_json['ac_medium']
    ac_hard = information_json['ac_hard']
    questions_list = information_json['stat_status_pairs']
    for question in questions_list:
        # question_id = int(question['stat']['question_id'])  # 1000093
        # question_frontend_id = question['stat']['frontend_question_id']  # LCP 13 / 面试题 17.08 / 1
        # question_title = question['stat']['question__title']  # '寻宝'
        question_simple_url = question['stat']['question__title_slug']  # 'xun-bao'
        # print(question_id, '\t', question_frontend_id, '\t', question_title, '\t', question_simple_url)
        question_status = question['status']  # ac / None
        # question_level = question['difficulty']['level']
        #
        # if question_level == 1:
        #     question_difficulty = "Easy"
        # elif question_level == 2:
        #     question_difficulty = "Medium"
        # elif question_level == 3:
        #     question_difficulty = "Hard"

        if question['paid_only']: continue
        if not question_status: continue
        # current_question_find = session.query(exists().where(Question.id == 1000090)).scalar()
        # if current_question_find: continue

        get_question_detail(question_simple_url)


def get_question_detail(simple_url):
    session = requests.Session()
    dbsession = DBSession()
    question_headers = {'User-Agent': user_agent,
                        'Connection': 'keep-alive',
                        'Content-Type': 'application/json',
                        'Referer': 'https://leetcode-cn.com/problems/' + simple_url}
    detailed_question_url = "https://leetcode-cn.com/graphql"
    params = {'operationName': "getQuestionDetail",
              'variables': {'titleSlug': simple_url},
              'query':
                  '''
                  query getQuestionDetail($titleSlug: String!) {
                            question(titleSlug: $titleSlug) {
                                questionId
                                questionFrontendId
                                titleSlug
                                title
                                translatedTitle 
                                difficulty
                                categoryTitle
                                similarQuestions
                                topicTags {
                                    name
                                    slug
                                    translatedName
                                }
                                content
                                translatedContent
                            }
                  }
                  '''
              }
    json_data = json.dumps(params).encode('utf8')
    question_detail = ()
    response = session.post(detailed_question_url, data=json_data, headers=question_headers, timeout=10)
    content = response.json()
    print(content)
    question_orm = Question(id=content['data']['question']['questionId'],
                            frontend_id=content['data']['question']['questionFrontendId'],
                            title_en=content['data']['question']['title'],
                            title_cn=content['data']['question']['translatedTitle'],
                            content_en=content['data']['question']['translatedContent'],
                            content_cn=content['data']['question']['content'],
                            simple_url=simple_url,
                            difficulty=content['data']['question']['difficulty'],
                            category_title=content['data']['question']['categoryTitle'],
                            tag=str(content['data']['question']['topicTags'])
                            )
    # dbsession.add(question_orm)
    # dbsession.commit()
    dbsession.close()
    process_writing_question(content)


def process_writing_question(content):
    id = content['data']['question']['questionId']
    frontend_id = content['data']['question']['questionFrontendId']
    title_en = content['data']['question']['title']
    title_cn = content['data']['question']['translatedTitle']
    content_cn = content['data']['question']['translatedContent']
    content_en = content['data']['question']['content']
    simple_url = content['data']['question']['titleSlug']
    difficulty = content['data']['question']['difficulty']
    category_title = content['data']['question']['categoryTitle']
    tags = content['data']['question']['topicTags']
    similarQuestions = content['data']['question']['similarQuestions']

    if category_title not in category:
        category[category_title] = category_title
    category_title_cn = category[category_title]

    current_question_path = ROOT_PATH + "\{}\{}. {}".format(category_title_cn, frontend_id, title_cn)
    print(current_question_path)
    if not os.path.exists(current_question_path):
        os.mkdir(current_question_path)
    sample_cn = open(ROOT_PATH + "\Sample\README.md", 'r', encoding='UTF-8')
    f_cn = open(current_question_path + "\README.md", 'w', encoding='UTF-8')
    for line in sample_cn.readlines():
        f_cn.write(line)
    f_cn.write("# [{}. {}]({})".format(frontend_id, title_cn, question_url + simple_url))

    f_cn.write("\n ### 题目描述\n")
    f_cn.write(content_cn)

    if len(tags) > 0:
        f_cn.write("\n**标签:\t**")
        for tag in tags:
            f_cn.write("[{}]({}) ".format(tag['translatedName'], tag_url + tag['slug']))

    similarQuestions = eval(similarQuestions)
    if len(similarQuestions) > 0:
        f_cn.write("\n ### 相似题目\n")
        # print(similarQuestions, type(similarQuestions))
        for similar_question in similarQuestions:
            # print(similar_question, type(similar_question))
            f_cn.write("- {}:\t[{}]({}) \n".format(diff[similar_question["difficulty"]],
                                                   similar_question['translatedTitle'],
                                                   question_url + similar_question['titleSlug']))

    sample_en = open(ROOT_PATH + "\Sample\README_EN.md", 'r', encoding='UTF-8')
    f_en = open(current_question_path + "\README_EN.md", 'w', encoding='UTF-8')
    for line in sample_en.readlines():
        f_en.write(line)
    f_en.write("# [{}. {}]({})".format(frontend_id, title_en, question_url + simple_url))

    f_en.write("\n ### Description\n")
    f_en.write(content_en)

    if len(tags) > 0:
        f_en.write("\n**Related Topic{}\t**".format("s" if len(tags) > 1 else ""))
        for tag in tags:
            f_en.write("[{}]({}) ".format(tag['name'], tag_url + tag['slug']))

    if len(similarQuestions) > 0:
        f_en.write("\n\n### Similar Question{}\n".format("s" if len(similarQuestions) > 1 else ""))
        # print(similarQuestions, type(similarQuestions))
        for similar_question in similarQuestions:
            # print(similar_question, type(similar_question))
            f_en.write(" - {}:\t[{}]({}) \n".format(similar_question["difficulty"],
                                                    similar_question['title'],
                                                    question_url + similar_question['titleSlug']))


if __name__ == '__main__':
    client = login(USERNAME, PASSWORD)
    # get_question_list(client)
    get_question_detail(simple_url="xun-bao")
    get_question_detail(simple_url="number-of-ways-to-wear-different-hats-to-each-other")
    get_question_detail(simple_url="string-rotation-lcci")
    get_question_detail(simple_url="department-highest-salary")
    get_question_detail(simple_url="the-dining-philosophers")
    get_question_detail(simple_url="first-unique-character-in-a-string")
