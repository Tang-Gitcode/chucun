# 测试序列化和反序列化的使用
import pickle

a1 = "唐展号豪"
a2 = 51121
a3 = [20, 30, 40]

with open(r"a.dat", "wb") as f:
    pickle.dump(a1, f)
    pickle.dump(a2, f)
    pickle.dump(a3, f)


with open(r"a.dat", "rb") as f:
    b1 = pickle.load(f)
    b2 = pickle.load(f)
    b3 = pickle.load(f)

    print(b1), print(b2), print(b3)

    print(id(a1)), print(id(b1))
