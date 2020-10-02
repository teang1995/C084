import sys


# <Exception 이름> | IP:<Exception을 발생시킨 명령어의 IP | <명령어> | <에러를 발생시킨 인덱스> | 0, <익덱스의 범위>
class SimpleCPUREGIndexError(Exception):
    def __init__(self, ip, process, invalid_idx, max_reg_idx):
        self.ip = ip
        self.process = process
        self.invalid_idx = invalid_idx
        self.max_reg_idx = max_reg_idx

    def __str__(self):
        return "SimpleCPU_REGIndexError | IP:{} | {} | {} | 0, {}"\
            .format(self.ip, self.process, self.invalid_idx, self.max_reg_idx)


class SimpleCPUIPIndexError(Exception):
    def __init__(self, ip, process, invalid_ip, max_ip):
        self.ip = ip
        self.process = process
        self.invalid_ip = invalid_ip
        self.max_ip = max_ip

    def __str__(self):
        return "SimpleCPUIPIndexError | IP:{} | {} | {} | 0, {}"\
            .format(self.ip, self.process, self.invalid_ip, self.max_ip)


class SimpleCPUMEMIndexError(Exception):
    def __init__(self, ip, process, invalid_idx, max_mem_idx):
        self.ip = ip
        self.process = process
        self.invalid_idx = invalid_idx
        self.max_mem_idx = max_mem_idx

    def __str__(self):
        return "SimpleCPUMEMIndexError | IP:{} | {} | {} | 0, {}"\
            .format(self.ip, self.process, self.invalid_idx, self.max_mem_idx)


class SimpleCPUCmdError(Exception):
    def __init__(self, func):
        self.func = func

    def __str__(self):
        return "SimpleCPUCmdError : There is no command named {}".format(self.func)


class SimpleCPU:
    '''
        SimpleCPU 모듈
        레지스터 크기 num_regs 와 mem_size 값을 받는다.
    '''
    def __init__(self, num_regs, mem_size):
        self.ip = 0
        self.num_regs = num_regs
        self.mem_size = mem_size
        self.max_ip = 0
        self.registers = [0 for _ in range(num_regs)]  # for saving data at register
        self.memory = [0 for _ in range(mem_size)]  # for saving data at memory
        self.cal_cmd_dict = {"add": self.add, "sub": self.sub, "div":self.div, "mul": self.mul}
        self.mem_cmd_dict = {"ld": self.ld, "st": self.st}
        self.bnc_cmd_dict = {"jump" : self.jump, "beq": self.beq, "ble": self.ble, "bne": self.bne}

    def process_line(self, process):
        split_list = process.replace("$", "").split(" ")
        func = split_list[0]
        try:
            if func in self.mem_cmd_dict:
                self.ip += 1
                idx1 = int(split_list[1])
                idx2 = int(split_list[2])
                if idx1 < 0 or idx1 >= self.num_regs:
                    raise SimpleCPUREGIndexError(self.ip, process, idx1, self.num_regs - 1)
                if idx2 < 0 or idx2 >= self.mem_size:
                    raise SimpleCPUMEMIndexError(self.ip, process, idx2, self.mem_size - 1)
                self.mem_cmd_dict[func](idx1, idx2)

            elif func in self.cal_cmd_dict:
                self.ip += 1
                dst = int(split_list[1])
                if dst > self.num_regs or dst < 0:
                    raise SimpleCPUREGIndexError(self.ip, process, dst, self.num_regs - 1)
                src1 = int(split_list[2])
                if src1 > self.num_regs or src1 < 0:
                    raise SimpleCPUREGIndexError(self.ip, process, src1, self.num_regs - 1)
                src2 = int(split_list[3])
                if src2 > self.num_regs or src2 < 0:
                    raise SimpleCPUREGIndexError(self.ip, process, src2, self.num_regs - 1)
                self.cal_cmd_dict[split_list[0]](dst, src1, src2)

            elif func in self.bnc_cmd_dict:
                self.ip += 1
                if func == "jump":
                    dst = int(split_list[1])
                    if dst < 0 or dst >= self.max_ip:
                        raise SimpleCPUIPIndexError(self.ip, process, dst, self.max_ip)
                    self.jump(dst)
                else:
                    src1 = int(split_list[1])
                    if src1 < 0 or src1 > self.num_regs:
                        raise SimpleCPUREGIndexError(self.ip, process, src1, self.num_regs - 1)
                    src2 = int(split_list[2])
                    if src2 < 0 or src2 > self.num_regs:
                        raise SimpleCPUREGIndexError(self.ip, process, src2, self.num_regs - 1)
                    dst = int(split_list[3])
                    if dst < 0 or dst >= self.max_ip:
                        raise SimpleCPUIPIndexError(self.ip, process, dst, self.max_ip)
                    self.bnc_cmd_dict[func](src1, src2, dst)

            else:
                raise SimpleCPUCmdError(func)

        except Exception as e:
            print(e)
            quit()

    def execute(self, program):
        memory = eval(program[0].replace("\n", ""))  # eval 안 쓰는 게 좋은데 다른 방법 찾기.
        self.memory = memory
        programs = []
        for process in program[1:]:
            process = process.replace("\n", "")
            process = process.replace(",", "")
            programs.append(process)
        self.max_ip = len(programs) - 1
        # print(programs)  # DEBUG
        while True:
            if self.ip == len(programs) - 1:
                self.process_line(programs[self.ip])
                break
            else:
                self.process_line(programs[self.ip])

    def ld(self, dst, src):
        self.registers[dst] = self.memory[src]

    def st(self, src, dst):
        self.memory[dst] = self.registers[src]

    def add(self, dst, src1, src2):
        # registers[dst] = registers[src1] + registers[src2]
        self.registers[dst] = self.registers[src1] + self.registers[src2]

    def sub(self, dst, src1, src2):
        # registers[dst] = registers[src1] - registers[src2]
        self.registers[dst] = self.registers[src1] - self.registers[src2]

    def div(self, dst, src1, src2):
        # registers[dst] = registers[src1] / registers[src2]
        try:
            if self.registers[src2] == 0:
                raise ZeroDivisionError
            self.registers[dst] = self.registers[src1] / self.registers[src2]
        except Exception as e:
            print(e)

    def mul(self, dst, src1, src2):
        # registers[dst] = registers[src1] * registers[src2]
        self.registers[dst] = self.registers[src1] * self.registers[src2]

    def jump(self, idx):
        # ip <- idx
        # 인덱스 오류 처리 필요
        self.ip = idx

    def beq(self, src1, src2, idx):
        # if src1 == src2 then ip <- idx
        if self.registers[src1] == self.registers[src2]:
            self.ip = idx

    def ble(self, src1, src2, idx):
        # if registers[src1] <= registers[src2] then ip <- idx
        if self.registers[src1] <= self.registers[src2]:
            self.ip = idx

    def bne(self, src1, src2, idx):
        # if registers[src1] != registers[src2] then ip <- idx
        if self.registers[src1] != self.registers[src2]:
            self.ip = idx

    def print_status(self):
        print("IP : {}".format(self.ip))
        print("Register File : ")
        for i, register in enumerate(self.registers):
            print("${} : {}".format(i, register))
        print("Memory : ")
        for i, mem in enumerate(self.memory):
            print("[{}] : {}".format(i, mem))


NUM_REGS = 5
MEM_SZ = 10

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("<Usage>: ./emulator <program.txt>")
        exit(1)

    with open(sys.argv[1]) as f:
        data = f.readlines()

    cpu = SimpleCPU(NUM_REGS, MEM_SZ)
    cpu.execute(data)
    cpu.print_status()
