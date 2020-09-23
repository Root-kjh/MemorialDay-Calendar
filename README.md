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
    >Response : JWT

* password modify(/user/password-modify)
    >Request : JWT, password, newPassword  
    >Response : true/false

* withdraw(/user/withdraw)
    >Request : JWT, password  
    >Response : true/false

### Calender Manage

* showCalender(/calender/show)
    >Request : JWT  
    >Response : json_calender_data

* setCalenderWithDay(/calender/set/day)
    >Request : year, month, day, dayCycle  
    >Response : true/false

* setCalenderWithWeek(/calender/set/week)
    >Request : year, month, day, weekCycle  
    >Response : true/false

* setCalenderWithMonth(/calender/set/month)
    >Request : year, month, day, monthCycle  
    >Response : true/false

* setCalenderWithYear(/calender/set/year)
    >Request : year, month, day, yearCycle  
    >Response : true/false