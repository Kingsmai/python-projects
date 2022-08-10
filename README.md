# python-small-projects

> Python 版本：3.9.13

项目来源于 Ai Sweigart 的 《Python Big Book》一书。
 
## 项目 1

> 项目名称：bagels
> 
> 项目介绍：猜数字游戏，系统生成一个三位数，用户猜测，系统给出提示，猜对则胜利
> 
> 标签：short, game, puzzle

### 项目延申

- [ ] 通过修改 `NUM_DIGITS` 改变秘密数字的位数。
- [ ] 通过修改 `MAX_GUESSES` 改变玩家猜测的次数。
- [ ] 尝试创建一个版本，其中秘密数字包含字母和（或）数字。

### 项目探讨

- 当你改变 `NUM_DIGITS` 常量时会发生什么？
- 当你改变 `MAX_GUESSES` 常量时会发生什么？
- 如果你将 `NUM_DIGITS` 设置为大于 10 的数字会发生什么？
- 如果你将 `secretNum = getSecretNum()` 替换为 `secretNum = '123'`，会发生什么？
- 如果你删除或注释掉 `numGuesses = 1`，会发生什么？
- 如果你删除或注释掉 `random.shuffle(numbers)`，会发生什么？
- 如果你删除或注释掉 `if guess == secretNum:` 和 `return 'You got it!'`，会发生什么？
- 如果你注释掉 `numGuesses += 1`，会发生什么？

## 项目 2

> 项目名称：birthday paradox 生日悖论
> 
> 项目介绍：生日悖论是指在一个随机选择的人群中，有两个人生日相同的概率是多少
> 
> 标签：short, math, simulation

### 项目探讨

- 本程序中生日是如何表示的？（提示：查看第 10 行）
- 你如何删除程序生成的最大生日限制？
- 如果你删除或注释掉第 50 行的 `num_birthday = int(response)`，会发生什么？
- 你如何让程序显示完整的月份名称，例如 'January' 而不是 'Jan'？
- 你如何让 'X simulations run...' 每 1,000 次模拟出现一次，而不是每 10,000 次？

## 项目 3

> 项目名称：bitmap message 位图信息
> 
> 项目介绍：将一段文本转换为位图信息
> 
> 标签：tiny, beginner, artistic

### 项目探讨

- 如果玩家输入空字符串会发生什么？
- 非空字符在位图变量的字符串中是否有影响？
- 第 45 行创建的 `i` 变量代表什么？
- 如果删除或注释掉第 42 行的 `print()` 会发生什么？