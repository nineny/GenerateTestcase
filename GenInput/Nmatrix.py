import random
import os
#โปรแกรมสุ่มเทสเคส สร้าง n แทนขนาดเมทริกซ์ จากนั้นสร้างเมทริกซ์ขนาด n x n
def generate_random_file(filename):
    # สุ่มค่า n เป็นขนาดเมทริกซ์ระหว่าง 1 และ 60
    n = random.randint(1, 60)
    
    # สร้างตารางขนาด n x n และเติมค่าสุ่มระหว่าง 1 ถึง 10000
    matrix = [[random.randint(1, 10**4) for _ in range(n)] for _ in range(n)]
    
    # สร้างไฟล์ใหม่และเขียนข้อมูล
    with open(filename, 'w') as file:
        # เขียนค่า m และ n ในบรรทัดแรก
        file.write(f"{n}\n")
        
        # เขียนค่าในตาราง
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')
    
    print(f"สร้างไฟล์ {filename} เสร็จสิ้น (n = {n})")
def main():
    #จำนวนเทสเคสที่ต้องการให้สร้าง
    a = 1
    b = 10
    
    # สร้างไฟล์ตั้งแต่ a ถึง b
    for i in range(a, b + 1):
        filename = f"{i:02d}.in"
        generate_random_file(filename)
    
    print(f"สร้างไฟล์เสร็จสิ้นทั้งหมด {b - a + 1} ไฟล์")
    print(f"ไฟล์ถูกสร้างที่: {os.path.abspath(os.curdir)}")

if __name__ == "__main__":
    main()
