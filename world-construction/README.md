# World Construction & Recovery

[← Main collection](../README.md) · [Scope](../docs/SCOPE.md) · [Verification](../docs/VERIFICATION.md)

Scene programs, editable environments, articulated assets, and simulation-ready reconstruction.

The identity/source check and the depth of technical reading are separate fields. The notes below summarize prior targeted reading; they do not report a new reproduction.

<a id="t002"></a>

## Code2Worlds-2: Physically Plausible Agent Harness for Embodied World Simulation

[paper](https://arxiv.org/abs/2610.17651) · [code](https://github.com/AIGeeksGroup/Code2Worlds-2) · [project](https://aigeeksgroup.github.io/Code2Worlds-2)

- **Type / date:** Paper / 2026-10-13.
- **Method:** Compiles generated scenes into MuJoCo-compatible worlds and refines physical settings with simulator feedback.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** Blender / Infinigen；CoACD；MuJoCo；VLM确切检查点本轮未确认
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2610.17651).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 可渲染4D资产还需要碰撞、物性、关节和运行验证才能用于具身仿真。

**方法：** 保留Code2Worlds生成器，增加SimReady编译器与仿真反馈精修：CoACD碰撞分解、物性与支撑估计、重力稳定、MJCF及MuJoCo状态检查。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b22"></a>

## VETR: Execution-Grounded Self-Improving Agent for Symbolic Graphics Reasoning

[paper](https://arxiv.org/abs/2610.13098)

- **Type / date:** Paper / 2026-10-09.
- **Method:** Uses execution-grounded verification and program revisions for symbolic graphics reasoning.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** GPT-5.6 Luna、Qwen3.8-27B; Blender环境与程序检查
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2610.13098).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** VLM生成图形程序容易在符号/空间关系上出错，单纯视觉打分缺少定位依据。

**方法：** 让agent执行Blender代码，读取执行结果及视觉反馈，验证几何约束并修正图形推理与编辑。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b20"></a>

## USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation

[paper](https://arxiv.org/abs/2610.11322) · [project](https://xingyoujun.github.io/usdcraft)

- **Type / date:** Paper / 2026-10-08.
- **Method:** Produces articulated USD assets with geometry-grounded programs and simulation-relevant physical properties.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** GPT-5.6 Sol（high）、GPT-6 Astra（low）; Claude Opus 5、Gemini 3.8 Flash; USD/Isaac Sim
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2610.11322).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 仅依靠图像外观生成资产，常忽略尺寸、轴向、关节范围和仿真可用性。

**方法：** 读取度量几何证据，编写并执行建模程序，通过几何测量反复复核，产出带物理/关节属性的USD资产。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b19"></a>

## EnvDreamer: Large-Scale Multimodal-to-Environment Generation for Embodied AI

[paper](https://arxiv.org/abs/2610.04301)

- **Type / date:** Paper / 2026-10-03.
- **Method:** Converts multimodal specifications into Unreal Engine environments and associated embodied tasks.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** 论文表述为GPT-5-class vLLM backend; Unreal Engine 5
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2610.04301).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 大规模具身研究需要从文本、图像等输入快速获得任务相关的可执行环境。

**方法：** 解析多模态需求，规划资产与空间，经Unreal Engine控制接口生成环境、任务和验证记录。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="p03"></a>

## Asking the World: Generalist Physical Reasoning through Agentic World Modeling and Probing

[paper](https://arxiv.org/abs/2609.39135)

- **Type / date:** Paper / 2026-09-30.
- **Method:** Constructs video-grounded multiphysics worlds and actively probes them to answer physical questions.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** Gemini 3 Flash; PolyWorld Engine; 方法不要求对LLM微调
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2609.39135).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** VLM直接给出物理结论缺少可运行的检验，复杂问题需要模拟和主动探测。

**方法：** agent在PolyWorld中构建场景、估计参数，执行模拟与反事实干预，把探测结果反馈给推理。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b21"></a>

## Real2Gym: Building Gyms from Videos, Bringing Skills to Robots

[paper](https://arxiv.org/abs/2609.37089) · [project](https://real2gym.github.io)

- **Type / date:** Paper / 2026-09-29.
- **Method:** Recovers interactive training environments from videos and uses them to support robot skill learning.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** GPT-6 Astra（medium）; SAM3; Contact-GraspNet; GPT-6 Astra（high）
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2609.37089).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 真实视频中的场景和操作难直接变成机器人可练习、可迁移的仿真任务。

**方法：** 从视频解析对象与交互，生成Blender/MuJoCo场景和gym接口，在重建环境中抽取、执行和学习技能。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="p02"></a>

## EMPIRIC: Experiment-Driven Learning of Residual World Models for Robot Planning

[paper](https://arxiv.org/abs/2609.35047) · [project](https://yichao-liang.github.io/empiric)

- **Type / date:** Paper / 2026-09-28.
- **Method:** Extends a physics engine with learned residual programs and identifies missing mechanisms through experiments.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** Claude Opus 5（high）; 贝叶斯参数与隐状态推断; 物理引擎＋Python残差
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2609.35047).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 现有物理引擎可能遗漏任务特有力、约束和隐状态；仅调已有参数不足以解释真实观察。

**方法：** 合成Python残差机制补充引擎，以贝叶斯推断识别参数和状态，再主动选择区分机制的实验，服务机器人规划。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b18"></a>

## Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs

[paper](https://arxiv.org/abs/2609.11499)

- **Type / date:** Paper / 2026-09-10.
- **Method:** Recursively composes scene programs while using rendered comparisons to preserve global structure.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** GPT-6 Astra，经coding CLI运行，high reasoning; 递归scene programs
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2609.11499).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 复杂世界一次生成代码容易丢全局关系；单独优化局部又可能破坏整体。

**方法：** 将世界拆成递归程序节点，执行global/local/global构建与渲染比较，在局部细化时维护全局空间约束。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="p01"></a>

## Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning

[paper](https://arxiv.org/abs/2608.27549) · [code](https://github.com/MirroS-Lab/Code-as-World) · [project](https://mirros-lab.github.io/code-as-world)

- **Type / date:** Paper / 2026-08-27.
- **Method:** Proposes, executes, renders, and revises world-program hypotheses for quantitative physical reasoning.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** SAM3、VGGT-Omega、SAM3D; Code-as-World-VL-4B/9B/27B; 发现agent及学生初始化checkpoint
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2608.27549).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 视频中的物理知识难直接量化和验证，需构造能运行、能测量的世界表示。

**方法：** agent从文本/视频构造并验证物理程序，再生成同步视频、状态及问答，用图像测量SFT和世界监督GRPO训练VLM。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b17"></a>

## PhyScene3D: Physically Consistent Interactive 3D Tabletop Scene Generation

[paper](https://arxiv.org/abs/2606.01649)

- **Type / date:** Paper / 2026-06-01.
- **Method:** Assembles interactive tabletop scenes using geometric placement and physics-based refinement.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** Qwen3-VL-8B; SFT＋GRPO/LoRA; GPT-4o
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2606.01649).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 生成位置和朝向的模型容易产生悬浮、穿插或不可交互的桌面场景。

**方法：** 先分层规划容器与AABB布局，用SDF对齐真实几何；通过物理奖励训练和测试时优化提高有效性。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b16"></a>

## SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects

[paper](https://arxiv.org/abs/2605.19587) · [project](https://scene-code.github.io)

- **Type / date:** Paper / 2026-05-19.
- **Method:** Builds editable indoor-scene programs with articulated objects, execution repair, and explicit scene-state registration.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** VLM planner/checker/constructor; Blender与SDF资产管线
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2605.19587).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 静态检索资产或整体网格难保证内部结构、部件编辑和关节编译。

**方法：** 生成ObjectPlan，按对象类别路由建模提示，逐部件合成Blender程序并执行修复；注册场景状态并导出仿真资产。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t034"></a>

## Real2Sim in HOI: Toward Physically Plausible HOI Reconstruction from Monocular Videos

[paper](https://arxiv.org/abs/2605.14462) · [project](https://knoxzhao.github.io/real2sim_in_HOI)

- **Type / date:** Paper / 2026-05-14.
- **Method:** Recovers human-object motion and projects it into physics-based simulation for more stable interaction rollouts.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** HA-HOI；人体／对象重建＋物理模拟
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2605.14462).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 视觉上连贯的人物和对象轨迹未必能在物理仿真中保持接触与功能。

**方法：** human-first、object-follow重建与对齐交互，再把运动学轨迹投射到物理人体—对象模拟中形成稳定rollout。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b15"></a>

## ChronoAgentic: A Code-based Multi-Agent World Simulator for Physically Grounded Simulation Construction

[paper](https://arxiv.org/abs/2605.14398) · [project](https://uwsbel.github.io/chrono-agentic-website)

- **Type / date:** Paper / 2026-05-14.
- **Method:** Constructs PyChrono simulations and repairs them using both rendered evidence and deterministic physical checks.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** Claude Opus 5; Gemini 2.5 Pro; NanoBanana或GPT Image 1.5→SAM3D; PyChrono
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2605.14398).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 直接生成看似合理的动画不保证受力和约束有效，需要物理执行及视觉证据共同验证。

**方法：** 多agent生成PyChrono代码，以确定性物理检查与视觉反馈修复；需要时通过图像生成和3D重建补充资产。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="g03"></a>

## CreativeGame:Toward Mechanic-Aware Creative Game Generation

[paper](https://arxiv.org/abs/2604.19926)

- **Type / date:** Paper / 2026-04-21.
- **Method:** Generates playable games using mechanic planning, prior design traces, and execution-based feedback.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** 作者报告Kimi与GPT-class后端; 机制计划、记忆和执行验证
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2604.19926).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** LLM游戏生成容易重复已有模板，单纯LLM创意打分又可能饱和且不可验证。

**方法：** 显式规划游戏机制，记录跨代lineage记忆，以运行信号和程序化奖励筛选迭代结果，结合测试与反思生成HTML5游戏。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="g02"></a>

## OpenGame: Open Agentic Coding for Games

[paper](https://arxiv.org/abs/2604.18394)

- **Type / date:** Paper / 2026-04-20.
- **Method:** Organizes game coding, tool use, debugging, and interactive evaluation into an agentic development workflow.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** GameCoder-27B，基于Qwen3.5-27B，CPT＋SFT＋RL; Claude Sonnet 4.6等; Phaser 3
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2604.18394).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 通用coding agent对游戏API、工程结构和交互验证的支持不足。

**方法：** 将任务规划、模板、工具调用和迭代验证组织成开发流程；训练GameCoder，并通过执行反馈优化模型。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t035"></a>

## V-Dreamer: Automating Robotic Simulation and Trajectory Synthesis via Video Generation Priors

[paper](https://arxiv.org/abs/2603.18811)

- **Type / date:** Paper / 2026-03-19.
- **Method:** Builds simulation-ready scenes and converts video motion proposals into executable robot demonstrations.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** LLM＋3D生成；视频先验；CoTracker3；VGGT
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2603.18811).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 机器人仿真环境和专家行为通常依赖固定资产与人工启发式。

**方法：** 从语言生成几何约束下的仿真场景，再用视频模型提出运动，以CoTracker3和VGGT对齐成可执行机器人轨迹并训练策略。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b14"></a>

## Code2Worlds: Empowering Coding LLMs for 4D World Generation

[paper](https://arxiv.org/abs/2602.11757) · [code](https://github.com/AIGeeksGroup/Code2Worlds) · [project](https://aigeeksgroup.github.io/Code2Worlds)

- **Type / date:** Paper / 2026-02-12.
- **Method:** Separates object creation from environment orchestration and iteratively revises dynamic scene programs.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** Gemini 3，覆盖生成、选择、规划和critic角色; GPT-4o，不能写成生成骨干
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2602.11757).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 复杂动态场景同时涉及对象外形和环境运动，单个长脚本难协调并修正时序。

**方法：** 分离对象建模和环境编排，多个角色生成脚本与运动参数，结合渲染/运动critic反馈迭代。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="n048"></a>

## SPARK: Sim-ready Part-level Articulated Reconstruction with VLM Knowledge

[paper](https://arxiv.org/abs/2512.01629)

- **Type / date:** Paper / 2025-12-01.
- **Method:** Combines visual-language knowledge, part generation, and kinematic refinement to recover simulation-ready articulated objects.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2512.01629).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 单图重建出的形状通常缺少可仿真的部件关节。

**方法：** VLM生成结构图与部件参考，扩散DiT生成部件和整体形状，再以可微运动学／渲染优化URDF。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="n030"></a>

## RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation

[paper](https://arxiv.org/abs/2506.18088) · [code](https://github.com/robotwin-Platform/robotwin) · [project](https://robotwin-platform.github.io)

- **Type / date:** Paper / 2025-06-22.
- **Method:** Builds diverse bimanual manipulation data with generated task programs and simulation-based correction.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** MLLM；RoboTwin仿真与对象库
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2506.18088).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 双臂任务生成缺少可扩展程序和足够场景变化。

**方法：** MLLM生成任务执行代码并在仿真中修正；沿五个维度做结构化域随机化，提供50任务和对象库。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t024"></a>

## PhysGen3D: Crafting a Miniature Interactive World from a Single Image

[paper](https://arxiv.org/abs/2503.20746) · [project](https://by-luckk.github.io/PhysGen3D)

- **Type / date:** Paper / 2025-03-26.
- **Method:** Reconstructs an image into an interactive miniature scene whose responses can be simulated under changed initial conditions.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** 单图感知／3D重建＋物理仿真＋渲染；具体组件待精读
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2503.20746).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 单图未来交互需要先估计可操作几何与物性。

**方法：** 恢复对象形状、姿态、物理和光照属性，建立可交互3D场景，物理模拟后渲染受用户初始条件控制的视频。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="n026"></a>

## PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos

[paper](https://arxiv.org/abs/2503.17973) · [project](https://jianghanxiao.github.io/phystwin-web)

- **Type / date:** Paper / 2025-03-23.
- **Method:** Fits deformable-object geometry, appearance, and physical parameters to videos for interactive simulation.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** 弹簧质点模拟；Gaussian splats
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2503.17973).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 可变形对象的视觉重建不能直接支持新交互。

**方法：** 结合弹簧质点物理、形状先验与Gaussian splats，通过多阶段逆建模拟合几何、物性和外观。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t027"></a>

## UnrealZoo: Enriching Photo-realistic Virtual Worlds for Embodied AI

[paper](https://arxiv.org/abs/2412.20977)

- **Type / date:** Paper / 2024-12-30.
- **Method:** Provides Unreal Engine worlds and interaction interfaces for embodied data collection and evaluation.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** Unreal Engine；UnrealCV
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2412.20977).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 具身研究需要多样且可交互的高保真环境与观测接口。

**方法：** 提供Unreal世界、可玩实体以及扩展UnrealCV的数据收集、并行交互和评测接口。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t026"></a>

## Scene Co-pilot: Procedural Text to Video Generation with Human in the Loop

[paper](https://arxiv.org/abs/2411.18644) · [project](https://abolfazl-sh.github.io/Scene_co-pilot_site)

- **Type / date:** Paper / 2024-11-26.
- **Method:** Supports human-guided scene generation and editing through procedural commands and Blender execution.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** LLM；程序化3D生成器；Blender
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2411.18644).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 直接像素生成不便精确编辑场景与镜头。

**方法：** Scene Codex将文本转换为程序化生成命令，BlenderGPT支持编辑，用户在Blender中检视和修改场景并输出视频。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="s103"></a>

## PhysMotion: Physics-Grounded Dynamics From a Single Image

[paper](https://arxiv.org/abs/2411.17189) · [project](https://supertan0204.github.io/physmotion_website)

- **Type / date:** Paper / 2024-11-26.
- **Method:** Simulates reconstructed objects and refines their rendered dynamics with a video diffusion model.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** Stable Diffusion、ControlNet、LoRA；MiDaS用于深度。
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2411.17189).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 单图动画需要受外力／力矩驱动，同时保持画面细节。

**方法：** 重建3D Gaussian，执行MPM，再用跨帧注意力的扩散模型细化视频。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="s102"></a>

## Phys4DGen: Physics-Compliant 4D Generation with Multi-Material Composition Perception

[paper](https://arxiv.org/abs/2411.16800) · [project](https://jiajinglin.github.io/Phys4DGen)

- **Type / date:** Paper / 2024-11-25.
- **Method:** Infers material composition and uses multiphysics simulation to generate dynamic 4D objects.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** LGM、SAM2、GPT-4o、MPM；A40 48GB（§4.1.1）。
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2411.16800).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 物理4D生成中多材料组成与物性设定难以自动处理。

**方法：** 分割材料区域，推断内部机械结构和材料属性，交由MPM生成动态。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b13"></a>

## The Scene Language: Representing Scenes with Programs, Words, and Embeddings

[paper](https://arxiv.org/abs/2410.16770)

- **Type / date:** Paper / 2024-10-22.
- **Method:** Combines programs, language, and visual embeddings to represent scene structure, semantics, and appearance.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** Claude 3.5 Sonnet; 程序、文本和embedding; 多后端，不能把单一扩散模型视为全部方法
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2410.16770).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 仅程序难表达开放语义，仅文本难表达精确层级，需统一结构、语义和对象身份。

**方法：** 用Python程序组织层级和重复，用自然语言描述内容，用embedding绑定视觉身份；从文本/图像推断并接多种渲染器。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="n025"></a>

## Articulate-Anything: Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model

[paper](https://arxiv.org/abs/2410.13882) · [project](https://articulate-anything.github.io)

- **Type / date:** Paper / 2024-10-03.
- **Method:** Generates and revises articulation code to turn multimodal object descriptions into simulator-compatible digital twins.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** Gemini 1.5 Flash；CLIP；CoTracker；PyBullet / SAPIEN
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2410.13882).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 从视觉输入获得可操作关节资产需要复杂人工建模。

**方法：** 检索部件并生成link和joint代码；actor-critic用渲染反馈与运动轨迹逐步修正。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="g01"></a>

## DreamGarden: A Designer Assistant for Growing Games from a Single Prompt

[paper](https://arxiv.org/abs/2410.01791)

- **Type / date:** Paper / 2024-10-02.
- **Method:** Decomposes a game concept into inspectable development plans and specialized implementation steps.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** GPT-4o; Unreal Engine; 游戏制作助手，不含专门视频生成骨干
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2410.01791).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 单轮提示难直接得到完整游戏，设计者需要可理解、可干预的生成过程。

**方法：** 递归拆解高层游戏想法，组织实现模块与任务，调用工具逐步构建Unreal游戏，允许用户介入调整。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b12"></a>

## SceneMotifCoder: Example-driven Visual Program Learning for Generating 3D Object Arrangements

[paper](https://arxiv.org/abs/2408.02211) · [project](https://3dlg-hcvc.github.io/smc)

- **Type / date:** Paper / 2024-08-05.
- **Method:** Learns compact arrangement programs from examples and reuses them to generate new object configurations.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** GPT-4-Vision-Preview、GPT-4-Turbo; GPT-4o
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2408.02211).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 少量例子往往包含重复、对称或层级布局规律，直接复制坐标缺少可编辑性和泛化。

**方法：** 由示例识别arrangement motif，抽象成参数化程序，再实例化并检索对象资产，生成相似结构的新布局。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b11"></a>

## Infinigen Indoors: Photorealistic Indoor Scenes using Procedural Generation

[paper](https://arxiv.org/abs/2406.11824)

- **Type / date:** Paper / 2024-06-17.
- **Method:** Extends procedural world generation to indoor assets and constraint-based scene arrangement.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** 程序化资产生成器＋约束式布局求解; 无需LLM/扩散模型作为核心
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2406.11824).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 希望程序生成器覆盖逼真的室内资产与布置，同时保留几何和语义真值。

**方法：** 程序化构造家具及材质，通过约束定义支撑、碰撞和房间关系，求解布局并用Blender渲染。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="n028"></a>

## Real2Code: Reconstruct Articulated Objects via Code Generation

[paper](https://arxiv.org/abs/2406.08474)

- **Type / date:** Paper / 2024-06-12.
- **Method:** Recovers articulated structure from visual evidence and generates executable joint and link descriptions.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** CodeLlama-7B；SAM；形状补全网络
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2406.08474).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 关节参数直接回归和复杂提示难以扩展到多部件对象。

**方法：** 从多视角分割和形状补全获取部件OBB，微调代码模型以轴／边选择生成关节MJCF。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b10"></a>

## BlenderAlchemy: Editing 3D Graphics with Vision-Language Models

[paper](https://arxiv.org/abs/2404.17672)

- **Type / date:** Paper / 2024-04-26.
- **Method:** Searches over Blender edits using visual-language feedback to revise scene geometry, materials, and lighting.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** GPT-4V; Blender; 不需要视频扩散模型
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2404.17672).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 用户难用底层材质节点或几何参数表达目标修改，单次VLM代码编辑也不稳定。

**方法：** VLM提出候选Blender编辑，以渲染图像反馈搜索和筛选操作，迭代改变几何、材质及灯光。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t032"></a>

## PhysDreamer: Physics-Based Interaction with 3D Objects via Video Generation

[paper](https://arxiv.org/abs/2404.13026) · [project](https://physdreamer.github.io)

- **Type / date:** Paper / 2024-04-19.
- **Method:** Uses video-generation priors to infer physical properties for explicit simulation of object interactions.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** 预训练视频先验＋物理仿真；具体组件待精读
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2404.13026).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 静态3D对象缺少能响应新力或操作的材料动态。

**方法：** 从预训练视频先验蒸馏物理属性，使显式物理对象可在新交互下模拟响应。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b24"></a>

## Video2Game: Real-time, Interactive, Realistic and Browser-Compatible Environment from a Single Video

[paper](https://arxiv.org/abs/2404.09833) · [project](https://video2game.github.io)

- **Type / date:** Paper / 2024-04-15.
- **Method:** Converts a scene video into an interactive environment that can run in a browser.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** NeRF及网格/材质转换; 浏览器渲染与物理引擎; 不是核心必要模块
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2404.09833).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** NeRF重建通常只能看，难直接编辑、碰撞或在浏览器实时交互。

**方法：** 从单视频重建神经场，转为网格和可实时渲染材质，配置物理与交互，导出浏览器环境。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b09"></a>

## PhyScene: Physically Interactable 3D Scene Synthesis for Embodied AI

[paper](https://arxiv.org/abs/2404.09465) · [project](https://physcene.github.io)

- **Type / date:** Paper / 2024-04-15.
- **Method:** Generates layouts with collision, room-boundary, and interaction constraints for embodied simulation.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** 条件布局扩散模型＋物理/可达性guidance; 不是方法必要模块
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2404.09465).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 视觉合理的布局可能碰撞、堵路或阻碍关节开启，不适合具身agent交互。

**方法：** 在布局扩散采样时加入碰撞、房间边界、可达性及交互性指导，结合关节对象构造可操作场景。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b08"></a>

## SceneScript: Reconstructing Scenes With An Autoregressive Structured Language Model

[paper](https://arxiv.org/abs/2403.13064)

- **Type / date:** Paper / 2024-03-19.
- **Method:** Reconstructs editable scenes as autoregressively generated structured language commands.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** 专门训练的encoder–decoder自回归Transformer; SceneScript结构token; 不是直接调用GPT生成通用代码
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2403.13064).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 纯点云/网格不便语义编辑；希望感知系统直接输出对象与建筑结构。

**方法：** 用自回归结构语言模型将感知输入转为场景命令序列，表示墙、门窗与对象，并支持编辑和扩展。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b07"></a>

## SceneCraft: An LLM Agent for Synthesizing 3D Scene as Blender Code

[paper](https://arxiv.org/abs/2403.01248)

- **Type / date:** Paper / 2024-03-02.
- **Method:** Produces Blender scene programs, refines them using rendered feedback, and learns reusable scene-building functions.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** GPT-4V; Blender Python; 可复用场景函数
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2403.01248).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 逐次从零生成场景脚本容易出错，也难积累可复用的构造经验。

**方法：** agent生成Blender Python并渲染观察，迭代修正脚本；将成功实现归纳为函数库用于后续任务。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b05"></a>

## Holodeck: Language Guided Generation of 3D Embodied AI Environments

[paper](https://arxiv.org/abs/2312.09067)

- **Type / date:** Paper / 2023-12-14.
- **Method:** Translates language into embodied environments through floor planning, asset retrieval, and spatial constraint solving.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** GPT-4; GPT-4V; AI2-THOR与Objaverse资产
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2312.09067).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 现有室内环境分布有限，难按任意用途和空间需求生成可交互场景。

**方法：** LLM从描述规划房间与空间约束，检索3D资产并优化布置，产出AI2-THOR环境。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b04"></a>

## RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation

[paper](https://arxiv.org/abs/2311.01455)

- **Type / date:** Paper / 2023-11-02.
- **Method:** Generates simulation tasks, scene layouts, and learning supervision for robot skill acquisition.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** GPT-4; Objaverse/PartNet-Mobility等来源; 任务相关RL/规划器，无统一视频骨干
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2311.01455).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 机器人任务、资产布局和奖励长期依赖人工，限制仿真数据规模和任务覆盖。

**方法：** LLM提出任务，配置资产、尺度、关节和布局，再生成奖励或选择学习路径，以强化学习/运动规划获取行为。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b23"></a>

## GenSim: Generating Robotic Simulation Tasks via Large Language Models

[paper](https://arxiv.org/abs/2310.01361) · [code](https://github.com/liruiw/GenSim) · [project](https://liruiw.github.io/gensim) · [data](https://huggingface.co/spaces/Gen-Sim/Gen-Sim)

- **Type / date:** Paper / 2023-10-02.
- **Method:** Generates robotic simulation-task code and demonstrations through language-model-guided task synthesis.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** GPT-4; CLIPort等机器人学习组件; 既有模拟后端
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2310.01361).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 机器人仿真任务和演示编写成本高，希望借LLM先验快速扩展任务集合。

**方法：** 给定已有API和示例，LLM编写任务与奖励代码，执行生成演示，并用任务数据训练机器人策略。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b03"></a>

## Infinite Photorealistic Worlds using Procedural Generation

[paper](https://arxiv.org/abs/2306.09310)

- **Type / date:** Paper / 2023-06-15.
- **Method:** Builds natural environments from procedural geometry, materials, and scene-generation rules.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** Blender程序化生成器与材质节点; 无需LLM/扩散模型作为生成前提
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2306.09310).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 扫描或人工制作资产限制多样性与真值标注，需从零生成可控的写实自然世界。

**方法：** 用程序规则生成几何、材质、植被及自然布局，并从场景直接取得几何与语义真值。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b02"></a>

## ProcTHOR: Large-Scale Embodied AI Using Procedural Generation

[paper](https://arxiv.org/abs/2206.06994)

- **Type / date:** Paper / 2022-06-14.
- **Method:** Procedurally assembles interactive houses for scalable embodied-agent training and evaluation.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** AI2-THOR; 程序规则与资产库; 场景生成核心不要求LLM
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2206.06994).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 具身策略训练受少量手工房屋限制，需要大规模且可交互的室内场景分布。

**方法：** 程序化采样房间拓扑、门、家具和小物体，检查布局后接入AI2-THOR，用生成环境训练与评价具身任务。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="b01"></a>

## Scenic: A Language for Scenario Specification and Scene Generation

[paper](https://arxiv.org/abs/1809.09310)

- **Type / date:** Paper / 2018-09-25.
- **Method:** Defines scene distributions with a probabilistic language and samples configurations subject to spatial constraints.
- **Scope:** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.
- **Models / representations in reading notes:** Scenic概率程序、约束和采样器; 原方法不要求LLM或视频生成模型
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/1809.09310).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 训练和测试需要覆盖受约束、低概率或危险场景，手动枚举场景既慢又难控制分布。

**方法：** 设计概率DSL描述空间关系、对象分布和软硬约束，通过约束采样生成可交给模拟器执行的场景。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>
