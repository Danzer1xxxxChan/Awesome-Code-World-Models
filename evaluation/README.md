# Data & Evaluation

[← Main collection](../README.md) · [Scope](../docs/SCOPE.md) · [Verification](../docs/VERIFICATION.md)

Code-world benchmarks alongside general video quality, control, memory, and physical evaluation.

The identity/source check and the depth of technical reading are separate fields. The notes below summarize prior targeted reading; they do not report a new reproduction.

<a id="t037"></a>

## PhysCodeGym: Benchmarking Coding Agents for Physically Verifiable 4D Reconstruction

[paper](https://arxiv.org/abs/2610.17288) · [code](https://github.com/ShaoShuai0605/PhysCodeGym)

- **Type / date:** Paper / 2026-10-12.
- **Method:** Evaluates video-to-program reconstruction with explicit physical variables and executable checks.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** 编码agent＋Blender；规则测量和VLM裁判
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2610.17288).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 重建视频外观和事件仍可能依赖错误物理机制。

**方法：** 156个video-to-Blender任务要求建模物性、初态、约束与力；联合视觉和物理指标，并检查程序、场景重执行和反事实干预。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="u049"></a>

## ExeWorldBench: Benchmarking Code-Based Executable 3D World Modeling

[paper](https://arxiv.org/abs/2610.15166)

- **Type / date:** Paper / 2026-10-10.
- **Method:** Evaluates code-based 3D world construction across mechanism, composition, and intent constraints.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2610.15166).

<a id="e08"></a>

## WorldSolver: Can LLM Agents Simulate the Physical Dynamics via Solver Generation?

[paper](https://arxiv.org/abs/2610.08720) · [code](https://github.com/sirujiang/WorldSolver)

- **Type / date:** Paper / 2026-10-06.
- **Method:** Tests agents on building executable physical solvers rather than only describing physical behavior.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** GPT-5.6 Sol、Claude Opus 5、Gemini-3.7-Flash、DeepSeek-V4.1-Flash、Qwen-3.8-Max、Kimi-K2.7-Code等; 可执行solver
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2610.08720).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 会解释物理现象不代表能写出正确、稳定且可泛化的数值模拟程序。

**方法：** agent从任务与现象要求编写求解器，用执行有效性、物理结果及运行/API成本评价，不以视频美观代替物理解。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="e07"></a>

## Video2World: Benchmarking Coding Agents for Interactive World Modeling from Embodied Videos

[paper](https://arxiv.org/abs/2610.04432) · [project](https://aetherlabsai.github.io/Video2World)

- **Type / date:** Paper / 2026-10-03.
- **Method:** Evaluates reconstruction of embodied videos into worlds with geometric, dynamic, and functional tests.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** GPT-5.6 Sol、Gemini 3.8 Flash、Claude Opus 5、Qwen3.8 Max、GPT-6 Astra、Fable-5.1等; 含API与coding CLI配置
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2610.04432).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 外观重建相似不代表能响应新动作或完成具身任务，需要把几何、动态和功能分开测。

**方法：** 在222个重建实例上让coding agent从具身视频构建世界，通过渲染、动态对齐及交互任务检验产物。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t003"></a>

## 4DCodeBench: Benchmarking Agents on Inverse Graphics of Dynamic Scenes

[paper](https://arxiv.org/abs/2610.03715) · [code](https://github.com/4DCodeBench/4DCodeBench) · [project](https://4dcodebench.com)

- **Type / date:** Paper / 2026-10-02.
- **Method:** Tests dynamic video reconstruction as executable graphics programs across scene and motion properties.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** 编码智能体＋Blender / Taichi / Warp等；评测含DINOv3与视觉估计器
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2610.03715).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 静态重建能力不足以说明能从视频恢复复杂动态。

**方法：** 200个视频任务要求代码重建并导出每帧几何、相机和物质对应；真实视频做图像域比较，合成场景额外比较3D几何与动态。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="e06"></a>

## World Editing: Intervening on Executable Worlds at Increasing Depth

[paper](https://arxiv.org/abs/2610.02331) · [project](https://vinesmsuic.github.io/IGMWorld)

- **Type / date:** Paper / 2026-10-01.
- **Method:** Benchmarks edits at different depths of an executable game world, from attributes to dynamics and systems.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** Gemini 3.5 Flash、Claude Opus 4.8、GPT-5.6 Luna、GPT-5.6 Sol; Minecraft、Terraria
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2610.02331).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 修改属性、实体、规则与系统的难度不同，仅检查工程是否构建无法验证编辑结果。

**方法：** IGMWorld/IGMBench在Minecraft与Terraria中设置递增深度的干预，执行行为测试并检查视觉结果，评价完整成功与局部条件满足。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="e05"></a>

## PROWBench: Do Video Models Render What the Program Specifies?

[paper](https://arxiv.org/abs/2610.02205) · [code](https://github.com/AlayaLab/PROWBench) · [project](https://alaya-lab.github.io/PROWBench)

- **Type / date:** Paper / 2026-10-01.
- **Method:** Checks generated observations against replayable world records, entity states, and timestamped events.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** EchoWM、SANA-WM、LingBot-World 2.0、AlayaWorld v1.1、Cosmos-Transfer2.5、C2R、CWM、LynnReal-Omni、PWM、MiniMax-H3、Seedance 2.5; SAM 3实体定位；Qwen3.6-27B事件、时间线与状态判断（§3.2）
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2610.02205).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 视觉合理不代表实体、相机、事件、长时状态与多视角都遵循同一程序世界。

**方法：** 保存共享几何和逐帧世界记录，再渲染Coarse 3D、CWM proxy和Colored-OBB；对比11种模型的控制、逻辑、视觉、重访和多视角表现。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="u068"></a>

## World Agent: Can Language Models Keep a World Running?

[paper](https://arxiv.org/abs/2609.32692) · [code](https://github.com/HCPLab-SYSU/WorldAgent-Benchmark)

- **Type / date:** Paper / 2026-09-26.
- **Method:** Studies agent-generated worlds and the evidence needed to validate their behavior.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2609.32692).

<a id="e04"></a>

## BVB: Benchmarking Agentic Video Understanding via Programmatic Reconstruction in Blender

[paper](https://arxiv.org/abs/2609.15478)

- **Type / date:** Paper / 2026-09-14.
- **Method:** Measures video understanding by reconstructing observed scenes and events as Blender programs.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** GPT-5.x/GPT-6 Astra、Claude、Gemini、Grok、Qwen、GLM、Kimi等家族; 本表仅列代表家族，不是逐项完整复现配置
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2609.15478).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 语言问答不能直接检验模型是否理解视频中的空间、轨迹和交互事实。

**方法：** 要求agent用Blender代码重建视频，在共享执行与预算下分别测时空事实保留、可执行性和感知相似。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="n034"></a>

## R2M-Bench: Evaluating Revisit Memory via Relative Consistency in Interactive Video World Models

[paper](https://arxiv.org/abs/2608.27328) · [code](https://github.com/AMAP-ML/R2MBench)

- **Type / date:** Paper / 2026-08-27.
- **Method:** Evaluates revisit memory with time-gap-matched controls to separate recall from short-term similarity.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** 基准；视频表征／视觉裁判
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2608.27328).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 慢运动或静止视频也可能取得很高的重访相似度。

**方法：** 比较同一视频中的重访、时间间隔匹配对照与短期参考，计算MemoryGain和归一化记忆比例。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="u069"></a>

## PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives

[paper](https://arxiv.org/abs/2608.13552) · [code](https://github.com/kxding/PlayWorld) · [project](https://kxding.github.io/project/PlayWorld)

- **Type / date:** Paper / 2026-08-13.
- **Method:** Uses agent players and sustained tasks to evaluate interactive generated environments.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2608.13552).

<a id="n031"></a>

## When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models

[paper](https://arxiv.org/abs/2607.14169) · [code](https://github.com/JaviMaligno/code-world-models)

- **Type / date:** Paper / 2026-07-15.
- **Method:** Analyzes why accurate replay of sampled transitions can still leave a programmatic model unsuitable for play.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** LLM合成程序＋经典规划；摘要报告GPT-5.x
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2607.14169).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 平均状态转移准确率可能漏掉决定规划胜负的稀有规则。

**方法：** 构造程序世界通过采样检验但导致规划失败的情形，分析规则稀有度、验证覆盖与实际游戏代价。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="e03"></a>

## GameCraft-Bench: Can Agents Build Playable Games End-to-End in a Real Game Engine?

[paper](https://arxiv.org/abs/2606.17861) · [project](https://tongxuluo.github.io/gamecraft-bench-website)

- **Type / date:** Paper / 2026-06-16.
- **Method:** Evaluates whether agents build complete, playable game-engine projects that satisfy specified requirements.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** Opus-4.7（Claude Code）、GPT-5.5（Codex）、MiMo-V2.5-Pro、DeepSeek-V4-Pro、Kimi-K2.6、GLM-5.1、MiniMax-M2.7
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2606.17861).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 单文件小游戏或编译率不能代表真实引擎中端到端构建可玩游戏的能力。

**方法：** 在同一真实引擎接口下运行140项任务，用需求、行为和产物检查评价完整游戏，控制agent预算和工具权限。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="e02"></a>

## WorldCoder-Bench: Benchmarking Physically Grounded 3D World Synthesis

[paper](https://arxiv.org/abs/2606.01869)

- **Type / date:** Paper / 2026-06-01.
- **Method:** Tests 3D world generation with hidden-state probes and executable behavior checks.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** GPT-5.4、Gemini-3.1-Pro、Claude-Opus-4.6、Qwen3.6-Plus、DeepSeek-V3.2/V4-Flash、Kimi-K2.5; GPT-5.4 source judge
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2606.01869).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 截图好看或代码能运行，不能证明物理属性和动态行为真的实现。

**方法：** 构造2,026项3D世界任务，用StateProbe读取约定状态并执行动作测试，区分结构、affordance、状态和转移覆盖。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="n033"></a>

## MBench: A Comprehensive Benchmark on Memory Capability for Video World Models

[paper](https://arxiv.org/abs/2606.00793) · [project](https://peanutup.github.io/MBench-project)

- **Type / date:** Paper / 2026-05-30.
- **Method:** Evaluates memory of entities, environments, and causal relations in video world models.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** 基准；非生成骨干
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2606.00793).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 视觉质量分数不足以刻画长期世界记忆。

**方法：** 把记忆分为实体、环境、因果三个层次共12子维度，结合规则指标与VLM评估。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="n035"></a>

## WBench: A Comprehensive Multi-turn Benchmark for Interactive Video World Model Evaluation

[paper](https://arxiv.org/abs/2605.25874) · [code](https://github.com/meituan-longcat/WBench) · [project](https://meituan-longcat.github.io/WBench)

- **Type / date:** Paper / 2026-05-25.
- **Method:** Tests interactive world generation across navigation, actions, event edits, and viewpoint changes.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** 基准；专用视觉模型＋多模态裁判
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2605.25874).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 现有单段测试不能系统评价多轮互动。

**方法：** 289案例、1058轮，覆盖导航、主体动作、事件编辑与视角切换；22子指标按五维度汇总。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="u063"></a>

## GameGen-Verifier: Parallel Keypoint-Based Verification for LLM-Generated Games via Runtime State Injection

[paper](https://arxiv.org/abs/2605.07442)

- **Type / date:** Paper / 2026-05-08.
- **Method:** Injects runtime states to verify mechanics of generated games through targeted execution checks.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2605.07442).

<a id="u067"></a>

## iWorld-Bench: A Benchmark for Interactive World Models with a Unified Action Generation Framework

[paper](https://arxiv.org/abs/2605.03941)

- **Type / date:** Paper / 2026-05-05.
- **Method:** Compares interactive world models using standardized actions and interaction tasks.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2605.03941).

<a id="e01"></a>

## GameDevBench: Evaluating Agentic Capabilities Through Game Development

[paper](https://arxiv.org/abs/2602.11103)

- **Type / date:** Paper / 2026-02-11.
- **Method:** Evaluates multimodal coding agents on game-development tasks grounded in runnable projects.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** Claude Haiku/Sonnet 4.5、Gemini 3 Flash/Pro、GPT-5.4 Mini/5.4、Qwen3.5-397B、Kimi K2.5; Claude Code、Codex、Gemini CLI、OpenHands等
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2602.11103).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 一般代码基准缺少图形编辑、引擎操作和多模态反馈，难评价真实游戏开发agent。

**方法：** 从教程构造132项任务，在游戏工程中考察代码、场景和编辑操作，并比较视频/MCP反馈及不同harness。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t015"></a>

## EgoControl: Controllable Egocentric Video Generation via 3D Full-Body Poses

[paper](https://arxiv.org/abs/2511.18173)

- **Type / date:** Paper / 2025-11-22.
- **Method:** Evaluation reference: measures camera-motion errors and visible-body control with tracked arm masks and presence checks.
- **Scope:** Included for its camera/body evaluation protocol (Section 4.1), not classified as an executable-world construction or engine-rendering method.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2511.18173).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 具身第一视角视频需要明确区分身体动作与相机变化。

**方法：** 用3D全身姿态表示全局相机动态和关节运动，以专用控制模块约束未来帧预测。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="u076"></a>

## VBench-2.0: Advancing Video Generation Benchmark Suite for Intrinsic Faithfulness

[paper](https://arxiv.org/abs/2503.21755) · [code](https://github.com/Vchitect/VBench) · [project](https://vchitect.github.io/VBench-2.0-project)

- **Type / date:** Paper / 2025-03-27.
- **Method:** Evaluates video-generation capabilities including control, human fidelity, physics, and commonsense.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2503.21755).

<a id="videophy2"></a>

## VideoPhy-2: A Challenging Action-Centric Physical Commonsense Evaluation in Video Generation

[paper](https://arxiv.org/abs/2503.06800) · [code](https://github.com/Hritikbansal/videophy/tree/main/VIDEOPHY2) · [project](https://videophy2.github.io/)

- **Type / date:** Paper / 2025-03-09.
- **Method:** Evaluates action-centered physical commonsense, semantic adherence, and individual physical rules in generated video.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2503.06800).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 补充通用画质测量，检查生成视频是否符合动作和物理常识。

**方法：** 以动作和物理规则组织测试，结合人工评价和自动评判器。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t038"></a>

## 3DTrajMaster: Mastering 3D Trajectory for Multi-Entity Motion in Video Generation

[paper](https://arxiv.org/abs/2412.07759) · [project](https://fuxiao0719.github.io/projects/3dtrajmaster)

- **Type / date:** Paper / 2024-12-10.
- **Method:** Evaluation reference: compares requested and estimated human trajectories using rotation and translation errors.
- **Scope:** Included for its 3D trajectory evaluation protocol (Section 4.3), not because 6DoF pose conditioning alone establishes an executable world.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2412.07759).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 2D控制难表达多实体三维平移与旋转。

**方法：** 以每个实体6DoF轨迹和参考作为条件，gated object injector注入运动；UE多视角数据、domain adapter和退火采样支持训练泛化。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t025"></a>

## How Far is Video Generation from World Model: A Physical Law Perspective

[paper](https://arxiv.org/abs/2411.02385) · [project](https://phyworld.github.io)

- **Type / date:** Paper / 2024-11-04.
- **Method:** Uses controlled physical simulations to analyze video models under distribution shift and composition.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** 视频扩散；物理可控2D数据试验台
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2411.02385).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 分布内预测好不代表学到了可外推物理规律。

**方法：** 用受经典力学控制的2D模拟数据，测试分布内、分布外与组合泛化并做缩放分析。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="u077"></a>

## VideoPhy: Evaluating Physical Commonsense for Video Generation

[paper](https://arxiv.org/abs/2406.03520)

- **Type / date:** Paper / 2024-06-05.
- **Method:** Measures semantic adherence and physical commonsense in generated videos.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2406.03520).

<a id="u078"></a>

## VBench: Comprehensive Benchmark Suite for Video Generative Models

[paper](https://arxiv.org/abs/2311.17982) · [code](https://github.com/Vchitect/VBench) · [project](https://vchitect.github.io/VBench-project)

- **Type / date:** Paper / 2023-11-29.
- **Method:** Measures video quality and condition consistency through separately defined evaluation dimensions.
- **Scope:** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2311.17982).
