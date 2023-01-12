import feedparser, datetime

tistory_uri="https://amylim.tistory.com" 
feed = feedparser.parse(tistory_uri+"/rss")

markdown_text = """

![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Amy%20Lim&fontSize=90&animation=twinkling)

## :computer: Skills
### BackEnd
<img src="https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=Java&logoColor=white"> <img src="https://img.shields.io/badge/Spring-6DB33F?style=for-the-badge&logo=Spring&logoColor=white"> <img src="https://img.shields.io/badge/Spring Boot-6DB33F?style=for-the-badge&logo=SpringBoot&logoColor=white"> <img src="https://img.shields.io/badge/JPA-59666C?style=for-the-badge&logo=Hibernate&logoColor=white"> <img src="https://img.shields.io/badge/Gradle-02303A?style=for-the-badge&logo=Gradle&logoColor=white"> <img src="https://img.shields.io/badge/Apache Maven-C71A36?style=for-the-badge&logo=Apache Maven&logoColor=white"> <img src="https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=Oracle&logoColor=white"> 
### FrontEnd
<img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> <img src="https://img.shields.io/badge/html-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"> <img src="https://img.shields.io/badge/Thymeleaf-005F0F?style=for-the-badge&logo=Thymeleaf&logoColor=white">

## :medal_sports: Certificate
- 정보처리기사 Engineer Information Processing (2022.11)

## :page_facing_up: Latest Blog Posts 

""" # list of blog posts will be appended here

lst = []

for i in feed['entries'][:3]:
  
    markdown_text += f"<a href =\"{i['link']}\"> {i['title']} </a> <br>"

    print(i['link'], i['title'])

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()

## :bar_chart: Stats
<div align="center">
  
|                                                       Solved.ac                                                        |                                                             Languages                                                              |
| :--------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------: |
| [![Solved.ac profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=amylim32897)](https://solved.ac/amylim32897) | [![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=amylim328&layout=compact&theme=dark)](https://github.com/anuraghazra/github-readme-stats)

| ![Amy's GitHub stats](https://github-readme-stats.vercel.app/api?username=amylim328&show_icons=true&theme=dark) |
| :-----------------------------------------------------------------------------------------------------------------------: |
  
</div> 