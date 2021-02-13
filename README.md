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
    >Request : userID, password  
    >Response : true/false 

* signin(/user/signin)
    >Request : userID, password  
    >Response : jwt

* password modify(/user/password-modify)
    >Request : jwt, password, newPassword  
    >Response : new jwt

* withdraw(/user/withdraw)
    >Request : jwt, password  
    >Response : true/false

### Calender Manage

* showCalender(/calender/show)
    >Request : jwt
    >Response : calender_data

* setCalender(/calender/set)
    >Request : jwt, title, year, month, day, cycleWith, cycleUnit  
    >Response : true/false

* updateCalender(/calender/update)
    >Request : jwt, idx, title, year, month, day, cycleWith, cycleUnit
    >Response : true/false

* delCalender(/calender/del)
    >Request : jwt, idx
    >Response : true/false