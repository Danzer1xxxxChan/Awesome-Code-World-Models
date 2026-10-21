# World Systems

[← Main collection](../README.md) · [Scope](../docs/SCOPE.md) · [Verification](../docs/VERIFICATION.md)

Code, engine state, and generated visual observations in one pipeline.

The identity/source check and the depth of technical reading are separate fields. The notes below summarize prior targeted reading; they do not report a new reproduction.

<a id="c10"></a>

## SolarRenderer: Few-Step Generative Reference Rendering

[paper](https://arxiv.org/abs/2610.28630) · [code](https://github.com/Enderfga/SolarRenderer) · [project](https://enderfga.cn/SolarRenderer/)

- **Type / date:** Paper / 2026-10-20.
- **Method:** Uses structure control and few-step LoRAs on MiniMax-H3 for reference rendering, including a block-causal variant.
- **Scope:** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.
- **Models / representations in reading notes:** MiniMax-H3; control LoRA＋few-step LoRA，少步初始化使用DMAD; SolarWM训练/推理框架，不是另一视频骨干
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2610.28630).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 让同一渲染接口接受多种结构视频，并降低参考条件生成的采样成本。

**方法：** 结构视频编码为latent，放到与目标帧对应的RoPE位置；冻结H3，用控制LoRA和少步LoRA训练；提供四步全片与独立块因果版本。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="u058"></a>

## Mallea: Building, Steering, and Memorizing Worlds with Coding Agent

[paper](https://arxiv.org/abs/2610.21283) · [project](https://lxycopper.github.io/Mallea)

- **Type / date:** Paper / 2026-10-15.
- **Method:** Combines world construction, rule edits, and object texture memory in a coding-agent workflow.
- **Scope:** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2610.21283).

<details>
<summary>中文 motivation / 方法笔记</summary>

**方法：** 按交互需要联合选择对象几何、属性和规则；以对象身份索引纹理记忆，并依状态变化保留或更新。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="c05"></a>

## AgentGarten: Code Worlds for Evolving Agents

[paper](https://arxiv.org/abs/2610.12374) · [code](https://github.com/MirroS-Lab/AgentGarten) · [project](https://mirros-lab.github.io/agent-garten)

- **Type / date:** Paper / 2026-10-08.
- **Method:** Connects simulation backends to a shared geometry-conditioned renderer and studies agent practice in the resulting environments.
- **Scope:** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.
- **Models / representations in reading notes:** Cosmos3-Nano; Wan 2.2 VAE
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2610.12374).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 具身agent需要可扩展、可互动且视觉丰富的练习环境；单一引擎资产和渲染域限制环境多样性。

**方法：** 代码世界交给已有引擎执行，统一导出深度/法线；流式模型生成观测；以Adversarial Forcing处理生成历史，并组织agent练习循环。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="u074"></a>

## Oneira: From Open-Ended Generation to Open-World Interaction in Video World Models

[paper](https://arxiv.org/abs/2610.01614) · [project](https://madaoer.github.io/projects/oneira)

- **Type / date:** Paper / 2026-10-01.
- **Method:** Registers objects and interaction outcomes from generated observations into a persistent, editable world state.
- **Scope:** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.
- **Models / representations in reading notes:** MiniMax-H3 Ref2VA；LoRA
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2610.01614).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 开放视觉生成需要将新对象纳入可操作状态，并保留先前交互后果。

**方法：** coding agent读取3D实例状态表并规划动作，引擎执行局部状态更新与相机路径渲染，MiniMax-H3生成视频，再从新画面注册对象。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="c04"></a>

## GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models

[paper](https://arxiv.org/abs/2609.25652) · [project](https://jimntu.github.io/gamedirector)

- **Type / date:** Paper / 2026-09-22.
- **Method:** Separates explicit combat states and gameplay rules from video generation through a textual directing interface.
- **Scope:** Explicit combat rules and states are in scope. This system does not claim a full 3D proxy or pixel-aligned trajectory interface.
- **Models / representations in reading notes:** Wan2.2-TI2V-5B; Gemma-4-E2B-it; ResNet-18＋单层GRU的AttackNet/SituationNet; GPT-5.5、Gemini-3.1-Pro
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2609.25652).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 纯视觉模拟难以明确执行可配置的血量、冷却和NPC策略；作者将战斗逻辑放到外部模块。

**方法：** AttackNet识别命中，SituationNet估计局势；程序更新战斗状态，LLM选择合法boss动作，再用文本控制视频生成并叠加HUD。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="c03"></a>

## Code Plans, Diffusion Renders: Open-Ended Generative World Modeling

[paper](https://arxiv.org/abs/2609.26458) · [project](https://becauseimbatman0.github.io/CoDeR)

- **Type / date:** Paper / 2026-09-22.
- **Method:** Combines a programmable Three.js world with a video artist and registers generated content back into the world.
- **Scope:** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.
- **Models / representations in reading notes:** GPT-6 Astra; MiniMax-H3＋LoRA/ControlNet; SMPL-H
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2609.26458).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 代码擅长空间规划和机制，视频擅长外观；作者希望二者合作构建可持续扩展的世界。

**方法：** Creator和Executors构造Three.js世界与角色；Artist把代理变成视频，再将生成外观注册回世界以支持后续视角和扩展。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="c02"></a>

## Programmable World Model

[paper](https://arxiv.org/abs/2609.10540) · [code](https://github.com/AlayaLab/pwm) · [project](https://alaya-lab.github.io/pwm)

- **Type / date:** Paper / 2026-09-09.
- **Method:** Executes entity rules in a persistent engine and turns state-enriched object boxes into aligned video conditions.
- **Scope:** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.
- **Models / representations in reading notes:** LingBot-World-v1＋Structured Spatial ControlNet; Qwen3-VL、ViPE、SAM3、WildDet3D
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2609.10540).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 用低成本、可编程的实体表示控制交互结果，同时保留视频模型生成丰富细节的能力。

**方法：** 引擎推进带身份和语义的OBB状态，将其编译为空间控制图；以空间控制分支连接视频模型，并结合历史与几何记忆。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="c01"></a>

## Code World Model: Coding Agent as World Brain

[paper](https://arxiv.org/abs/2608.25927) · [code](https://github.com/buaacyw/code-world-model) · [project](https://buaacyw.github.io/cwm/)

- **Type / date:** Paper / 2026-08-26.
- **Method:** Maintains world state with a coding agent and compiles execution into proxy videos for visual generation.
- **Scope:** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.
- **Models / representations in reading notes:** GPT-5.6 Sol; GPT Image 2; MiniMax-H3 Ref2VA＋rank-128 LoRA
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2608.25927).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 隐式视频预测难以直接编辑和检查持久的世界规则；作者希望把可执行状态与视觉表现解耦。

**方法：** coding agent基于现有引擎控制、碰撞和循环编写世界；运行后导出深度与语义ID代理，LoRA适配视频模型，首帧锚定外观。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="c07"></a>

## StreamRender-H3: Interactive Coding Worlds with Real-time Streaming Diffusion Render

[project](https://nvlabs.github.io/Sana/Sol-Engine/StreamRender-H3/)

- **Type / date:** Technical report / date not stated.
- **Method:** Pairs a code game engine with a two-step streaming renderer for interactive visual feedback.
- **Scope:** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.
- **Models / representations in reading notes:** MiniMax-H3 Ref2VA的两步因果蒸馏版本; Three.js，不是学习模型; 不以固定coding LLM为渲染方法前提
- **Primary-source identity checked:** 2026-10-22; [source](https://nvlabs.github.io/Sana/Sol-Engine/StreamRender-H3/).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 代码世界已有高频、确定的交互状态，难点是让神经外观生成跟上实时输入。

**方法：** Three.js赛车引擎输出语义图；将H3适配为两步因果学生，结合流式推理、codec与运行时优化持续呈现画面。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="z078"></a>

## Streaming Code World Model

[code](https://github.com/TingtingLiao/streaming-code-world-model)

- **Type / date:** Implementation / date not stated.
- **Method:** Adapts Code World Model to causal chunked rendering using diffusion forcing and few-step self-forcing distillation.
- **Scope:** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.
- **Models / representations in reading notes:** MiniMax-H3；流式 LoRA 与4步DMD蒸馏
- **Primary-source identity checked:** 2026-10-22; [source](https://github.com/TingtingLiao/streaming-code-world-model).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 在线代理条件到达时，不能预先访问未来条件；同时需降低长时漂移和采样成本。

**方法：** MiniMax-H3 上的滑动注意力与旋转 RoPE KV 缓存、带噪历史和4步蒸馏；作者 README 明确目前尚未实时。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="n061"></a>

## Roblox Reality: Hybrid Architecture for Photorealistic Multiplayer Gaming

[source](https://about.roblox.com/newsroom/2026/04/roblox-reality-hybrid-architecture-democratizing-photorealistic-multiplayer-gaming)

- **Type / date:** Official report / date not stated.
- **Method:** Describes a hybrid multiplayer architecture combining authoritative game state with generated visual presentation.
- **Scope:** An official architecture description, not an independently reproduced end-to-end research benchmark.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://about.roblox.com/newsroom/2026/04/roblox-reality-hybrid-architecture-democratizing-photorealistic-multiplayer-gaming).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 在保留多人一致状态和创作工具的同时降低高保真资产制作负担。

**方法：** 共享服务器推进世界，边缘端依渲染与3D上下文做super-upsampling，并讨论本地角色叠加和响应控制。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="n059"></a>

## RenderFlow: Single-Step Neural Rendering via Flow Matching

[paper](https://studios.disneyresearch.com/2026/05/31/renderflow-single-step-neural-rendering-via-flow-matching/)

- **Type / date:** Paper / date not stated.
- **Method:** Maps structured rendering buffers to video observations with a single-step flow-based neural renderer.
- **Scope:** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.
- **Models / representations in reading notes:** Wan2.1＋G-buffer / envmap / keyframe adapters
- **Primary-source identity checked:** 2026-10-22; [source](https://studios.disneyresearch.com/2026/05/31/renderflow-single-step-neural-rendering-via-flow-matching/).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 多步扩散渲染的随机性和计算量妨碍高效、稳定的图形管线。

**方法：** 以干净albedo latent为起点进行bridge／flow matching；G-buffer属性、环境光与可选稀疏关键帧通过不同适配器注入。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="c08"></a>

## Matrix-Game 4.0

[paper](https://github.com/SkyworkAI/Matrix-Game/blob/main/Matrix-Game-4/docs/Matrix_Game_4_0.pdf) · [code](https://github.com/SkyworkAI/Matrix-Game/tree/main/Matrix-Game-4) · [project](https://matrix-game-v4-0.github.io/page/) · [data](https://huggingface.co/Skywork/Matrix-Game-4.0)

- **Type / date:** Technical report / date not stated.
- **Method:** Streams generated visuals from executable low-poly games while keeping gameplay and physics in the native engine.
- **Scope:** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.
- **Models / representations in reading notes:** Wan2.2-TI2V-5B→Wan2.2-Fun-5B-Control→官方5B场景模型; UMT5、Wan2.2 VAE，实时路径另用TAEHV
- **Primary-source identity checked:** 2026-10-22; [source](https://github.com/SkyworkAI/Matrix-Game/tree/main/Matrix-Game-4).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 希望保留传统引擎的规则、控制和碰撞，同时通过生成模型提升低模画面。

**方法：** 原生C++/OpenGL低模游戏持续输出RGB条件；场景专用视频模型生成画面，质量与实时配置采用不同步数和解码器。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="c09"></a>

## EdenLive: Real-Time Generative Rendering from Any Visual Reference

[code](https://github.com/VAST-AI-Research/EdenLive)

- **Type / date:** Implementation / date not stated.
- **Method:** Provides an interactive generative renderer that accepts engine imagery or other visual references.
- **Scope:** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.
- **Models / representations in reading notes:** Wan2.2-TI2V-5B、Wan2.1-I2V-14B; DINOv3及其派生编码器; FLUX.2 [klein] 9B
- **Primary-source identity checked:** 2026-10-22; [source](https://github.com/VAST-AI-Research/EdenLive).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 代理可能来自不同引擎、画风和构建工具，作者希望减少对固定代理外观的依赖。

**方法：** 用proxy视觉编码器提取参考视频条件，结合首帧和文本训练渲染器；同时提供双向离线与四步chunk-AR路径。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="n060"></a>

## DLSS 5: Real-Time Neural Rendering with Generative AI

[source](https://research.nvidia.com/labs/adlr/DLSS5/)

- **Type / date:** Official report / date not stated.
- **Method:** Uses game-engine color and motion information for generative neural enhancement in a real-time graphics pipeline.
- **Scope:** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.
- **Models / representations in reading notes:** 单步像素空间扩散神经渲染器
- **Primary-source identity checked:** 2026-10-22; [source](https://research.nvidia.com/labs/adlr/DLSS5/).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 希望在游戏的帧预算内补充高质量材质与照明细节，并保留引擎控制。

**方法：** 官方摘要描述像素空间单步扩散：推理接收RGB、运动向量、时间状态与艺术控制；场景属性用于训练一致性监督。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="c06"></a>

## Code Video Model

[paper](https://code-video-model.github.io/tech_report.pdf) · [code](https://github.com/code-video-model/CodeVideoModel) · [project](https://code-video-model.github.io/)

- **Type / date:** Technical report / date not stated.
- **Method:** Generates executable previs and uses proxy videos, reference appearance, and early-step conditioning to produce final clips.
- **Scope:** Connects an executable engine or explicit rule system to learned visual observations; the linked artifact may be a paper, implementation, or architecture report.
- **Models / representations in reading notes:** GPT-6; GPT-Image-2; MiniMax-H3
- **Primary-source identity checked:** 2026-10-22; [source](https://code-video-model.github.io/).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 文本难以精确表达镜头和动作；可执行代码能提供可编辑、可复现的视频预演。

**方法：** GPT生成Three.js代理视频，配合首帧和文本输入冻结视频模型；默认20步采样的前5步使用代理，后续去噪释放外观自由度。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>
