# 文档编写说明

[toc]

## 编写环境

1. vscode
    - markdown preview插件
    - vim插件
2. git
3. cmd命令行
4. ssh

## 目录结构

```
.
├── bin
│   ├── mecdoc1
│   ├── mecdoc2
│   ├── mecindex
│   └── mecprd
├── dingtalk.py
├── index.html
├── index.md
├── mec0
│   ├── assets
│   │   ├── 01jiagou_kmvj7zvwv.png
│   │   ├── bg.jpeg
│   │   ├── biaoding.png
│   │   └── yuanli.png
│   ├── dingtalk.py
│   ├── index.html
│   ├── 适用于车路协同的基于毫米波雷达和智能摄像机的数据融合算法实现.docx
│   ├── 适用于车路协同的基于毫米波雷达和智能摄像机的数据融合算法实现.md
│   └── 适用于车路协同的基于毫米波雷达和智能摄像机的数据融合算法实现.pdf
├── mec1.0
│   ├── assets
│   │   ├── 01jiagou_kmvj7zvwv.png
│   │   └── drawio.svg
│   ├── flows.json
│   ├── report.py
│   ├── standard
│   │   ├── T∕CSAE248-2022合作式智能运输系统车路协同云控系统C-V2X设备接入技术规范.pdf
│   │   ├── T∕CSAE248-2022合作式智能运输系统车路协同云控系统C-V2X设备接入技术规范.pdf.html
│   │   ├── T∕ITS0117RSU与中心子系统间接口规范.pdf
│   │   ├── T∕ITS0180.1-2021车路协同信息交互技术要求第1部分：路侧设施与云控平台.pdf
│   │   └── T∕ITS0180.1-2021车路协同信息交互技术要求第1部分：路侧设施与云控平台.pdf.html
│   ├── 基于海康雷视一体机的MEC设计.docx
│   ├── 基于海康雷视一体机的MEC设计.md
│   └── 基于海康雷视一体机的MEC设计.pdf
├── mec2.0
│   ├── MEC2.0华为感知设备调研报告.md
│   ├── data
│   │   ├── acc7320
│   │   │   ├── ACC7310测速雷达上位机软件及雷达固件
│   │   │   │   ├── ACC7310-HT雷达调试工具V8.7.exe
│   │   │   │   ├── JTCS#S#HV5.0#SV3.3#20200116.ht802
│   │   │   │   └── RemoteUpdate4.11_fast.exe
│   │   │   ├── ACC7320&ACC7322-通信协议(带鉴权)20210831.html
│   │   │   ├── ACC7320&ACC7322-通信协议(带鉴权)20210831.pdf
│   │   │   ├── ACC7320-无锡所型检报告 （802）.html
│   │   │   ├── ACC7320-无锡所型检报告 （802）.pdf
│   │   │   ├── ACC7320对外协议-250.html
│   │   │   ├── ACC7320对外协议-250.pdf
│   │   │   ├── ACC7320安装配置.html
│   │   │   ├── ACC7320安装配置.pdf
│   │   │   ├── ACC7320调试固件.rar
│   │   │   ├── ITS多目标跟踪雷达ACC7320彩页v1.0-编码02412425.pptx
│   │   │   ├── 用户使用手册-ACC7320(V10.9)-20211228.html
│   │   │   └── 用户使用手册-ACC7320(V10.9)-20211228.pdf
│   │   ├── holographic
│   │   │   ├── resource
│   │   │   │   ├── Checklist.xlsx
│   │   │   │   ├── Communication_Matrix.xlsx
│   │   │   │   ├── Configuration Planning.xlsx
│   │   │   │   ├── Data_Planning_0000001208634490.xlsx
│   │   │   │   ├── Document Description.zip
│   │   │   │   ├── weak_pwd.txt
│   │   │   │   ├── 数据规划.xlsx
│   │   │   │   ├── 数据规划_0000001198537566.xlsx
│   │   │   │   └── 工勘参考模板-全息路口.xlsx
│   │   │   ├── zh-cn_bookmap_0000001253014351.hhc
│   │   │   └── zh-cn_topic_0298342602.html
│   │   ├── its800
│   │   │   ├── ITS8009.1.0通用接口(雷达).pdf
│   │   │   ├── ITS8009.1.0通用接口(雷达).pdf.html
│   │   │   ├── IVS1800&ITS8009.1.0MIB接口参考.pdf
│   │   │   ├── IVS1800&ITS8009.1.0MIB接口参考.pdf.html
│   │   │   ├── IVS1800&ITS8009.1.0接口参考(RESTFUL&GAT1400).pdf
│   │   │   ├── IVS1800&ITS8009.1.0接口参考(RESTFUL&GAT1400).pdf.html
│   │   │   ├── IVS1800&ITS8009.1.0接口参考(RESTFUL).pdf
│   │   │   ├── IVS1800&ITS8009.1.0接口参考(RESTFUL).pdf.html
│   │   │   ├── IVS1800&ITS8009.1.0算法开发指南(基于昇腾310).pdf
│   │   │   └── IVS1800&ITS8009.1.0算法开发指南(基于昇腾310).pdf.html
│   │   ├── sdc
│   │   │   ├── HoloSensSDCAPI协议说明.pdf
│   │   │   ├── HoloSensSDCAPI协议说明.pdf.html
│   │   │   ├── HoloSensSDC全网智能接口对接TLV数据详解.pdf
│   │   │   ├── HoloSensSDC全网智能接口对接TLV数据详解.pdf.html
│   │   │   ├── 华为SDC9.0.0APP开发指南(pdf).pdf
│   │   │   ├── 华为SDC9.0.0APP开发指南(pdf).pdf.html
│   │   │   ├── 华为SDC9.0.0MIB参考.pdf
│   │   │   ├── 华为SDC9.0.0MIB参考.pdf.html
│   │   │   ├── 华为SDC9.0.0OMAPI协议说明(pdf).pdf
│   │   │   ├── 华为SDC9.0.0OMAPI协议说明(pdf).pdf.html
│   │   │   ├── 华为SDC配套件安装专题(html).pdf
│   │   │   └── 华为SDC配套件安装专题(html).pdf.html
│   │   └── 机器视觉解决方案10.0.0产品文档（全息路口）.chm
│   ├── dingtalk.py
│   ├── report.html
│   └── 华为文档查看器 ICS Lite使用手册.md
├── prd
│   ├── assets
│   │   ├── 01jiagou_kmvj7zvwv.png
│   │   ├── Screen Shot 2022-05-24 at 17.41.11.png
│   │   └── drawio.svg
│   ├── index.html
│   └── index.md
└── readme.md

```

## 发布说明

1. 将bin目录添加到系统path
2. 通过markdown插件生成html
3. 运行mecdoc[n]命令，n:1,2,3,4...
