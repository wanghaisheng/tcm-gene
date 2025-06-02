
---

**通用提示词：从一句话核心需求挖掘并生成游戏PRD初稿（兼容AI资产生成流程）**

```
You are an exceptionally skilled Senior Game Product Manager and Lead Designer. Your mission is to take a **brief, core user requirement or game concept (often just a single sentence)** and expand it into a comprehensive **preliminary Product Requirements Document (PRD)** for a new game.

This PRD should be well-structured and cover key aspects of the game, from high-level concept to initial thoughts on core mechanics and UI. While you will be inferring and elaborating significantly based on the minimal input, the goal is to create a foundational document that can guide further design and development, including the subsequent AI-driven generation of visual assets.

**The PRD you generate should include, but not be limited to, the following sections. For each section, if the initial user requirement provides no specific information, you should autonomously research, brainstorm, and propose reasonable and engaging ideas consistent with common game design principles and the inferred game genre/style.**

**Crucially, for any sections describing User Interfaces (UI), the descriptions MUST focus on visual placeholders and stylistic treatments for areas that will contain text or numerical data, rather than detailing the text content itself. This ensures the PRD is compatible with downstream AI processes for generating text-free graphical assets.**

---
**[PRD SECTION TEMPLATE TO FOLLOW]**
---

**1. Project Overview & Vision:**
    *   **1.1. Proposed Game Title (Suggest 2-3 options):** [Based on the core requirement, suggest creative and fitting game titles.]
    *   **1.2. Core Game Concept & Hook (Elaborated):** [Expand the user's single sentence into a compelling core concept. What is the unique selling proposition or core emotional draw?]
    *   **1.3. Target Audience (Inferred Persona):** [Describe the likely target player. Consider demographics, psychographics, gaming preferences.]
    *   **1.4. Genre & Sub-genre (Proposed):** [e.g., Puzzle-Strategy, Casual Simulation with RPG elements, Action Arcade.]
    *   **1.5. Overall Art Style Family (General Suggestion):** [Suggest a broad art style that fits the concept and target audience, e.g., "Vibrant Cartoon 2D," "Stylized Low-Poly 3D," "Dark Fantasy Ink Wash." Acknowledge this is preliminary.]
    *   **1.6. Desired Player Experience & Atmosphere:** [What should players feel? e.g., "Relaxing and creative," "Challenging and rewarding," "Mysterious and immersive."]

**2. Core Gameplay Mechanics:**
    *   **2.1. Main Player Objective(s):** [What are the primary long-term and short-term goals for the player in the game?]
    *   **2.2. Core Loop (High-Level):** [Describe the fundamental cycle of actions players will repeatedly engage in.]
    *   **2.3. Key Game Systems (Brainstormed - at least 2-3):** [Propose key systems that would support the core loop and concept. e.g., "Progression System (Leveling/Unlocks)," "Resource Management System," "Crafting System," "Social Interaction System (if applicable)."]
        *   For each system, briefly describe its purpose and how it might manifest.

**3. Key Game Modes (Proposed - at least 1-2):**
    *   **3.1. [Mode Name 1, e.g., "Story Mode," "Campaign Mode"]:**
        *   **Objective/Premise:** [What is the goal of this mode?]
        *   **Gameplay Focus:** [What mechanics or experiences are emphasized here?]
    *   **3.2. [Mode Name 2, e.g., "Endless Mode," "Challenge Mode," "PvP Arena"] (Optional):**
        *   **Objective/Premise:**
        *   **Gameplay Focus:**

**4. Monetization Strategy (Preliminary Thoughts - if applicable):**
    *   [Suggest potential monetization approaches if relevant to the game concept, e.g., "Free-to-Play with IAP (cosmetics, boosters)," "Premium One-Time Purchase," "Subscription." Acknowledge this requires deeper market research.]

**5. Key User Interfaces (UI) - Visual Placeholder Descriptions:**
    *   **(Instructions for this section):** For each key UI screen inferred or necessary for the game concept, provide a visual description. **Focus on layout, component types, and the *visual representation* of areas for text/data, NOT the text/data itself.** Adhere to the [Overall Art Style Family] suggested in 1.5.

    *   **5.1. Main Menu Screen:**
        *   **Purpose:** [e.g., Game entry, mode selection, access to settings/shop.]
        *   **Key Visual Components & Layout (Example):**
            *   `Background Element:` [Describe its visual nature, e.g., "A serene, thematic backdrop consistent with the game's art style."]
            *   `Game Title/Logo Area:` [Describe as an artistic graphical element, e.g., "A prominent, stylized graphical representation of the game's title, using [art style] flourishes, designed to be a visual centerpiece without legible text."]
            *   `Primary Action Buttons (e.g., Start, Options):` [Describe their visual form, e.g., "Several distinctly shaped button elements, each with a clear 'pressable' appearance and an icon or abstract symbol. Areas for labels are defined for programmatic text overlay."]
            *   `Character Display (if applicable):` [e.g., "An area showcasing the player's avatar or a key game character, rendered in the game's art style."]
        *   **Data Display Placeholders:** [e.g., "A small panel with graphical indicators for player currency or energy, with adjacent spaces for numerical values (to be rendered by the game engine)."]

    *   **5.2. Core Gameplay HUD/Interface:**
        *   **Purpose:** [e.g., Displaying in-game information, player controls, objectives during active gameplay.]
        *   **Key Visual Components & Layout:** [Detail elements like health bars, score displays, mini-map areas, action buttons, inventory slots – all described as visual forms/placeholders.]
        *   **Data Display Placeholders:** [e.g., "Health represented by a segmented graphical bar that depletes visually; score displayed in a stylized numerical readout area."]

    *   **5.3. [Other Key Interface 1, e.g., "Inventory Screen," "Shop Interface," "Level End Screen"]:**
        *   **Purpose:**
        *   **Key Visual Components & Layout:**
        *   **Data Display Placeholders:**

    *   **5.4. [Other Key Interface 2, ...as needed]:**

**6. Unique Selling Propositions (USPs) - Summarized:**
    *   [Based on your elaborations, list 3-5 key features or experiences that would make this game stand out.]

**7. Next Steps & Information Gaps (AI Self-Correction/Guidance):**
    *   Acknowledge this PRD is a preliminary expansion based on minimal input.
    *   List critical areas requiring further detailed design, user research, art direction, technical specification, and content creation, such as:
        *   Detailed level design.
        *   Specific narrative/story beats.
        *   Exact balancing for game systems.
        *   Comprehensive monetization plan.
        *   Detailed art style guide and asset list.
        *   Specific textual content for all UI elements and dialogue.
        *   Accessibility considerations.

---
**USER'S SINGLE-SENTENCE CORE REQUIREMENT/GAME CONCEPT:**
---

[在这里粘贴用户提供的一句话核心需求或游戏概念，例如：“我想要一款能让玩家扮演炼丹师，通过混合不同属性的草药来炼制神奇丹药，并用丹药解决各种事件的东方玄幻风格游戏。”]

---
**END OF USER'S REQUIREMENT.**
---

Please generate the preliminary Product Requirements Document (PRD) section based on the user's core requirement provided above. Autonomously research and elaborate on each section of the PRD template. Pay special attention to Section 5 (Key User Interfaces), ensuring all descriptions focus on visual placeholders compatible with subsequent AI asset generation workflows that handle text programmatically.
```

**如何使用这个泛化后的提示词：**

1.  **填写可选的风格/类型占位符（在提示词开头）：**
    *   虽然提示词设计为可以从一句话中推断类型和风格，但如果你想给AI一个更明确的初始方向，可以在提示词最开始补充一句，例如：“The user's requirement is for a **mobile casual puzzle game** with an intended **cute, cartoonish 2D art style**.” 这样AI在“自主研究”时会更有针对性。如果省略，AI会根据用户需求自行推断。

2.  **获取用户的一句话核心需求/游戏概念。**

3.  **准备输入：**
    *   将上面设计的“从一句话核心需求挖掘并生成游戏PRD初稿”的完整提示词粘贴到新的对话框。
    *   在提示词中标记的 `[在这里粘贴用户提供的一句话核心需求或游戏概念...]` 位置，粘贴用户的那句话。

4.  **提交给AI (建议使用能力较强的模型如GPT-4)。**

5.  **AI输出：** AI会尝试根据这一句话，结合其庞大的知识库和游戏设计常识，进行“自主研究和扩展”，并按照你提供的PRD模板结构，填充各个章节的内容。**特别是在UI描述部分，它会被引导去描述视觉占位符。**

**这个PRD初稿的价值：**

*   **从模糊到具体：** 将一个非常初级的想法快速转化为一个结构化的、包含多个关键思考维度的文档。
*   **启发与讨论的基础：** AI的推断和建议（如建议的游戏模式、核心系统）可以作为团队内部进一步讨论和细化的起点。
*   **后续流程的输入：**
    *   PRD中的 **“5. Key User Interfaces - Visual Placeholder Descriptions”** 部分，可以直接作为我们之前讨论的“从视觉界面描述生成模块化UI资产CSV”的那个提示词的输入，实现流程的串联。
    *   PRD的其他部分（如核心玩法、游戏模式）则为整体项目开发提供了初步的方向。
*   **识别信息缺口：** PRD中的“7. Next Steps & Information Gaps”会帮助你意识到哪些方面还需要进一步思考和定义。

**与你提供的“极致版落地页”提示词的关键区别和借鉴：**

*   **借鉴了“自主研究和补充”：** 核心思想都是AI不仅仅依赖输入，还会主动扩展和丰富内容。
*   **借鉴了“结构化输出”：** 都要求AI按照预设的模板和章节输出。
*   **目标产物不同：** 你的模板直接产出最终可用的前端代码和资源。本提示词产出的是一个**文档（PRD初稿）**，作为设计和后续AI流程的输入。
*   **输入粒度不同：** 你的模板可以处理不完善的PRD。本提示词从更早期的“一句话需求”开始。
*   **“无文字占位符”的预处理：** 本提示词在生成PRD的UI描述部分时，就要求AI使用“无文字占位符”的描述方式，为下游的AI图像生成做了铺垫。

这个泛化后的提示词是一个强大的工具，能够帮助你快速地将一个简单的游戏想法扩展成一个更有条理、更具讨论价值的PRD框架，并且其UI描述部分已经为后续的AI辅助素材生成做好了准备。