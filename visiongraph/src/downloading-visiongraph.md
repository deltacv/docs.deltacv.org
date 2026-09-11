# Downloading VisionGraph

## Bundled with VisionBench (recommended)

VisionGraph is designed to be used seamlessly alongside VisionBench. Together they form a complete vision development suite: VisionBench handles pipeline execution in the background while VisionGraph gives you a visual, fully previewable node-based editor on top of it.

<div class="promo-card">
  <span class="promo-icon"><i class="fa-solid fa-box-open" aria-hidden="true"></i></span>
  <div class="promo-body">
    <p class="promo-title">Included with VisionBench</p>
    <p class="promo-desc">VisionGraph is bundled in every release — no separate download needed.</p>
  </div>
  <a class="promo-btn" href="/visionbench/downloading-visionbench.html#from-visiongraph">Download VisionBench →</a>
</div>

<span id="how-to-use"></span>
Once launched, switch to the **VisionGraph** tab in the top-right corner of the VisionBench window to create and run your projects.

<img src="assets/image (4) (1) (1).png" alt="VisionGraph tab in VisionBench" class="screenshot-sm">

From here, you can:
- **Instant Preview**: Simply click an existing project once in the list to activate its pipeline and view its output directly in the VisionBench preview window.
- **Create a New Project**: Click the "New" button at the bottom to start a fresh project file.
- **Open the Editor**: Select your project and click "Open Selected Project" to launch the visual node editor.
- **Run Pipelines**: VisionGraph pipelines run automatically within VisionBench, providing real-time feedback as you edit.


## Running from source (development)

You can also run VisionGraph directly from source using Gradle. This is useful for testing the latest unreleased changes or contributing to the project.

```bash
git clone https://github.com/deltacv/VisionGraph.git
cd VisionGraph
./gradlew runEv
```

> [!NOTE]
> Standalone VisionGraph does not currently support live pipeline previews. While you can still design and export pipelines, real-time visual feedback is only available when using VisionGraph through the VisionBench bundle.
