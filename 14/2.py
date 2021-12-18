import importlib.util

FILE = "input"
STEPS = 40

# Import all the code from part 1
spec = importlib.util.spec_from_file_location("1", "1.py")
part1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(part1)
main = part1.main

if __name__ == '__main__':
    print(main(STEPS))  # 3447389044530
