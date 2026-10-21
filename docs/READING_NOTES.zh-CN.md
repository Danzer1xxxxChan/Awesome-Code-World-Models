# Code World Models · 逐篇阅读笔记

[返回主页](../README.md) · [核验说明](VERIFICATION.md)

题录、来源与范围已于2026-10-22复核。下列motivation、方法与模型来自此前定向阅读，未宣称本轮对全部论文重新阅读全文或独立复现。

通用姿态/轨迹评测参考与完整方法分开归类；请查看每项scope说明。

## World Systems

### SolarRenderer: Few-Step Generative Reference Rendering
[paper](https://arxiv.org/abs/2610.28630) · [code](https://github.com/Enderfga/SolarRenderer) · [project](https://enderfga.cn/SolarRenderer/)

**Motivation：** 让同一渲染接口接受多种结构视频，并降低参考条件生成的采样成本。

**方法：** 结构视频编码为latent，放到与目标帧对应的RoPE位置；冻结H3，用控制LoRA和少步LoRA训练；提供四步全片与独立块因果版本。

**模型/表示：** MiniMax-H3；control LoRA＋few-step LoRA，少步初始化使用DMAD；SolarWM训练/推理框架，不是另一视频骨干

**范围与证据：** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.

### Mallea: Building, Steering, and Memorizing Worlds with Coding Agent
[paper](https://arxiv.org/abs/2610.21283) · [project](https://lxycopper.github.io/Mallea)

**Motivation：** 详见原始论文或官方说明。

**方法：** 按交互需要联合选择对象几何、属性和规则；以对象身份索引纹理记忆，并依状态变化保留或更新。

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.

### AgentGarten: Code Worlds for Evolving Agents
[paper](https://arxiv.org/abs/2610.12374) · [code](https://github.com/MirroS-Lab/AgentGarten) · [project](https://mirros-lab.github.io/agent-garten)

**Motivation：** 具身agent需要可扩展、可互动且视觉丰富的练习环境；单一引擎资产和渲染域限制环境多样性。

**方法：** 代码世界交给已有引擎执行，统一导出深度/法线；流式模型生成观测；以Adversarial Forcing处理生成历史，并组织agent练习循环。

**模型/表示：** Cosmos3-Nano；Wan 2.2 VAE

**范围与证据：** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.

### Oneira: From Open-Ended Generation to Open-World Interaction in Video World Models
[paper](https://arxiv.org/abs/2610.01614) · [project](https://madaoer.github.io/projects/oneira)

**Motivation：** 开放视觉生成需要将新对象纳入可操作状态，并保留先前交互后果。

**方法：** coding agent读取3D实例状态表并规划动作，引擎执行局部状态更新与相机路径渲染，MiniMax-H3生成视频，再从新画面注册对象。

**模型/表示：** MiniMax-H3 Ref2VA；LoRA

**范围与证据：** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.

### GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models
[paper](https://arxiv.org/abs/2609.25652) · [project](https://jimntu.github.io/gamedirector)

**Motivation：** 纯视觉模拟难以明确执行可配置的血量、冷却和NPC策略；作者将战斗逻辑放到外部模块。

**方法：** AttackNet识别命中，SituationNet估计局势；程序更新战斗状态，LLM选择合法boss动作，再用文本控制视频生成并叠加HUD。

**模型/表示：** Wan2.2-TI2V-5B；Gemma-4-E2B-it；ResNet-18＋单层GRU的AttackNet/SituationNet；GPT-5.5、Gemini-3.1-Pro

**范围与证据：** Explicit combat rules and states are in scope. This system does not claim a full 3D proxy or pixel-aligned trajectory interface.

### Code Plans, Diffusion Renders: Open-Ended Generative World Modeling
[paper](https://arxiv.org/abs/2609.26458) · [project](https://becauseimbatman0.github.io/CoDeR)

**Motivation：** 代码擅长空间规划和机制，视频擅长外观；作者希望二者合作构建可持续扩展的世界。

**方法：** Creator和Executors构造Three.js世界与角色；Artist把代理变成视频，再将生成外观注册回世界以支持后续视角和扩展。

**模型/表示：** GPT-6 Astra；MiniMax-H3＋LoRA/ControlNet；SMPL-H

**范围与证据：** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.

### Programmable World Model
[paper](https://arxiv.org/abs/2609.10540) · [code](https://github.com/AlayaLab/pwm) · [project](https://alaya-lab.github.io/pwm)

**Motivation：** 用低成本、可编程的实体表示控制交互结果，同时保留视频模型生成丰富细节的能力。

**方法：** 引擎推进带身份和语义的OBB状态，将其编译为空间控制图；以空间控制分支连接视频模型，并结合历史与几何记忆。

**模型/表示：** LingBot-World-v1＋Structured Spatial ControlNet；Qwen3-VL、ViPE、SAM3、WildDet3D

**范围与证据：** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.

### Code World Model: Coding Agent as World Brain
[paper](https://arxiv.org/abs/2608.25927) · [code](https://github.com/buaacyw/code-world-model) · [project](https://buaacyw.github.io/cwm/)

**Motivation：** 隐式视频预测难以直接编辑和检查持久的世界规则；作者希望把可执行状态与视觉表现解耦。

**方法：** coding agent基于现有引擎控制、碰撞和循环编写世界；运行后导出深度与语义ID代理，LoRA适配视频模型，首帧锚定外观。

**模型/表示：** GPT-5.6 Sol；GPT Image 2；MiniMax-H3 Ref2VA＋rank-128 LoRA

**范围与证据：** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.

### StreamRender-H3: Interactive Coding Worlds with Real-time Streaming Diffusion Render
[project](https://nvlabs.github.io/Sana/Sol-Engine/StreamRender-H3/)

**Motivation：** 代码世界已有高频、确定的交互状态，难点是让神经外观生成跟上实时输入。

**方法：** Three.js赛车引擎输出语义图；将H3适配为两步因果学生，结合流式推理、codec与运行时优化持续呈现画面。

**模型/表示：** MiniMax-H3 Ref2VA的两步因果蒸馏版本；Three.js，不是学习模型；不以固定coding LLM为渲染方法前提

**范围与证据：** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.

### Streaming Code World Model
[code](https://github.com/TingtingLiao/streaming-code-world-model)

**Motivation：** 在线代理条件到达时，不能预先访问未来条件；同时需降低长时漂移和采样成本。

**方法：** MiniMax-H3 上的滑动注意力与旋转 RoPE KV 缓存、带噪历史和4步蒸馏；作者 README 明确目前尚未实时。

**模型/表示：** MiniMax-H3；流式 LoRA 与4步DMD蒸馏

**范围与证据：** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.

### Roblox Reality: Hybrid Architecture for Photorealistic Multiplayer Gaming
[source](https://about.roblox.com/newsroom/2026/04/roblox-reality-hybrid-architecture-democratizing-photorealistic-multiplayer-gaming)

**Motivation：** 在保留多人一致状态和创作工具的同时降低高保真资产制作负担。

**方法：** 共享服务器推进世界，边缘端依渲染与3D上下文做super-upsampling，并讨论本地角色叠加和响应控制。

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** An official architecture description, not an independently reproduced end-to-end research benchmark.

### RenderFlow: Single-Step Neural Rendering via Flow Matching
[paper](https://studios.disneyresearch.com/2026/05/31/renderflow-single-step-neural-rendering-via-flow-matching/)

**Motivation：** 多步扩散渲染的随机性和计算量妨碍高效、稳定的图形管线。

**方法：** 以干净albedo latent为起点进行bridge／flow matching；G-buffer属性、环境光与可选稀疏关键帧通过不同适配器注入。

**模型/表示：** Wan2.1＋G-buffer / envmap / keyframe adapters

**范围与证据：** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.

### Matrix-Game 4.0
[paper](https://github.com/SkyworkAI/Matrix-Game/blob/main/Matrix-Game-4/docs/Matrix_Game_4_0.pdf) · [code](https://github.com/SkyworkAI/Matrix-Game/tree/main/Matrix-Game-4) · [project](https://matrix-game-v4-0.github.io/page/) · [data](https://huggingface.co/Skywork/Matrix-Game-4.0)

**Motivation：** 希望保留传统引擎的规则、控制和碰撞，同时通过生成模型提升低模画面。

**方法：** 原生C++/OpenGL低模游戏持续输出RGB条件；场景专用视频模型生成画面，质量与实时配置采用不同步数和解码器。

**模型/表示：** Wan2.2-TI2V-5B→Wan2.2-Fun-5B-Control→官方5B场景模型；UMT5、Wan2.2 VAE，实时路径另用TAEHV

**范围与证据：** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.

### EdenLive: Real-Time Generative Rendering from Any Visual Reference
[code](https://github.com/VAST-AI-Research/EdenLive)

**Motivation：** 代理可能来自不同引擎、画风和构建工具，作者希望减少对固定代理外观的依赖。

**方法：** 用proxy视觉编码器提取参考视频条件，结合首帧和文本训练渲染器；同时提供双向离线与四步chunk-AR路径。

**模型/表示：** Wan2.2-TI2V-5B、Wan2.1-I2V-14B；DINOv3及其派生编码器；FLUX.2 [klein] 9B

**范围与证据：** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.

### DLSS 5: Real-Time Neural Rendering with Generative AI
[source](https://research.nvidia.com/labs/adlr/DLSS5/)

**Motivation：** 希望在游戏的帧预算内补充高质量材质与照明细节，并保留引擎控制。

**方法：** 官方摘要描述像素空间单步扩散：推理接收RGB、运动向量、时间状态与艺术控制；场景属性用于训练一致性监督。

**模型/表示：** 单步像素空间扩散神经渲染器

**范围与证据：** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.

### Code Video Model
[paper](https://code-video-model.github.io/tech_report.pdf) · [code](https://github.com/code-video-model/CodeVideoModel) · [project](https://code-video-model.github.io/)

**Motivation：** 文本难以精确表达镜头和动作；可执行代码能提供可编辑、可复现的视频预演。

**方法：** GPT生成Three.js代理视频，配合首帧和文本输入冻结视频模型；默认20步采样的前5步使用代理，后续去噪释放外观自由度。

**模型/表示：** GPT-6；GPT-Image-2；MiniMax-H3

**范围与证据：** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.

## World Construction & Recovery

### Code2Worlds-2: Physically Plausible Agent Harness for Embodied World Simulation
[paper](https://arxiv.org/abs/2610.17651) · [code](https://github.com/AIGeeksGroup/Code2Worlds-2) · [project](https://aigeeksgroup.github.io/Code2Worlds-2)

**Motivation：** 可渲染4D资产还需要碰撞、物性、关节和运行验证才能用于具身仿真。

**方法：** 保留Code2Worlds生成器，增加SimReady编译器与仿真反馈精修：CoACD碰撞分解、物性与支撑估计、重力稳定、MJCF及MuJoCo状态检查。

**模型/表示：** Blender / Infinigen；CoACD；MuJoCo；VLM确切检查点本轮未确认

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### VETR: Execution-Grounded Self-Improving Agent for Symbolic Graphics Reasoning
[paper](https://arxiv.org/abs/2610.13098)

**Motivation：** VLM生成图形程序容易在符号/空间关系上出错，单纯视觉打分缺少定位依据。

**方法：** 让agent执行Blender代码，读取执行结果及视觉反馈，验证几何约束并修正图形推理与编辑。

**模型/表示：** GPT-5.6 Luna、Qwen3.8-27B；Blender环境与程序检查

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation
[paper](https://arxiv.org/abs/2610.11322) · [project](https://xingyoujun.github.io/usdcraft)

**Motivation：** 仅依靠图像外观生成资产，常忽略尺寸、轴向、关节范围和仿真可用性。

**方法：** 读取度量几何证据，编写并执行建模程序，通过几何测量反复复核，产出带物理/关节属性的USD资产。

**模型/表示：** GPT-5.6 Sol（high）、GPT-6 Astra（low）；Claude Opus 5、Gemini 3.8 Flash；USD/Isaac Sim

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### EnvDreamer: Large-Scale Multimodal-to-Environment Generation for Embodied AI
[paper](https://arxiv.org/abs/2610.04301)

**Motivation：** 大规模具身研究需要从文本、图像等输入快速获得任务相关的可执行环境。

**方法：** 解析多模态需求，规划资产与空间，经Unreal Engine控制接口生成环境、任务和验证记录。

**模型/表示：** 论文表述为GPT-5-class vLLM backend；Unreal Engine 5

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### Asking the World: Generalist Physical Reasoning through Agentic World Modeling and Probing
[paper](https://arxiv.org/abs/2609.39135)

**Motivation：** VLM直接给出物理结论缺少可运行的检验，复杂问题需要模拟和主动探测。

**方法：** agent在PolyWorld中构建场景、估计参数，执行模拟与反事实干预，把探测结果反馈给推理。

**模型/表示：** Gemini 3 Flash；PolyWorld Engine；方法不要求对LLM微调

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### Real2Gym: Building Gyms from Videos, Bringing Skills to Robots
[paper](https://arxiv.org/abs/2609.37089) · [project](https://real2gym.github.io)

**Motivation：** 真实视频中的场景和操作难直接变成机器人可练习、可迁移的仿真任务。

**方法：** 从视频解析对象与交互，生成Blender/MuJoCo场景和gym接口，在重建环境中抽取、执行和学习技能。

**模型/表示：** GPT-6 Astra（medium）；SAM3；Contact-GraspNet；GPT-6 Astra（high）

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### EMPIRIC: Experiment-Driven Learning of Residual World Models for Robot Planning
[paper](https://arxiv.org/abs/2609.35047) · [project](https://yichao-liang.github.io/empiric)

**Motivation：** 现有物理引擎可能遗漏任务特有力、约束和隐状态；仅调已有参数不足以解释真实观察。

**方法：** 合成Python残差机制补充引擎，以贝叶斯推断识别参数和状态，再主动选择区分机制的实验，服务机器人规划。

**模型/表示：** Claude Opus 5（high）；贝叶斯参数与隐状态推断；物理引擎＋Python残差

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs
[paper](https://arxiv.org/abs/2609.11499)

**Motivation：** 复杂世界一次生成代码容易丢全局关系；单独优化局部又可能破坏整体。

**方法：** 将世界拆成递归程序节点，执行global/local/global构建与渲染比较，在局部细化时维护全局空间约束。

**模型/表示：** GPT-6 Astra，经coding CLI运行，high reasoning；递归scene programs

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning
[paper](https://arxiv.org/abs/2608.27549) · [code](https://github.com/MirroS-Lab/Code-as-World) · [project](https://mirros-lab.github.io/code-as-world)

**Motivation：** 视频中的物理知识难直接量化和验证，需构造能运行、能测量的世界表示。

**方法：** agent从文本/视频构造并验证物理程序，再生成同步视频、状态及问答，用图像测量SFT和世界监督GRPO训练VLM。

**模型/表示：** SAM3、VGGT-Omega、SAM3D；Code-as-World-VL-4B/9B/27B；发现agent及学生初始化checkpoint

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### PhyScene3D: Physically Consistent Interactive 3D Tabletop Scene Generation
[paper](https://arxiv.org/abs/2606.01649)

**Motivation：** 生成位置和朝向的模型容易产生悬浮、穿插或不可交互的桌面场景。

**方法：** 先分层规划容器与AABB布局，用SDF对齐真实几何；通过物理奖励训练和测试时优化提高有效性。

**模型/表示：** Qwen3-VL-8B；SFT＋GRPO/LoRA；GPT-4o

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects
[paper](https://arxiv.org/abs/2605.19587) · [project](https://scene-code.github.io)

**Motivation：** 静态检索资产或整体网格难保证内部结构、部件编辑和关节编译。

**方法：** 生成ObjectPlan，按对象类别路由建模提示，逐部件合成Blender程序并执行修复；注册场景状态并导出仿真资产。

**模型/表示：** VLM planner/checker/constructor；Blender与SDF资产管线

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### Real2Sim in HOI: Toward Physically Plausible HOI Reconstruction from Monocular Videos
[paper](https://arxiv.org/abs/2605.14462) · [project](https://knoxzhao.github.io/real2sim_in_HOI)

**Motivation：** 视觉上连贯的人物和对象轨迹未必能在物理仿真中保持接触与功能。

**方法：** human-first、object-follow重建与对齐交互，再把运动学轨迹投射到物理人体—对象模拟中形成稳定rollout。

**模型/表示：** HA-HOI；人体／对象重建＋物理模拟

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### ChronoAgentic: A Code-based Multi-Agent World Simulator for Physically Grounded Simulation Construction
[paper](https://arxiv.org/abs/2605.14398) · [project](https://uwsbel.github.io/chrono-agentic-website)

**Motivation：** 直接生成看似合理的动画不保证受力和约束有效，需要物理执行及视觉证据共同验证。

**方法：** 多agent生成PyChrono代码，以确定性物理检查与视觉反馈修复；需要时通过图像生成和3D重建补充资产。

**模型/表示：** Claude Opus 5；Gemini 2.5 Pro；NanoBanana或GPT Image 1.5→SAM3D；PyChrono

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### CreativeGame:Toward Mechanic-Aware Creative Game Generation
[paper](https://arxiv.org/abs/2604.19926)

**Motivation：** LLM游戏生成容易重复已有模板，单纯LLM创意打分又可能饱和且不可验证。

**方法：** 显式规划游戏机制，记录跨代lineage记忆，以运行信号和程序化奖励筛选迭代结果，结合测试与反思生成HTML5游戏。

**模型/表示：** 作者报告Kimi与GPT-class后端；机制计划、记忆和执行验证

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### OpenGame: Open Agentic Coding for Games
[paper](https://arxiv.org/abs/2604.18394)

**Motivation：** 通用coding agent对游戏API、工程结构和交互验证的支持不足。

**方法：** 将任务规划、模板、工具调用和迭代验证组织成开发流程；训练GameCoder，并通过执行反馈优化模型。

**模型/表示：** GameCoder-27B，基于Qwen3.5-27B，CPT＋SFT＋RL；Claude Sonnet 4.6等；Phaser 3

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### V-Dreamer: Automating Robotic Simulation and Trajectory Synthesis via Video Generation Priors
[paper](https://arxiv.org/abs/2603.18811)

**Motivation：** 机器人仿真环境和专家行为通常依赖固定资产与人工启发式。

**方法：** 从语言生成几何约束下的仿真场景，再用视频模型提出运动，以CoTracker3和VGGT对齐成可执行机器人轨迹并训练策略。

**模型/表示：** LLM＋3D生成；视频先验；CoTracker3；VGGT

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### Code2Worlds: Empowering Coding LLMs for 4D World Generation
[paper](https://arxiv.org/abs/2602.11757) · [code](https://github.com/AIGeeksGroup/Code2Worlds) · [project](https://aigeeksgroup.github.io/Code2Worlds)

**Motivation：** 复杂动态场景同时涉及对象外形和环境运动，单个长脚本难协调并修正时序。

**方法：** 分离对象建模和环境编排，多个角色生成脚本与运动参数，结合渲染/运动critic反馈迭代。

**模型/表示：** Gemini 3，覆盖生成、选择、规划和critic角色；GPT-4o，不能写成生成骨干

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### SPARK: Sim-ready Part-level Articulated Reconstruction with VLM Knowledge
[paper](https://arxiv.org/abs/2512.01629)

**Motivation：** 单图重建出的形状通常缺少可仿真的部件关节。

**方法：** VLM生成结构图与部件参考，扩散DiT生成部件和整体形状，再以可微运动学／渲染优化URDF。

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation
[paper](https://arxiv.org/abs/2506.18088) · [code](https://github.com/robotwin-Platform/robotwin) · [project](https://robotwin-platform.github.io)

**Motivation：** 双臂任务生成缺少可扩展程序和足够场景变化。

**方法：** MLLM生成任务执行代码并在仿真中修正；沿五个维度做结构化域随机化，提供50任务和对象库。

**模型/表示：** MLLM；RoboTwin仿真与对象库

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### PhysGen3D: Crafting a Miniature Interactive World from a Single Image
[paper](https://arxiv.org/abs/2503.20746) · [project](https://by-luckk.github.io/PhysGen3D)

**Motivation：** 单图未来交互需要先估计可操作几何与物性。

**方法：** 恢复对象形状、姿态、物理和光照属性，建立可交互3D场景，物理模拟后渲染受用户初始条件控制的视频。

**模型/表示：** 单图感知／3D重建＋物理仿真＋渲染；具体组件待精读

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos
[paper](https://arxiv.org/abs/2503.17973) · [project](https://jianghanxiao.github.io/phystwin-web)

**Motivation：** 可变形对象的视觉重建不能直接支持新交互。

**方法：** 结合弹簧质点物理、形状先验与Gaussian splats，通过多阶段逆建模拟合几何、物性和外观。

**模型/表示：** 弹簧质点模拟；Gaussian splats

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### UnrealZoo: Enriching Photo-realistic Virtual Worlds for Embodied AI
[paper](https://arxiv.org/abs/2412.20977)

**Motivation：** 具身研究需要多样且可交互的高保真环境与观测接口。

**方法：** 提供Unreal世界、可玩实体以及扩展UnrealCV的数据收集、并行交互和评测接口。

**模型/表示：** Unreal Engine；UnrealCV

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### Scene Co-pilot: Procedural Text to Video Generation with Human in the Loop
[paper](https://arxiv.org/abs/2411.18644) · [project](https://abolfazl-sh.github.io/Scene_co-pilot_site)

**Motivation：** 直接像素生成不便精确编辑场景与镜头。

**方法：** Scene Codex将文本转换为程序化生成命令，BlenderGPT支持编辑，用户在Blender中检视和修改场景并输出视频。

**模型/表示：** LLM；程序化3D生成器；Blender

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### PhysMotion: Physics-Grounded Dynamics From a Single Image
[paper](https://arxiv.org/abs/2411.17189) · [project](https://supertan0204.github.io/physmotion_website)

**Motivation：** 单图动画需要受外力／力矩驱动，同时保持画面细节。

**方法：** 重建3D Gaussian，执行MPM，再用跨帧注意力的扩散模型细化视频。

**模型/表示：** Stable Diffusion、ControlNet、LoRA；MiDaS用于深度。

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### Phys4DGen: Physics-Compliant 4D Generation with Multi-Material Composition Perception
[paper](https://arxiv.org/abs/2411.16800) · [project](https://jiajinglin.github.io/Phys4DGen)

**Motivation：** 物理4D生成中多材料组成与物性设定难以自动处理。

**方法：** 分割材料区域，推断内部机械结构和材料属性，交由MPM生成动态。

**模型/表示：** LGM、SAM2、GPT-4o、MPM；A40 48GB（§4.1.1）。

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### The Scene Language: Representing Scenes with Programs, Words, and Embeddings
[paper](https://arxiv.org/abs/2410.16770)

**Motivation：** 仅程序难表达开放语义，仅文本难表达精确层级，需统一结构、语义和对象身份。

**方法：** 用Python程序组织层级和重复，用自然语言描述内容，用embedding绑定视觉身份；从文本/图像推断并接多种渲染器。

**模型/表示：** Claude 3.5 Sonnet；程序、文本和embedding；多后端，不能把单一扩散模型视为全部方法

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### Articulate-Anything: Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model
[paper](https://arxiv.org/abs/2410.13882) · [project](https://articulate-anything.github.io)

**Motivation：** 从视觉输入获得可操作关节资产需要复杂人工建模。

**方法：** 检索部件并生成link和joint代码；actor-critic用渲染反馈与运动轨迹逐步修正。

**模型/表示：** Gemini 1.5 Flash；CLIP；CoTracker；PyBullet / SAPIEN

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### DreamGarden: A Designer Assistant for Growing Games from a Single Prompt
[paper](https://arxiv.org/abs/2410.01791)

**Motivation：** 单轮提示难直接得到完整游戏，设计者需要可理解、可干预的生成过程。

**方法：** 递归拆解高层游戏想法，组织实现模块与任务，调用工具逐步构建Unreal游戏，允许用户介入调整。

**模型/表示：** GPT-4o；Unreal Engine；游戏制作助手，不含专门视频生成骨干

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### SceneMotifCoder: Example-driven Visual Program Learning for Generating 3D Object Arrangements
[paper](https://arxiv.org/abs/2408.02211) · [project](https://3dlg-hcvc.github.io/smc)

**Motivation：** 少量例子往往包含重复、对称或层级布局规律，直接复制坐标缺少可编辑性和泛化。

**方法：** 由示例识别arrangement motif，抽象成参数化程序，再实例化并检索对象资产，生成相似结构的新布局。

**模型/表示：** GPT-4-Vision-Preview、GPT-4-Turbo；GPT-4o

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### Infinigen Indoors: Photorealistic Indoor Scenes using Procedural Generation
[paper](https://arxiv.org/abs/2406.11824)

**Motivation：** 希望程序生成器覆盖逼真的室内资产与布置，同时保留几何和语义真值。

**方法：** 程序化构造家具及材质，通过约束定义支撑、碰撞和房间关系，求解布局并用Blender渲染。

**模型/表示：** 程序化资产生成器＋约束式布局求解；无需LLM/扩散模型作为核心

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### Real2Code: Reconstruct Articulated Objects via Code Generation
[paper](https://arxiv.org/abs/2406.08474)

**Motivation：** 关节参数直接回归和复杂提示难以扩展到多部件对象。

**方法：** 从多视角分割和形状补全获取部件OBB，微调代码模型以轴／边选择生成关节MJCF。

**模型/表示：** CodeLlama-7B；SAM；形状补全网络

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### BlenderAlchemy: Editing 3D Graphics with Vision-Language Models
[paper](https://arxiv.org/abs/2404.17672)

**Motivation：** 用户难用底层材质节点或几何参数表达目标修改，单次VLM代码编辑也不稳定。

**方法：** VLM提出候选Blender编辑，以渲染图像反馈搜索和筛选操作，迭代改变几何、材质及灯光。

**模型/表示：** GPT-4V；Blender；不需要视频扩散模型

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### PhysDreamer: Physics-Based Interaction with 3D Objects via Video Generation
[paper](https://arxiv.org/abs/2404.13026) · [project](https://physdreamer.github.io)

**Motivation：** 静态3D对象缺少能响应新力或操作的材料动态。

**方法：** 从预训练视频先验蒸馏物理属性，使显式物理对象可在新交互下模拟响应。

**模型/表示：** 预训练视频先验＋物理仿真；具体组件待精读

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### Video2Game: Real-time, Interactive, Realistic and Browser-Compatible Environment from a Single Video
[paper](https://arxiv.org/abs/2404.09833) · [project](https://video2game.github.io)

**Motivation：** NeRF重建通常只能看，难直接编辑、碰撞或在浏览器实时交互。

**方法：** 从单视频重建神经场，转为网格和可实时渲染材质，配置物理与交互，导出浏览器环境。

**模型/表示：** NeRF及网格/材质转换；浏览器渲染与物理引擎；不是核心必要模块

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### PhyScene: Physically Interactable 3D Scene Synthesis for Embodied AI
[paper](https://arxiv.org/abs/2404.09465) · [project](https://physcene.github.io)

**Motivation：** 视觉合理的布局可能碰撞、堵路或阻碍关节开启，不适合具身agent交互。

**方法：** 在布局扩散采样时加入碰撞、房间边界、可达性及交互性指导，结合关节对象构造可操作场景。

**模型/表示：** 条件布局扩散模型＋物理/可达性guidance；不是方法必要模块

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### SceneScript: Reconstructing Scenes With An Autoregressive Structured Language Model
[paper](https://arxiv.org/abs/2403.13064)

**Motivation：** 纯点云/网格不便语义编辑；希望感知系统直接输出对象与建筑结构。

**方法：** 用自回归结构语言模型将感知输入转为场景命令序列，表示墙、门窗与对象，并支持编辑和扩展。

**模型/表示：** 专门训练的encoder–decoder自回归Transformer；SceneScript结构token；不是直接调用GPT生成通用代码

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### SceneCraft: An LLM Agent for Synthesizing 3D Scene as Blender Code
[paper](https://arxiv.org/abs/2403.01248)

**Motivation：** 逐次从零生成场景脚本容易出错，也难积累可复用的构造经验。

**方法：** agent生成Blender Python并渲染观察，迭代修正脚本；将成功实现归纳为函数库用于后续任务。

**模型/表示：** GPT-4V；Blender Python；可复用场景函数

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### Holodeck: Language Guided Generation of 3D Embodied AI Environments
[paper](https://arxiv.org/abs/2312.09067)

**Motivation：** 现有室内环境分布有限，难按任意用途和空间需求生成可交互场景。

**方法：** LLM从描述规划房间与空间约束，检索3D资产并优化布置，产出AI2-THOR环境。

**模型/表示：** GPT-4；GPT-4V；AI2-THOR与Objaverse资产

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation
[paper](https://arxiv.org/abs/2311.01455)

**Motivation：** 机器人任务、资产布局和奖励长期依赖人工，限制仿真数据规模和任务覆盖。

**方法：** LLM提出任务，配置资产、尺度、关节和布局，再生成奖励或选择学习路径，以强化学习/运动规划获取行为。

**模型/表示：** GPT-4；Objaverse/PartNet-Mobility等来源；任务相关RL/规划器，无统一视频骨干

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### GenSim: Generating Robotic Simulation Tasks via Large Language Models
[paper](https://arxiv.org/abs/2310.01361) · [code](https://github.com/liruiw/GenSim) · [project](https://liruiw.github.io/gensim) · [data](https://huggingface.co/spaces/Gen-Sim/Gen-Sim)

**Motivation：** 机器人仿真任务和演示编写成本高，希望借LLM先验快速扩展任务集合。

**方法：** 给定已有API和示例，LLM编写任务与奖励代码，执行生成演示，并用任务数据训练机器人策略。

**模型/表示：** GPT-4；CLIPort等机器人学习组件；既有模拟后端

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### Infinite Photorealistic Worlds using Procedural Generation
[paper](https://arxiv.org/abs/2306.09310)

**Motivation：** 扫描或人工制作资产限制多样性与真值标注，需从零生成可控的写实自然世界。

**方法：** 用程序规则生成几何、材质、植被及自然布局，并从场景直接取得几何与语义真值。

**模型/表示：** Blender程序化生成器与材质节点；无需LLM/扩散模型作为生成前提

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### ProcTHOR: Large-Scale Embodied AI Using Procedural Generation
[paper](https://arxiv.org/abs/2206.06994)

**Motivation：** 具身策略训练受少量手工房屋限制，需要大规模且可交互的室内场景分布。

**方法：** 程序化采样房间拓扑、门、家具和小物体，检查布局后接入AI2-THOR，用生成环境训练与评价具身任务。

**模型/表示：** AI2-THOR；程序规则与资产库；场景生成核心不要求LLM

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

### Scenic: A Language for Scenario Specification and Scene Generation
[paper](https://arxiv.org/abs/1809.09310)

**Motivation：** 训练和测试需要覆盖受约束、低概率或危险场景，手动枚举场景既慢又难控制分布。

**方法：** 设计概率DSL描述空间关系、对象分布和软硬约束，通过约束采样生成可交给模拟器执行的场景。

**模型/表示：** Scenic概率程序、约束和采样器；原方法不要求LLM或视频生成模型

**范围与证据：** Produces or reconstructs an engine scene, articulated configuration, simulation mechanism, or executable visual environment.

## Programmatic Dynamics & Rules

### RoleWorld: Knowledge Transfer in World Modeling with Functional Role Abstractions
[paper](https://arxiv.org/abs/2610.13172)

**Motivation：** 外观和对象名字变化会破坏规则复用，需要按对象在机制中的功能进行跨世界迁移。

**方法：** 学习角色原型及可执行转移规则；迁移时保持原型和规则，调整目标世界的角色绑定与参数。

**模型/表示：** GPT-5.6 Sol；Qwen3-8B、GPT-5.6 Luna；functional role prototypes＋程序规则

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

### Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks
[paper](https://arxiv.org/abs/2610.11794)

**Motivation：** 仅存对话或直接改代码不易积累稳定、可反思的机制知识。

**方法：** 将自然语言规则簿编译成转移、观测和目标程序，利用失败和重放反馈递归修正规则簿，固定底层LLM。

**模型/表示：** Claude Opus 5；Claude Code，extra-high reasoning；外部规则簿与程序，不更新LLM权重

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

### Kepler: Auditable World Models for ARC-AGI-3
[paper](https://arxiv.org/abs/2610.00834) · [project](https://kepler-harness.vercel.app)

**Motivation：** 历史拟合不保证新行动预测正确；世界模型的成功需要可追查的验证证据。

**方法：** 对程序假设进行转移重放认证，规划后加入行动时的条件预测检查，用新观察定位不成立的假设。

**模型/表示：** Claude Opus 5、GPT-5.6 Sol（max）；可执行假设＋重放/预测验证

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

### Twin: Playing an Unknown Game with a Test-Time Digital Twin
[paper](https://arxiv.org/abs/2608.14490) · [code](https://github.com/Alexyskoutnev/TWIN-ARC-AGI-3) · [project](https://arc-agi-3-twin.vercel.app)

**Motivation：** 未知游戏的即时推理容易遗忘机制，也缺少行动前可验证的预测工具。

**方法：** coding agent边玩边构造数字孪生，要求重放历史转移；通过孪生搜索计划，在新反例出现时修改程序。

**模型/表示：** GPT-5.6 Sol，xhigh；Claude Opus 5的外部结果不是Twin骨干

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

### Tycho: Active Abstraction with Programmatic World Models for ARC-AGI-3
[paper](https://arxiv.org/abs/2607.28287) · [code](https://github.com/NIMI-research/Tycho)

**Motivation：** 未知交互游戏中，建模过早或抽象错误会浪费预算，需要判断何时探索、建模、修复或直接行动。

**方法：** actor与builder协作维护可执行假设，主动测试抽象，依据模型有效性选择规划或绕过模型。

**模型/表示：** Claude Opus 4.8；GPT-5.6 Sol、Claude Opus 5；Tycho actor–builder工作流

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

### World-Time Compute with Verified Code World Models
[paper](https://arxiv.org/abs/2609.09163) · [code](https://github.com/quome-cloud/openworld)

**Motivation：** 详见原始论文或官方说明。

**方法：** 验证程序生成精确训练轨迹

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

### OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration for ARC-AGI-3
[paper](https://arxiv.org/abs/2607.01531)

**Motivation：** 对象抽象本身可能错；在错误对象/属性定义上继续修动态规则会低效。

**方法：** 优先探测并修订ontology，再更新可执行世界程序；将交互预算投向最能区分抽象假设的动作。

**模型/表示：** Claude Opus 4.8，主要配置high；论文报告1M窗口

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

### Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games
[paper](https://arxiv.org/abs/2606.16070)

**Motivation：** 只看单步预测不足以说明世界模型能否支持决策；需要衡量多步行动后果。

**方法：** 结合轨迹及截图提取的信息合成独立可执行环境，以K步前瞻比较候选动作，迭代修复对规划重要的模型误差。

**模型/表示：** Qwen3-Coder-480B-A35B-Instruct-Turbo；Qwen3-Max-Thinking及DeepSeek-V4-Pro/Flash等

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

### Distilling Game Code World Model Generation into Lightweight Large Language Models
[paper](https://arxiv.org/abs/2605.24375)

**Motivation：** 依赖大闭源LLM生成游戏模拟器成本高，希望把可执行规则合成能力迁移到小模型。

**方法：** 以游戏代码数据进行SFT，再用执行反馈和可验证奖励做GRPO；分开训练与留出游戏，检验生成程序的规则正确性。

**模型/表示：** Qwen2.5-3B-Instruct；SFT＋GRPO/RLVR；GPT-4o不是学生骨干

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

### Executable World Models for ARC-AGI-3 in the Era of Coding Agents
[paper](https://arxiv.org/abs/2605.05138) · [code](https://github.com/astroseger/arc-3-agents-baseline1)

**Motivation：** 详见原始论文或官方说明。

**方法：** 验证驱动的程序世界baseline

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

### Learning Abstractions for Hierarchical Planning in Program-Synthesis Agents
[paper](https://arxiv.org/abs/2602.00929)

**Motivation：** 单任务合成的高层技能难复用；抽象应同时保留符号可规划性和低层可执行性。

**方法：** TheoryCoder-2从经验学习PDDL高层operator、Python谓词及低层转移，进行分层搜索并积累可复用抽象。

**模型/表示：** GPT-4o；BFS；o4-mini不是方法的默认骨干

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

### One Life to Learn: Inferring Symbolic World Models for Stochastic Environments from Unguided Exploration
[paper](https://arxiv.org/abs/2510.12088) · [project](https://onelife-worldmodel.github.io)

**Motivation：** 无任务奖励、少量且危险的探索下，需发现稀疏激活的随机机制，并区分相互冲突的候选规律。

**方法：** 探索收集对象状态转移；LLM生成最小前提—效果Python规律；推断规律权重，只向解释实际变化的规律分配信用。

**模型/表示：** 概率化原子程序规律及其可学习权重

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

### Code World Models for General Game Playing
[paper](https://arxiv.org/abs/2510.04542)

**Motivation：** 规则文本和轨迹不能直接被搜索算法调用，需要编译成一致、可执行的游戏接口。

**方法：** 合成OpenSpiel风格的合法动作、状态转移和终止等Python函数，以轨迹测试修正；结合MCTS/ISMCTS处理完全或不完全信息游戏。

**模型/表示：** Gemini 2.5 Pro；MCTS、ISMCTS；PPO策略，不是视觉生成器

**范围与证据：** The visual/spatial game-rule component is relevant; purely textual or nonvisual symbolic planning is not the focus of this collection.

### Finite Automata Extraction: Low-data World Model Learning as Programs from Gameplay Video
[paper](https://arxiv.org/abs/2508.11836)

**Motivation：** 希望用少量gameplay视频恢复可执行机制，减少大规模交互和数据需求。

**方法：** 在Retro Coder DSL中构造神经符号表示并提取有限自动机，用程序解释观测中的游戏演化。

**模型/表示：** Retro Coder DSL＋finite automata；未找到将GPT类模型作为核心的证据

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

### PoE-World: Compositional World Modeling with Products of Programmatic Experts
[paper](https://arxiv.org/abs/2505.10819) · [project](https://topwasu.github.io/poe-world)

**Motivation：** 单个确定性程序难表达随机动态；整块修复不利于复用对象级局部机制。

**方法：** 生成多个局部程序专家，以带权概率乘积组成预测分布；学习专家权重并在Atari中进行基于模型的规划。

**模型/表示：** gpt-4o-2024-08-06；加权programmatic experts，无视频扩散骨干

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

### Synthesizing world models for bilevel planning
[paper](https://arxiv.org/abs/2503.20124)

**Motivation：** 低层模型逐步搜索成本高；只用高层语言计划又可能忽略真实动作前提。

**方法：** TheoryCoder同时合成Python低层动态和可执行高层抽象，把任务分成高层规划与低层实现，并用交互修正规则。

**模型/表示：** GPT-4o；双层符号规划；o1属于baseline

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

### FactorSim: Generative Simulation via Factorized Representation
[paper](https://arxiv.org/abs/2409.17652)

**Motivation：** 长指令下直接生成完整仿真容易遗漏状态依赖。

**方法：** 把环境分解为因子化POMDP，逐步生成状态、动作相关／无关转移与观察模块；只取相关代码作为上下文。

**模型/表示：** GPT-4；Llama 3

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

### Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search
[paper](https://arxiv.org/abs/2405.15383)

**Motivation：** 一次生成或简单反复调试容易停在错误程序；需要利用测试信号有效分配合成预算。

**方法：** GIF-MCTS把Generate、Improve、Fix作为树搜索动作，依据轨迹执行误差选择分支；在CWMB上分别检验预测与控制。

**模型/表示：** Llama-3-70B、GPT-4 Turbo；GIF-MCTS，不是预训练模型

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

### WorldCoder, a Model-Based LLM Agent: Building World Models by Writing Code and Interacting with the Environment
[paper](https://arxiv.org/abs/2402.12275)

**Motivation：** LLM直接行动缺少可检验的动态知识，也难在新交互后持续修正环境理解。

**方法：** 合成Python转移/奖励模型，要求符合已见经验，并满足乐观的目标可达约束；以搜索选择修正，再用模型规划和收集新经验。

**模型/表示：** GPT-4；值迭代/MCTS，非视频生成模型

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

### Automated Game Design via Conceptual Expansion
[paper](https://arxiv.org/abs/1809.02232)

**Motivation：** 自动游戏设计需要超越参数扰动，重组已有游戏中的内容和机制。

**方法：** 学习近似游戏表示，在概念空间扩展和组合原有机制，形成新游戏并检验其行为/设计特征。

**模型/表示：** conceptual expansion与符号游戏表示；不依赖现代LLM/视频扩散模型

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

### Game Engine Learning from Video
[paper](https://www.ijcai.org/Proceedings/2017/518)

**Motivation：** 从观测游戏恢复可运行的前向机制，使学习不依赖源代码或现成转移模型。

**方法：** 从Super Mario Bros.视频取得对象/运动表示，搜索并修订预测规则，形成前向游戏引擎用于模拟和agent学习。

**模型/表示：** 对象/规则表示与符号搜索；无需LLM或扩散骨干；IJCAI 2017前史

**范围与证据：** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.

## Generative Rendering

### RoboRender: Robot-Oriented Video Generation for Visual Sim-to-Real Transfer
[paper](https://arxiv.org/abs/2610.09254) · [project](https://robo-render.github.io)

**Motivation：** 机器人合成视频需要同时保持多视角、动作标签和场景结构。

**方法：** 把仿真深度、机器人保留RGB与噪声目标通道拼接，再联合堆叠视角；LoRA适配并用上一块末帧延续。

**模型/表示：** Wan2.1-T2V-1.3B＋LoRA

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### CoaG: Cylinders on a Grid for Coarse 3D Layout Control in Video Generation
[paper](https://arxiv.org/abs/2609.24208) · [project](https://zshyang.github.io/CoaG)

**Motivation：** 希望用低成本3D信号控制多人位置、规模与遮挡。

**方法：** 地面线框网格编码尺度与相机运动，稳定色圆柱编码人物位置和遮挡；用自动数据引擎和LoRA适配控制模型。

**模型/表示：** Wan2.2-Fun-A14B-Control；rank-64 LoRA

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### LynnReal-Omni: Native multi-modal Video Generation for Agentic Visual Workflows
[paper](https://arxiv.org/abs/2609.15863)

**Motivation：** 分散的视频任务接口限制智能体组合引用、3D场景与游戏控制。

**方法：** MiniMax-H3系共享多模态DiT编码异构条件，联合多任务流匹配与少步蒸馏；有界历史、轻量解码器支持流式生成。

**模型/表示：** MiniMax-H3系；32B Standard / 27B Flash

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### RGBX-Next: Towards Realistic Generative Rendering from G-Buffers
[paper](https://arxiv.org/abs/2608.13929)

**Motivation：** 单任务渲染器和合成数据难以同时覆盖真实外观、多种图形编辑与长视频。

**方法：** 用带类型的帧槽统一RGB与G-buffer条件／目标，以X-patchify压缩多模态输入；合成与估计真实内在属性联合训练，支持分块延续。

**模型/表示：** Wan2.1-14B；冻结VAE

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### UniMoCa: Unifying Motion and Camera Controls as Visual Proxies for Faithful Human Video Generation
[paper](https://arxiv.org/abs/2608.01944) · [project](https://tanliming-daniel.github.io/UniMoCa)

**Motivation：** 视觉动作图与非视觉相机参数存在异构接口和归因冲突。

**方法：** 把3D人体、多人布局和相机轨迹统一为MCVP视觉代理；显式相机标记区分运动来源，proxy token与视频token联合训练。

**模型/表示：** Wan2.2 I2V；MCVP proxy encoder

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### VideoCoCo: Code-as-CoT for Physically-Consistent Video Generation via an Agentic Dual-Engine System
[paper](https://arxiv.org/abs/2607.27380)

**Motivation：** 文本或稀疏分镜不能把完整物理过程明确实例化。

**方法：** 编码agent写Blender时空程序，执行成确定性draft；指令agent描述外观变换，用VideoCoCo-3K适配draft-conditioned视频编辑器。

**模型/表示：** Blender Python；OmniWeaving初始化；全量或LoRA编辑器适配

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### Generative World Renderer at the Speed of Play
[paper](https://arxiv.org/abs/2607.18703)

**Motivation：** 高质量离线生成速度与上下文使用方式不适合持续交互，需要整条渲染链路提速。

**方法：** 将AlayaRenderer转为因果学生并蒸馏为四步，压缩条件编码器与解码器，结合流式执行减少生成开销。

**模型/表示：** AlayaRenderer / Wan2.1系；四步因果视频模型；轻量条件编码器与TAEHV解码器

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### ProxyUp: Training-Free Proxy-Conditioned Video Generation for Controllable Dynamics
[paper](https://arxiv.org/abs/2607.03732) · [project](https://zanue.github.io/proxyup)

**Motivation：** 粗代理视频的运动约束与逼真外观生成相互牵制。

**方法：** 免训练ODE反演提取前景运动latent，区域噪声处理背景，再用SFR使组合latent返回可采样区域。

**模型/表示：** Wan2.2

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### 3D Scene-Adaptive Trajectory-Controllable Human Image Animation with Camera Movement
[paper](https://arxiv.org/abs/2606.30514) · [project](https://robinhood256100.github.io/web-disp)

**Motivation：** 人体轨迹和镜头改变后还应适应真实地形与可见区域。

**方法：** 地面自适应3D运动重定向，配合按场景可见性mask融合点云先验到latent以支持新视角。

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### Directing the World: Fast Autoregressive Video Generation with Compositional Human-Camera Control
[paper](https://arxiv.org/abs/2606.27964) · [project](https://whydahuzi.github.io/Directing-the-World.github.io)

**Motivation：** 长时AR视频加入人体和相机条件后会互相干扰并破坏生成先验。

**方法：** 先学SMPL运动控制，再引入与因果块对齐的相机控制；t-guided projection、Motion-CFG和Fast-Slow训练稳定适配。

**模型/表示：** MMPL自回归骨干；SMPL；ControlNet式分支

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### ActCam: Zero-Shot Joint Camera and 3D Motion Control for Video Generation
[paper](https://arxiv.org/abs/2605.06667) · [project](https://elkhomar.github.io/actcam)

**Motivation：** 人体动作和镜头运动混合在2D条件中，难以独立重组。

**方法：** 重建背景深度与3D姿态，在目标相机下渲染对齐条件；前期pose＋depth、后期只保留pose，免训练完成联合控制。

**模型/表示：** VACE；MoGe；3D姿态恢复

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### ComSim: Building Scalable Real-World Robot Data Generation via Compositional Simulation
[paper](https://arxiv.org/abs/2604.11386) · [project](https://faceong.github.io/ComSim)

**Motivation：** 仿真图像和真实图像有域差，纯视频生成又可能破坏动作对应关系。

**方法：** 重放真实动作得到配对仿真观察，组合动作动态与视觉动态条件的分数生成伪真实视频，再训练并部署机器人策略。

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### Lighting-grounded Video Generation with Renderer-based Agent Reasoning
[paper](https://arxiv.org/abs/2604.07966)

**Motivation：** 布局、照明与相机耦合，限制电影和虚拟制作中的编辑。

**方法：** renderer-based agent构造场景、HDR照明与相机；渲染diffuse、rough GGX、glossy GGX组成9通道proxy，用编码器／adapter和分阶段训练生成视频。

**模型/表示：** Wan2.2-TI2V-5B＋LoRA；轻量proxy encoder

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### HumANDiff: Articulated Noise Diffusion for Motion-Consistent Human Video Generation
[paper](https://arxiv.org/abs/2604.05961) · [project](https://taohuumd.github.io/projects/HumANDiff)

**Motivation：** 独立像素噪声难保持人体表面运动对应。

**方法：** 在SMPL的UV表面采样共享高斯噪声并随姿态渲染到图像，配合外观／运动联合学习和一致性监督。

**模型/表示：** CogVideoX-5B-I2V；另在Wan2.1-I2V验证

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### Generative World Renderer
[paper](https://arxiv.org/abs/2604.02329) · [project](https://alaya-studio.github.io/renderer)

**Motivation：** 需要把现有高质量游戏数据转成同步、可学习的渲染监督，并支持可控的图像形成。

**方法：** 采集AAA游戏RGB与G-buffer配对，训练条件视频渲染及逆向分解，使几何、材质与外观能够分开控制。

**模型/表示：** Wan2.1-T2V-1.3B，全量适配；同步RGB与五类G-buffer通道

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### VideoWeaver: Multimodal Multi-View Video-to-Video Transfer for Embodied Agents
[paper](https://arxiv.org/abs/2603.25420)

**Motivation：** 详见原始论文或官方说明。

**方法：** 官方摘要：所有视图由Pi3提供的共享4D latent空间锚定，用于多视图V2V；直接符合B。

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### Hand2World: Autoregressive Egocentric Interaction Generation via Free-Space Hand Gestures
[paper](https://arxiv.org/abs/2602.09600)

**Motivation：** 自由空间手势与接触训练数据有域差，手运动与头部视角又易混淆。

**方法：** 用投影3D手网格提供遮挡不变条件，以Plücker射线独立控制相机；把双向模型蒸馏为因果生成器。

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### Coarse-to-Real: Generative Rendering for Populated Dynamic Scenes
[paper](https://arxiv.org/abs/2601.22301) · [project](https://gonzalognogales.github.io/coarse2real)

**Motivation：** 粗仿真能控制城市人群，但缺少配对真实监督，结构条件也可能泄漏CG外观。

**方法：** 先用真实视频适配生成先验，再冻结骨干，通过DINOv3特征adapter连接合成／真实控制，做domain hedging。

**模型/表示：** Wan2.1；DINOv3 ViT；T5-XXL

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### FrameDiffuser: G-Buffer-Conditioned Diffusion for Neural Forward Frame Rendering
[paper](https://arxiv.org/abs/2512.16670)

**Motivation：** 面向特定环境渲染时，既要跟随精确结构，又要抑制逐帧生成的闪烁。

**方法：** 以多通道G-buffer控制单帧扩散，上一生成帧提供时间上下文；通过轻量适配学习目标环境的前向渲染。

**模型/表示：** Stable Diffusion 1.5；10通道ControlNet＋rank-64 ControlLoRA；前一生成帧

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### LAMP: Language-Assisted Motion Planning for Controllable Video Generation
[paper](https://arxiv.org/abs/2512.03619) · [project](https://cyberiada.github.io/LAMP)

**Motivation：** 自然语言难直接回归有结构、可编辑的对象和镜头轨迹。

**方法：** LLM产生电影运动DSL，确定性转换为对象／相机3D轨迹，再编译成控制视频或接入其他生成器；程序化数据训练运动规划器。

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### PhysChoreo: Physics-Controllable Video Generation with Part-Aware Semantic Grounding
[paper](https://arxiv.org/abs/2511.20562)

**Motivation：** 物性通常只按整体对象估计，且物理视频多只能修改初始条件。

**方法：** 部件语义估计物理场，MPM／刚体求解器接受随时间编辑的参数和力；轨迹视频约束后续视频生成。

**模型/表示：** InstantMesh；PartField；GPT-5；Taichi；Wan2.2-Fun-5B-Control

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### X2Video: Adapting Diffusion Models for Multimodal Controllable Neural Video Rendering
[paper](https://arxiv.org/abs/2510.08530) · [project](https://luckyhzt.github.io/x2video)

**Motivation：** 全局文本和单一结构条件不足以控制局部材质、光照与时间变化。

**方法：** 结合内在通道、参考图和局部/全局文本，用参考与时间attention以及递归关键帧/插帧完成视频渲染。

**模型/表示：** 基于Stable Diffusion 2.1的XRGB；参考/时间attention与区域文本控制；不是直接以CogVideoX为基础

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### IllumiCraft: Unified Geometry and Illumination Diffusion for Controllable Video Generation
[paper](https://arxiv.org/abs/2506.03150)

**Motivation：** 光照控制缺少跨帧几何联系。

**方法：** 将HDR环境视频、重光照外观与3D点轨迹共同注入视频扩散。

**模型/表示：** Wan2.1 1.3B；4×A6000训练（§4.2）。

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### Uni3C: Unifying Precisely 3D-Enhanced Camera and Human Motion Controls for Video Generation
[paper](https://arxiv.org/abs/2504.14899) · [code](https://github.com/ewrfcas/Uni3C)

**Motivation：** 相机与人体控制需要共享3D坐标，同时减少大型骨干的适配成本。

**方法：** 轻量PCDController以目标相机下的点云渲染视频控制Wan-I2V；与人体动画及3D世界引导模块组合。

**模型/表示：** Wan-I2V 14B；约0.95B PCDController

**范围与证据：** The joint scene-and-character guidance is relevant; ordinary camera control without an executable visual-world interface is outside the method scope.

### Cosmos-Transfer1: Conditional World Generation with Adaptive Multimodal Control
[paper](https://arxiv.org/abs/2503.14492) · [code](https://github.com/nvidia-cosmos/cosmos-transfer1)

**Motivation：** 详见原始论文或官方说明。

**方法：** 结构控制的现实化与域迁移

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### ReBot: Scaling Robot Learning with Real-to-Sim-to-Real Robotic Video Synthesis
[paper](https://arxiv.org/abs/2503.14526) · [project](https://yuffish.github.io/rebot)

**Motivation：** 真实机器人动作昂贵，希望保留动作标签并替换对象与环境。

**方法：** 在Isaac Sim重放轨迹，补全真实背景，把仿真机器人／对象合成回背景，训练Octo或OpenVLA。

**模型/表示：** Isaac Sim 4.1 / Isaac Lab；Octo；OpenVLA

**范围与证据：** An engine-grounded data-synthesis pipeline; its composition step should not be mistaken for diffusion-based rendering.

### Re$^3$Sim: Generating High-Fidelity Simulation Data via 3D-Photorealistic Real-to-Sim for Robotic Manipulation
[paper](https://arxiv.org/abs/2502.08645) · [project](https://re3sim.github.io)

**Motivation：** 几何与外观域差阻碍低成本仿真数据迁移。

**方法：** 重建真实场景并与物理仿真连接，以高保真神经渲染生成跨视角示范，验证策略迁移。

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** A real-to-sim and observation-generation predecessor; its renderer is not presented as a code-conditioned diffusion world model.

### CineMaster: A 3D-Aware and Controllable Framework for Cinematic Text-to-Video Generation
[paper](https://arxiv.org/abs/2502.08639) · [project](https://cinemaster-dev.github.io)

**Motivation：** 电影创作需要同时指定对象布局、对象运动和相机。

**方法：** 在Blender中编排3D框与相机关键帧，导出深度、类别与相机轨迹；语义布局注入模块和camera adapter控制视频DiT。

**模型/表示：** 预训练T2V DiT＋3D VAE＋T5；未披露可确认的商品检查点

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### MotionCanvas: Cinematic Shot Design with Controllable Image-to-Video Generation
[paper](https://arxiv.org/abs/2502.04299) · [project](https://motion-canvas25.github.io)

**Motivation：** 创作者在3D场景中表达意图，而训练视频常只能可靠提取2D运动。

**方法：** 将场景中心的相机／对象编排翻译成屏幕空间轨迹和框；DCT编码点轨迹，微调运动条件视频DiT。

**模型/表示：** 内部DiT-I2V；3D VAE；DCT轨迹token

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### DiffusionRenderer: Neural Inverse and Forward Rendering with Video Diffusion Models
[paper](https://arxiv.org/abs/2501.18590) · [project](https://research.nvidia.com/labs/toronto-ai/DiffusionRenderer/)

**Motivation：** 传统渲染资产制作昂贵，真实视频又缺少几何/材质分解；需要共享生成先验连接正向与逆向渲染。

**方法：** 逆向模型把RGB视频分解为几何/材质缓冲区，正向模型按这些条件生成RGB，支持光照与材质编辑。

**模型/表示：** Stable Video Diffusion（SVD img2vid）适配；几何与材质G-buffer

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### Diffusion as Shader: 3D-aware Video Diffusion for Versatile Video Generation Control
[paper](https://arxiv.org/abs/2501.03847) · [code](https://github.com/IGL-HKUST/DiffusionAsShader) · [project](https://igl-hkust.github.io/das)

**Motivation：** 相机、对象、动作各用独立条件网络会割裂控制接口；3D对应可统一这些需求。

**方法：** 将3D跟踪/对应关系编码成tracking videos，微调I2V模型支持相机控制、网格动画、动作迁移与对象操控。

**模型/表示：** CogVideoX-I2V；深度/分割/3D tracking工具

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### AutoVFX: Physically Realistic Video Editing from Natural Language Instructions
[paper](https://arxiv.org/abs/2411.02394) · [project](https://haoyuhsu.github.io/autovfx-website)

**Motivation：** 真实视频的复杂特效编辑需要组合重建、物理和可控操作。

**方法：** 神经场景建模后由LLM组合编辑API，执行对象／物理修改，再以光照、阴影和遮挡感知渲染合成回视频。

**模型/表示：** GPT-4 / GPT-4V；SuGaR；Blender；资产检索／生成

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### Tex4D: Zero-shot 4D Scene Texturing with Video Diffusion Models
[paper](https://arxiv.org/abs/2410.10821) · [project](https://tex4d.github.io)

**Motivation：** 动态网格纹理需要跨视角与跨时间一致。

**方法：** 在UV空间聚合多视角latent，修改DDIM并混合参考UV纹理，生成动态纹理序列。

**模型/表示：** 深度条件CTRL-Adapter；UV latent聚合与DDIM。

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### PhysGen: Rigid-Body Physics-Grounded Image-to-Video Generation
[paper](https://arxiv.org/abs/2409.18964) · [project](https://stevenlsw.github.io/physgen)

**Motivation：** 详见原始论文或官方说明。

**方法：** 图像理解、刚体仿真与视频生成细化

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### SimGen: Simulator-conditioned Driving Scene Generation
[paper](https://arxiv.org/abs/2406.09386)

**Motivation：** 真实布局数据有限，直接条件生成容易域内过拟合。

**方法：** 混合MetaDrive仿真和真实DIVA视频，用级联扩散解决域差与多条件冲突。

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### Champ: Controllable and Consistent Human Image Animation with 3D Parametric Guidance
[paper](https://arxiv.org/abs/2403.14781) · [project](https://fudan-generative-vision.github.io/champ)

**Motivation：** 2D骨架不足以表达人体体形和三维朝向。

**方法：** 从SMPL渲染深度、法线、语义图，并融合骨架条件驱动潜在扩散，支持体形对齐。

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Included for parameterized-character rendering. This does not bring all reference-image or pose-transfer methods into the method corpus.

### Generative Rendering: Controllable 4D-Guided Video Generation with 2D Diffusion Models
[paper](https://arxiv.org/abs/2312.01409) · [project](https://primecai.github.io/generative_rendering/)

**Motivation：** 图像扩散外观能力强，但逐帧运行会闪烁；动画网格已知的跨帧对应应能提供控制。

**方法：** 从4D网格导出深度、UV和对象ID，用深度ControlNet、UV一致噪声和跨帧/UV特征注入生成连贯视频。

**模型/表示：** Stable Diffusion系2D模型＋depth ControlNet；主要通过推理时注入实现

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### GPT4Motion: Scripting Physical Motions in Text-to-Video Generation via Blender-Oriented GPT Planning
[paper](https://arxiv.org/abs/2311.12631)

**Motivation：** 将文本中的物理过程明确交给模拟器，而非完全依靠像素模型推断。

**方法：** GPT-4生成Blender Python物理脚本，执行刚体／布料／液体模拟并导出动态条件；ControlNet引导Stable Diffusion生成画面。

**模型/表示：** GPT-4＋Blender物理引擎；Stable Diffusion＋ControlNet

**范围与证据：** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.

### Enhancing Photorealism Enhancement
[paper](https://arxiv.org/abs/2105.04619) · [code](https://github.com/intel-isl/PhotorealismEnhancement)

**Motivation：** 合成画面的外观域差会使普通图像翻译出现伪影。

**方法：** 利用渲染管线中间表示、卷积网络和多层感知对抗监督，并按布局分布采样局部图像块。

**模型/表示：** G-buffer条件卷积网络＋对抗训练

**范围与证据：** An engine-to-observation appearance-enhancement predecessor, not a rule-learning or world-construction system.

### Deferred Neural Rendering: Image Synthesis using Neural Textures
[paper](https://arxiv.org/abs/1904.12356)

**Motivation：** 不完美几何难以直接渲染逼真且一致的观察。

**方法：** 在代理网格表面学习高维Neural Texture，再以延迟神经渲染器解码成RGB。

**模型/表示：** Neural Textures＋卷积神经渲染器

**范围与证据：** A learned scene-rendering predecessor using an explicit surface representation, not a complete programmable world model.

## Data & Evaluation

### PhysCodeGym: Benchmarking Coding Agents for Physically Verifiable 4D Reconstruction
[paper](https://arxiv.org/abs/2610.17288) · [code](https://github.com/ShaoShuai0605/PhysCodeGym)

**Motivation：** 重建视频外观和事件仍可能依赖错误物理机制。

**方法：** 156个video-to-Blender任务要求建模物性、初态、约束与力；联合视觉和物理指标，并检查程序、场景重执行和反事实干预。

**模型/表示：** 编码agent＋Blender；规则测量和VLM裁判

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### ExeWorldBench: Benchmarking Code-Based Executable 3D World Modeling
[paper](https://arxiv.org/abs/2610.15166)

**Motivation：** 详见原始论文或官方说明。

**方法：** 机制/组合/意图驱动的可执行3D构造

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### WorldSolver: Can LLM Agents Simulate the Physical Dynamics via Solver Generation?
[paper](https://arxiv.org/abs/2610.08720) · [code](https://github.com/sirujiang/WorldSolver)

**Motivation：** 会解释物理现象不代表能写出正确、稳定且可泛化的数值模拟程序。

**方法：** agent从任务与现象要求编写求解器，用执行有效性、物理结果及运行/API成本评价，不以视频美观代替物理解。

**模型/表示：** GPT-5.6 Sol、Claude Opus 5、Gemini-3.7-Flash、DeepSeek-V4.1-Flash、Qwen-3.8-Max、Kimi-K2.7-Code等；可执行solver

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### Video2World: Benchmarking Coding Agents for Interactive World Modeling from Embodied Videos
[paper](https://arxiv.org/abs/2610.04432) · [project](https://aetherlabsai.github.io/Video2World)

**Motivation：** 外观重建相似不代表能响应新动作或完成具身任务，需要把几何、动态和功能分开测。

**方法：** 在222个重建实例上让coding agent从具身视频构建世界，通过渲染、动态对齐及交互任务检验产物。

**模型/表示：** GPT-5.6 Sol、Gemini 3.8 Flash、Claude Opus 5、Qwen3.8 Max、GPT-6 Astra、Fable-5.1等；含API与coding CLI配置

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### 4DCodeBench: Benchmarking Agents on Inverse Graphics of Dynamic Scenes
[paper](https://arxiv.org/abs/2610.03715) · [code](https://github.com/4DCodeBench/4DCodeBench) · [project](https://4dcodebench.com)

**Motivation：** 静态重建能力不足以说明能从视频恢复复杂动态。

**方法：** 200个视频任务要求代码重建并导出每帧几何、相机和物质对应；真实视频做图像域比较，合成场景额外比较3D几何与动态。

**模型/表示：** 编码智能体＋Blender / Taichi / Warp等；评测含DINOv3与视觉估计器

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### World Editing: Intervening on Executable Worlds at Increasing Depth
[paper](https://arxiv.org/abs/2610.02331) · [project](https://vinesmsuic.github.io/IGMWorld)

**Motivation：** 修改属性、实体、规则与系统的难度不同，仅检查工程是否构建无法验证编辑结果。

**方法：** IGMWorld/IGMBench在Minecraft与Terraria中设置递增深度的干预，执行行为测试并检查视觉结果，评价完整成功与局部条件满足。

**模型/表示：** Gemini 3.5 Flash、Claude Opus 4.8、GPT-5.6 Luna、GPT-5.6 Sol；Minecraft、Terraria

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### PROWBench: Do Video Models Render What the Program Specifies?
[paper](https://arxiv.org/abs/2610.02205) · [code](https://github.com/AlayaLab/PROWBench) · [project](https://alaya-lab.github.io/PROWBench)

**Motivation：** 视觉合理不代表实体、相机、事件、长时状态与多视角都遵循同一程序世界。

**方法：** 保存共享几何和逐帧世界记录，再渲染Coarse 3D、CWM proxy和Colored-OBB；对比11种模型的控制、逻辑、视觉、重访和多视角表现。

**模型/表示：** EchoWM、SANA-WM、LingBot-World 2.0、AlayaWorld v1.1、Cosmos-Transfer2.5、C2R、CWM、LynnReal-Omni、PWM、MiniMax-H3、Seedance 2.5；SAM 3实体定位；Qwen3.6-27B事件、时间线与状态判断（§3.2）

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### World Agent: Can Language Models Keep a World Running?
[paper](https://arxiv.org/abs/2609.32692) · [code](https://github.com/HCPLab-SYSU/WorldAgent-Benchmark)

**Motivation：** 详见原始论文或官方说明。

**方法：** 程序世界生成与验证

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### BVB: Benchmarking Agentic Video Understanding via Programmatic Reconstruction in Blender
[paper](https://arxiv.org/abs/2609.15478)

**Motivation：** 语言问答不能直接检验模型是否理解视频中的空间、轨迹和交互事实。

**方法：** 要求agent用Blender代码重建视频，在共享执行与预算下分别测时空事实保留、可执行性和感知相似。

**模型/表示：** GPT-5.x/GPT-6 Astra、Claude、Gemini、Grok、Qwen、GLM、Kimi等家族；本表仅列代表家族，不是逐项完整复现配置

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### R2M-Bench: Evaluating Revisit Memory via Relative Consistency in Interactive Video World Models
[paper](https://arxiv.org/abs/2608.27328) · [code](https://github.com/AMAP-ML/R2MBench)

**Motivation：** 慢运动或静止视频也可能取得很高的重访相似度。

**方法：** 比较同一视频中的重访、时间间隔匹配对照与短期参考，计算MemoryGain和归一化记忆比例。

**模型/表示：** 基准；视频表征／视觉裁判

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives
[paper](https://arxiv.org/abs/2608.13552) · [code](https://github.com/kxding/PlayWorld) · [project](https://kxding.github.io/project/PlayWorld)

**Motivation：** 详见原始论文或官方说明。

**方法：** 智能体玩家的长时目标评估

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models
[paper](https://arxiv.org/abs/2607.14169) · [code](https://github.com/JaviMaligno/code-world-models)

**Motivation：** 平均状态转移准确率可能漏掉决定规划胜负的稀有规则。

**方法：** 构造程序世界通过采样检验但导致规划失败的情形，分析规则稀有度、验证覆盖与实际游戏代价。

**模型/表示：** LLM合成程序＋经典规划；摘要报告GPT-5.x

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### GameCraft-Bench: Can Agents Build Playable Games End-to-End in a Real Game Engine?
[paper](https://arxiv.org/abs/2606.17861) · [project](https://tongxuluo.github.io/gamecraft-bench-website)

**Motivation：** 单文件小游戏或编译率不能代表真实引擎中端到端构建可玩游戏的能力。

**方法：** 在同一真实引擎接口下运行140项任务，用需求、行为和产物检查评价完整游戏，控制agent预算和工具权限。

**模型/表示：** Opus-4.7（Claude Code）、GPT-5.5（Codex）、MiMo-V2.5-Pro、DeepSeek-V4-Pro、Kimi-K2.6、GLM-5.1、MiniMax-M2.7

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### WorldCoder-Bench: Benchmarking Physically Grounded 3D World Synthesis
[paper](https://arxiv.org/abs/2606.01869)

**Motivation：** 截图好看或代码能运行，不能证明物理属性和动态行为真的实现。

**方法：** 构造2,026项3D世界任务，用StateProbe读取约定状态并执行动作测试，区分结构、affordance、状态和转移覆盖。

**模型/表示：** GPT-5.4、Gemini-3.1-Pro、Claude-Opus-4.6、Qwen3.6-Plus、DeepSeek-V3.2/V4-Flash、Kimi-K2.5；GPT-5.4 source judge

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### MBench: A Comprehensive Benchmark on Memory Capability for Video World Models
[paper](https://arxiv.org/abs/2606.00793) · [project](https://peanutup.github.io/MBench-project)

**Motivation：** 视觉质量分数不足以刻画长期世界记忆。

**方法：** 把记忆分为实体、环境、因果三个层次共12子维度，结合规则指标与VLM评估。

**模型/表示：** 基准；非生成骨干

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### WBench: A Comprehensive Multi-turn Benchmark for Interactive Video World Model Evaluation
[paper](https://arxiv.org/abs/2605.25874) · [code](https://github.com/meituan-longcat/WBench) · [project](https://meituan-longcat.github.io/WBench)

**Motivation：** 现有单段测试不能系统评价多轮互动。

**方法：** 289案例、1058轮，覆盖导航、主体动作、事件编辑与视角切换；22子指标按五维度汇总。

**模型/表示：** 基准；专用视觉模型＋多模态裁判

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### GameGen-Verifier: Parallel Keypoint-Based Verification for LLM-Generated Games via Runtime State Injection
[paper](https://arxiv.org/abs/2605.07442)

**Motivation：** 详见原始论文或官方说明。

**方法：** 状态注入与机制关键点验证

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### iWorld-Bench: A Benchmark for Interactive World Models with a Unified Action Generation Framework
[paper](https://arxiv.org/abs/2605.03941)

**Motivation：** 详见原始论文或官方说明。

**方法：** 统一动作与多类交互世界模型比较

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### GameDevBench: Evaluating Agentic Capabilities Through Game Development
[paper](https://arxiv.org/abs/2602.11103)

**Motivation：** 一般代码基准缺少图形编辑、引擎操作和多模态反馈，难评价真实游戏开发agent。

**方法：** 从教程构造132项任务，在游戏工程中考察代码、场景和编辑操作，并比较视频/MCP反馈及不同harness。

**模型/表示：** Claude Haiku/Sonnet 4.5、Gemini 3 Flash/Pro、GPT-5.4 Mini/5.4、Qwen3.5-397B、Kimi K2.5；Claude Code、Codex、Gemini CLI、OpenHands等

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### EgoControl: Controllable Egocentric Video Generation via 3D Full-Body Poses
[paper](https://arxiv.org/abs/2511.18173)

**Motivation：** 具身第一视角视频需要明确区分身体动作与相机变化。

**方法：** 用3D全身姿态表示全局相机动态和关节运动，以专用控制模块约束未来帧预测。

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Included for its camera/body evaluation protocol (Section 4.1), not classified as an executable-world construction or engine-rendering method.

### VBench-2.0: Advancing Video Generation Benchmark Suite for Intrinsic Faithfulness
[paper](https://arxiv.org/abs/2503.21755) · [code](https://github.com/Vchitect/VBench) · [project](https://vchitect.github.io/VBench-2.0-project)

**Motivation：** 详见原始论文或官方说明。

**方法：** 从表面质量到内在能力的评测

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### VideoPhy-2: A Challenging Action-Centric Physical Commonsense Evaluation in Video Generation
[paper](https://arxiv.org/abs/2503.06800) · [code](https://github.com/Hritikbansal/videophy/tree/main/VIDEOPHY2) · [project](https://videophy2.github.io/)

**Motivation：** 补充通用画质测量，检查生成视频是否符合动作和物理常识。

**方法：** 以动作和物理规则组织测试，结合人工评价和自动评判器。

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### 3DTrajMaster: Mastering 3D Trajectory for Multi-Entity Motion in Video Generation
[paper](https://arxiv.org/abs/2412.07759) · [project](https://fuxiao0719.github.io/projects/3dtrajmaster)

**Motivation：** 2D控制难表达多实体三维平移与旋转。

**方法：** 以每个实体6DoF轨迹和参考作为条件，gated object injector注入运动；UE多视角数据、domain adapter和退火采样支持训练泛化。

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Included for its 3D trajectory evaluation protocol (Section 4.3), not because 6DoF pose conditioning alone establishes an executable world.

### How Far is Video Generation from World Model: A Physical Law Perspective
[paper](https://arxiv.org/abs/2411.02385) · [project](https://phyworld.github.io)

**Motivation：** 分布内预测好不代表学到了可外推物理规律。

**方法：** 用受经典力学控制的2D模拟数据，测试分布内、分布外与组合泛化并做缩放分析。

**模型/表示：** 视频扩散；物理可控2D数据试验台

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### VideoPhy: Evaluating Physical Commonsense for Video Generation
[paper](https://arxiv.org/abs/2406.03520)

**Motivation：** 详见原始论文或官方说明。

**方法：** 物理常识与语义遵循分别评价

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

### VBench: Comprehensive Benchmark Suite for Video Generative Models
[paper](https://arxiv.org/abs/2311.17982) · [code](https://github.com/Vchitect/VBench) · [project](https://vchitect.github.io/VBench-project)

**Motivation：** 详见原始论文或官方说明。

**方法：** 视频生成的维度化质量评测

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Included as an evaluation resource. General quality, control, memory, and physical tests complement executable-world-specific evidence.

## Surveys & Perspectives

### AI for Games in the Foundation Model Era
[paper](https://arxiv.org/abs/2609.16679) · [project](https://eurekaleo.github.io/awesome-ai-for-games)

**Motivation：** 详见原始论文或官方说明。

**方法：** 按输出用途和主要证据主张组织

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Context and research organization; counted separately from original methods and systems.

### From Generation to Simulation: How Far Are World Models from Being True Simulators?
[paper](https://arxiv.org/abs/2608.23070) · [code](https://github.com/AtongWang/world-model-simulators)

**Motivation：** 详见原始论文或官方说明。

**方法：** 生成视频到可用模拟器的差距

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Context and research organization; counted separately from original methods and systems.

### From Pixels to States: Rethinking Interactive World Models as Game Engines
[paper](https://arxiv.org/abs/2607.14076)

**Motivation：** 详见原始论文或官方说明。

**方法：** 从游戏引擎的动作—状态—观察循环梳理

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Context and research organization; counted separately from original methods and systems.

### Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends
[paper](https://arxiv.org/abs/2606.01164) · [code](https://github.com/liujiuming123/Awesome-Interactive-World-Model)

**Motivation：** 详见原始论文或官方说明。

**方法：** 动作可控性、长时一致性、实时性

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Context and research organization; counted separately from original methods and systems.

### Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond
[paper](https://arxiv.org/abs/2604.22748) · [code](https://github.com/matrix-agent/awesome-agentic-world-modeling)

**Motivation：** 详见原始论文或官方说明。

**方法：** 定义预测、模拟与模型修订的能力边界，并讨论与应用匹配的评测。

**模型/表示：** 本目录未断言具体checkpoint。

**范围与证据：** Context and research organization; counted separately from original methods and systems.

### A Mechanistic View on Video Generation as World Models: State and Dynamics
[paper](https://arxiv.org/abs/2601.17067)

**Motivation：** 视觉相似或短视频质量无法完整刻画“世界模型”能力，需要按状态与动态解释方法。

**方法：** 以状态构建与动力学为两条轴，连接持久性、因果和评测；适合与本文的代码职责框架对照。

**模型/表示：** 不适用，属于综述/机制分析；状态—动态与评测组织参考

**范围与证据：** Context and research organization; counted separately from original methods and systems.

### 3D and 4D World Modeling: A Survey
[paper](https://arxiv.org/abs/2509.07996) · [code](https://github.com/worldbench/awesome-3d-4d-world-models) · [project](https://worldbench.github.io/survey)

**Motivation：** 多种世界表示和传感模态发展分散，需要统一梳理表示、方法、数据与评测。

**方法：** 按VideoGen、OccGen、LiDARGen等表示组织研究，汇总数据、应用及指标；本文仅借其表示与评测矩阵。

**模型/表示：** 不适用，不存在单一采用骨干；多表示分类与指标组织参考

**范围与证据：** Context and research organization; counted separately from original methods and systems.

### Understanding World or Predicting Future? A Comprehensive Survey of World Models
[paper](https://arxiv.org/abs/2411.14499) · [code](https://github.com/tsinghua-fib-lab/World-Model)

**Motivation：** world model同时指表示、预测和模拟，概念分歧影响方法比较与应用理解。

**方法：** 先定义概念，再按内部表示/未来预测及应用组织研究，讨论评测和开放问题；可借鉴其范围界定。

**模型/表示：** 不适用，综述本身不训练统一模型；定义和宏观组织参考

**范围与证据：** Context and research organization; counted separately from original methods and systems.
