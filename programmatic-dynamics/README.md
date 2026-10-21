# Programmatic Dynamics & Rules

[← Main collection](../README.md) · [Scope](../docs/SCOPE.md) · [Verification](../docs/VERIFICATION.md)

Executable transition models, rule induction, active identification, and planning.

The identity/source check and the depth of technical reading are separate fields. The notes below summarize prior targeted reading; they do not report a new reproduction.

<a id="a16"></a>

## RoleWorld: Knowledge Transfer in World Modeling with Functional Role Abstractions

[paper](https://arxiv.org/abs/2610.13172)

- **Type / date:** Paper / 2026-10-09.
- **Method:** Transfers executable world knowledge across environments through functional-role abstractions.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** GPT-5.6 Sol; Qwen3-8B、GPT-5.6 Luna; functional role prototypes＋程序规则
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2610.13172).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 外观和对象名字变化会破坏规则复用，需要按对象在机制中的功能进行跨世界迁移。

**方法：** 学习角色原型及可执行转移规则；迁移时保持原型和规则，调整目标世界的角色绑定与参数。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="a14"></a>

## Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks

[paper](https://arxiv.org/abs/2610.11794)

- **Type / date:** Paper / 2026-10-08.
- **Method:** Revises reflective rulebooks and compiles them into executable models for prediction and planning.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** Claude Opus 5; Claude Code，extra-high reasoning; 外部规则簿与程序，不更新LLM权重
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2610.11794).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 仅存对话或直接改代码不易积累稳定、可反思的机制知识。

**方法：** 将自然语言规则簿编译成转移、观测和目标程序，利用失败和重放反馈递归修正规则簿，固定底层LLM。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="a13"></a>

## Kepler: Auditable World Models for ARC-AGI-3

[paper](https://arxiv.org/abs/2610.00834) · [project](https://kepler-harness.vercel.app)

- **Type / date:** Paper / 2026-09-30.
- **Method:** Audits executable game hypotheses using replay and action-time prediction checks.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** Claude Opus 5、GPT-5.6 Sol（max）; 可执行假设＋重放/预测验证
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2610.00834).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 历史拟合不保证新行动预测正确；世界模型的成功需要可追查的验证证据。

**方法：** 对程序假设进行转移重放认证，规划后加入行动时的条件预测检查，用新观察定位不成立的假设。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="a12"></a>

## Twin: Playing an Unknown Game with a Test-Time Digital Twin

[paper](https://arxiv.org/abs/2608.14490) · [code](https://github.com/Alexyskoutnev/TWIN-ARC-AGI-3) · [project](https://arc-agi-3-twin.vercel.app)

- **Type / date:** Paper / 2026-08-14.
- **Method:** Creates a test-time game twin and checks replayed transitions before using it to select actions.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** GPT-5.6 Sol，xhigh; Claude Opus 5的外部结果不是Twin骨干
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2608.14490).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 未知游戏的即时推理容易遗忘机制，也缺少行动前可验证的预测工具。

**方法：** coding agent边玩边构造数字孪生，要求重放历史转移；通过孪生搜索计划，在新反例出现时修改程序。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="a11"></a>

## Tycho: Active Abstraction with Programmatic World Models for ARC-AGI-3

[paper](https://arxiv.org/abs/2607.28287) · [code](https://github.com/NIMI-research/Tycho)

- **Type / date:** Paper / 2026-07-30.
- **Method:** Actively builds and tests programmatic abstractions for unfamiliar interactive visual puzzles.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** Claude Opus 4.8; GPT-5.6 Sol、Claude Opus 5; Tycho actor–builder工作流
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2607.28287).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 未知交互游戏中，建模过早或抽象错误会浪费预算，需要判断何时探索、建模、修复或直接行动。

**方法：** actor与builder协作维护可执行假设，主动测试抽象，依据模型有效性选择规划或绕过模型。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="u048"></a>

## World-Time Compute with Verified Code World Models

[paper](https://arxiv.org/abs/2609.09163) · [code](https://github.com/quome-cloud/openworld)

- **Type / date:** Paper / 2026-07-07.
- **Method:** Uses verified world programs to generate precise training trajectories for downstream models.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2609.09163).

<a id="a15"></a>

## OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration for ARC-AGI-3

[paper](https://arxiv.org/abs/2607.01531)

- **Type / date:** Paper / 2026-07-01.
- **Method:** Prioritizes ontology errors when exploring and repairing programmatic models of interactive visual environments.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** Claude Opus 4.8，主要配置high; 论文报告1M窗口
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2607.01531).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 对象抽象本身可能错；在错误对象/属性定义上继续修动态规则会低效。

**方法：** 优先探测并修订ontology，再更新可执行世界程序；将交互预算投向最能区分抽象假设的动作。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="a10"></a>

## Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games

[paper](https://arxiv.org/abs/2606.16070)

- **Type / date:** Paper / 2026-06-14.
- **Method:** Evaluates synthesized game models with multi-step lookahead under partial observability.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** Qwen3-Coder-480B-A35B-Instruct-Turbo; Qwen3-Max-Thinking及DeepSeek-V4-Pro/Flash等
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2606.16070).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 只看单步预测不足以说明世界模型能否支持决策；需要衡量多步行动后果。

**方法：** 结合轨迹及截图提取的信息合成独立可执行环境，以K步前瞻比较候选动作，迭代修复对规划重要的模型误差。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="a08"></a>

## Distilling Game Code World Model Generation into Lightweight Large Language Models

[paper](https://arxiv.org/abs/2605.24375)

- **Type / date:** Paper / 2026-05-23.
- **Method:** Distills game-world program generation into smaller coding models using supervised and verifiable-reward training.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** Qwen2.5-3B-Instruct; SFT＋GRPO/RLVR; GPT-4o不是学生骨干
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2605.24375).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 依赖大闭源LLM生成游戏模拟器成本高，希望把可执行规则合成能力迁移到小模型。

**方法：** 以游戏代码数据进行SFT，再用执行反馈和可验证奖励做GRPO；分开训练与留出游戏，检验生成程序的规则正确性。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="u050"></a>

## Executable World Models for ARC-AGI-3 in the Era of Coding Agents

[paper](https://arxiv.org/abs/2605.05138) · [code](https://github.com/astroseger/arc-3-agents-baseline1)

- **Type / date:** Paper / 2026-05-06.
- **Method:** Studies verification-driven executable world models for ARC-AGI-3 environments.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** No particular checkpoint is asserted in this catalog.
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2605.05138).

<a id="a17"></a>

## Learning Abstractions for Hierarchical Planning in Program-Synthesis Agents

[paper](https://arxiv.org/abs/2602.00929)

- **Type / date:** Paper / 2026-01-31.
- **Method:** Learns reusable program abstractions for hierarchical planning from interaction experience.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** GPT-4o; BFS; o4-mini不是方法的默认骨干
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2602.00929).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 单任务合成的高层技能难复用；抽象应同时保留符号可规划性和低层可执行性。

**方法：** TheoryCoder-2从经验学习PDDL高层operator、Python谓词及低层转移，进行分层搜索并积累可复用抽象。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="a07"></a>

## One Life to Learn: Inferring Symbolic World Models for Stochastic Environments from Unguided Exploration

[paper](https://arxiv.org/abs/2510.12088) · [project](https://onelife-worldmodel.github.io)

- **Type / date:** Paper / 2025-10-14.
- **Method:** Infers stochastic symbolic dynamics through unguided exploration in an object-oriented game environment.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** 概率化原子程序规律及其可学习权重
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2510.12088).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 无任务奖励、少量且危险的探索下，需发现稀疏激活的随机机制，并区分相互冲突的候选规律。

**方法：** 探索收集对象状态转移；LLM生成最小前提—效果Python规律；推断规律权重，只向解释实际变化的规律分配信用。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="a06"></a>

## Code World Models for General Game Playing

[paper](https://arxiv.org/abs/2510.04542)

- **Type / date:** Paper / 2025-10-06.
- **Method:** Compiles game descriptions and trajectories into executable rules for transition, legality, and search.
- **Scope:** The visual/spatial game-rule component is relevant; purely textual or nonvisual symbolic planning is not the focus of this collection.
- **Models / representations in reading notes:** Gemini 2.5 Pro; MCTS、ISMCTS; PPO策略，不是视觉生成器
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2510.04542).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 规则文本和轨迹不能直接被搜索算法调用，需要编译成一致、可执行的游戏接口。

**方法：** 合成OpenSpiel风格的合法动作、状态转移和终止等Python函数，以轨迹测试修正；结合MCTS/ISMCTS处理完全或不完全信息游戏。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="a05"></a>

## Finite Automata Extraction: Low-data World Model Learning as Programs from Gameplay Video

[paper](https://arxiv.org/abs/2508.11836)

- **Type / date:** Paper / 2025-08-15.
- **Method:** Extracts compact program-like game dynamics from a small amount of gameplay video.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** Retro Coder DSL＋finite automata; 未找到将GPT类模型作为核心的证据
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2508.11836).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 希望用少量gameplay视频恢复可执行机制，减少大规模交互和数据需求。

**方法：** 在Retro Coder DSL中构造神经符号表示并提取有限自动机，用程序解释观测中的游戏演化。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="a04"></a>

## PoE-World: Compositional World Modeling with Products of Programmatic Experts

[paper](https://arxiv.org/abs/2505.10819) · [project](https://topwasu.github.io/poe-world)

- **Type / date:** Paper / 2025-05-16.
- **Method:** Combines programmatic experts to model stochastic game dynamics for planning.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** gpt-4o-2024-08-06; 加权programmatic experts，无视频扩散骨干
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2505.10819).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 单个确定性程序难表达随机动态；整块修复不利于复用对象级局部机制。

**方法：** 生成多个局部程序专家，以带权概率乘积组成预测分布；学习专家权重并在Atari中进行基于模型的规划。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="a03"></a>

## Synthesizing world models for bilevel planning

[paper](https://arxiv.org/abs/2503.20124)

- **Type / date:** Paper / 2025-03-26.
- **Method:** Learns executable world abstractions and uses them in hierarchical planning.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** GPT-4o; 双层符号规划; o1属于baseline
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2503.20124).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 低层模型逐步搜索成本高；只用高层语言计划又可能忽略真实动作前提。

**方法：** TheoryCoder同时合成Python低层动态和可执行高层抽象，把任务分成高层规划与低层实现，并用交互修正规则。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="n001"></a>

## FactorSim: Generative Simulation via Factorized Representation

[paper](https://arxiv.org/abs/2409.17652)

- **Type / date:** Paper / 2024-09-26.
- **Method:** Factorizes simulation generation into state, action-dependent dynamics, independent dynamics, and observation components.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** GPT-4；Llama 3
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2409.17652).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 长指令下直接生成完整仿真容易遗漏状态依赖。

**方法：** 把环境分解为因子化POMDP，逐步生成状态、动作相关／无关转移与观察模块；只取相关代码作为上下文。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="a02"></a>

## Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search

[paper](https://arxiv.org/abs/2405.15383)

- **Type / date:** Paper / 2024-05-24.
- **Method:** Searches over world-model programs with generation, improvement, and execution-based repair operations.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** Llama-3-70B、GPT-4 Turbo; GIF-MCTS，不是预训练模型
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2405.15383).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 一次生成或简单反复调试容易停在错误程序；需要利用测试信号有效分配合成预算。

**方法：** GIF-MCTS把Generate、Improve、Fix作为树搜索动作，依据轨迹执行误差选择分支；在CWMB上分别检验预测与控制。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="a01"></a>

## WorldCoder, a Model-Based LLM Agent: Building World Models by Writing Code and Interacting with the Environment

[paper](https://arxiv.org/abs/2402.12275)

- **Type / date:** Paper / 2024-02-19.
- **Method:** Synthesizes executable transition models from interaction and uses planning constraints to guide model revisions.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** GPT-4; 值迭代/MCTS，非视频生成模型
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/2402.12275).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** LLM直接行动缺少可检验的动态知识，也难在新交互后持续修正环境理解。

**方法：** 合成Python转移/奖励模型，要求符合已见经验，并满足乐观的目标可达约束；以搜索选择修正，再用模型规划和收集新经验。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="h02"></a>

## Automated Game Design via Conceptual Expansion

[paper](https://arxiv.org/abs/1809.02232)

- **Type / date:** Paper / 2018-09-06.
- **Method:** Recombines learned game representations to synthesize new game mechanics and content.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** conceptual expansion与符号游戏表示; 不依赖现代LLM/视频扩散模型
- **Primary-source identity checked:** 2026-10-22; [source](https://arxiv.org/abs/1809.02232).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 自动游戏设计需要超越参数扰动，重组已有游戏中的内容和机制。

**方法：** 学习近似游戏表示，在概念空间扩展和组合原有机制，形成新游戏并检验其行为/设计特征。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>

<a id="h01"></a>

## Game Engine Learning from Video

[paper](https://www.ijcai.org/Proceedings/2017/518)

- **Type / date:** Paper / date not stated.
- **Method:** Learns an executable approximation of a game engine from gameplay video.
- **Scope:** Represents visual/spatial game transitions as executable programs. This branch supplies dynamics for planning; it does not imply a generative video renderer.
- **Models / representations in reading notes:** 对象/规则表示与符号搜索; 无需LLM或扩散骨干; IJCAI 2017前史
- **Primary-source identity checked:** 2026-10-22; [source](https://www.ijcai.org/Proceedings/2017/518).

<details>
<summary>中文 motivation / 方法笔记</summary>

**Motivation：** 从观测游戏恢复可运行的前向机制，使学习不依赖源代码或现成转移模型。

**方法：** 从Super Mario Bros.视频取得对象/运动表示，搜索并修订预测规则，形成前向游戏引擎用于模拟和agent学习。

这些技术笔记来自既有定向阅读；本轮新核验的题名、来源与范围不等于重新完整精读或复现。

</details>
