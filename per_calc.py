VALUE_ERROR_MESSAGE = "올바른 숫자를 입력해야합니다."
VALUE_SOURCE_MESSAGE = "source 값을 입력하세요: "
VALUE_TARGET_MESSAGE = "target 값을 입력하세요: "
VALUE_PER_MESSAGE = "비율 값을 입력하세요: "
PROGRAM_END_MESSAGE = "프로그램을 종료합니다."

def source_per():
    while True:
        try:
            _source = int(input(VALUE_SOURCE_MESSAGE))  
        except ValueError:
            print(VALUE_ERROR_MESSAGE)
            continue
        while True:
            try:
                _per = int(input(VALUE_PER_MESSAGE))
            except ValueError:
                print(VALUE_ERROR_MESSAGE)
                continue
            break
        break

    print(f"{_source}의 {_per}%은(는) {_source * (_per / 100)}입니다.")

def target_per():
    while True:
        try:
            _source = int(input(VALUE_SOURCE_MESSAGE))  
        except ValueError:
            print(VALUE_ERROR_MESSAGE)
            continue
        while True:
            try:
                _target = int(input(VALUE_TARGET_MESSAGE))
            except ValueError:
                print(VALUE_ERROR_MESSAGE)
                continue
            break
        break

    print(f"{_source}에서 {_target}은(는) {_target / _source * 100}% 입니다.")

while True:
    print("1. source의 n% 구하기")
    print("2. source에서 target은 n%인지 구하기")
    print("3. 프로그램 종료")
    print("무엇을 원하십니까?")
    try:
        _select = int(input("> "))                
    except ValueError:
        print(VALUE_ERROR_MESSAGE)
        continue

    if _select == 1:
        source_per()
    elif _select == 2:
        target_per()
    elif _select == 3:
        print(PROGRAM_END_MESSAGE)
    else:
        print(VALUE_ERROR_MESSAGE)
        continue
    break