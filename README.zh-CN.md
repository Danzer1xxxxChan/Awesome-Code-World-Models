# Awesome Code World Models · 中文导览

[English / 完整文献目录](README.md) · [逐篇阅读笔记](docs/READING_NOTES.zh-CN.md) · [核验记录](docs/VERIFICATION.md)

这个仓库围绕一个问题组织文献：**如何构建或恢复一个可执行的视觉世界，并把其运行结果变成可靠、可控的生成画面？**

主页先展示代表性工作的官方视频，再按研究问题组织全部文献：

| 分类 | 讨论内容 |
|---|---|
| [完整世界系统](world-systems/README.md) | 代码、引擎状态、条件接口和生成观察如何组合。也区分论文、实现和架构报告。 |
| [世界构建与恢复](world-construction/README.md) | 场景程序、3D/4D环境、关节对象、物理机制的创建、恢复与编辑。 |
| [程序化动态与规则](programmatic-dynamics/README.md) | 从交互或观察学习可执行状态转移，用于预测、检验与规划。 |
| [生成式渲染](generative-rendering/README.md) | 从引擎、场景缓冲、物理模拟或参数化角色生成视频观察。 |
| [数据与评测](evaluation/README.md) | 同时讨论通用画质、姿态/轨迹、身份、物理、记忆和程序世界的专门测试。 |
| [综述与观点](surveys/README.md) | 相关领域的定义、技术脉络与综合分析。 |

范围内的工作保留逐篇条目，完整系统与组件工作分别说明。输入是2D还是3D、是不是视频，并不独立决定是否纳入。普通姿态控制论文也可能作为**评测参考**出现，这不表示它被归为完整Code World Model。

本次重新核实了题名、唯一标识、原始来源、可取得的日期与分类依据，日期为 **2026-10-22**。具体方法、模型等技术笔记来自既有定向阅读；题录核验不等于本轮重新完整精读或独立复现全部工作。

文献源数据可下载为 [JSON](data/papers.json)、[CSV](data/papers.csv) 和 [BibTeX](references.bib)。视频、预览图和作者原始链接见[媒体清单](data/media.json)。所有第三方媒体保留原有权利与许可。

新增或修正文献请参考[贡献说明](CONTRIBUTING.md)。
