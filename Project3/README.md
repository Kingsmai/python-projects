# 项目 3

> 项目名称：bitmap message 位图信息
> 
> 项目介绍：将一段文本转换为位图信息
> 
> 标签：tiny, beginner, artistic

## 项目概述

该程序使用多行字符串作为位图，即每个像素只有两种可能颜色的 2D 图像，以确定它应该如何显示来自用户的消息。 在这个位图中，空格字符代表一个空白空间，所有其他字符都被用户消息中的字符替换。 提供的位图类似于世界地图，但您可以将其更改为您想要的任何图像。 空格或消息字符系统的二进制简单性使其非常适合初学者。 尝试尝试不同的消息，看看结果如何！

## 运行画面

```
Bitmap Message, by Al Sweigart al@inventwithpython.com
Enter the message to display with the bitmap.
> Hello!

Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!He
   lo!Hello!Hello   l  !He lo  e      llo!Hello!Hello!Hello!Hello!He
  llo!Hello!Hello!Hello He lo H  l !Hello!Hello!Hello!Hello!Hello H
 el      lo!Hello!Hello!He       lo!Hello!Hello!Hello!Hello!Hel
          o!Hello!Hello          lo  e lo!H ll !Hello!Hello!H l
           !Hello!He            llo!Hel   Hello!Hello!Hell ! e
            Hello!He           ello!Hello!Hello!Hello!Hell  H
   l        H llo! ell         ello!Hello!Hell !Hello  el o
               lo!H  l         ello!Hello!Hell   ell !He  o
                 !Hello         llo!Hello!Hel    el   He  o
                 !Hello!H        lo!Hello!Hell    l  !H llo
                   ello!Hel         Hello!He          H llo Hell
                   ello!Hell         ello!H  l        Hell !H l o!
                   ello!Hell         ello!H l o           o!H l   H
                     lo!Hel          ello! el             o!Hel   H
                     lo!He            llo! e            llo!Hell
                    llo!H             llo!              llo!Hello
                    llo!              ll                 lo!Hell   e
                    llo                                       l    e
                    ll     l                    H
Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!Hello!He
```

## 工作原理

Instead of individually typing each character of the world map pattern, you can copy and paste the whole thing from https://inventwithpython.com/bitmapworld.txt. A line of 68 periods at the top and bottom of the pattern acts as a ruler to help you align it correctly. However, the program will still work if you make typos in the pattern.

The `bitmap.splitlines()` method call on line 43 returns a list of strings, each of which is a line in the multiline bitmap string. Using a multiline string makes the bitmap easier to edit into whatever pattern you like. The program fills in any non-space character in the pattern, which is why asterisks, periods, or any other character do the same thing.

The `message[i % len(message)]` code on line 51 causes the repetition of the text in `message`. As i increases from 0 to a number larger than `len(message)`, the expression `i % len(message)` evaluates to `0` again. This causes `message[i % len(message)]` to repeat the characters in `message` as `i` increases.

## 项目探讨

- 如果玩家输入空字符串会发生什么？
- 非空字符在位图变量的字符串中是否有影响？
- 第 45 行创建的 `i` 变量代表什么？
- 如果删除或注释掉第 42 行的 `print()` 会发生什么？