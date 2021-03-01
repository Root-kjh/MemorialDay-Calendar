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

### User Manage

* signup(/user/signup)
    * Request(POST)
        * Json : username, password  
    * Response : true/false 

* signin(/user/signin)
    * Request(POST)
        * Json : username, password  
    * Response : jwt

* password modify(/user/password-modify)
    * Request(PUT)
        * Auth : jwt
        * Json : newPassword  
    * Response : new jwt

* withdraw(/user/withdraw)
    * Request(DEL)
        * Auth: jwt
        * Json : password  
    * Response : true/false

### Calender Manage

* showCalender(/calender/show)
    * Request(GET)
        * Auth: jwt
    * Response : calender_data

* setCalender(/calender/set)
    * Request(POST)
        * Auth: jwt
        * Json: title, year, month, day, cycleWith, cycleUnit  
    * Response : true/false

* updateCalender(/calender/update/&#60;calenderID&#62;/)
    * Request
        * Auth: jwt
        * PathParameter: calenderID 
        * Json: title, year, month, day, cycleWith, cycleUnit
    * Response : true/false

* delCalender(/calender/del/&#60;calenderID&#62;/)
    * Request(DEL)
        * Auth: jwt
        * PathParameter: calnederID
    * Response : true/false