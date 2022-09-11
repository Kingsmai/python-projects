from selenium import webdriver
from selenium.webdriver.common.by import By
import time

SUCCESS_MSG = "We've queued this item for an update! Check back in a minute..."

failed = [1, 5, 6, 7, 13, 19, 32, 34, 49, 58, 62, 76, 95, 105, 111, 112, 113, 115, 122, 128, 133, 135, 137, 143, 145, 148, 165, 167, 175, 181, 182, 187, 192, 196, 200, 206, 210, 215, 217, 226, 227, 228, 234, 238, 239, 240, 245, 249, 255, 257, 261, 268, 275, 278, 290, 293, 295, 297, 300, 311, 312, 314, 318, 320, 322, 326, 327, 334, 336, 338, 342, 347, 349, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1200, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229, 1230, 1231, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1240, 1241, 1242, 1243, 1244, 1245, 1246, 1247, 1248, 1249, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1258, 1259, 1260, 1261, 1262, 1263, 1264, 1265, 1266, 1267, 1268, 1269, 1270, 1271, 1272, 1273, 1274, 1275, 1276, 1277, 1278, 1279, 1280, 1281, 1282, 1283, 1284, 1285, 1286, 1287, 1288, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1315, 1316, 1317, 1318, 1319, 1320, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328, 1329, 1330, 1331, 1332, 1333, 1334, 1335, 1336, 1337, 1338, 1339, 1340, 1341, 1342, 1343, 1344, 1345, 1346, 1347, 1348, 1349, 1350, 1351, 1352, 1353, 1354, 1355, 1356, 1357, 1358, 1359, 1360, 1362, 1364, 1365, 1366, 1368, 1371, 1373, 1374, 1377, 1378, 1380, 1381, 1382, 1383, 1384, 1386, 1387, 1388, 1390, 1391, 1395, 1397, 1401, 1402, 1405, 1409, 1412, 1413, 1414, 1417, 1418, 1419, 1423, 1424, 1425, 1428, 1429, 1430, 1431, 1433, 1435, 1436, 1437, 1438, 1439, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1514, 1515, 1516, 1517, 1518, 1519, 1520, 1521, 1522, 1523, 1524, 1525, 1526, 1527, 1528, 1529, 1530, 1531, 1532, 1533, 1534, 1535, 1536, 1537, 1538, 1539, 1541, 1542, 1543, 1547, 1549, 1551, 1552, 1553, 1555, 1556, 1557, 1558, 1559, 1560, 1561, 1562, 1563, 1564, 1565, 1566, 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608, 1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644, 1645, 1646, 1647, 1648, 1649, 1650, 1651, 1652, 1653, 1654, 1655, 1656, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665, 1666, 1667, 1668, 1669, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1678, 1679, 1680, 1681, 1682, 1683, 1684, 1685, 1686, 1687, 1688, 1689, 1690, 1691, 1692, 1693, 1694, 1695, 1696, 1697, 1698, 1699, 1700, 1701, 1702, 1703, 1704, 1705, 1706, 1707, 1708, 1709, 1710, 1711, 1712, 1713, 1714, 1715, 1716, 1717, 1718, 1719, 1720, 1721, 1722, 1723, 1724, 1725, 1726, 1727, 1728, 1729, 1730, 1731, 1732, 1733, 1734, 1735, 1736, 1737, 1738, 1739, 1740, 1741, 1742, 1743, 1744, 1745, 1746, 1747, 1748, 1749, 1750, 1751, 1752, 1753, 1754, 1755, 1756, 1757, 1758, 1759, 1760, 1761, 1762, 1763, 1764, 1765, 1766, 1767, 1768, 1769, 1770, 1771, 1772, 1773, 1774, 1775, 1776, 1777, 1778, 1779, 1780, 1781, 1782, 1783, 1784, 1785, 1786, 1787, 1788, 1789, 1790, 1791, 1792, 1793, 1794, 1795, 1796, 1797, 1798, 1799, 1800, 1801, 1802, 1803, 1804, 1805, 1806, 1807, 1808, 1809, 1810, 1811, 1812, 1813, 1814, 1815, 1816, 1817, 1818, 1819, 1820, 1821, 1822, 1823, 1824, 1825, 1826, 1827, 1828, 1829, 1830, 1831, 1832, 1833, 1834, 1835, 1836, 1837, 1838, 1839, 1840, 1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848, 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859, 1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889, 1890, 1891, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070, 2071, 2073, 2074, 2075, 2076, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111, 2112, 2113, 2114, 2115, 2116, 2117, 2118, 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129, 2130, 2131, 2132, 2133, 2134, 2135, 2136, 2137, 2138, 2139, 2140, 2141, 2143, 2144, 2145, 2150, 2151, 2152, 2153, 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165, 2166, 2167, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2175, 2176, 2177, 2178, 2179, 2180, 2181, 2182, 2184, 2185, 2186, 2187, 2188, 2189, 2190, 2193, 2194, 2195, 2196, 2197, 2198, 2199, 2200, 2201, 2202, 2203, 2204, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2219, 2220, 2221, 2222, 2223, 2224, 2225, 2226, 2227, 2228, 2229, 2230, 2231, 2232, 2233, 2234, 2235, 2236, 2237, 2238, 2239, 2240, 2241, 2242, 2243, 2244, 2245, 2246, 2247, 2248, 2249, 2250, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259, 2260, 2261, 2262, 2263, 2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273, 2274, 2275, 2276, 2277, 2278, 2279, 2280, 2281, 2282, 2283, 2284, 2285, 2286, 2287, 2288, 2289, 2290, 2291, 2292, 2293, 2294, 2295, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2308, 2309, 2310, 2311, 2312, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320, 2321, 2322, 2323, 2324, 2325, 2326, 2327, 2328, 2329, 2330, 2331, 2332, 2333, 2334, 2335, 2336, 2337, 2338, 2339, 2340, 2341, 2342, 2343, 2344, 2345, 2346, 2347, 2348, 2349, 2350, 2351, 2352, 2353, 2354, 2355, 2356, 2357, 2358, 2359, 2360, 2361, 2362, 2363, 2364, 2365, 2366, 2367, 2368, 2369, 2370, 2371, 2372, 2373, 2374, 2375, 2376, 2377, 2378, 2379, 2380, 2381, 2382, 2383, 2384, 2387, 2388, 2389, 2390, 2391, 2392, 2393, 2394, 2396, 2397, 2398, 2400, 2401, 2402, 2404, 2405, 2408, 2410, 2411, 2412, 2413, 2415, 2416, 2417, 2420, 2421, 2422, 2423, 2424, 2426, 2431, 2432, 2435, 2437, 2439, 2440, 2441, 2443, 2445, 2446, 2451, 2452, 2453, 2455, 2457, 2459, 2460, 2461, 2464, 2466, 2467, 2468, 2470, 2471, 2472, 2473, 2475, 2476, 2477, 2478, 2479, 2480, 2481, 2482, 2483, 2484, 2485, 2486, 2487, 2488, 2489, 2490, 2493, 2494, 2495, 2500, 2502, 2505, 2506, 2507, 2508, 2509, 2510, 2511, 2513, 2515, 2516, 2518, 2519, 2520, 2521, 2525, 2526, 2527, 2528, 2529, 2534, 2536, 2537, 2538, 2540, 2545, 2549, 2552, 2553, 2557, 2558, 2559, 2562, 2563, 2564, 2565, 2567, 2568, 2569, 2571, 2575, 2576, 2577, 2579, 2582, 2583, 2585, 2586, 2587, 2588, 2589, 2590, 2592, 2593, 2594, 2596, 2597, 2599, 2600, 2601, 2602, 2603, 2604, 2605, 2606, 2607, 2608, 2610, 2611, 2612, 2614, 2615, 2618, 2619, 2621, 2622, 2626, 2627, 2628, 2630, 2631, 2632, 2634, 2635, 2636, 2637, 2638, 2639, 2641, 2643, 2644, 2646, 2647, 2648, 2649, 2650, 2651, 2652, 2653, 2654, 2655, 2657, 2659, 2660, 2662, 2663, 2664, 2668, 2670, 2672, 2673, 2677, 2678, 2679, 2680, 2681, 2682, 2683, 2684, 2685, 2686, 2687, 2689, 2692, 2693, 2695, 2697, 2699, 2706, 2708, 2709, 2710, 2712, 2713, 2715, 2716, 2717, 2718, 2719, 2720, 2721, 2722, 2723, 2724, 2725, 2726, 2727, 2728, 2729, 2730, 2731, 2732, 2733, 2734, 2735, 2736, 2737, 2738, 2739, 2740, 2741, 2742, 2743, 2744, 2745, 2746, 2747, 2748, 2749, 2750, 2751, 2752, 2753, 2754, 2755, 2756, 2757, 2758, 2759, 2760, 2761, 2762, 2763, 2764, 2765, 2766, 2767, 2768, 2769, 2770, 2771, 2772, 2773, 2774, 2775, 2776, 2777, 2778, 2779, 2780, 2781, 2782, 2783, 2784, 2785, 2786, 2787, 2788, 2789, 2792, 2795, 2801, 2803, 2804, 2805, 2810, 2811, 2812, 2813, 2815, 2816, 2818, 2819, 2821, 2822, 2826, 2829, 2831, 2832, 2833, 2835, 2839, 2841, 2843, 2844, 2848, 2854, 2858, 2859, 2862, 2871, 2875, 2876, 2877, 2880, 2887, 2892, 2893, 2894, 2896, 2897, 2899, 2904, 2908, 2913, 2916, 2917, 2918, 2919, 2921, 2922, 2927, 2930, 2931, 2932, 2933, 2934, 2935, 2936, 2937, 2938, 2939, 2940, 2941, 2943, 2944, 2945, 2946, 2947, 2948, 2949, 2950, 2951, 2952, 2953, 2955, 2956, 2957, 2958, 2959, 2960, 2961, 2962, 2963, 2964, 2965, 2966, 2967, 2968, 2969, 2970, 2971, 2972, 2973, 2974, 2975, 2976, 2977, 2978, 2979, 2980, 2981, 2982, 2983, 2984, 2985, 2986, 2987, 2988, 2989, 2990, 2991, 2992, 2993, 2994, 2995, 2996, 2997, 2998, 2999, 3000, 3001, 3002, 3003, 3004, 3005, 3006, 3007, 3008, 3009, 3010, 3011, 3012, 3013, 3014, 3015, 3016, 3017, 3018, 3019, 3020, 3021, 3022, 3023, 3024, 3025, 3026, 3027, 3028, 3029, 3030, 3031, 3032, 3033, 3034, 3035, 3036, 3037, 3038, 3039, 3040, 3041, 3042, 3043, 3044, 3045, 3047, 3048, 3049, 3050, 3051, 3052, 3053, 3054, 3055, 3056, 3057, 3058, 3059, 3060, 3061, 3062, 3063, 3064, 3065, 3066, 3067, 3068, 3069, 3070, 3071, 3072, 3073, 3074, 3075, 3076, 3077, 3078, 3079, 3080, 3081, 3082, 3083, 3084, 3085, 3086, 3087, 3088, 3089, 3090, 3091, 3092, 3093, 3094, 3095, 3096, 3097, 3098, 3099, 3100, 3101, 3102, 3103, 3104, 3105, 3106, 3107, 3108, 3109, 3110, 3111, 3112, 3113, 3114, 3115, 3116, 3117, 3118, 3119, 3120, 3121, 3122, 3123, 3124, 3125, 3126, 3127, 3128, 3129, 3130, 3131, 3132, 3133, 3134, 3135, 3136, 3137, 3138, 3139, 3140, 3141, 3142, 3143, 3144, 3145, 3146, 3147, 3148, 3149, 3150, 3151, 3152, 3153, 3154, 3155, 3156, 3157, 3158, 3159, 3160, 3161, 3162, 3163, 3164, 3165, 3166, 3167, 3168, 3169, 3170, 3171, 3172, 3173, 3174, 3175, 3176, 3177, 3178, 3179, 3180, 3181, 3182, 3183, 3184, 3185, 3186, 3187, 3188, 3190, 3191, 3192, 3193, 3194, 3195, 3198, 3199, 3200, 3202, 3204, 3205, 3206, 3207, 3209, 3211, 3212, 3215, 3216, 3217, 3218, 3221, 3222, 3226, 3227, 3228, 3230, 3234, 3236, 3238, 3242, 3243, 3245, 3247, 3249, 3251, 3259, 3260, 3261, 3265, 3266, 3268, 3270, 3271, 3272, 3276, 3278, 3284, 3285, 3287, 3288, 3292, 3295, 3298, 3299, 3300, 3305, 3308, 3317, 3318, 3320, 3322, 3324, 3326, 3327, 3328, 3329, 3330, 3335, 3341, 3344, 3346, 3347, 3349, 3353, 3356, 3363, 3365, 3367, 3370, 3372, 3379, 3380, 3381, 3384, 3385, 3386, 3392, 3398, 3401, 3403, 3404, 3406, 3407, 3409, 3411, 3412, 3413, 3415, 3417, 3420, 3422, 3426, 3428, 3432, 3436, 3437, 3444, 3453, 3457, 3458, 3465, 3467, 3471, 3480, 3481, 3484, 3486, 3487, 3489, 3490, 3491, 3492, 3505, 3510, 3512, 3514, 3515, 3518, 3520, 3525, 3529, 3542, 3547, 3556, 3561, 3562, 3563, 3568, 3571, 3577, 3582, 3583, 3584, 3592, 3600, 3604, 3609, 3624, 3625, 3631, 3638, 3642, 3645, 3646, 3648, 3649, 3658, 3665, 3673, 3678, 3680, 3681, 3696, 3698, 3699, 3701, 3704, 3705, 3714, 3716, 3722, 3724, 3730, 3731, 3745, 3746, 3747, 3749, 3754, 3761, 3763, 3773, 3780, 3782, 3788, 3790, 3792, 3806, 3814, 3818, 3831, 3832, 3842, 3843, 3844, 3847, 3854, 3869, 3874, 3880, 3893, 3905, 3910, 3911, 3912, 3927, 3929, 3930, 3931, 3932, 3937, 3938, 3941, 3949, 3951, 3956, 3959, 3965, 3972, 3973, 3976, 3983, 3987, 3991, 4001, 4003, 4015, 4020, 4024, 4025, 4030, 4038, 4040, 4046, 4047, 4048, 4051, 4052, 4054, 4057, 4060, 4074, 4084, 4085, 4088, 4094, 4096, 4099, 4102, 4128, 4132, 4133, 4138, 4139, 4140, 4145, 4152, 4156, 4169, 4181, 4183, 4189, 4193, 4195, 4206, 4215, 4220, 4224, 4228, 4231, 4237, 4242, 4244, 4246, 4247, 4254, 4259, 4275, 4276, 4281, 4287, 4292, 4302, 4318, 4319, 4329, 4331, 4334, 4339, 4341, 4348, 4359, 4364, 4377, 4398, 4403, 4407, 4410, 4415, 4416, 4421, 4437, 4439, 4455, 4464, 4498, 4513, 4532, 4537, 4544, 4549, 4567, 4589, 4593, 4604, 4608, 4615, 4620, 4624, 4639, 4644, 4664, 4668, 4671, 4693, 4703, 4706, 4719, 4721, 4729, 4730, 4749, 4757, 4763, 4772, 4790, 4794, 4795, 4797, 4800, 4801, 4805, 4811, 4819, 4827, 4831, 4836, 4845, 4850, 4868, 4888, 4901, 4906, 4908, 4911, 4914, 4925, 4936, 4937, 4942, 4951, 4969, 4986, 5012, 5016, 5017, 5025, 5044, 5061, 5071, 5075, 5086, 5088, 5096, 5113, 5121, 5128, 5130, 5135, 5144, 5145, 5148, 5152, 5163, 5169, 5176, 5182, 5187, 5197, 5204, 5205, 5213, 5215, 5226, 5240, 5242, 5250, 5258, 5275, 5287, 5294, 5296, 5305, 5312, 5313, 5326, 5336, 5340, 5354, 5370, 5374, 5380, 5385, 5387, 5393, 5399, 5401, 5403, 5413, 5430, 5434, 5445, 5469, 5476, 5486, 5487, 5507, 5511, 5513, 5515, 5538, 5587, 5589, 5592, 5606, 5610, 5618, 5644, 5648, 5652, 5661, 5671, 5685, 5699, 5724, 5763, 5766, 5776, 5780, 5784, 5788, 5795, 5798, 5806, 5811, 5815, 5819, 5838, 5852, 5856, 5865, 5868, 5879, 5885, 5890, 5902, 5909, 5919, 5927, 5948, 5951, 5959, 5960, 5972, 5975, 5989, 5998, 6000, 6004, 6011, 6013, 6017, 6035, 6057, 6061, 6073, 6075, 6090, 6093, 6105, 6131, 6141, 6158, 6176, 6180, 6187, 6194, 6207, 6208, 6211, 6213, 6219, 6246, 6248, 6271, 6275, 6279, 6284, 6297, 6303, 6308, 6313, 6326, 6328, 6332, 6337, 6342, 6377, 6395, 6411, 6421, 6422, 6424, 6446, 6456, 6476, 6480, 6489, 6506, 6510, 6539, 6541, 6542, 6556, 6561, 6565, 6579, 6590, 6602, 6616, 6617, 6622, 6623, 6626, 6630, 6639, 6644, 6677, 6681, 6686, 6695, 6712, 6717, 6724, 6735, 6739, 6744, 6748, 6753, 6763, 6779, 6780, 6782, 6783, 6785, 6786, 6790, 6791, 6792, 6793, 6794, 6795, 6798, 6799, 6802, 6803, 6805, 6806, 6807, 6808, 6809, 6810, 6811, 6813, 6814, 6815, 6817, 6818, 6822, 6823, 6837, 6842, 6846, 6848, 6855, 6863, 6870, 6880, 6882, 6886, 6888, 6926, 6975, 6980, 6982, 6987, 6992, 7001, 7006, 7007, 7010, 7029, 7033, 7034, 7038, 7051, 7070, 7082, 7087, 7096, 7099, 7103, 7108, 7111, 7148, 7169, 7171, 7172, 7173, 7174, 7185, 7187, 7195, 7196, 7204, 7207, 7212, 7216, 7257, 7267, 7270, 7276, 7279, 7304, 7307, 7312, 7314, 7316, 7331, 7335, 7340, 7360, 7373, 7374, 7378, 7382, 7383, 7403, 7406, 7424, 7425, 7433, 7442, 7447, 7460, 7463, 7470, 7478, 7505, 7532, 7536, 7571, 7575, 7587, 7598, 7611, 7613, 7617, 7618, 7621, 7625, 7629, 7638, 7641, 7645, 7660, 7677, 7702, 7707, 7708, 7711, 7722, 7727, 7745, 7747, 7771, 7773, 7787, 7796, 7803, 7806, 7822, 7825, 7838, 7842, 7851, 7855, 7859, 7862, 7865, 7866, 7867, 7868, 7876, 7877, 7882, 7893, 7894, 7895, 7910, 7941, 7946, 7949, 7950, 7962, 7968, 7974, 7981, 7982, 7983, 7987, 7993, 7999, 8003, 8024, 8039, 8043, 8046, 8048, 8066, 8071, 8092, 8096, 8097, 8126, 8151, 8156, 8158, 8160, 8162, 8164, 8173, 8178, 8182, 8194, 8207, 8220, 8228, 8233, 8236, 8251, 8255, 8269, 8279, 8305, 8323, 8335, 8340, 8342, 8349, 8373, 8380, 8385, 8405, 8410, 8415, 8416, 8418, 8425, 8446, 8450, 8460, 8490, 8491, 8496, 8506, 8510, 8543, 8548, 8563, 8570, 8572, 8574, 8578, 8582, 8583, 8586, 8590, 8594, 8609, 8614, 8624, 8629, 8631, 8636, 8639, 8644, 8645, 8648, 8653, 8655, 8657, 8674, 8680, 8683, 8700, 8704, 8713, 8717, 8721, 8724, 8729, 8733, 8760, 8769, 8770, 8793, 8804, 8808, 8819, 8826, 8835, 8865]
failed_no = []

try:
    driver = webdriver.Firefox()
    start_time = time.time()
    # for i in range(0, 8888):
    for index, i in enumerate(failed):
        url = f"https://opensea.io/assets/matic/0xe63b8e3fc67af4afa4022e2b28e3d7761ac8f74f/{i}"
        try:
            driver.get(url)
            btn = driver.find_element(By.CSS_SELECTOR, "button.sc-1xf18x6-0.sc-glfma3-0.hiIVBZ.gVeaIW.sc-1skvztv-0.fPnOUC:nth-child(1)")
            btn.click()
            time.sleep(0.2)
            msg = driver.find_element(By.CSS_SELECTOR, "#__next > div.sc-1xf18x6-0.sc-1twd32i-0.sc-ihijgw-0.haVRLx.kKpYwv.gpOOSX > div > div.sc-1xf18x6-0.sc-1twd32i-0.iQOhGx.kKpYwv")
            if msg.text != SUCCESS_MSG:
                failed_no.append(i)
        except:
            failed_no.append(i)
        finally:
            current_time = time.time()
            estimateTime = round(((current_time - start_time) / (i + 1) * (len(failed) - index)) / 60, 2)
            print(f"Processing: {url}, estimate time: {estimateTime}mins")
            time.sleep(0.8)
except:
    try:
        driver.close()
    finally:
        print("Browser Closed!")   
finally:
    success = True
    print(f'Operation {"SUCCESS" if success else "FAILED"} in {current_time - start_time} seconds')
    print(f'FAILED NFTs => {failed_no}')