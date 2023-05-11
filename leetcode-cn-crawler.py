import argparse
import json
import os
import time

import requests
from sqlalchemy import Column, create_engine, Integer, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists

from template import readme_adding, README_CN, README_EN, sql_solution, normal_solution, shell_solution

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', nargs='+', help="username")
parser.add_argument('-p', '--password', nargs='+', help="password")
parser.add_argument('-dp', '--database', nargs='+', help="database")
parser.add_argument('-g', '--github', nargs='+', help="github")
parser.add_argument('-r', '--output', nargs='+', help="output_directory_path")
args = parser.parse_args()

argsDict = vars(args)

DB_PATH = args.database[0]
USERNAME = args.username[0]
PASSWORD = args.password[0]
GITHUBURL = args.github[0]
ROOT_PATH = args.output[0]

# if os.path.exists(ROOT_PATH + DB_PATH): os.remove(ROOT_PATH + DB_PATH)

user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

requests.packages.urllib3.disable_warnings()
leetcode_url = 'https://leetcode.cn/'
sign_in_url = 'https://leetcode.cn/accounts/login/'
submissions_url = 'https://leetcode.cn/submissions/'
problems_url = "https://leetcode.cn/api/problems/all/"
question_url = "https://leetcode.cn/problems/"
tag_url = "https://leetcode.cn/tag/"

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

diff_short = {
    'Easy': "易",
    'Medium': "中",
    'Hard': "难"
}

for key in category:
    path = category[key]
    isExists = os.path.exists(ROOT_PATH + path)
    if not isExists:
        os.mkdir(ROOT_PATH + path)
Base = declarative_base()


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    frontend_id = Column(TEXT, nullable=False)
    simple_url = Column(TEXT, nullable=False)
    title_cn = Column(TEXT, nullable=False)
    title_en = Column(TEXT, nullable=False)
    difficulty = Column(TEXT, nullable=False)
    category_title_cn = Column(TEXT, nullable=False)
    tags = Column(TEXT)


engine = create_engine('{}?check_same_thread=False?charset=utf8'.format("sqlite:///" + ROOT_PATH + DB_PATH), echo=False)
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
    global user_name
    global num_solved
    global num_total
    global ac_easy
    global ac_medium
    global ac_hard
    user_name = information_json['user_name']
    num_solved = information_json['num_solved']
    num_total = information_json['num_total']
    ac_easy = information_json['ac_easy']
    ac_medium = information_json['ac_medium']
    ac_hard = information_json['ac_hard']
    questions_list = information_json['stat_status_pairs']
    for question in questions_list:
        question_id = int(question['stat']['question_id'])  # 1000093
        question_frontend_id = question['stat']['frontend_question_id']  # LCP 13 / 面试题 17.08 / 1
        question_title = question['stat']['question__title']  # '寻宝'
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

        if len(question_frontend_id) == 4 and question_frontend_id[0] == '5': continue
        if question['stat']['question__hide']: continue
        if not question_status: continue

        # print(question_id, question_frontend_id, type(question_frontend_id), question_title)
        current_question_find = dbsession.query(exists().where(Question.id == question_id)).scalar()
        if current_question_find: continue
        # print(question_title)
        get_question_detail(question_simple_url)


def get_question_detail(simple_url):
    session = requests.Session()
    question_headers = {'User-Agent': user_agent,
                        'Connection': 'keep-alive',
                        'Content-Type': 'application/json',
                        'Referer': 'https://leetcode.cn/problems/' + simple_url}
    detailed_question_url = "https://leetcode.cn/graphql"
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
    # print(content)
    if content['data']['question']['translatedTitle'] == None: return
    print(content['data']['question']['questionId'],
          content['data']['question']['questionFrontendId'],
          content['data']['question']['translatedTitle'])

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

    current_question_path = ROOT_PATH + "/{}/{}. {}".format(category_title_cn, frontend_id, title_cn)
    if not os.path.exists(current_question_path):
        os.mkdir(current_question_path)
    sample_cn = open(os.getcwd() + "/Sample/Question/README.md", 'r', encoding='UTF-8')
    f_cn = open(current_question_path + "/README.md", 'w', encoding='UTF-8')
    for line in sample_cn.readlines():
        f_cn.write(line)
    f_cn.write("# [{}. {}]({})\n".format(frontend_id, title_cn, question_url + simple_url))

    f_cn.write(content_cn if content_cn else "")

    if len(tags) > 0:
        f_cn.write("\n**标签:**  ")
        for tag in tags:
            f_cn.write("[{}]({}) ".format(tag['translatedName'], tag_url + tag['slug']))

    try:
        similarQuestions = eval(similarQuestions)
        if len(similarQuestions) > 0:
            f_cn.write("\n ### 相似题目\n")
            # print(similarQuestions, type(similarQuestions))
            for similar_question in similarQuestions:
                # print(similar_question, type(similar_question))
                f_cn.write("- {}:\t[{}]({}) \n".format(diff[similar_question["difficulty"]],
                                                       similar_question['translatedTitle'],
                                                       question_url + similar_question['titleSlug']))
    except:
        pass

    solution_content = normal_solution
    if (category_title == "Database"):
        solution_content = sql_solution
    elif (category_title == "Shell"):
        solution_content = shell_solution
    f_cn.write(solution_content)
    sample_cn.close()
    f_cn.close()

    sample_en = open(os.getcwd() + "/Sample/Question/README_EN.md", 'r', encoding='UTF-8')
    f_en = open(current_question_path + "/README_EN.md", 'w', encoding='UTF-8')
    for line in sample_en.readlines():
        f_en.write(line)
    f_en.write("# [{}. {}]({})".format(frontend_id, title_en, question_url + simple_url))

    f_en.write("\n ### Description\n")
    f_en.write(content_en if content_en else "")

    if len(tags) > 0:
        f_en.write("\n**Related Topic{}**  ".format("s" if len(tags) > 1 else ""))
        for tag in tags:
            f_en.write("[{}]({}) ".format(tag['name'], tag_url + tag['slug']))

    try:
        if len(similarQuestions) > 0:
            f_en.write("\n\n### Similar Question{}\n".format("s" if len(similarQuestions) > 1 else ""))
            # print(similarQuestions, type(similarQuestions))
            for similar_question in similarQuestions:
                # print(similar_question, type(similar_question))
                f_en.write(" - {}:\t[{}]({}) \n".format(similar_question["difficulty"],
                                                        similar_question['title'],
                                                        question_url + similar_question['titleSlug']))
    except:
        pass
    sample_en.close()
    f_en.close()
    add_this_new_question_to_db(id, frontend_id, simple_url, title_cn, title_en, difficulty, category_title_cn, tags)


def add_this_new_question_to_db(id, frontend_id, simple_url, title_cn, title_en, difficulty, category_title_cn, tags):
    question_orm = Question(id=id,
                            frontend_id=frontend_id,
                            simple_url=simple_url,
                            title_cn=title_cn,
                            title_en=title_en,
                            difficulty=difficulty,
                            category_title_cn=category_title_cn,
                            tags=str(tags)
                            )
    dbsession.add(question_orm)
    dbsession.commit()


def write_main_readme():
    main_readme_cn = open(ROOT_PATH + "/README.md", 'w', encoding='UTF-8')
    main_readme_en = open(ROOT_PATH + "/README_EN.md", 'w', encoding='UTF-8')
    main_readme_cn.write(README_CN.format(
        user_name=user_name,
        num_solved=num_solved,
        num_total=num_total,
        ac_easy=ac_easy,
        ac_medium=ac_medium,
        ac_hard=ac_hard,
        time=curr_time
    ))
    main_readme_en.write(README_EN.format(
        user_name=user_name,
        num_solved=num_solved,
        num_total=num_total,
        ac_easy=ac_easy,
        ac_medium=ac_medium,
        ac_hard=ac_hard,
        time=curr_time
    ))

    results = dbsession.query(Question).order_by(Question.id).all()
    for result in results:
        WebURL_cn = \
            "{}/tree/master/{}/{}. {}".format(GITHUBURL, result.category_title_cn, result.frontend_id, result.title_cn)
        WebURL_cn = WebURL_cn.replace(' ', '%20')
        WebURL_en = \
            "{}/tree/master/{}/{}. {}/README_EN.md".format(
                GITHUBURL, result.category_title_cn, result.frontend_id, result.title_cn)
        WebURL_en = WebURL_en.replace(' ', '%20')
        tags_cn = ""
        for tag in eval(result.tags):
            tags_cn += "[{}]({}) ".format(tag['translatedName'], tag_url + tag['slug'])
        main_readme_cn.write(readme_adding.format(
            frontend_id=result.frontend_id,
            formal_url=question_url + result.simple_url,
            title=result.title_cn,
            githubURL=WebURL_cn,
            # solution="",
            difficulty=diff_short[result.difficulty],
            tags=tags_cn
        ))
        tags_en = ""
        for tag in eval(result.tags):
            tags_en += "[{}]({}) ".format(tag['name'], tag_url + tag['slug'])
        main_readme_en.write(readme_adding.format(
            frontend_id=result.frontend_id,
            formal_url=question_url + result.simple_url,
            title=result.title_en,
            githubURL=WebURL_en,
            # solution="",
            difficulty=result.difficulty,
            tags=tags_en
        ))

    main_readme_cn.close()
    main_readme_en.close()


if __name__ == '__main__':
    dbsession = DBSession()
    client = login(USERNAME, PASSWORD)
    get_question_list(client)
    curr_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    write_main_readme()
    dbsession.close()
