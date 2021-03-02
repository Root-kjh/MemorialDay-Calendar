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

* options
    * Request(Options)
    * Response(Allow: POST)

* signup(/auth/signup)
    * Request(POST)
        * Json : username, password  
    * Response : true/false 

* signin(/auth/signin)
    * Request(POST)
        * Json : username, password  
    * Response : jwt

### User

* options
    * Request(Options)
    * Response(Allow: PATCH, DELETE)

* password modify(/user/password)
    * Request(PATCH)
        * Auth : jwt
        * Json : newPassword  
    * Response : new jwt

* withdraw(/user/)
    * Request(DEL)
        * Auth: jwt
    * Response : true/false

### Calender

* options
    * Request(Options)
    * Response(Allow: GET, POST, PUT, DELETE)

* showCalender(/calender)
    * Request(GET)
        * Auth: jwt
    * Response : calender_data

* setCalender(/calender)
    * Request(POST)
        * Auth: jwt
        * Json: title, year, month, day, cycleWith, cycleUnit  
    * Response : true/false

* updateCalender(/calender/&#60;calenderID&#62;)
    * Request(PUT)
        * Auth: jwt
        * PathParameter: calenderID 
        * Json: title, year, month, day, cycleWith, cycleUnit
    * Response : true/false

* delCalender(/calender/&#60;calenderID&#62;)
    * Request(DELETE)
        * Auth: jwt
        * PathParameter: calnederID
    * Response : true/false