# Scope and classification

[← Main collection](../README.md)

This collection follows one workflow: **construct or recover an executable visual world, execute it, and produce visual observations**. A paper can contribute to one part without claiming a complete world model.

## Method and system scope

The world is represented by a program, a scene or engine configuration, an articulated model, or explicit spatial entities and executable rules. Relevant work creates, reconstructs, edits, identifies, executes, or visually realizes this object.

| Research problem | Examples | Reason for inclusion |
|---|---|---|
| Generate a scene program | SceneCraft, Code2Worlds | The output is an executable scene rather than only an image. |
| Recover or revise a world | Code as Worlds, EMPIRIC, Code2Worlds-2 | Mechanisms or physical scene configurations can be executed and checked. |
| Learn game dynamics as code | WorldCoder, PoE-World, Twin | Explicit spatial game transitions support prediction and planning. A neural renderer is not required. |
| Render engine execution | Code Video Model, PWM, Matrix-Game 4.0 | A world/engine determines structure or state; a learned visual stage realizes observations. |
| Render a parameterized character | Champ, HumANDiff, Directing the World | An articulated character is executed/rendered into visual guidance or surface correspondences. This is a bounded component, not a full game engine. |
| Learn scene-driven visual realization | Deferred Neural Rendering, DiffusionRenderer | Historical rendering methods make explicit scene information part of the observation interface. |
| Maintain partial game rules | GameDirector | Explicit combat state and rules are relevant; the interface is text, not a full 3D proxy. |

The input format is not the boundary. A proxy video may encode a program's execution; a pose video may come from an articulated character; depth can be simulated or estimated. What matters is the demonstrated relation to a world representation and the method's responsibility.

## Evaluation scope

Evaluation resources are included according to what they measure. They do **not** need to implement an executable world themselves.

- Video quality and temporal behavior: VBench and VBench-2.0.
- Physical commonsense: VideoPhy and VideoPhy-2.
- Camera, body, and trajectory adherence: task-specific protocols introduced by control papers, including EgoControl and 3DTrajMaster. These entries are marked **evaluation reference**, not classified as executable-world methods.
- World reconstruction and execution: 4DCodeBench, WorldCoder-Bench, PhysCodeGym.
- Program-to-video alignment: PROWBench and the tests reported with programmable-world systems.
- Memory and interaction: MBench, R2M-Bench, WBench, PlayWorld, and related protocols.

General scores and specialized tests answer different questions. Image quality is not evidence of correct world transitions; fitting a recorded trajectory does not establish recovery of the true physical mechanism; plausible real-world physics may not match an intentionally fictional game rule. The evaluation notes should identify the target, reference, visibility assumptions, and evaluator limitations.

## Outside the method scope

- Code that creates educational slides or explanatory videos rather than a visual environment.
- GUI/app next-screen prediction without a spatial/game/physical-world modeling contribution.
- Generic image/video editing, camera control, or physical-variable prompting without a demonstrated executable-world interface.
- Purely latent world prediction or geometry caches are not included solely because they could be connected to an engine in future.
- Engine-generated training data alone do not establish an executable-world interface at inference.

An excluded method can still introduce a relevant evaluation protocol. That is a distinct role and is labeled accordingly. Audio-only work is outside this visual collection.

## Category and counting rules

Each unique work has one primary category. Secondary responsibilities are explained in its summary and scope note. Reports, repositories, and checkpoints belonging to the same work are links in one record; paper versions are not counted as separate works. Surveys are listed and counted separately from original methods. The repository's reference total is not a count of complete code world models.
