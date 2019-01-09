# Youboard Website
국내/해외 인기유투버, 채널, 영상을 순위별로 보여주는 웹사이트 개발

## 개발 스택
|           [VueJS](https://vuejs.org/)            |               [Vuetify](https://vuetifyjs.com)               |           [MongoDB](https://www.mongodb.com/)            |           [Flask](http://flask.pocoo.org/)            |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| <img src="https://vuejs.org/images/logo.png" width=100/> | <img src="https://cdn.vuetifyjs.com/images/logos/v-alt.svg" width=100/> | <img src="https://webassets.mongodb.com/_com_assets/cms/mongodb-logo-rgb-j6w271g1xn.jpg" width=100/> | <img src="http://flask.pocoo.org/static/logo/flask.svg" width=100/>

## 개발 계획
1. backend: wizdeo 사이트 scraping
 
   frontend: VueJs, Vuetify로 정적 페이지 생성
   
2. backend: scraping한 데이터 db에 저장, 정적페이지와 연동

   frontend : 반응형 페이지로 구현, youtube api로 동영상 및 썸네일 띄우기

3. - 공유하기 기능추가_ 각종 sns와 연동
   - 검색 기능 추가
   - 애드센스, GA 추가 등 SEO 관련 기능
   - 모바일 무한스크롤 10개씩 로딩하도록
   
4. admin page 구현

5. 배포하기(version 1.0)

## repo 구성
- UI, 요구사항 관련은 project_proposal 폴더에 저장.
- 기능별로 각각 브랜치에 커밋하기.

  master
  
     └ back/scraping
     
     └ back/flask
     
     └ front/youboard
     
     └ front/admin
