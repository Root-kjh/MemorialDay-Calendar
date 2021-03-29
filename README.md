# MemorialDay-Calendar

## 기능

* 기념일의 월/일을 저장 후 돌아오는 기념일 표시
* Save the month/day of the anniversary and mark the return anniversary

* n일에 한번 돌아오는 기념일
* a return day on the (n)

* n주에 한번 돌아오는 기념일
* a return week on the (n)

* n달에 한번 돌아오는 기념일
* a return month on the (n)

* n년에 한번 돌아오는 기념일
* a return year on the (n)

## API Docs

* Success Response: {"Message": "Success"}
* Fail Response: {"Message": "Failed"}

* Userinfo
   * Long:user_id
   * String:username
   * String:jwt

* SetAnniversary
   * String:title
   * Date:start_day(yyyy-mm-dd)
   * String:cycleWith
   * int:cycleUnit  

* GetAnniversary
   * int:anniversary_id
   * String:title
   * Date:start_day(yyyy-mm-dd)
   * String:cycleWith
   * int:cycleUnit 

### Auth

* signup(/auth/signup/)
    * Request(POST)
        * Json
            * String:username
            * String:password  
    * Response : Success/ Fail

* signin(/auth/signin/)
    * Request(POST)
        * Json : username, password  
    * Response : Userinfo

### User

* password modify(/user/&#60;user_id&#62;/)
    * Request(PATCH)
        * Auth : jwt
        * PathParameter: Long:user_id
        * Json : String:password
    * Response : Success/ Fail

* withdraw(/user/&#60;user_id&#62;/)
    * Request(DELETE)
        * Auth: jwt
        * PathParameter: Long:user_id
    * Response : Success/ Fail

### Calender

* showCalender(/user/&#60;user_id&#62;/calender/)
    * Request(GET)
        * Auth: jwt
        * PathParameter: Long:user_id
    * Response : GetAnniversary

* setCalender(/user/&#60;user_id&#62;/calender/)
    * Request(POST)
        * Auth: jwt
        * PathParameter: Long:user_id
        * Json : SetAnniversary
    * Response : Success/ Fail

* updateCalender(/user/&#60;user_id&#62;/calender/&#60;anniversary_id&#62;/)
    * Request(PUT)
        * Auth: jwt
        * PathParameter: 
            * Long:user_id
            * Long:anniversary_id 
        * Json: SetAnniversary
    * Response : Success/ Fail

* delCalender(/user/&#60;user_id&#62;/calender/&#60;anniversary_id&#62;/)
    * Request(DELETE)
        * Auth: jwt
        * PathParameter: 
            * Long:user_id
            * Long:anniversary_id 
    * Response : Success/ Fail
