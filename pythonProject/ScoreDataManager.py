import datetime


class StudentInfo:
    def __init__(self, n, e, i):
        self.name = n
        self.email = e
        self.id = i  # 년도 학과 순번 4+2+2 자리수

    # 멤버변수 출력
    def print_info(self):
        print("--학생정보 출력--")
        print("이름:" + self.name)
        print("e-mail:" + self.email)
        print("id:" + self.id)


class ScoreDataManager:
    Administer_ID = "admin"
    Administer_PW = "1234"

    major_dictionary = {1: "프로그래밍", 2: "기획", 3: "그래픽"}
    major_subjects_list = [[], [], [], []]  # 학과별 과목들 dictionary 리스트
    max_subjects = 5  # 학과별 최대 과목 수
    major_counter = [0, 1, 1, 1]  # 학과에 추가된 학생 수를 기록 # 0번방 사용 안함
    major_studentInfo_lists = [[], [], [], []]  # 학과별 학생들 info # 0번방 사용 안함

    # 관리자 프로세스 실행
    # 잘못 입력 시 NotImplementdError
    @staticmethod
    def run():

        flag = ScoreDataManager.certificate()
        if flag:  # 로그인 성공 시
            while True:
                print("<관리자 메뉴>")
                print("1.학생추가")
                print("2.과목추가")
                print("3.과목삭제")
                print("4.관리자 모드 종료")
                num = int(input("입력:"))
                if num < 1 or num > 4:
                    raise NotImplementedError('잘못된 입력 값입니다')

                if num == 4:
                    ScoreDataManager.exit_admin()
                    break  # 관리자 모드 반복문 종료

    # 관리자 로그인 인증
    # 로그인 성공 시 true
    @staticmethod
    def certificate() -> bool:
        _id = input("ID:")
        _pw = input("PW:")
        if _id != ScoreDataManager.Administer_ID or _pw != ScoreDataManager.Administer_PW:
            print("관리자 로그인 성공")
            return False
        print("아이디 혹은 비밀번호가 틀립니다")
        return True

    # 과목을 선택하여 return
    # 잘못 입력 시 NotImplementdError
    @staticmethod
    def select_major() -> int:
        major = int(input("학과(1.프로그래밍 ,2.기획, 3.그래픽):"))
        if major in ScoreDataManager.major_dictionary:
            return major
        else:
            raise NotImplementedError('잘못된 입력 값입니다')

    # 추가 입력할 지 여부를 판단하는 함수
    # 추가 입력을 선택할 경우 true
    # 잘못 입력 시 NotImplementError
    @staticmethod
    def select_continue() -> bool:
        c = input("추가입력(y/n")
        if c == "y":
            return True
        elif c == "n":
            return False
        else:
            raise NotImplementedError('잘못된 입력 값입니다')

    # 학생 추가 프로세스
    @staticmethod
    def new_student():
        flag = True
        while flag:
            # 전공 선택
            major = ScoreDataManager.select_major()
            # 학생 정보 입력
            name = input("이름:")
            e_mail = input("e-mail:")
            # 학번 생성 : 년도 + 학과 코드 + 입력 순번
            cur_year = datetime.datetime.today().year  # 현재 년도
            cur_count = ScoreDataManager.major_counter[major]  # 현재 순번
            _id = str(cur_year) + "{0:02d}".format(major) + "{0:02d}".format(cur_count)

            # 새로운 학생 정보 생성
            student_info = StudentInfo(name, e_mail, _id)
            student_info.print_info()
            # 학생 정보를 등록
            ScoreDataManager.major_studentInfo_lists[major].append(student_info)
            
            # 계속 추가로 진행할지 여부를 선택
            flag = ScoreDataManager.select_continue()
            
    #  새로운 과목 추가
    @staticmethod
    def new_subject():
        # 전공 선택
        major = ScoreDataManager.select_major()

        # 이미 최대라면 raise
        if len(ScoreDataManager.major_subjects_list) >= 5:
            print("학과별로 5과목을 초과할 수 없습니다")
            raise NotImplementedError("학과 최대치 도달")
        # 새로운 과목을 추가
        print("새로운 과목을 추가합니다...")
        sub_name = input("과목명:")
        ScoreDataManager.major_subjects_list[major].append(sub_name)

    # 기존 과목에서 제거
    @staticmethod
    def delete_subject():
        # 전공 선택
        major = ScoreDataManager.select_major()

        # 현재 전공의 과목들을 출력
        print("기존 과목을 삭제합니다...")
        for item in ScoreDataManager.major_subjects_list[major]:
            print(item + " ", end="")
        print()

        # 삭제할 과목 선택
        sub_name = input("과목명:")
        if sub_name in ScoreDataManager.major_studentInfo_lists:
            ScoreDataManager.major_studentInfo_lists.remove(sub_name)
            print("과목 삭제 완료")
        else:
            print("과목명을 잘못 입력하셨습니다")

        # 현재 정공의 과목들을 출력
        for item in ScoreDataManager.major_subjects_list[major]:
            print(item + " ", end="")
        print()

    # 관리자 모드 종료
    @staticmethod
    def exit_admin():
        print("관리자 모드를 종료합니다")

    # 모든 학과의 학생 정보를 출력
    @staticmethod
    def print_all_students_info():
        for student_list in ScoreDataManager.major_studentInfo_lists:
            print()
            for item in student_list:
                item.print_info()
