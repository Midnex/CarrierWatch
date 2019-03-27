# scratch paper

from datetime import datetime
from datetime import date
from calendar import monthrange

table = ((1,'January'),(2,'February'),(3,'March'),(4,'April'),(5,'May'),(6,'June'),(7,'July'),(8,'August'),(9,'September'),(0,'October'))

list = ['2375364', '1749223', '2454144', '2307839', '2362126', '2021600', '659526', '1400003', '2377096', '1243946', '1460227', '2469063', '2875802', '2057864', '2631703', '2079126', '503104', '124860', '2963686', '2965681', '2474551', '1866639', '2627898', '2267218', '1580734', '1733082', '2093129', '2843881', '1843536', '1995418', '1460728', '2841091', '1502769', '2250349', '2446965', '1995444', '2316314', '2964734', '2177299', '2119348', '1264210', '1204798', '1991458', '2083725', '974209', '2514282', '2376141', '1334430', '2436919', '2426155', '2387697', '1718638', '1164136', '2076277', '1401150', '2431692', '2377306', '1349221', '1557130', '2291589', '2009867', '1758605', '1327266', '905569', '1589532', '3115440', '1836422', '652762', '3093786', '2099831', '1026634', '1286888', '1958419', '2557431', '2847621', '2363868', '2464242', '2568411', '2575446', '2576430', '2056255', '1537210', '2156343', '1124806', '2140326', '2032488', '2890049', '2173739', '2310631', '2453206', '2469011', '2577581', '1855225', '1998214', '1009857', '1503347', '2430811', '2022232', '1317472', '2373560', '2471713', '2572007', '674045', '1016698', '2378104', '3077818', '2474489', '1510403', '2580906', '2109199', '1843012', '1911520', '2857256', '2177518', '2254336', '2475440', '2819570', '2152445', '2913105', '2090271', '2475713', '2502994', '1880266', '2110697', '2111812', '86317', '183949', '173800', '541583', '250379', '225540', '1598342', '519476', '142962', '1002334', '420088', '316754', '1465714', '335555', '2858208', '2270729', '896370', '1421882', '836858', '1359005', '2257865', '264184', '62227', '2322983', '292920', '1386339', '2460755', '791960', '186375', '945634', '527894', '318756', '1190646', '2847254', '2427598', '1992743', '915648', '1981739', '189250', '1158910', '1764248', '851339', '452417', '75250', '2255822', '708936', '2363617', '2471401', '1520385', '1780612', '1633579', '535932', '326335', '1633068', '229132', '798287', '71821', '342250', '1456111', '2152220', '2271761', '2332780', '2382463', '700999', '2572325', '1844779', '2005216', '2120102', '673488', '282721', '585115', '462173', '767997', '793730', '853373', '3101132', '1021713', '1033522', '1176136', '1470023', '1582731', '1704272', '1761786', '1839667', '808339', '2568463', '1788545', '1976998', '2846724', '900137', '1312259', '1443372', '1548300', '297785', '2100688', '2097460', '2485859', '2792074', '2568641', '2197943', '2340662', '2833789', '1158816', '1590119', '2279497', '2349620', '1933966', '2251609', '3096255', '2281684', '2016502', '2372798', '2263549', '2576543', '2474744', '2290989', '869047', '1607161', '2477345', '2468577', '2924678', '2918859', '1995650', '3103484', '1527352', '2788706', '1991081', '1873117', '1357611', '2458804', '2548442', '2371019', '2375576', '2370470', '2586034', '1805413', '2259804', '2061730', '1561500', '2441417', '1327315', '2460406', '2395887', '2475455', '2627049', '1469099', '678899', '1508344', '1546600', '1859989', '2473365', '2958807', '2123363', '2450712', '2487330', '1302563', '2073556', '2296115', '2470819', '2596550', '699924', '515980', '600862', '1153974', '2006567', '1450565', '1922154', '2843523', '2033380', '2382834', '2828543', '1962554', '3092361', '1299469', '1613468', '1683159', '1313980', '2914147', '2568210', '1459789', '1680133', '2465617', '2275054', '2968258', '2560398', '2426130', '2476164', '2573193', '2586882', '2474430', '2589390', '2345587', '2860241', '2381085', '859199', '1375361', '1546529', '1847291', '2542559', '2125529', '2857968', '2167597', '1858714', '1737910', '809972', '2282525', '2581055', '2380014', '2422064', '2478805', '337272', '2258314', '2314248', '2854677', '1170043', '1828933', '2926977', '2819346', '1346818', '465188', '245896', '2496546', '1717105', '807083', '188929', '1120756', '1423780', '2133912', '2799602', '634404', '2509773', '995622', '2543260', '1302053', '2008349', '2843595', '2464708', '2476248', '1244872', '1956060', '2840800', '1160468', '1745228', '1356022', '1940456', '2982458', '1497016', '1029808', '2158611', '2588231', '1102762', '2386522', '2517261', '2388088', '2445078', '2372148', '2390282', '2389018', '2828509', '2436320', '685077', '2490984', '1654035', '2856912', '2388212', '2418314', '858274', '1332114', '2184394', '90849', '2393479', '2152128', '1813530', '293250', '466144', '263813', '1283118', '1775733', '1345451', '1934741', '2836242', '295027', '2159714', '572464', '2937130', '1850056', '1998297', '2126893', '286764', '908382', '1728782', '1837119', '1223016', '728630', '242534', '118022', '609150', '185732', '204837', '248002', '1834223', '1317606', '86734', '1691419', '1428405', '22520', '36684', '1479588', '565021', '859207', '1055718', '603523', '1328967', '1345616', '1701515', '864736', '2461558', '322235', '2355934', '304876', '1476928', '449018', '528760', '467063', '71811', '1053464', '1267279', '169319', '2404524', '1834637', '1194542', '1362468', '1930689', '2286341', '2341009', '1859050', '2489677', '1844537', '1905557', '1164020', '2126609', '236453', '116690', '8329', '9853', '184230', '192981', '204961', '226073', '707347', '329494', '434099', '707733', '730107', '1238808', '926654', '1021626', '1134220', '1172513', '1257876', '1292700', '1390536', '1462593', '1604948', '1505243', '2137425', '2121064', '1646419', '2526979', '1463226', '1469183', '2263088', '2439500', '2941054', '2379061', '2513655', '2127913', '1240880', '1759025', '534056', '2634384', '2192670', '2542992', '478807', '957179', '1249652', '1471436', '2572744', '1473595', '1430510', '2171423', '2099850', '1360463', '2485828', '2288195', '2830503', '2102548', '2192698', '2491265', '2273379', '2839595', '1831879', '2464491', '1612556', '2480971', '1624728', '2022172', '2173244', '1592536', '2484779', '2485062', '2487394', '1812958', '31120', '1467507', '1107551', '2995146', '2926921', '2284051', '2487450', '1963789', '2006072', '2292170', '2126444', '2921463', '1477005', '2287307', '2473068', '2485436', '2117041', '1662728', '1669630', '1488512', '387872', '2565598', '2379727', '2404549', '2489167', '2643616', '3117632', '823614', '2491486', '2555452', '2005898', '1610595', '968652', '2867232', '2529425', '2826486', '230066', '1525151', '1585968', '2139122', '2576211', '1556931', '1913243', '1182092', '685886', '2258142', '1145145', '1866840', '2389803', '1870762', '3090624', '1734448', '1466429', '2956210', '2990651', '2254459', '1858036', '2386122', '2036504', '2834333', '2490026', '863843', '3001251', '1369348', '2185061', '2859643', '1636172', '2380340', '2392285', '2861091', '2920779', '969319', '2276984', '1720747', '2597074', '1537994', '2138808', '3106844', '2569505', '1311523', '1353002', '2546445', '2575652', '3002125', '1781261', '1932716', '2276021', '2492567', '870226', '1494056', '1752236', '1760277', '2364972', '2497672', '2365847', '1750679', '2382522', '1401341', '3087693', '2593468', '1787374', '2531626', '2098522', '1441340', '2291286', '2493503', '2538099', '1874170', '2139129', '2016926', '2438425', '1488746', '1847472', '1062242', '1870255', '2044083', '253988', '1489263', '1559900', '1838396', '2026586', '1930743', '2020945', '914841', '1726851', '2351386', '2455109', '2916923', '2850126', '2111991', '2579162', '1333754', '1264226', '1726970', '1762874', '366855', '1883652', '2014839', '1564592', '691117', '1943083', '2364682', '690147', '520645', '2288564', '1836165', '292991', '2071995', '569618', '183667', '2029256', '125563', '1771161', '1581602', '606920', '241572', '2057593', '2962067', '122275', '214440', '637350', '2130352', '363340', '2386867', '594314', '2492649', '1747093', '299015', '2393255', '154712', '1871881', '733', '1073995', '1453177', '841776', '1890957', '969177', '1180819', '1190102', '1375756', '1807687', '561272', '1818437', '2867445', '2327057', '430285', '2039891', '2395901', '2497722', '2587370', '1850355', '1939802', '1987947', '960874', '77949', '30925', '3118625', '121018', '55787', '247552', '281239', '452325', '611357', '1499032', '606056', '687249', '2564216', '832143', '961135', '1158619', '1296555', '1358641', '1495228', '1762267', '561187', '1574801', '942583', '2162417', '2485091', '1870373', '802310', '2301295', '1570504', '2455252', '1065987', '2316797', '2589709', '2580976', '1586766', '2590289', '2140154', '2435654', '2597317', '1494984', '2420075', '2164986', '2253873', '2554483', '2626917', '2017946', '499433', '282628', '2371591', '2609234', '2088915', '2266357', '1118370', '2495871', '1765092', '2282629', '2445837', '2520657', '1672639', '2369348', '2608689', '2598457', '3127725', '1864495', '2991712', '2265613', '2079595', '2387105', '2493230', '2533966', '2633978', '1884682', '309163', '889951', '2358678', '2635806', '2937231', '2350096', '1337798', '1494635', '2466402', '2883070', '2386957', '2131209', '2889014', '1544955', '2001304', '2511620', '519805', '1034325', '790144', '2476161', '239232', '2486976', '942912', '2497935', '1750636', '1829197', '659150', '2530280', '868289', '2427133', '1621357', '1971229', '2839052', '232414', '1233399', '213641', '1580845', '2137808', '2268124', '2120819', '2302219', '2411650', '2598217', '2377029', '2557812', '1847663', '2854766', '2870042', '1310035', '2255842', '2413287', '2850145', '2410193', '2434978', '3118166', '2318208', '2075115', '1734748', '2549924', '584020', '1318209', '940772', '1983516', '2874071', '2035975', '2134984', '1913140', '1705448', '1218160', '2506742', '2295817', '2887910', '2554295', '2596750', '2621718', '1900094', '1350650', '101924', '842889', '1644430', '1644876', '2294664', '2635916', '2397279', '2400780', '2501393', '2984543', '1701017', '749055', '2499373', '2192070', '2385559', '1848462', '1535728', '2300119', '2880182', '2995681', '382250', '2895388', '3097075', '2400746', '2581302', '2912041', '1858117', '1942975', '1725695', '1759385', '1737182', '2509092', '2155728', '2499224', '2277372', '1809588', '2294794', '2302880', '3007539', '2190975', '2952357', '1728403', '2373157', '2380414', '1926441', '1995689', '2536606', '1497230', '1474851', '2023249', '2176779', '2424136', '2468544', '2406412', '2085784', '2515071', '2820351', '2061086', '608342', '1728303', '216548', '223391', '44002', '2395846', '1468246', '35207', '316933', '2150583', '1614362', '189247', '167240', '2427492', '168332', '1931200', '760583', '2407815', '2199407', '900466', '1877996', '1632087', '242877', '2380029', '21474', '2102278', '1451301', '237129', '377926', '105234', '2013895', '1759992', '244843', '3007470', '212390', '2368914', '1836332', '444507', '1393524', '296708', '2300369', '2343566', '2099392', '1988238', '2127792', '257155', '547914', '337394', '393521', '561161', '1063285', '375704', '515580', '755157', '805405', '877423', '953472', '1651990', '1667771', '1727243', '1755171', '1885915', '2456289', '2266014', '2101890', '1197487', '962294', '2355374', '1137361', '2264377', '2183173', '994751', '1555321', '1836175', '1840962', '2383295', '269854', '2591495', '39632', '2078484', '3052855', '310343', '1500245', '718977', '1373051', '2180046', '2788074', '1773038', '1836570', '2305727', '2385900', '2405026', '2487161', '2585745', '3009480', '1369646', '2419936', '2312867', '2800311', '732271', '2042595', '1872546', '579197', '2283746', '2057294', '2335231', '2440672', '2157616', '2948212', '247437', '1811441', '3001944', '2504717', '3143894', '2509900', '2357298', '2316950', '735996', '1962527', '841464', '862739', '2896419', '2943834', '2512734', '2400167', '1755046', '1898077', '1334369', '2260145', '1256758', '2112934', '268727', '741086', '326390', '2199666', '2846152', '2166861', '1989142', '3132689', '1749383', '2207405', '2549053', '2173593', '2629010', '2836486', '1648850', '3008534', '1801928', '2639946', '2592822', '2290893', '2513946', '2201745', '2642931', '769234', '2019895', '2512539', '2169579', '2033716', '969054', '704846', '1667265', '1620026', '464352', '2305744', '2466541', '2144048', '1302617', '2451710', '2092535', '1039621', '1487361', '2308198', '2411949', '2881100', '928155', '1657373', '1159324', '2498304', '2137355', '1865570', '2043605', '2348288', '1876969', '714284', '570328', '2412306', '2424494', '2152055', '1145747', '1402557', '2315223', '2553931', '1028042', '1192355', '941034', '2206518', '2320050', '1654763', '2135049', '2312547', '2414779', '1597774', '2410968', '2640622', '2084428', '2151977', '2014244', '1666389', '1107593', '753551', '572641', '2108707', '38111', '113693', '2305141', '3135988', '1021526', '2175724', '2042870', '2061680', '2061704', '1315942', '2512683', '2132649', '286600', '2098729', '2156589', '2407342', '2412914', '2472810', '2584620', '990114', '1508926', '1594603', '1652062', '433293', '387295', '2399893', '1716174', '1188254', '224017', '906037', '1448329', '658909', '2438985', '59571', '190997', '1018527', '1143545', '1184578', '1407133', '2255585', '1020742', '76507', '1885718', '257176', '1909102', '268239', '98583', '2082074', '721468', '694138', '258149', '84337', '2031902', '2033670', '781203', '191755', '2289508', '2415333', '2525328', '2047328', '51442', '164663', '170798', '190081', '251441', '188696', '597454', '603945', '1774504', '812244', '1022182', '1274817', '863960', '1710288', '1362008', '314990', '2312069', '2414433', '2643485', '1362652', '2415080', '2634731', '1715101', '3059454', '814404', '1592354', '2292785', '2440046', '2322371', '58950', '2409272', '956906', '2141335', '2816482', '1977913', '1965933', '1849999', '2643530', '3015371', '1680013', '2991812', '2415658', '2457012', '2458188', '1392096', '1810071', '2112116', '1861952', '2015493', '2115145', '2568048', '2439624', '1726877', '2170792', '2518864', '3126924', '2921916', '2248733', '2322945', '3017836', '1837220', '2018512', '2349609', '1216397', '1499885', '1380907', '1388712', '1161445', '2171562', '2305971', '1206010', '2523064', '1717212', '1741025', '1658177', '2198466', '3000692', '1480260', '1015106', '2161821', '2166000', '2564508', '2437574', '1850645', '2170719', '2629788', '499565', '1212879', '2627598', '2911274', '1785866', '2066441', '2901939', '2504786', '3067135', '1653459', '2405580', '2167861', '617228', '1835758', '2643757', '2195549', '1634283', '2319408', '601722', '2017546', '2345722', '1409485', '1152067', '1919376', '1882407', '1282181', '2417457', '2321776', '1541623', '2102975', '1451852', '1507999', '1905406', '1464210', '1027071', '2779192', '2455922', '2517634', '1198032', '1745683', '1792339', '2071574', '856494', '1617442', '1289454', '2520536', '2384655', '2130741', '2411719', '2574854', '1048970', '2554023', '1335696', '944158', '2059982', '1847284', '1485738', '1540306', '2171739', '2064987', '2584536', '2789130', '1914417', '1196617', '2779515', '2351531', '2608633', '2114411', '1425222', '2824661', '2066782', '2815057', '2050415', '2041611', '2519443', '2104226', '2780006', '2315262', '1588474', '1772436', '2183393', '2211607', '2262545', '2784108', '141717', '343038', '1171975', '1268999', '200167', '1313194', '2267429', '540864', '2028242', '1734709', '453625', '619805', '243107', '1681136', '2911249', '1772377', '2098366', '2196716', '1575970', '732225', '714367', '1926183', '647008', '2278627', '2169442', '757896', '2136430', '1284430', '242009', '1827963', '1791045', '2146636', '2327085', '2516406', '937555', '46326', '2779922', '2164657', '1750906', '2155663', '2183286', '2126270', '2474214', '1948634', '2053099', '2015419', '2057557', '10553', '95469', '132723', '242611', '263106', '278987', '521126', '1158934', '850855', '1348167', '1645960', '1330706', '2206957', '2889066', '2424211', '2883326', '2163616', '2418970', '2422487', '2052029', '1873982', '2094732', '3020747', '1497343', '1290252', '2064376', '2779781', '2314478', '2274856', '1271739', '2175737', '2600060', '2430468', '1267557', '1636132', '2517820', '2816169', '2010508', '2196404', '1957861', '2342351', '2348271', '2878524', '2907498', '3160921', '1892762', '2327846', '2404651', '2784881', '1834018', '2411590', '2572260', '2171207', '1334028', '1921315', '697438', '2036649', '2085148', '1310356', '1538771', '2425831', '2911895', '2316386', '2511495', '2058745', '1276641', '1787889', '2285240', '2398316', '2499236', '1130903', '2783311', '1765945', '2510643', '2395323', '2276060', '3015891', '3162366', '2530853', '2447375', '2420984', '2521420', '2158062', '2335002', '2461364', '1646762', '2469649', '2028086', '2844233', '2911235', '2130070', '2528665', '1114795', '2065015', '2199585', '1854467', '2433844', '1455261', '2278262', '1994530', '2782876', '2554334', '1427924', '2117484', '2828116', '456876', '2048473', '2914170', '2513876', '2778621', '2411955', '3163143', '1020465', '2044293', '2841123', '3159368', '2424990', '2427577', '2876293', '2793577', '2440186', '3018453', '1348871', '2510913', '2919644', '2057719', '1373179', '1920557', '3166888', '1842709', '2937854', '1930903', '1155869', '1063813', '2533868', '1061298', '2844119', '2570529', '2349264', '2517256', '2154731', '2179336', '2433039', '3036170', '1256096', '1675917', '507293', '2070936', '2004222', '929285', '2064057', '1537418', '2256091', '527473', '247604', '251923', '146060', '181944', '2380287', '874203', '8314', '1169936', '547703', '1186413', '306770', '917240', '1294655', '136554', '256401', '147887', '2386416', '1833010', '1215999', '1472817', '1993091', '2068346', '1610857', '191761', '1722624', '2355940', '949323', '1015896', '1839710', '976560', '543340', '1947663', '303391', '2066554', '282131', '1665504', '1865932', '2050691', '2065390', '2519393', '2112475', '232734', '1219854', '2014429', '2050481', '587180', '328429', '237360', '486778', '511408', '573771', '618245', '333591', '467848', '863217', '968614', '1136427', '1351272', '1303937', '1380680', '1316085', '1497914', '1642360', '1759560', '2921098', '2045546', '1736798', '1998914', '1639151', '2525894', '1541569', '1912628', '223634', '2422693', '2057947', '2340771', '1076604', '2327327', '2054934', '2534689', '1322110', '2333406', '215372', '1370123', '1631357', '1803734', '1926878', '2439424', '2468174', '1874889', '2529424', '1454615', '2513894', '1576197', '1804897', '2429273', '2189162', '2201166', '2013594', '2318494', '2924532', '2336004', '2506315', '851342', '2552381', '2199288', '1544943', '976175', '2904405', '1946999', '2327561', '1675115', '627071', '2523205', '133956', '12136', '2425429', '2529848', '570302', '2384695', '1977951', '1681189', '1632599', '2049456', '1050403', '1519455', '2918808', '472807', '2137465', '2786103', '2064053', '2077140', '866753', '564981', '1881363', '2892562', '837931', '2311561', '1986767', '1030134', '2016272', '972986', '2538211', '2476273', '2538284', '2459786', '1959805', '2178881', '2792167', '2053183', '850068', '2540083', '2540467', '2435868', '2430580', '1928967', '2322963', '1877441', '2543387', '1417264', '2306499', '1962356', '3038079', '2370376', '1357009', '2071213', '997501', '2918101', '2824863', '1639419', '775815', '2183084', '2348419', '2402648', '2787978', '1882222', '2088459', '2788011', '2477339', '1826540', '1544288', '2903087', '1362644', '576849', '2068001', '2845842', '2539313', '1437566', '459181', '757148', '1431890', '1803439', '288155', '887550', '193227', '688143', '286319', '151057', '983548', '153935', '347196', '2431743', '632334', '1798600', '168358', '164228', '1632617', '353550', '1543578', '1650068', '583906', '1735832', '1103960', '1843517', '329496', '1163395', '173829', '1664970', '2336048', '2036998', '1446296', '1341816', '1460045', '562917', '1247640', '165420', '2441139', '333182', '1374674', '2609387', '1091105', '2353070', '2774404', '2380088', '2534297', '2792711', '1892911', '2054079', '44035', '29793', '41190', '241829', '273416', '532188', '595733', '702088', '1134917', '1429227', '1021374', '1539823', '1556815', '1674234', '1374682', '2542736', '1939234', '2395693', '2996067', '1244781', '2192974', '2284650', '2437495', '2001254', '3049588', '2784118', '2184825', '1817085', '3055169', '397085', '2724602', '1401590', '1972198', '1539220', '2354185', '2931532', '2811585', '2118139', '1584683', '1673471', '1811206', '2208005', '2925521', '2270425', '1456186', '1977170', '2790368', '2813207', '2394517', '2548189', '1761708', '1557742', '2644057', '1861195', '2960292', '2039050', '2271858', '2935700', '2081077', '2396843', '2540426', '532917', '1114546', '1172413', '2079236', '2084378', '2076111', '2467439', '2438596', '1307958', '1590749', '1818661', '2071259', '1113299', '2544526', '2540486', '2573439', '2779568', '1699067', '623018', '2551782', '1668403', '1840121', '2795567', '2632534', '1895310', '1426158', '1165583', '2796982', '2438521', '1339590', '956500', '1714043', '2558043', '2539605', '2799824', '1579940', '2266661', '2938584', '1710382', '2862416', '2549272', '1853408', '1913240', '2060314', '2345513', '2447639', '1994204', '2421793', '2494840', '2548139', '2796879', '1971872', '1980879', '814696', '2548204', '2550827', '1789239', '1514576', '1159758', '2114681', '569632', '1208624', '1463884', '2314662', '1063821', '2178495', '1559417', '2923337', '1467586', '2936394', '2815279', '2447112', '2804283', '2868338', '2929531', '2073335', '2820512', '372475', '1518121', '2084451', '2791430', '1812215', '2538137', '1429120', '1724561', '2588788', '1740665', '2068095', '2442431', '1298627', '1679092', '2349440', '2552451', '2405394', '2553678', '1369343', '2519910', '2165823', '2577883', '2114777', '186668', '1998762', '1554845', '551028', '312802', '2405501', '2641551', '2803661', '2824956', '1153876', '1452065', '75892', '61733', '1168426', '653783', '1292487', '2054977', '71317', '1948956', '388638', '113459', '257540', '1421598', '1877329', '475463', '248505', '2150991', '200860', '1127025', '71984', '1268158', '1323771', '703852', '1418734', '2293395', '2282911', '1577878', '2057147', '2538564', '2529497', '1467280', '891827', '1322425', '500737', '93919', '244311', '1725122', '308155', '548880', '569258', '2184631', '1484596', '2938997', '2202546', '2332652', '2401401', '2445464', '2597865', '2778476', '2131061', '82866', '124433', '222', '278702', '357546', '363794', '807505', '1372951', '1413150', '1339561', '1757300', '2968595', '2450331', '993345', '2813389', '2935879', '2936066', '2184829', '1897640', '2037668', '2307441', '2992572', '1588530', '1757289', '1614936', '677034', '2544114', '1904676', '1813769', '2199508', '2258095', '1202098', '2938856', '2551387', '1777691', '1312675', '2119683', '2203976', '2443605', '2447546', '1600121', '1526463', '2723677', '2181087', '3033859', '2935484', '2200774', '2422861', '1667417', '2572910', '1532073', '2006034', '2454460', '1806346', '2073353', '178393', '2354478', '1475323', '2321983', '2203201', '2449623', '2456730', '2446862', '2565691', '912915', '1518115', '2516438', '2780827', '2072502', '649541', '1550894', '2092150', '2170112', '1410704', '1027893', '1619622', '2357911', '3063325', '1439740', '1668602', '2774343', '2284759', '2544918', '2369624', '2725583', '688455', '1974987', '1209875', '1433597', '1506356', '794620', '1863064', '2101442', '1442016', '2050793', '2351923', '1953535', '130582', '2106553', '2159555', '1736555', '2502138', '2202687', '2205185', '2556965', '1283286', '1860283', '3064506', '2636795', '2309327', '1763801', '279273', '2934329', '1150323', '1198568', '1822456', '2792964', '1828194', '2513961', '2546688', '1408348', '1523861', '2934787', '1287557', '2356913', '2200002', '1299125', '1555031', '3066446', '259884', '2358639', '2424456', '2842875', '3059535', '1440888', '2197324', '2357168', '2354746', '1714262', '2134343', '1157651', '1873432', '2846042', '2429455', '290471', '302521', '555398', '751462', '532189', '1463697', '180162', '601866', '752774', '885288', '1891990', '1440552', '1528446', '2343635', '2195667', '437028', '526722', '1470721', '2533212', '1999058', '2260142', '2333678', '1300956', '74481', '563314', '739037', '8287', '3070327', '2880759', '2527064', '2825294', '3011832', '124813', '75559', '264809', '706550', '732482', '850216', '1481667', '1825903', '2293735', '1958758', '2276024', '2068939', '2562905', '2343531', '2784861', '2193271', '1476808', '2727853', '2323902', '1917662', '1937017', '1969319', '2383634', '1574565', '2003220', '1723424', '2858678', '1569100', '1814191', '2933095', '2415434', '1124713', '1740463', '1886994', '2278811', '2405895', '2564235', '1830343', '1853254', '2556012', '2327150', '1965782', '2326130', '1697778', '2469417', '3018230', '2359515', '2559621', '2340675', '2458458', '2361831', '1970268', '2983956', '835158', '2559677', '1313030', '2343434', '1527178', '2472891', '1301733', '2891194', '2207512', '23868', '478587', '2554729', '2389122', '1832891', '2367859', '1628698', '3028137', '2419927', '2578858', '1917406', '998590', '1304217', '1330321', '2252358', '2200015', '2562433', '2264544', '2208701', '2362129', '2364332', '2097382', '1370829', '1971627', '1281430', '2091806', '2944050', '2562403', '2371047', '1306068', '2276986', '2088936', '2539566', '1261249', '1079985', '2726891', '1972539', '1091106', '429136', '1007597', '1153928', '270360', '80806', '1175706', '1848068', '672425', '1193154', '821186', '363648', '717551', '41208', '214435', '915583', '229999', '389779', '1583228', '124500', '284634', '925877', '1341028', '472938', '1767348', '1308278', '1420479', '782294', '1497411', '934043', '1308391', '1196304', '251720', '188932', '1162977', '121058', '50467', '2164195', '2170913', '2251646', '2495722', '1912531', '1980230', '2012932', '2089596', '668590', '783', '222303', '82598', '543885', '649444', '758399', '843407', '853227', '1583755', '1400069', '1755484', '2259495', '2457825', '3063182', '2191556', '1202288', '2292288', '2461541', '1250899', '3061077', '2793726', '2358757', '2529593', '2728415', '1973861', '1456178', '2065022', '2102070', '1144579', '212675', '1021966', '1598772', '1787584', '1568350', '2347816', '2453321', '1761809', '2360206', '2461599', '2939092', '2451337', '2363783', '912597', '2945365', '2363517', '2465641', '2836263', '1080604', '1619226', '987433', '2041960', '2137577', '1179916', '2335821', '2391139', '809710', '1567162', '1865942', '2461825', '2432315', '2456817', '2106361', '1345143', '1570505', '1029998', '2415328', '1588737', '1519649', '3062241', '3081291', '1001157', '1542144', '2287218', '2396022', '2570234', '2100004', '2542051', '1301864', '2459305', '1555129', '2484138', '1310572', '2569859', '2262960', '2260927', '1697836', '2101645', '2508307', '2450831', '1850538', '2339627', '1699312', '2864462', '2111996', '1825728', '938430', '1658178', '1438442', '1704371', '3080754', '266889', '2889637', '2540927', '2449101', '2462760', '1963891', '1916638', '1722682', '1515235', '1822113', '2344892', '1467802', '2839776', '1989814', '532782', '2451936', '2487790', '1643205', '2287757', '2726433', '2153487', '2264080', '2446518', '2467085', '2909747', '1908974', '2841529', '896385', '2573961', '2263112', '2170092', '2466453', '2309975', '2258045', '1842144', '1585417', '2887667', '1367126', '2960710', '2090988', '237481', '1186742', '2360720', '1175060', '1149607', '2107510', '946423', '1137540', '538279', '2096411', '1567294', '1458152', '1676043', '1578314', '459147', '2264109', '2409336', '2552861', '1962382', '2101104', '10715', '179485', '507656', '506498', '878741', '1002166', '1183750', '1578813', '1454028', '1510193', '2174426', '1368378', '2021826', '2548440', '2198961', '107052', '2471900', '1937002', '2471086', '2839499', '2076370', '1083198', '2263431', '1519701', '2268480', '1773967', '2571257', '2345820', '1828053', '934932', '717687', '1307209', '1848433', '2440904', '1442672', '293004', '2048930', '625020', '550967', '127388', '1084196', '593775', '439508', '12399', '1624661', '691303', '688890', '485439', '2842766', '1889123', '2103623', '1932400', '2123111', '269764', '1074309', '696103', '1786803', '2836945', '1363675', '164242', '2054477', '2309794', '2270482', '2961543', '1921071', '2415565', '2496662', '2778396', '2047652', '1589154', '2184122', '686314', '2013618', '2275778', '2867970', '2344877', '2511308', '2526673', '1918397', '2185537', '2511326', '1475605', '552495', '1891087', '2045708', '2465501', '2148432', '1908989', '2095629', '3000364', '2114086', '1819335', '265499', '2065407', '2640168', '2210783', '2403890', '1009676', '1985452', '1862845', '2954137', '2961898', '1628852', '2188010', '2552017', '1405938', '2543511', '2400231', '2861113', '269495', '271313', '2870841', '285564', '2332403', '1068000', '503586', '1024395', '1366681', '947662', '2573740', '2890735', '738785', '2573778', '2361661', '2366491', '2780477', '1385972', '3071155', '2287030', '2092671', '2271291', '2140197', '2140256', '3075935', '2147565', '2727039', '2505269', '2326549', '2456504', '3036298', '1349186', '146931', '2552302', '867278', '2419631', '2572653', '2537902', '345512', '2584940', '1966113', '1581081', '2058008', '2352986', '2369081', '2361544', '1789962', '1374707', '2498960', '1404949', '1834624', '1166020', '167586', '1088961', '2184679', '2446603', '2408514', '557177', '2375056', '1152048', '1162696', '2007044', '303024', '1198210', '2151118', '2973522', '1720789', '3109253', '1416219', '1586454', '1098487', '1413623', '1017520', '2210041', '1772254', '2857274', '1985580', '1487768', '1874531', '2608297', '322551', '2439977', '2407460', '1856650', '2157483', '2832938', '2085921', '2294045', '2313207', '2108372', '2304330', '1889805', '1599077', '2380242', '2179556', '1072842', '2417615', '2050425', '2078583', '1781896', '1928129', '2325813', '2444624', '1813999', '1978424', '2556745', '2177286', '2432914', '2309636', '1638417', '1855984', '2447829', '804800', '2324960', '2387500', '970673', '1122881', '2412690', '1336992', '1929875', '1160885', '3107268', '2529067', '3051061', '2344732', '2568232', '1645918', '2567912', '2502466', '2402695', '2537304', '1532306', '2491597', '2567268', '2113644', '1500970', '2475849', '2005311', '1529441', '1508880', '981858', '2377262', '2040808', '2831127', '2537812', '2386038', '606327', '2324336', '2541477', '1068168', '2590579', '3006133', '2364341', '2113849', '909286', '2107794', '2084278', '2194565', '2149619', '983615', '2391847', '1766322', '1862285', '2423003', '1575065', '2571783', '2182893', '2360362', '2120999', '236685', '2486468', '562730', '2785406', '2537204', '2798607', '1350702', '2438943', '2498457', '2183528', '2502084', '2629284', '2293394', '2865442', '2864473', '2269416', '2514991', '653550', '1859796', '2516070', '313256', '2436946', '2574751', '1219927', '2432532', '719040', '2569061', '2366077', '2986411', '2510029', '2800201', '2961213', '2955876', '2594354', '2843260', '2357090', '2998888', '3069767', '2956800', '3054974', '1765842', '892706', '2183544', '3040450', '1011377', '1431708', '2643189', '1907052', '2002873', '2138749', '2152207', '2153087', '2155312', '2157123', '2158056', '2162713', '2846568', '2333060', '2847186', '2859278', '2871871', '2873317', '2874526', '2877047', '2880883', '2882409', '2893078', '2893545', '2895394', '2896185', '2907305', '2898498', '2909483', '2907438', '2858729', '2913207', '2923327', '2932280', '2933191', '2938606', '2939026', '2949831', '2166465', '2171226', '2175391', '2005730', '2176398', '2154804', '2186149', '2190718', '2191069', '2192230', '2197782', '2199190', '2200953', '2203581', '1399644', '2206529', '2207374', '1234448', '1906875', '2252189', '2251987', '2252901', '2253794', '2253696', '2126312', '2262239', '2261048', '2263143', '2265080', '2265442', '2270006', '2271362', '2273443', '2274068', '865346', '2271728', '2276913', '2275408', '2278507', '2277322', '2275830', '2284174', '808188', '2297856', '2297155', '2303030', '2304463', '2193222', '2307040', '2307421', '2311973', '2312647', '2315799', '2316465', '2320595', '2318087', '2323517', '2309872', '2139306', '2330546', '2333646', '2333514', '2334809', '2344455', '2345121', '2345995', '2326381', '2349919', '2351035', '2354676', '2352497', '2359388', '2364675', '2370728', '2366377', '2333844', '2372812', '2372579', '2353911', '2381054', '2382208', '2381538', '2381735', '2382556', '2382818', '2383214', '2377335', '2384538', '2383712', '2384637', '2386943', '2388814', '2390169', '2390835', '2383239', '2397103', '2397529', '2404764', '2397916', '2397976', '2403772', '2404449', '2404591', '2404658', '2326354', '2413443', '2416947', '2423007', '2455354', '2430142', '2432420', '2436339', '2436869', '2435249', '2440469', '2435955', '2441601', '2446121', '2446301', '2450146', '2776672', '2453200', '2455491', '2455962', '2460421', '2462452', '2465726', '2977746', '546360', '2472903', '1911405', '2475525', '2479250', '2483658', '2482372', '2480279', '2489366', '2490106', '2491082', '2496631', '2508661', '2507160', '2515738', '2518006', '2518151', '2518944', '2523328', '2433902', '2533351', '2534176', '2444367', '2530956', '2539848', '2539994', '2084049', '2542075', '2542278', '2548750', '2549469', '2553047', '2554478', '2556570', '2561331', '2566154', '2563404', '2569566', '2570572', '2570652', '2519467', '2571570', '2572158', '2574343', '2578173', '2581733', '2579055', '2586864', '2587834', '1193771', '2590842', '2590239', '2593954', '2595331', '2561688', '2597562', '2628769', '2627955', '2628951', '2630605', '2630745', '2631859', '2632649', '2780996', '2639652', '2639605', '2641623', '2725897', '2632785', '2585228', '2778447', '2780794', '2780918', '2783895', '2785155', '2787262', '2788049', '2792055', '2794561', '2794505', '2798034', '2798100', '2803666', '2815441', '2825952', '2826234', '2590190', '2826796', '2833282', '2833598', '2837830', '2839215', '2836971', '2813041', '491559', '1806414', '1880156', '1873832', '1881189', '1887003', '1900412', '933278', '1913019', '1914475', '1907518', '1927612', '1576526', '1943990', '1946939', '1948812', '1954362', '1873257', '1567066', '1968699', '1974446', '1980828', '1930924', '2005313', '2000877', '2008527', '2014067', '2018627', '2019012', '2031040', '2033179', '2034786', '2043142', '2045696', '2045816', '2051324', '2054341', '2055437', '2061207', '2061723', '1848543', '2071848', '2080514', '2020250', '2071529', '2094352', '2097284', '2097131', '2099423', '2101681', '2101980', '2107475', '2108765', '2042467', '2113634', '2120501', '2121683', '2121902', '2010525', '661642', '3000001', '3004446', '3032952', '3035338', '3054347', '3058397', '3061694', '3070787', '3076884', '3077362', '86876', '3097066', '3099374', '3104125', '3120489', '3128709', '2909497', '61832', '3148819', '68033', '239039', '3177404', '70754', '8273', '8298', '172598', '140050', '515220', '252936', '254513', '513937', '320009', '2071509', '354428', '337197', '2214518', '385284', '465646', '2215557', '516243', '525275', '2221491', '612044', '2955477', '653536', '660417', '683624', '693334', '693448', '2223729', '728753', '2224001', '749076', '736956', '846702', '848970', '822411', '862914', '881867', '2226892', '904773', '961858', '813744', '974126', '989637', '979609', '1013003', '1212547', '1031630', '2833114', '1695289', '1065153', '1063188', '1061823', '1128799', '1190776', '1193153', '1371933', '1214721', '1220599', '1242404', '1252423', '1251610', '1227150', '1287069', '1197479', '2233403', '1316140', '1331870', '1328723', '1336782', '1344585', '1348386', '1357170', '1373509', '1374224', '1375843', '1377768', '1391015', '1401656', '1415676', '1358413', '1421801', '1438400', '1438483', '1438918', '1188500', '2235559', '3088832', '1453883', '1447522', '1465551', '1463755', '1466191', '1471248', '1430188', '1340341', '1492292', '1507288', '1323104', '1535278', '1535925', '1538482', '1539006', '1349591', '1560372', '1232868', '1496265', '1587362', '3046993', '1600593', '648673', '1630416', '1634748', '1594323', '1657987', '1661686', '1663735', '1272778', '1671353', '1517442', '1674822', '1678530', '1676229', '2492171', '1647365', '1688513', '1325054', '1677331', '1537302', '1701494', '1701648', '1707323', '1706214', '1707956', '1717826', '1540979', '1770114', '1774464', '1782107', '1227530', '1790783', '1804373', '1701181', '1830932', '1836146', '1839253', '1842134', '1841647', '1841873', '1965177', '1452661']


# last line of list 1452661 gives a ValueError: invalid literal for int() with base 10: ''. Why?

def dotCheck(list):
	currYear = date.today().year
	currMonth = date.today().month
	for dotNum in list:
		if currYear % 2 == 1:
			if int(dotNum[-2:-1]) % 2 == 1:
				print(dotNum,dotNum[-2:-1], 'is odd, register this year')
			elif int(dotNum[-2:-1]) % 2 == 0:
				print(dotNum,dotNum[-2:-1], 'is even register next year')
			else:
				print(dotNum,dotNum[-2:-1], 'Something Went Wrong')



# check if more than 2 years since date - ia
# check if odd year or even year and what current year - ia

# add month check also



# dotCheck(list)

for dotNum in list:
	monthID = int(dotNum[-1])
	yearID = int(dotNum[-2:-1])
	currMID = int(datetime.now().strftime('%m'))
	currYID = int(datetime.now().strftime('%y'))
	if monthID >= currMID: # greater than or equal.... wow yea i typed that.
		print(str(table[monthID][0]) + ' > = ' + str(table[currMID][0]), dotNum, currMID, currYID)
	elif monthID <= currMID: # less than or equal.... rw struggles...
		print(str(table[monthID][0]) + ' < = ' + str(table[currMID][0]), dotNum, currMID, currYID)
