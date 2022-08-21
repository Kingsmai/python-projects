# 项目 2

> 项目名称：birthday paradox 生日悖论
> 
> 项目介绍：生日悖论是指在一个随机选择的人群中，有两个人生日相同的概率是多少
> 
> 标签：short, math, simulation

## 项目概述

生日悖论，也称为生日问题，是即使在一小群人中，两个人生日相同的概率也非常高。 在一组 70 人中，有 99.9% 的机会有两个人的生日相同。 但即使在一个只有 23 人的小团体中，也有 50% 的机会匹配生日。 这个程序执行几个概率实验来确定不同大小组的百分比。 我们将这些类型的实验称为蒙特卡罗实验 (Monte Carlo experiments)，在这些实验中，我们进行了多次随机试验以了解可能的结果。

您可以在 https://en.wikipedia.org/wiki/Birthday_problem 找到有关生日悖论的更多信息。

## 运行画面

```
Birthday Paradox, by Al Sweigart al@inventwithpython.com
--snip--
How many birthdays shall I generate? (Max 100)
> 23
Here are 23 birthdays:
Oct 9, Sep 1, May 28, Jul 29, Feb 17, Jan 8, Aug 18, Feb 19, Dec 1, Jan 22,
May 16, Sep 25, Oct 6, May 6, May 26, Oct 11, Dec 19, Jun 28, Jul 29, Dec 6,
Nov 26, Aug 18, Mar 18
In this simulation, multiple people have a birthday on Jul 29
Generating 23 random birthdays 100,000 times...
Press Enter to begin...
Let's run another 100,000 simulations.
0 simulations run...
10000 simulations run...
--snip--
90000 simulations run...
100000 simulations run.
Out of 100,000 simulations of 23 people, there was a
matching birthday in that group 50955 times. This means
that 23 people have a 50.95 % chance of
having a matching birthday in their group.
That's probably more than you would think!
```

## 工作原理

运行 100,000 次模拟可能需要一段时间，这就是第 95 和 96 行报告另外 10,000 次模拟已完成的原因。 此反馈可以向用户保证程序没有冻结。 请注意，某些整数，例如第 95 行的 `10_000` 和第 93 和 103 行的 `100_000`，都有下划线。 这些下划线没有特殊含义，但 Python 允许使用它们，以便程序员可以使整数值更易于阅读。 换句话说，从 `100_000` 读取“十万”比从 `100000` 读取“十万”更容易。

## 项目探讨

- 本程序中生日是如何表示的？（提示：查看第 10 行）
- 你如何删除程序生成的最大生日限制？
- 如果你删除或注释掉第 50 行的 `num_birthday = int(response)`，会发生什么？
- 你如何让程序显示完整的月份名称，例如 'January' 而不是 'Jan'？
- 你如何让 'X simulations run...' 每 1,000 次模拟出现一次，而不是每 10,000 次？
