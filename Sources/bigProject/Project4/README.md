# 项目

> 项目名称：Blackjack 二十一点
>
> 项目介绍：二十一点游戏
>
> 标签：large, game, card game

## 项目概述

Blackjack，也称为二十一点，是一种纸牌游戏，玩家试图在不超过 21 点的情况下获得尽可能接近的点数。 该程序使用用文本字符绘制的图像，称为 ASCII 艺术。 美国信息交换标准代码 (ASCII) 是文本字符到 Unicode 取代它之前计算机使用的数字代码的映射。 这个程序中的扑克牌是 ASCII 艺术的一个例子：

```
 ___   ___
|A  | |10 |
| ♣ | | ♦ |
|__A| |_10|
```

## 运行画面

```
Blackjack, by Al Sweigart al@inventwithpython.com

    Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.
Money: 5000
How much do you bet? (1-5000, or QUIT)
> 400
Bet: 400

DEALER: ???
 ___   ___
|## | |2  |
|###| | ♥ |
|_##| |__2|

PLAYER: 17
 ___   ___
|K  | |7  |
| ♠ | | ♦ |
|__K| |__7|


(H)it, (S)tand, (D)ouble down
> h
You drew a 4 of ♦.
--snip--
DEALER: 18
 ___   ___   ___
|K  | |2  | |6  |
| ♦ | | ♥ | | ♠ |
|__K| |__2| |__6|

PLAYER: 21
 ___   ___   ___
|K  | |7  | |4  |
| ♠ | | ♦ | | ♦ |
|__K| |__7| |__4|

You won $400!
--snip—
```

## 工作原理

您的键盘上不存在纸牌符号，这就是我们调用 chr() 函数来创建它们的原因。 传递给 chr() 的整数称为 Unicode 代码点，它是根据 Unicode 标准标识字符的唯一编号。 Unicode 经常被误解。 然而，Ned Batchelder 的 2012 PyCon US 演讲“Pragmatic Unicode, or How Do I Stop the Pain?” 是对 Unicode 的精彩介绍，您可以在 https://youtu.be/sgHbC6udIqc/ 找到它。 附录 B 提供了可以在 Python 程序中使用的 Unicode 字符的完整列表。

## 项目延申

输入源代码并运行几次后，尝试对其进行实验性更改。 二十一点有几个您可以实施的自定义规则。 例如，如果前两张牌具有相同的价值，玩家可以将它们分成两只并分别下注。 此外，如果玩家的前两张牌获得“21 点”（黑桃 A 和黑色 J），玩家将赢得 10 比 1 的奖金。 您可以从 https://en.wikipedia.org/wiki/Blackjack 了解有关该游戏的更多信息。

## 项目探讨

- 你如何让玩家以不同的金额开始？
- 程序如何防止玩家下注超过他们拥有的金额？
- 程序如何表示一张单独的牌？
- 程序如何表示一手牌？
- 在行 197 上创建的 `rows` 列表中的每个字符串都代表什么？
- 如果你在行 148 上删除或注释掉 `random.shuffle(deck)`，会发生什么？
- 如果你在行 112 上将 `money -= bet` 改为 `money += bet` 会发生什么？
- 当在 `displayHands()` 函数中将 `showDealerHand` 设置为 `True` 时会发生什么？ 当它为 `False` 时会发生什么？