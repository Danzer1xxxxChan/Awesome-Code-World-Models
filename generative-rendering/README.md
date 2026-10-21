# Generative Rendering

[← Main collection](../README.md) · [Scope](../docs/SCOPE.md) · [Verification](../docs/VERIFICATION.md)

Engine-to-video, rendering buffers, scene choreography, character rendering, and simulation-to-real observations.

The identity/source check and the depth of technical reading are separate fields. The notes below summarize prior targeted reading; they do not report a new reproduction.

<a id="n006"></a>

## RoboRender: Robot-Oriented Video Generation for Visual Sim-to-Real Transfer

[paper](https://arxiv.org/abs/2610.09254) · [project](https://robo-render.github.io)

- **Type / date:** Paper / 2026-10-07.
- **Method:** Converts simulated robot observations into more realistic training videos using geometry and robot-preserving conditions.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** Wan2.1-T2V-1.3B＋LoRA
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2610.09254).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 机器人合成视频需要同时保持多视角、动作标签和场景结构。

**方法：** 把仿真深度、机器人保留RGB与噪声目标通道拼接，再联合堆叠视角；LoRA适配并用上一块末帧延续。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t018"></a>

## CoaG: Cylinders on a Grid for Coarse 3D Layout Control in Video Generation

[paper](https://arxiv.org/abs/2609.24208) · [project](https://zshyang.github.io/CoaG)

- **Type / date:** Paper / 2026-09-21.
- **Method:** Renders coarse 3D layouts with stable object identities to guide camera and entity placement.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** Wan2.2-Fun-A14B-Control；rank-64 LoRA
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2609.24208).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 希望用低成本3D信号控制多人位置、规模与遮挡。

**方法：** 地面线框网格编码尺度与相机运动，稳定色圆柱编码人物位置和遮挡；用自动数据引擎和LoRA适配控制模型。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="n052"></a>

## LynnReal-Omni: Native multi-modal Video Generation for Agentic Visual Workflows

[paper](https://arxiv.org/abs/2609.15863)

- **Type / date:** Paper / 2026-09-14.
- **Method:** Unifies rendering, reference control, and editing with heterogeneous visual conditions in shared video models.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** MiniMax-H3系；32B Standard / 27B Flash
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2609.15863).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 分散的视频任务接口限制智能体组合引用、3D场景与游戏控制。

**方法：** MiniMax-H3系共享多模态DiT编码异构条件，联合多任务流匹配与少步蒸馏；有界历史、轻量解码器支持流式生成。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="n002"></a>

## RGBX-Next: Towards Realistic Generative Rendering from G-Buffers

[paper](https://arxiv.org/abs/2608.13929)

- **Type / date:** Paper / 2026-08-14.
- **Method:** Unifies RGB and typed rendering-buffer inputs in a multimodal video renderer.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** Wan2.1-14B；冻结VAE
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2608.13929).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 单任务渲染器和合成数据难以同时覆盖真实外观、多种图形编辑与长视频。

**方法：** 用带类型的帧槽统一RGB与G-buffer条件／目标，以X-patchify压缩多模态输入；合成与估计真实内在属性联合训练，支持分块延续。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t012"></a>

## UniMoCa: Unifying Motion and Camera Controls as Visual Proxies for Faithful Human Video Generation

[paper](https://arxiv.org/abs/2608.01944) · [project](https://tanliming-daniel.github.io/UniMoCa)

- **Type / date:** Paper / 2026-08-03.
- **Method:** Combines articulated motion, multi-person layouts, and camera trajectories into visual proxies.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** Wan2.2 I2V；MCVP proxy encoder
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2608.01944).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 视觉动作图与非视觉相机参数存在异构接口和归因冲突。

**方法：** 把3D人体、多人布局和相机轨迹统一为MCVP视觉代理；显式相机标记区分运动来源，proxy token与视频token联合训练。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t004"></a>

## VideoCoCo: Code-as-CoT for Physically-Consistent Video Generation via an Agentic Dual-Engine System

[paper](https://arxiv.org/abs/2607.27380)

- **Type / date:** Paper / 2026-07-29.
- **Method:** Generates executable Blender drafts and uses a second visual engine to produce physically guided videos.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** Blender Python；OmniWeaving初始化；全量或LoRA编辑器适配
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2607.27380).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 文本或稀疏分镜不能把完整物理过程明确实例化。

**方法：** 编码agent写Blender时空程序，执行成确定性draft；指令agent描述外观变换，用VideoCoCo-3K适配draft-conditioned视频编辑器。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="r05"></a>

## Generative World Renderer at the Speed of Play

[paper](https://arxiv.org/abs/2607.18703)

- **Type / date:** Paper / 2026-07-21.
- **Method:** Accelerates buffer-conditioned world rendering with few-step autoregression and a lightweight video codec.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** AlayaRenderer / Wan2.1系; 四步因果视频模型; 轻量条件编码器与TAEHV解码器
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2607.18703).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 高质量离线生成速度与上下文使用方式不适合持续交互，需要整条渲染链路提速。

**方法：** 将AlayaRenderer转为因果学生并蒸馏为四步，压缩条件编码器与解码器，结合流式执行减少生成开销。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="n039"></a>

## ProxyUp: Training-Free Proxy-Conditioned Video Generation for Controllable Dynamics

[paper](https://arxiv.org/abs/2607.03732) · [project](https://zanue.github.io/proxyup)

- **Type / date:** Paper / 2026-07-04.
- **Method:** Uses motion extracted from proxy videos to control a pretrained video generator without additional training.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** Wan2.2
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2607.03732).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 粗代理视频的运动约束与逼真外观生成相互牵制。

**方法：** 免训练ODE反演提取前景运动latent，区域噪声处理背景，再用SFR使组合latent返回可采样区域。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t033"></a>

## 3D Scene-Adaptive Trajectory-Controllable Human Image Animation with Camera Movement

[paper](https://arxiv.org/abs/2606.30514) · [project](https://robinhood256100.github.io/web-disp)

- **Type / date:** Paper / 2026-06-29.
- **Method:** Adapts articulated motion to scene geometry and combines visibility-aware conditions for camera-controlled character animation.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2606.30514).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 人体轨迹和镜头改变后还应适应真实地形与可见区域。

**方法：** 地面自适应3D运动重定向，配合按场景可见性mask融合点云先验到latent以支持新视角。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t013"></a>

## Directing the World: Fast Autoregressive Video Generation with Compositional Human-Camera Control

[paper](https://arxiv.org/abs/2606.27964) · [project](https://whydahuzi.github.io/Directing-the-World.github.io)

- **Type / date:** Paper / 2026-06-26.
- **Method:** Composes human-motion and camera controls in fast autoregressive video generation.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** MMPL自回归骨干；SMPL；ControlNet式分支
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2606.27964).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 长时AR视频加入人体和相机条件后会互相干扰并破坏生成先验。

**方法：** 先学SMPL运动控制，再引入与因果块对齐的相机控制；t-guided projection、Motion-CFG和Fast-Slow训练稳定适配。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t011"></a>

## ActCam: Zero-Shot Joint Camera and 3D Motion Control for Video Generation

[paper](https://arxiv.org/abs/2605.06667) · [project](https://elkhomar.github.io/actcam)

- **Type / date:** Paper / 2026-05-07.
- **Method:** Reprojects character and scene conditions under a target camera and schedules their use during video sampling.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** VACE；MoGe；3D姿态恢复
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2605.06667).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 人体动作和镜头运动混合在2D条件中，难以独立重组。

**方法：** 重建背景深度与3D姿态，在目标相机下渲染对齐条件；前期pose＋depth、后期只保留pose，免训练完成联合控制。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="n007"></a>

## ComSim: Building Scalable Real-World Robot Data Generation via Compositional Simulation

[paper](https://arxiv.org/abs/2604.11386) · [project](https://faceong.github.io/ComSim)

- **Type / date:** Paper / 2026-04-13.
- **Method:** Replays real actions in simulation and composes dynamics conditions to synthesize robot training videos.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2604.11386).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 仿真图像和真实图像有域差，纯视频生成又可能破坏动作对应关系。

**方法：** 重放真实动作得到配对仿真观察，组合动作动态与视觉动态条件的分数生成伪真实视频，再训练并部署机器人策略。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t005"></a>

## Lighting-grounded Video Generation with Renderer-based Agent Reasoning

[paper](https://arxiv.org/abs/2604.07966)

- **Type / date:** Paper / 2026-04-09.
- **Method:** Uses an agent-controlled renderer to supply lighting-grounded conditions for video generation.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** Wan2.2-TI2V-5B＋LoRA；轻量proxy encoder
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2604.07966).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 布局、照明与相机耦合，限制电影和虚拟制作中的编辑。

**方法：** renderer-based agent构造场景、HDR照明与相机；渲染diffuse、rough GGX、glossy GGX组成9通道proxy，用编码器／adapter和分阶段训练生成视频。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t014"></a>

## HumANDiff: Articulated Noise Diffusion for Motion-Consistent Human Video Generation

[paper](https://arxiv.org/abs/2604.05961) · [project](https://taohuumd.github.io/projects/HumANDiff)

- **Type / date:** Paper / 2026-04-07.
- **Method:** Renders surface-attached noise through an articulated body to improve motion-consistent video synthesis.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** CogVideoX-5B-I2V；另在Wan2.1-I2V验证
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2604.05961).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 独立像素噪声难保持人体表面运动对应。

**方法：** 在SMPL的UV表面采样共享高斯噪声并随姿态渲染到图像，配合外观／运动联合学习和一致性监督。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="r04"></a>

## Generative World Renderer

[paper](https://arxiv.org/abs/2604.02329) · [project](https://alaya-studio.github.io/renderer)

- **Type / date:** Paper / 2026-04-02.
- **Method:** Trains generative rendering from synchronized game imagery and structured rendering buffers.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** Wan2.1-T2V-1.3B，全量适配; 同步RGB与五类G-buffer通道
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2604.02329).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 需要把现有高质量游戏数据转成同步、可学习的渲染监督，并支持可控的图像形成。

**方法：** 采集AAA游戏RGB与G-buffer配对，训练条件视频渲染及逆向分解，使几何、材质与外观能够分开控制。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="u057"></a>

## VideoWeaver: Multimodal Multi-View Video-to-Video Transfer for Embodied Agents

[paper](https://arxiv.org/abs/2603.25420)

- **Type / date:** Paper / 2026-03-26.
- **Method:** Transfers synchronized multimodal scene views into videos for embodied-agent workflows.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2603.25420).

<a id="t016"></a>

## Hand2World: Autoregressive Egocentric Interaction Generation via Free-Space Hand Gestures

[paper](https://arxiv.org/abs/2602.09600)

- **Type / date:** Paper / 2026-02-10.
- **Method:** Uses projected hand geometry and camera rays to control generated egocentric interactions.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2602.09600).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 自由空间手势与接触训练数据有域差，手运动与头部视角又易混淆。

**方法：** 用投影3D手网格提供遮挡不变条件，以Plücker射线独立控制相机；把双向模型蒸馏为因果生成器。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="r03"></a>

## Coarse-to-Real: Generative Rendering for Populated Dynamic Scenes

[paper](https://arxiv.org/abs/2601.22301) · [project](https://gonzalognogales.github.io/coarse2real)

- **Type / date:** Paper / 2026-01-29.
- **Method:** Transfers coarse 3D crowd simulations into realistic videos through staged synthetic-real adaptation.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** Wan2.1；DINOv3 ViT；T5-XXL
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2601.22301).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 粗仿真能控制城市人群，但缺少配对真实监督，结构条件也可能泄漏CG外观。

**方法：** 先用真实视频适配生成先验，再冻结骨干，通过DINOv3特征adapter连接合成／真实控制，做domain hedging。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="r02"></a>

## FrameDiffuser: G-Buffer-Conditioned Diffusion for Neural Forward Frame Rendering

[paper](https://arxiv.org/abs/2512.16670)

- **Type / date:** Paper / 2025-12-18.
- **Method:** Conditions frame generation on rendering buffers and previous outputs for temporally coherent neural rendering.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** Stable Diffusion 1.5; 10通道ControlNet＋rank-64 ControlLoRA; 前一生成帧
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2512.16670).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 面向特定环境渲染时，既要跟随精确结构，又要抑制逐帧生成的闪烁。

**方法：** 以多通道G-buffer控制单帧扩散，上一生成帧提供时间上下文；通过轻量适配学习目标环境的前向渲染。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t006"></a>

## LAMP: Language-Assisted Motion Planning for Controllable Video Generation

[paper](https://arxiv.org/abs/2512.03619) · [project](https://cyberiada.github.io/LAMP)

- **Type / date:** Paper / 2025-12-03.
- **Method:** Compiles a motion-planning language into object-camera trajectories and visual control signals.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2512.03619).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 自然语言难直接回归有结构、可编辑的对象和镜头轨迹。

**方法：** LLM产生电影运动DSL，确定性转换为对象／相机3D轨迹，再编译成控制视频或接入其他生成器；程序化数据训练运动规划器。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t007"></a>

## PhysChoreo: Physics-Controllable Video Generation with Part-Aware Semantic Grounding

[paper](https://arxiv.org/abs/2511.20562)

- **Type / date:** Paper / 2025-11-25.
- **Method:** Grounds part-level physical controls in rigid-body and material-point simulation before visual generation.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** InstantMesh；PartField；GPT-5；Taichi；Wan2.2-Fun-5B-Control
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2511.20562).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 物性通常只按整体对象估计，且物理视频多只能修改初始条件。

**方法：** 部件语义估计物理场，MPM／刚体求解器接受随时间编辑的参数和力；轨迹视频约束后续视频生成。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="r09"></a>

## X2Video: Adapting Diffusion Models for Multimodal Controllable Neural Video Rendering

[paper](https://arxiv.org/abs/2510.08530) · [project](https://luckyhzt.github.io/x2video)

- **Type / date:** Paper / 2025-10-09.
- **Method:** Adapts diffusion models to intrinsic rendering channels, reference imagery, and local or global text control.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** 基于Stable Diffusion 2.1的XRGB; 参考/时间attention与区域文本控制; 不是直接以CogVideoX为基础
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2510.08530).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 全局文本和单一结构条件不足以控制局部材质、光照与时间变化。

**方法：** 结合内在通道、参考图和局部/全局文本，用参考与时间attention以及递归关键帧/插帧完成视频渲染。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="s101"></a>

## IllumiCraft: Unified Geometry and Illumination Diffusion for Controllable Video Generation

[paper](https://arxiv.org/abs/2506.03150)

- **Type / date:** Paper / 2025-06-03.
- **Method:** Combines rendered lighting, appearance references, and geometric motion conditions for controllable video synthesis.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** Wan2.1 1.3B；4×A6000训练（§4.2）。
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2506.03150).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 光照控制缺少跨帧几何联系。

**方法：** 将HDR环境视频、重光照外观与3D点轨迹共同注入视频扩散。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="u071"></a>

## Uni3C: Unifying Precisely 3D-Enhanced Camera and Human Motion Controls for Video Generation

[paper](https://arxiv.org/abs/2504.14899) · [code](https://github.com/ewrfcas/Uni3C)

- **Type / date:** Paper / 2025-04-21.
- **Method:** Combines scene point clouds and articulated characters in a shared 3D guidance interface for camera and motion control.
- **Scope:** The joint scene-and-character guidance is relevant; ordinary camera control without an executable visual-world interface is outside the method scope.
- **Models / representations in reading notes:** Wan-I2V 14B；约0.95B PCDController
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2504.14899).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 相机与人体控制需要共享3D坐标，同时减少大型骨干的适配成本。

**方法：** 轻量PCDController以目标相机下的点云渲染视频控制Wan-I2V；与人体动画及3D世界引导模块组合。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="u037"></a>

## Cosmos-Transfer1: Conditional World Generation with Adaptive Multimodal Control

[paper](https://arxiv.org/abs/2503.14492) · [code](https://github.com/nvidia-cosmos/cosmos-transfer1)

- **Type / date:** Paper / 2025-03-18.
- **Method:** Transfers structured simulation or visual conditions into generated observations using multimodal control.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2503.14492).

<a id="n038"></a>

## ReBot: Scaling Robot Learning with Real-to-Sim-to-Real Robotic Video Synthesis

[paper](https://arxiv.org/abs/2503.14526) · [project](https://yuffish.github.io/rebot)

- **Type / date:** Paper / 2025-03-15.
- **Method:** Replays robotic trajectories in simulation and composites robot-object renderings into real backgrounds.
- **Scope:** An engine-grounded data-synthesis pipeline; its composition step should not be mistaken for diffusion-based rendering.
- **Models / representations in reading notes:** Isaac Sim 4.1 / Isaac Lab；Octo；OpenVLA
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2503.14526).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 真实机器人动作昂贵，希望保留动作标签并替换对象与环境。

**方法：** 在Isaac Sim重放轨迹，补全真实背景，把仿真机器人／对象合成回背景，训练Octo或OpenVLA。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="n008"></a>

## Re$^3$Sim: Generating High-Fidelity Simulation Data via 3D-Photorealistic Real-to-Sim for Robotic Manipulation

[paper](https://arxiv.org/abs/2502.08645) · [project](https://re3sim.github.io)

- **Type / date:** Paper / 2025-02-12.
- **Method:** Reconstructs real scenes and connects them to physical simulation and photorealistic demonstration rendering.
- **Scope:** A real-to-sim and observation-generation predecessor; its renderer is not presented as a code-conditioned diffusion world model.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2502.08645).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 几何与外观域差阻碍低成本仿真数据迁移。

**方法：** 重建真实场景并与物理仿真连接，以高保真神经渲染生成跨视角示范，验证策略迁移。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t001"></a>

## CineMaster: A 3D-Aware and Controllable Framework for Cinematic Text-to-Video Generation

[paper](https://arxiv.org/abs/2502.08639) · [project](https://cinemaster-dev.github.io)

- **Type / date:** Paper / 2025-02-12.
- **Method:** Compiles 3D object and camera choreography into depth, class, and camera conditions for cinematic video generation.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** 预训练T2V DiT＋3D VAE＋T5；未披露可确认的商品检查点
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2502.08639).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 电影创作需要同时指定对象布局、对象运动和相机。

**方法：** 在Blender中编排3D框与相机关键帧，导出深度、类别与相机轨迹；语义布局注入模块和camera adapter控制视频DiT。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t021"></a>

## MotionCanvas: Cinematic Shot Design with Controllable Image-to-Video Generation

[paper](https://arxiv.org/abs/2502.04299) · [project](https://motion-canvas25.github.io)

- **Type / date:** Paper / 2025-02-06.
- **Method:** Translates scene-centered shot design into object and camera motion conditions for video generation.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** 内部DiT-I2V；3D VAE；DCT轨迹token
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2502.04299).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 创作者在3D场景中表达意图，而训练视频常只能可靠提取2D运动。

**方法：** 将场景中心的相机／对象编排翻译成屏幕空间轨迹和框；DCT编码点轨迹，微调运动条件视频DiT。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="r01"></a>

## DiffusionRenderer: Neural Inverse and Forward Rendering with Video Diffusion Models

[paper](https://arxiv.org/abs/2501.18590) · [project](https://research.nvidia.com/labs/toronto-ai/DiffusionRenderer/)

- **Type / date:** Paper / 2025-01-30.
- **Method:** Learns inverse and forward rendering between RGB videos, scene buffers, and lighting conditions.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** Stable Video Diffusion（SVD img2vid）适配; 几何与材质G-buffer
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2501.18590).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 传统渲染资产制作昂贵，真实视频又缺少几何/材质分解；需要共享生成先验连接正向与逆向渲染。

**方法：** 逆向模型把RGB视频分解为几何/材质缓冲区，正向模型按这些条件生成RGB，支持光照与材质编辑。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="r06"></a>

## Diffusion as Shader: 3D-aware Video Diffusion for Versatile Video Generation Control

[paper](https://arxiv.org/abs/2501.03847) · [code](https://github.com/IGL-HKUST/DiffusionAsShader) · [project](https://igl-hkust.github.io/das)

- **Type / date:** Paper / 2025-01-07.
- **Method:** Uses rendered 3D tracking guidance to control camera motion, mesh animation, and object motion in video generation.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** CogVideoX-I2V; 深度/分割/3D tracking工具
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2501.03847).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 相机、对象、动作各用独立条件网络会割裂控制接口；3D对应可统一这些需求。

**方法：** 将3D跟踪/对应关系编码成tracking videos，微调I2V模型支持相机控制、网格动画、动作迁移与对象操控。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t036"></a>

## AutoVFX: Physically Realistic Video Editing from Natural Language Instructions

[paper](https://arxiv.org/abs/2411.02394) · [project](https://haoyuhsu.github.io/autovfx-website)

- **Type / date:** Paper / 2024-11-04.
- **Method:** Executes language-directed scene and physics edits, then renders and composites their visual consequences into video.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** GPT-4 / GPT-4V；SuGaR；Blender；资产检索／生成
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2411.02394).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 真实视频的复杂特效编辑需要组合重建、物理和可控操作。

**方法：** 神经场景建模后由LLM组合编辑API，执行对象／物理修改，再以光照、阴影和遮挡感知渲染合成回视频。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="s104"></a>

## Tex4D: Zero-shot 4D Scene Texturing with Video Diffusion Models

[paper](https://arxiv.org/abs/2410.10821) · [project](https://tex4d.github.io)

- **Type / date:** Paper / 2024-10-14.
- **Method:** Uses shared UV-space information across views and time to texture dynamic scenes with video diffusion.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** 深度条件CTRL-Adapter；UV latent聚合与DDIM。
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2410.10821).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 动态网格纹理需要跨视角与跨时间一致。

**方法：** 在UV空间聚合多视角latent，修改DDIM并混合参考UV纹理，生成动态纹理序列。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="u073"></a>

## PhysGen: Rigid-Body Physics-Grounded Image-to-Video Generation

[paper](https://arxiv.org/abs/2409.18964) · [project](https://stevenlsw.github.io/physgen)

- **Type / date:** Paper / 2024-09-27.
- **Method:** Runs estimated rigid-body dynamics and refines the resulting renderings into videos.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2409.18964).

<a id="n029"></a>

## SimGen: Simulator-conditioned Driving Scene Generation

[paper](https://arxiv.org/abs/2406.09386)

- **Type / date:** Paper / 2024-06-13.
- **Method:** Uses simulator observations as explicit controls for realistic driving-scene generation.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2406.09386).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 真实布局数据有限，直接条件生成容易域内过拟合。

**方法：** 混合MetaDrive仿真和真实DIVA视频，用级联扩散解决域差与多条件冲突。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="t028"></a>

## Champ: Controllable and Consistent Human Image Animation with 3D Parametric Guidance

[paper](https://arxiv.org/abs/2403.14781) · [project](https://fudan-generative-vision.github.io/champ)

- **Type / date:** Paper / 2024-03-21.
- **Method:** Renders an articulated human model into depth, normal, semantic, and pose guidance for character animation.
- **Scope:** Included for parameterized-character rendering. This does not bring all reference-image or pose-transfer methods into the method corpus.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2403.14781).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 2D骨架不足以表达人体体形和三维朝向。

**方法：** 从SMPL渲染深度、法线、语义图，并融合骨架条件驱动潜在扩散，支持体形对齐。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="r07"></a>

## Generative Rendering: Controllable 4D-Guided Video Generation with 2D Diffusion Models

[paper](https://arxiv.org/abs/2312.01409) · [project](https://primecai.github.io/generative_rendering/)

- **Type / date:** Paper / 2023-12-03.
- **Method:** Uses explicit 4D scene correspondences to guide temporally coherent generation with image diffusion models.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** Stable Diffusion系2D模型＋depth ControlNet; 主要通过推理时注入实现
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2312.01409).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 图像扩散外观能力强，但逐帧运行会闪烁；动画网格已知的跨帧对应应能提供控制。

**方法：** 从4D网格导出深度、UV和对象ID，用深度ControlNet、UV一致噪声和跨帧/UV特征注入生成连贯视频。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="u072"></a>

## GPT4Motion: Scripting Physical Motions in Text-to-Video Generation via Blender-Oriented GPT Planning

[paper](https://arxiv.org/abs/2311.12631)

- **Type / date:** Paper / 2023-11-21.
- **Method:** Generates Blender physics scripts and uses their execution to guide visual synthesis.
- **Scope:** Studies visual realization from an explicit scene, engine output, parameterized character, physical simulation, or its rendered control signals.
- **Models / representations in reading notes:** GPT-4＋Blender物理引擎; Stable Diffusion＋ControlNet
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2311.12631).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 将文本中的物理过程明确交给模拟器，而非完全依靠像素模型推断。

**方法：** GPT-4生成Blender Python物理脚本，执行刚体／布料／液体模拟并导出动态条件；ControlNet引导Stable Diffusion生成画面。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="n043"></a>

## Enhancing Photorealism Enhancement

[paper](https://arxiv.org/abs/2105.04619) · [code](https://github.com/intel-isl/PhotorealismEnhancement)

- **Type / date:** Paper / 2021-05-10.
- **Method:** Enhances rendered game imagery using rendering-buffer information and learned appearance refinement.
- **Scope:** An engine-to-observation appearance-enhancement predecessor, not a rule-learning or world-construction system.
- **Models / representations in reading notes:** G-buffer条件卷积网络＋对抗训练
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2105.04619).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 合成画面的外观域差会使普通图像翻译出现伪影。

**方法：** 利用渲染管线中间表示、卷积网络和多层感知对抗监督，并按布局分布采样局部图像块。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="n042"></a>

## Deferred Neural Rendering: Image Synthesis using Neural Textures

[paper](https://arxiv.org/abs/1904.12356)

- **Type / date:** Paper / 2019-04-28.
- **Method:** Learns surface-attached neural textures and decodes them into scene observations with a neural renderer.
- **Scope:** A learned scene-rendering predecessor using an explicit surface representation, not a complete programmable world model.
- **Models / representations in reading notes:** Neural Textures＋卷积神经渲染器
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/1904.12356).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 不完美几何难以直接渲染逼真且一致的观察。

**方法：** 在代理网格表面学习高维Neural Texture，再以延迟神经渲染器解码成RGB。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>
