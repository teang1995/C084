import sys


class SimpleCPU:
    '''
        SimpleCPU 모듈
        레지스터 크기 num_regs 와 mem_size 값을 받는다.
    '''
    def __init__(self, num_regs, mem_size):
        self.ip = 0
        self.registers = [0 for _ in range(NUM_REGS)] # for saving data
        self.memory = [0 for _ in range(MEM_SZ)] # for saving data

    def execute(self, program):
        # Implement this one
        memory = eval(program[0].replace("\n", ""))
        self.memory = memory
        programs = []
        for process in program[1:]:
            process = process.replace("\n", "")
            programs.append(process)

        for process in programs:
            '''
            split_list[0] : 명령어
            split_list[1]~[3] : parameters
            '''
            split_list = process.split(" ")
            if split_list[0] == "ld":
                self.ld(int(split_list[1]), int(split_list[2]))
                self.ip += 1

            if split_list[0] == "add":
                dst = int(split_list[1].replace("$", ""))
                src1 = int(split_list[2].replace("$", ""))
                src2 = int(split_list[3].replace("$", ""))
                self.add(dst, src1, src2)
                self.ip += 1

            if split_list[1] == "ble":
                src1 = int(split_list[1].replace("$", ""))
                src2 = int(split_list[2].replace("$", ""))
                dst = int(split_list[3])
                self.ble(src1, src2, dst)
                self.ip += 1

            if split_list[0] == "st":
                src = int(split_list[1].replace("$", ""))
                dst = int(split_list[2])
                self.st(src, dst)
                self.ip += 1

    def ld(self, src, dst):
        # 인덱스 오류 처리 필요
        self.registers[dst] = self.memory[src]

    def st(self, src, dst):
        # 인덱스 오류 처리 필요
        self.memory[dst] = self.regiterss(src)

    def add(self, dst, src1, src2):
        # registers[dst] = registers[src1] + registers[src2]
        # 인덱스 오류 처리 필요
        self.registers[dst] = self.registers[src1] + self.registers[src2]

    def sub(self, dst, src1, src2):
        # registers[dst] = registers[src1] - registers[src2]
        # 인덱스 오류 처리 필요
        self.registers[dst] = self.registers[src1] - self.registers[src2]

    def div(self, dst, src1, src2):
        # registers[dst] = registers[src1] / registers[src2]
        # 인덱스 오류 처리 필요
        # division by zero 오류 처리 필요
        # 자료형은 어떻게 되더라?
        self.registers[dst] = self.registers[src1] / self.registers[src2]

    def mul(self, dst, src1, src2):
        # registers[dst] = registers[src1] * registers[src2]
        # 인덱스 오류 처리 필요
        # 자료형은 어떻게 되더라?
        self.registers[dst] = self.registers[src1] * self.registers[src2]

    def jump(self, idx):
        # ip <- idx
        # 인덱스 오류 처리 필요
        self.ip = idx

    def beq(self, src1, src2, idx):
        # if src1 == src2 then ip <- idx
        # 인덱스 오류 처리 필요
        if self.regiters[src1] == self.registers[src2]:
            self.ip = idx

    def ble(self, src1, src2, idx):
        # if registers[src1] <= registers[src2] then ip <- idx
        # 인덱스 오류 처리 필요
        if self.registers[src1] <= self.registers[src2]:
            self.ip = idx

    def bne(self, src1, src2, idx):
        # if registers[src1] != registers[src2] then ip <- idx
        # 인덱스 오류 처리 필요
        if self.registers[src1] != self.registers[src2]:
            self.ip = idx

    def print_status(self):
        print("IP : {}".format(self.ip))
        print("Register File : ")
        for i, register in enumerate(self.registers):
            print("${} : {}".format(i, register))
        print("Memory : ")
        for i, data in enumerate(self.memory):
            print("[{}] : {}".format(i, data))

# 상수 선언
NUM_REGS = 5
MEM_SZ = 10

# 본 if문은 c의 main함수와 유사한 역할을 합니다. 
# 프로그램을 파이썬 인터프리터로 실행할 경우에 실행되는 블락입니다. 
# 다른 파이썬 프로그램이 본 파일을 라이브러리 형태로 참조하고자 할 경우 실행되지 않습니다.
if __name__ == '__main__':
    # sys.argv는 프로그램의 인자를 가진 리스트입니다.
    # sys.argv[0]은 여러분이 입력한 실행 프로그램의 이름이 들어있습니다.
    # sys.argv[1:] 부터 프로그램에 인자로 입력한 값이 들어 있습니다.
    if len(sys.argv) != 2:
        print("<Usage>: ./emulator <program.txt>")
        exit(1)

    with open(sys.argv[1]) as f:
        # 텍스트 파일의 데이터를 전부 읽어오는 코드 입니다.
        # 이 부분은 for loop 등 기타 방법으로 변형해서 사용해도 됩니다.
        data = f.readlines() 

    # 이 부분은 예시로 제공된 코드입니다. 실제로 동작하지 않으니 동작하도록 수정해서 사용해야 합니다.
    cpu = SimpleCPU(NUM_REGS, MEM_SZ)
    cpu.execute(data)
    cpu.print_status()
