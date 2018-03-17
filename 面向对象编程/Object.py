# 面向对象最重要的概念就是类(class)和实例(instance),必须牢记类是抽象的模版,比如Student类,而实例是根据类创建出来的一个个具体的对象,
# 每个对象都拥有相同的方法,但各自的数据可能不同.
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger(__name__)


class Student(object):
    def __init__(self, name, age):
        logging.info("对象构造方法")
        self.name = name
        self.age = age

    def info(self):
        print('姓名:', self.name, ',年龄:', self.age)

    def __info(self):
        print('内部属性,外部无法访问')


# chenhe = Student('陈贺', 21);
# chenhe.info()


class StudentA(Student):
    def __init__(self, name, age):
        print("子类构造方法")
        super.__init__(name, age)


studentA = Student('陈贺', 21);
studentA.info()
print(type(studentA))
