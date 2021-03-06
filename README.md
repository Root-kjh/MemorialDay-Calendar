# MemorialDay-Calendar
매 년 돌아오는 기념일 리마인더

## 기능

* 기념일의 월/일을 저장 후 매년 돌아오는 기념일 표시

* Android 어플을 이용해 매년 돌아오는 기념일 리마인드

* n일에 한번 돌아오는 기념일

* n주에 한번 돌아오는 기념일

* n달에 한번 돌아오는 기념일

* n년에 한번 돌아오는 기념일

## API Docs

### Auth

* signup(/auth/signup/)
    * Request(POST)
        * Json : username, password  
    * Response : Success/ Fail

* signin(/auth/signin/)
    * Request(POST)
        * Json : username, password  
    * Response : userinfo(pk, username, jwt)

### User

* password modify(/user/&#60;pk&#62;/)
    * Request(PATCH)
        * Auth : jwt
        * PathParameter: pk
        * Json : Password  
    * Response : Success/ Fail

* withdraw(/user/&#60;pk&#62;/)
    * Request(DELETE)
        * Auth: jwt
        * PathParameter: pk
    * Response : Success/ Fail

### Calender

* showCalender(/calender/)
    * Request(GET)
        * Auth: jwt
    * Response : calender_data(pk, title, start_day(yyyy-mm-dd), cycle_with, cycle_unit)

* setCalender(/calender/)
    * Request(POST)
        * Auth: jwt
        * Json: title, start_day(yyyy-mm-dd), cycleWith, cycleUnit  
    * Response : Success/ Fail

* updateCalender(/calender/&#60;pk&#62;/)
    * Request(PUT)
        * Auth: jwt
        * PathParameter: pk 
        * Json: title, start_day(yyyy-mm-dd), cycleWith, cycleUnit
    * Response : Success/ Fail

* delCalender(/calender/&#60;pk&#62;/)
    * Request(DELETE)
        * Auth: jwt
        * PathParameter: pk
    * Response : Success/ Fail