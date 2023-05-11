from matplotlib import transforms
import numpy as np
import sys
import os
import matplotlib.pyplot as plt

# print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
# print("PATH:", os.environ.get('PATH'))
# print(sys.path)
img_save_path = "D:\\PycharmProjects\\PYTEST\\fig\\" 


global_train_acc=np.random.random(10)
global_test_acc=np.random.random(10)

def show_acc_curv():
    # 训练准确率曲线的x、y
    train_x = list(range(len(global_train_acc)))
    train_y = global_train_acc

    # 测试准确率曲线的x、y
    # 每ratio个训练准确率对应一个测试准确率
    test_x = train_x
    test_y = global_test_acc

    plt.title('test')
    plt.plot(train_x, train_y, color='green', label='training accuracy')
    plt.plot(test_x, test_y, color='red', label='testing accuracy')
    plt.legend()
    plt.xlabel('iterations')
    plt.ylabel('accs')
    plt.savefig(img_save_path + 'acc_curv_' + '.jpg')
    plt.show()

if __name__ == '__main__':
    print(1/30)
    print(1//30)
    print(1%30)
    #show_acc_curv()#跑通

