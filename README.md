# Random Data Generate
随机数据生成器

## 依赖安装
```bash
pip install -r requirements.txt
```

## 数字
```python
import random

for _ in range(9):
    print('----------------------------------------------------------------')
    print('随机整数（min ～ max）：', random.randint(0, 9))
    print('随机整数（min ～ max，步进 step）', random.randrange(0, 100, 2))
    print('随机浮点数（0 ～ 1）：', random.random())
    print('随机浮点数（min ～ max）：', random.uniform(0, 9))

```

## 字符串
```python
import random
import string

letters = string.ascii_letters + string.digits

for _ in range(9):
    print('----------------------------------------------------------------')
    print('随机字符：', random.sample(letters, 10))
    print('随机字符串：', ''.join(random.choice(letters) for _ in range(10)))
    print('随机枚举值：', random.choice(letters))
    print('随机打乱：', ''.join(random.sample(letters, len(letters))))

```