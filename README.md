# server
megaLittleLion server 레포지토리입니다.

# 영화 평점 사이트 API 명세

---

# Members앱 API

## POST - [Members] 회원가입

`http://127.0.0.1:8000/members/signup/`

**Request**

```json
curl --location 'http://127.0.0.1:8000/members/signup/' \
--header 'Content-Type: application/json' \
--header 'charset: utf-8' \
--data-raw '{
    "user_id" : "adddddam",
    "nickname" : "Adam",
    "password" : "1234",
	"pwcheck" : "1234"
```

**Response**

```json
HTTP 200 OK

{
    "message": "회원가입 되었습니다."
}
```

## POST - [Members] 회원가입 실패

**Response**

```json
HTTP_400_BAD_REQUEST

{
    "message": "회원가입에 실패하였습니다."
}
```

## POST - [Members] 로그인

`http://127.0.0.1:8000/members/login/`

**Request**

```json
curl --location 'http://127.0.0.1:8000/account/login/' \
--data '{
    "user_id" : "adddddam",
    "password" : "1234"
}'
```

**Response**

```json
{
    "message": "로그인 되었습니다."
}
```

## POST - [Members] 로그인 실패

```json
HTTP_400_BAD_REQUEST

{
    "message": "아이디가 일치하는 계정이 없습니다."
}
```

```json
HTTP_400_BAD_REQUEST

{
    "message": "비밀번호가 틀렸습니다."
}
```

## POST - 닉네임 중복 체크

`http://127.0.0.1:8000/members/uniquecheck/nickname/`

```json
HTTP_400_BAD_REQUEST

{
    "message": "닉네임 중복"
}
```

```json
HTTP_200_OK

{
    "message": "중복 아님"
}
```


---

# Movie앱 API

## GET - [MainPage] 메인페이지 API

`http://127.0.0.1:8000/movie/`

## GET [DetailPage] 영화 상세페이지 호출

`http://127.0.0.1:8000/movie/<str:moviename>/`

**Request**

```json
curl --location 'http://127.0.0.1:8000/movie/<str:moviename>/ \

```

**Response**

```json
{
"title_kor": "그레이 맨",
"title_eng": "The Gray Man, 2022",
"poster_url": "https://movie-phinf.pstatic.net/20220707_187/165715990860275QAG_JPEG/movie_image.jpg?type=m203_290_2",
"rating_aud": "8.02",
"rating_cri": "",
"rating_net": "8.40",
"genre": "액션,스릴러",
"showtimes": "127분",
"release_date": "2022.07.13 개봉",
"rate": "15세 관람가",
"summary": "그 누구도 실체를 몰라 `그레이 맨`으로 불리는 CIA의 암살 전문 요원이 우연히 CIA의 감추고 싶은 비밀을 알게 되고, CIA의 사주를 받은 소시오패스 전 동료에게 쫓기며 시작되는 액션 블록버스터",
"staff": [
{
"name": "앤서니 루소",
"role": "감독",
"image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fssl.pstatic.net%2Fsstatic%2Fpeople%2F185%2F202207111035175201.png&type=u111_139&quality=95"
},
{
"name": "라이언 고슬링",
"role": "주연",
"image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fimgmovie.naver.net%2Fmdi%2Fpi%2F000000057%2FPM5751_144824_000.jpg&type=u111_139&quality=95"
},
{
"name": "크리스 에반스",
"role": "주연",
"image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fssl.pstatic.net%2Fsstatic%2Fpeople%2F110%2F202206081151278971.png&type=u111_139&quality=95"
},
{
"name": "아나 데 아르마스",
"role": "주연",
"image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fimgmovie.naver.net%2Fmdi%2Fpi%2F000001712%2FPM171281_181850_000.jpg&type=u111_139&quality=95"
},
{
"name": "레게장 페이지",
"role": "주연",
"image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fssl.pstatic.net%2Fsstatic%2Fpeople%2F37%2F202012241413274941.jpg&type=u111_139&quality=95"
}
]
},
```

## GET [DetailPage] 영화 상세 코멘트 작성

`http://127.0.0.1:8000/movie/<str:moviename>/comments/`

Request

```json
{
		"comment": "액션씬이 참 멋있었다!"
}
```

Response

```json
{
"title_kor": "그레이 맨",
"title_eng": "The Gray Man, 2022",
"poster_url": "https://movie-phinf.pstatic.net/20220707_187/165715990860275QAG_JPEG/movie_image.jpg?type=m203_290_2",
"rating_aud": "8.02",
"rating_cri": "",
"rating_net": "8.40",
"genre": "액션,스릴러",
"showtimes": "127분",
"release_date": "2022.07.13 개봉",
"rate": "15세 관람가",
"summary": "그 누구도 실체를 몰라 `그레이 맨`으로 불리는 CIA의 암살 전문 요원이 우연히 CIA의 감추고 싶은 비밀을 알게 되고, CIA의 사주를 받은 소시오패스 전 동료에게 쫓기며 시작되는 액션 블록버스터",
"staff": [
{
"name": "앤서니 루소",
"role": "감독",
"image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fssl.pstatic.net%2Fsstatic%2Fpeople%2F185%2F202207111035175201.png&type=u111_139&quality=95"
},
{
"name": "라이언 고슬링",
"role": "주연",
"image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fimgmovie.naver.net%2Fmdi%2Fpi%2F000000057%2FPM5751_144824_000.jpg&type=u111_139&quality=95"
},
{
"name": "크리스 에반스",
"role": "주연",
"image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fssl.pstatic.net%2Fsstatic%2Fpeople%2F110%2F202206081151278971.png&type=u111_139&quality=95"
},
{
"name": "아나 데 아르마스",
"role": "주연",
"image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fimgmovie.naver.net%2Fmdi%2Fpi%2F000001712%2FPM171281_181850_000.jpg&type=u111_139&quality=95"
},
{
"name": "레게장 페이지",
"role": "주연",
"image_url": "https://search.pstatic.net/common/?src=https%3A%2F%2Fssl.pstatic.net%2Fsstatic%2Fpeople%2F37%2F202012241413274941.jpg&type=u111_139&quality=95"
}
]
"comment": "액션씬이 참 멋있었다!"
},
```
