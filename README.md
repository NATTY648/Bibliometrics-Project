bibliometrics-mini: Cancer PET Imaging & Cellular Proliferation (2000–2009)

这是一个基于 Python 的文献计量学微型项目（bibliometrics-mini），针对肿瘤 PET 成像、分子表达与电学纳米传感2000–2009 年交叉领域文献开展全流程数据挖掘、网络分析与可视化。
项目采用 Python 主分析 + VOSviewer 交叉验证 双工具架构，严格遵循课程 10 项数据透明度、可复现规范，为课程期末大作业完整成果仓库。

---

## 1. 目录结构与成果说明 (Repository Structure)
   本项目仓库严格遵循课程可复现性、规范性要求，目录划分清晰，所有文件与成果一一对应，完整覆盖数据、代码、运行结果、论文、答辩材料、反思等全流程内容。核心结构如下：

```
project/
├── .gitignore                      # Git忽略文件配置，排除缓存、临时文件
├── Makefile                        # 自动化运行脚本，支持一键执行分析、测试
├── README.md                       # 项目说明文档（本文件）
├── requirements.csv                # Python依赖包清单，可一键安装
├── run.py                          # 项目主运行入口，直接执行完整分析流水线
├── Bibliometrics_Python_Minimal_Project_Tr...docx # 课程论文Word版本备份
├── config/                         # 项目全局配置目录
│   └── query.yaml                 # 数据筛选、分析阈值、输出路径等统一配置
├── data/                           # 数据集目录
│   ├── raw/                        # 原始数据归档目录（本次数据已迁移至processed）
│   ├── processed/                  # 清洗后结构化数据
│   │   ├── work_authors.csv        # 论文-作者关联表
│   │   ├── work_keywords.csv       # 论文-关键词关联表
│   │   ├── work_references.csv     # 论文-参考文献关联表
│   │   └── works_clean.csv         # 清洗后完整论文数据表（含年度、作者、关键词等）
│   ├── sample/                     # 测试样本数据
│   │   └── openalex_works_sample.jsonl # OpenAlex格式小样本数据，用于快速调试
│   └── sample-wos/                 # WoS原始导出数据（2000-2009年）
│       ├── download2000u31.txt
│       ├── download2001u79.txt
│       ├── download2002u136.txt
│       ├── download2003u188.txt
│       ├── download2004u280.txt
│       ├── download2005u338.txt
│       ├── sample2006u509.txt
│       ├── download2007u674.txt
│       ├── download2008u864.txt
│       └── download2009u1066.txt
├── docs/                           # 学术合规与说明文档
│   ├── ai_usage.docx               # AI辅助编程、数据核验说明，满足课程合规要求
│   └── data_model.docx             # 数据模型、字段定义与清洗规则说明
├── src/                            # 核心源代码目录
│   └── bmmini/                     # 文献计量分析核心包
│       ├── __init__.py
│       ├── fetch_openalex.py       # OpenAlex数据获取模块
│       ├── parse_wos.py            # WoS原始数据解析模块
│       ├── normalize.py            # 数据归一化、关键词合并、去重模块
│       ├── matrices.py             # 共现/共被引/耦合矩阵构建模块
│       ├── metrics.py              # 网络指标计算（度、中心性、聚类等）模块
│       ├── utils.py                # 通用工具函数
│       ├── pipeline.py             # 全流程主流水线模块
│       └── visualize.py           # 可视化模块（静态PNG+交互式HTML）
├── tests/                          # 单元测试目录
│   ├── __pycache__/
│   └── test_matrices.py            # 矩阵构建与计算逻辑的自动化测试
├── outputs/                        # 全流程运行产出物（重点模块）
│   ├── tables/                     # 网络分析数据表（原始结果，可追溯）
│   │   ├── network_qc_summary.csv       # 网络质量控制汇总表
│   │   ├── network_metrics_keyword_cooccurrence.csv # 关键词共现网络节点指标
│   │   ├── network_metrics_coauthorship.csv # 机构合作网络节点指标
│   │   ├── network_metrics_co_citation.csv # 文献共被引网络节点指标
│   │   ├── network_metrics_bibliographic_coupling.csv # 文献耦合网络节点指标
│   │   ├── keyword_cooccurrence_edges.csv # 关键词共现网络边表
│   │   ├── coauthorship_edges.csv      # 机构合作网络边表
│   │   ├── co_citation_edges.csv       # 文献共被引网络边表
│   │   ├── bibliographic_coupling_edges.csv # 文献耦合网络边表
│   │   ├── descriptive_indicators.csv  # 文献计量描述性统计（发文量、被引等）
│   │   ├── cluster_summary_keyword_cooccurrence.csv # 关键词共现网络聚类汇总
│   │   ├── cluster_summary_coauthorship.csv # 机构合作网络聚类汇总
│   │   ├── cluster_summary_co_citation.csv # 文献共被引网络聚类汇总
│   │   └── cluster_summary_bibliographic_coupling.csv # 文献耦合网络聚类汇总
│   ├── figures/                    # Python生成可视化图谱（对应课程「3图1表」）
│   │   ├── annual_trend.png        # 年度发文趋势图（对应RQ1：领域发展态势）
│   │   ├── keyword_cooccurrence_network.png/html # 关键词共现网络（对应RQ2：学科热点）
│   │   ├── coauthorship_network.png/html # 机构合作网络（对应RQ2：合作格局）
│   │   ├── co_citation_network.png/html # 文献共被引网络（对应RQ3：知识基础）
│   │   └── bibliographic_coupling_network.png/html # 文献耦合网络（补充分析）
│   └── vosviewer/                  # VOSviewer交叉验证图谱（共6张）
│       ├── vos_cocitation_cluster.png      # 文献共被引网络聚类视图
│       ├── vos_cocitation_density.png       # 文献共被引网络密度视图
│       ├── vos_keyword_cluster.png         # 关键词共现网络聚类视图
│       ├── vosviewer_keyword_evolution.png   # 关键词共现网络时间演化视图
│       ├── vos_organization_cluster.png    # 机构合作网络聚类视图
│       └── vos_organization_evolution.png  # 机构合作网络时间演化视图
├── reports/                        # 自动生成综合报告
│   ├── bibliometrics_report.html   # 响应式综合数据报告（重点模块）
│   └── method_note.md               # 矩阵公式、计算口径与指标说明
├── paper/                          # 课程正式论文
│   └── report.docx                 # 标准IMRaD结构mini review终稿
├── presentation/                   # 答辩汇报材料
│   └── final_presentation.pptx     # 答辩PPT
├── reflection/                     # 个人学习反思
│   └── reflection.docx             # 项目过程反思、问题解决与学习总结
```

---

## 2. 数据源说明 (Data Source)

* 数据来源：Web of Science (WoS) Core Collection 导出记录。
* 数据范围：2000 年至 2009 年的 4,165 篇 Articles 与 Reviews（已去重并规范化）。
* 数据指标：
  * Seed 论文总数：4,165 篇
  * 总被引频次：307,626 次
  * 篇均被引数：73.86 次
  * H-指数：225
  * 独立作者数：15,693 人

---

## 3. 本地复现运行指南 (Running Instructions)

项目使用纯 Python 编写，无需配置复杂的 Java 桌面环境。

### 3.1 环境准备
建议在 Python 3.11 环境下运行，直接使用系统 Pip 安装依赖包：
```bash
pip install -r requirements.txt
```

### 3.2 运行总流水线 (Pipeline)
运行完整流水线（生成表格、HTML 报告、PNG 图表，核心作业流程）
```powershell
python run.py
```
运行完成后，可在 `outputs/` 和 `reports/` 目录下查看更新的分析结果。

### 3.3 运行单元测试
通过 `pytest` 执行矩阵与网络计算逻辑的自动化测试，确保计算过程符合数学公式：
```bash
$env:PYTHONPATH="src"
python -m pytest tests/
```

---

## 4. 核心计算逻辑与公式 (Core Logic)

* 关键词共现矩阵：W = K^T·K (K为论文-关键词长表的二部图关联矩阵)。
* 文献共被引矩阵：C = A^T·A (A为论文-被引参考文献的关联矩阵)。
* 文献耦合矩阵：B = A·A^T。
* 中介中心性距离转换：由于文献计量是相似度加权网络，计算路径时使用 D = 1/W 转换为距离矩阵。
* 社区分裂：采用贪婪模块度最大化算法（Newman-Girvan 算法）在 NetworkX 中完成聚类。

### 5 重要更新！！！
个人在“完美的随意文献计量检索.zip”更新了以下内容：

* python生成的图片中圆圈缩小，类群之间间距进一步放大，经多次实验，均无类群碰撞的错误。
* 改进了数据清洗，可在config/invalid_keywords.txt中修改无效关键词，并列出了清洗前后的文本数量变化。
* 增加了辅助工具clean.py 可一键清空当前配置对应的所有输出文件。其可自动读取 config/query.yaml 中的输出路径，精准清理当前课题的生成结果。
* 改进了数据源选择
  模式 1：在线检索 OpenAlex 文献并完整分析（需配置 API 密钥，默认使用作者API）
  python run.py --fetch-openalex
  自动完成：API 抓取文献 → 数据清洗 → 四类网络计算 → 可视化绘图 → 生成报告。
  模式 2：本地 Web of Science 数据集分析
  python run.py --use-wos
  读取 data/sample-wos/ 下的 WoS 导出 txt 文件，执行完整分析流程。
  模式 3：本地已有 JSONL 数据直接分析
  python run.py
* 统一了3种模式数据集分析的通用函数框架，两者输出完全一致。
* 试设计了多文献类的分析，即可创建config/query1.yaml等等多个query，修改其中参数输出对应的文献检索结果，
  可通过修改辅助工具cross_analysis.py进行交叉验证，对应废案癌症双检索交叉讨论+交叉验证可供参考。
* 更多详细信息请看zip中的readme。
