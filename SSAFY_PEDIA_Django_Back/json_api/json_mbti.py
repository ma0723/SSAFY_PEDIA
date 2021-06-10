import json
# from pprint import pprint
import sys


def movie_info(movies_list):
    result = []
    
    genre_list = [{"pk": 28, "name": "액션"}, {"pk": 12, "name": "모험"}, {"pk": 16, "name": "애니메이션"}, {"pk": 35, "name": "코미디"}, {"pk": 80, "name": "범죄"}, { "pk": 99, "name": "다큐멘터리"}, { "pk": 18, "name": "드라마"}, { "pk": 10751, "name": "가족"}, { "pk": 14, "name": "판타지"}, { "pk": 36, "name": "역사"}, { "pk": 27, "name": "공포"}, { "pk": 10402, "name": "음악"}, { "pk": 9648, "name": "미스터리"}, { "pk": 10749, "name": "로맨스"}, { "pk": 878, "name": "SF"}, { "pk": 10770, "name": "TV 영화"}, { "pk": 53, "name": "스릴러"}, {"pk": 10752, "name": "전쟁"}, {"pk": 37, "name": "서부"}]

    # 내가 원하는 정보의 key값
    key_list = ['release_date', 'title', 'poster_path', 'vote_average', 'overview']
    # for 문을 이용하여 key가 key_list 내부에 있으면 info ditionary에 추가
    i = 61
    # 4개씩
    # estj (1-4)
    # istj (5-8)
    # estp (9-12)
    # istp (13-16)
    # infp (17-20)
    # enfp (21-24)
    # infj (25-28)
    # enfj (29-32)
    # esfp (33-36)
    # isfp (37-40)
    # entj (41-44)
    # intj (45-48)
    # isfj (49-52)
    # intp (53-56)
    # entp (57-60)
    # esfj (61-64)
    for movie in movies_list:
        fields = {}
        # print(movie)
        for key in key_list:
            fields[key] = movie[key]
        fields['genre'] = movie['genres'][0]["name"]
        fields['mbti'] = "esfj" 
        # print(fields)
        info = { 
            "model": "movies.mbti",
            "pk": i,
        }
        info["fields"] = fields
        result.append(info)
        i += 1
    return result

if __name__ == '__main__':
    movies_json = open('esfj.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    movies = movie_info(movies_list)
    with open('mbti_esfj.json', 'w', encoding="utf-8") as f:
        json.dump(movies, f, ensure_ascii=False, indent="\t")