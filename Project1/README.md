# 项目 1

> 项目名称：bagels
> 
> 项目介绍：猜数字游戏，系统生成一个三位数，用户猜测，系统给出提示，猜对则胜利
> 
> 标签：short, game, puzzle

## 项目延申

- [ ] 通过修改 `NUM_DIGITS` 改变秘密数字的位数。
- [ ] 通过修改 `MAX_GUESSES` 改变玩家猜测的次数。
- [ ] 尝试创建一个版本，其中秘密数字包含字母和（或）数字。

## 项目探讨

- 当你改变 `NUM_DIGITS` 常量时会发生什么？
- 当你改变 `MAX_GUESSES` 常量时会发生什么？
- 如果你将 `NUM_DIGITS` 设置为大于 10 的数字会发生什么？
- 如果你将 `secretNum = getSecretNum()` 替换为 `secretNum = '123'`，会发生什么？
- 如果你删除或注释掉 `numGuesses = 1`，会发生什么？
- 如果你删除或注释掉 `random.shuffle(numbers)`，会发生什么？
- 如果你删除或注释掉 `if guess == secretNum:` 和 `return 'You got it!'`，会发生什么？
- 如果你注释掉 `numGuesses += 1`，会发生什么？