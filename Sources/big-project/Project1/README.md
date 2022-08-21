# 项目 1

> 项目名称：bagels
>
> 项目介绍：猜数字游戏，系统生成一个三位数，用户猜测，系统给出提示，猜对则胜利
>
> 标签：short, game, puzzle

## 项目概述

在逻辑游戏 Bagels 中，您必须根据线索猜出一个秘密的三位数字。

游戏会根据您的猜测提供以下提示之一：

- “Pico”表示您的猜测在错误的位置有一个正确的数字，
- “Fermi”表示您的猜测在正确的位置有一个正确的数字，
- “Bagels”如果您的 猜测没有正确的数字。

您有 10 次机会猜测密码。

## 运行画面

```
Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.
Guess #1:
> 123
Pico
Guess #2:
> 456
Bagels
Guess #3:
> 178
Pico Pico
--snip--
Guess #7:
> 791
Fermi Fermi
Guess #8:
> 701
You got it!
Do you want to play again? (yes or no)
> no
Thanks for playing!
```

## 工作原理

请记住，该程序不使用整数值，而是使用包含数字的字符串值。 例如，`'426'` 是与 `426` 不同的值。我们需要这样做，因为我们正在执行与秘密数字的字符串比较，而不是数学运算。 请记住，`"0"`可以是前导数字：字符串`"026"`与`"26"`不同，但整数 `026` 与 `26` 相同。

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
