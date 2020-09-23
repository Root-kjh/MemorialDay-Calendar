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
    >Response : true/false

* password modify(/user/password-modify)
    >Request : session, password, newPassword  
    >Response : true/false

* logout(/user/logout)
    >Request : session  
    >Response : destroy session
* withdraw(/user/withdraw)
    >Request : session, password  
    >Response : true/false

### Calender Manage

* showCalender(/calender/show)
    >Response : calender_data

* setCalender(/calender/set)
    >Request : session, year, month, day, cycleWith, cycleUnit  
    >Response : true/false