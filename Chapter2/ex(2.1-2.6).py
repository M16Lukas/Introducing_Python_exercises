hour = 1
minute = 60
second = 60

# 2.1 : 1시간은 몇 초인가?
print(minute * second)

# 2.2 : 계산한 결과를 seconds_per_hour 변수에 저장하라
seconds_per_hour = minute * second

# 2.3 : 1일은 몇 초인가? seconds_per_hour 변수를 사용하라
print(seconds_per_hour * 24)

# 2.4 : 계산한 결과를 seconds_per_day 변수에 저장하라
seconds_per_day = seconds_per_hour * 24

# 2.5 : 부동소수점(/) 나눗셈을 사용, seconds_per_day 를 seconds_per_hour 로 나누어라
print(seconds_per_day / seconds_per_hour)

# 2.6 : 정수(//) 나눗셈을 사용, seconds_per_day 를 seconds_per_hour 로 나누어라
print(seconds_per_day // seconds_per_hour)
